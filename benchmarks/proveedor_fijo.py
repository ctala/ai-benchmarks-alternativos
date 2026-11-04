#!/usr/bin/env python3
"""Proveedor fijo por modelo abierto — el examen de v5 se rinde en UN endpoint declarado.

POR QUÉ EXISTE (corte-v5 6.3 · DECISIONES, 4-nov-2026: «mismo modelo, mismas condiciones»)
----------------------------------------------------------------------------------------
OpenRouter es un router: el mismo id de un modelo abierto lo sirven hasta 48 proveedores,
con cuantizaciones de `int4` a `bf16` y contextos de 8.000 a 1.000.000. Sin fijar el ruteo,
un examen de 160 tests queda repartido entre los proveedores que respondieron ese día, y
la nota del «modelo X» es en realidad la de una mezcla. El 4-nov, 40 de los 47 abiertos
rankeados tenían runs de más de un proveedor.

QUÉ HACE
--------
`--declarar` lee el endpoints API de OpenRouter para cada abierto rankeado y elige UNO:

  1. Apto: `status` 0, contexto ≥ 128.000, declara `tools` y `max_tokens` (y `reasoning` si el modelo tiene
     interruptor, porque el examen de v5 lo apaga en peldaño 1-2), y no es una variante
     de nivel de servicio (`/turbo`, `/fast`, `/flex`…), que sirve otra cosa con el mismo id.
  2. Entre los aptos (DECISIONES, 4-nov-2026): uno SIN CUANTIZAR (bf16/fp16/fp32) si lo
     hay; si no, el del AUTOR (la cuantización que él publica); si no, la cuantización más
     alta. Empates: el proveedor con más runs nuestros (continuidad), después el más barato.

La elección queda en `proveedores_declarados.json`, versionada. El adapter la consume:
`provider: {order: [tag], allow_fallbacks: false}`, y si OpenRouter devuelve el run servido
por otro proveedor, el run falla ruidoso en vez de guardarse como éxito.

Uso:
    python benchmarks/proveedor_fijo.py --declarar          # rehace la declaración (red)
    python benchmarks/proveedor_fijo.py z-ai/glm-5.1        # qué se declaró para ese id
"""
import argparse
import json
import re
import sys
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROOT = AQUI.parent
DECLARADOS = AQUI / "proveedores_declarados.json"
ENDPOINTS_API = "https://openrouter.ai/api/v1/models/{id}/endpoints"

# Mayor = mejor. `unknown` va al fondo: no se elige a ciegas sobre una cuantización conocida.
CUANT_RANGO = {"fp32": 9, "bf16": 8, "fp16": 8, "fp8": 6, "int8": 6, "fp6": 5,
               "mxfp4": 3, "nvfp4": 3, "fp4": 3, "int4": 2, "unknown": 0, None: 0}

SIN_CUANTIZAR = CUANT_RANGO["fp16"]   # bf16, fp16, fp32

# Prefijo del id del modelo → prefijo del `tag` del endpoint que sirve el propio autor.
AUTOR = {"z-ai": "z-ai", "moonshotai": "moonshotai", "qwen": "alibaba", "mistralai": "mistral",
         "xiaomi": "xiaomi", "minimax": "minimax", "tencent": "tencent", "deepseek": "deepseek",
         "google": "google-ai-studio", "nvidia": "nvidia", "stepfun": "stepfun"}

# El examen necesita prompt + techo de salida (hasta 98.304 en agent_long_horizon) y la
# conversación de 12 turnos. 4-nov-2026: el declarado de Qwen 3.8 27B (`cerebras/fp16`,
# 65.536) daba 404 «Filter by Context Length» en cada request del lote.
CONTEXTO_MIN = 128000

# Techo de salida. 4-nov-2026: un endpoint rechaza con 404 todo request cuyo `max_tokens`
# supera su `max_completion_tokens` (Ling en DeepInfra, 32.768, contra los 49.152 de
# `business_strategy`). Se prefiere un endpoint que acepte al menos el presupuesto por
# defecto (`suites.PRESUPUESTO_DEFECTO`); si el modelo no tiene ninguno, se queda el apto.
# Y el adapter recorta el pedido al techo del declarado (`techo_salida`): `max_tokens` es
# un techo y no una reserva, así que pedir lo que el proveedor acepta no cambia la
# respuesta salvo que el modelo de verdad lo necesitara, y eso lo caza check_truncamiento.
SALIDA_MIN = 32768

VARIANTE_DE_SERVICIO = re.compile(r"/(turbo|fast|spot|highspeed|flex|priority)\b")

_cache: dict | None = None


def cargar() -> dict:
    global _cache
    if _cache is None:
        try:
            _cache = json.loads(DECLARADOS.read_text(encoding="utf-8"))
        except FileNotFoundError:
            _cache = {"modelos": {}}
    return _cache


def declarado(model_id: str) -> dict | None:
    """La declaración para este id de OpenRouter, o None si el modelo no tiene proveedor fijo."""
    for d in cargar().get("modelos", {}).values():
        if d.get("id") == model_id:
            return d
    return None


def techo_salida(model_id: str) -> int | None:
    """El `max_completion_tokens` del endpoint declarado; None = sin límite o sin proveedor fijo."""
    d = declarado(model_id)
    return (d or {}).get("techo_salida") or None


def ruteo(model_id: str) -> dict | None:
    """El bloque `provider` que el adapter manda a OpenRouter. None = ruteo libre."""
    d = declarado(model_id)
    if not d:
        return None
    return {"order": [d["tag"]], "allow_fallbacks": False}


def yaml_harbor(model_id: str, carpeta: Path | None = None) -> Path | None:
    """Escribe el config de mini-swe-agent que fija el proveedor en Harbor; None = libre.

    Harbor lo lee en el host (`--ak config_file=<ruta>`) y lo pasa al agente encima de su
    `mini.yaml`. El proveedor que sirvió cada paso queda en la trayectoria y `export_harbor`
    lo conserva, así que un intento fuera del declarado se ve (corte-v5 6.4 y 6.5).
    """
    r = ruteo(model_id)
    if not r:
        return None
    carpeta = carpeta or (ROOT / "jobs" / "_proveedor_fijo")
    carpeta.mkdir(parents=True, exist_ok=True)
    ruta = carpeta / (model_id.replace("/", "__") + ".yaml")
    ruta.write_text("model:\n  model_kwargs:\n    extra_body:\n      provider:\n"
                    f"        order: [\"{r['order'][0]}\"]\n        allow_fallbacks: false\n",
                    encoding="utf-8")
    return ruta


def coincide(model_id: str, upstream: str | None) -> bool | None:
    """¿El run lo sirvió el proveedor declarado? None si el modelo no tiene proveedor fijo."""
    d = declarado(model_id)
    if not d:
        return None
    return (upstream or "").strip().lower() == d["provider_name"].strip().lower()


_censo_cache: dict | None = None


def cuantizacion_de(model_id: str, upstream: str | None) -> str | None:
    """La cuantización del endpoint que sirvió el run (corte-v5 6.4). No se calcula: se lee.

    Con proveedor fijo, la de la declaración. Si no, la del censo del día por (modelo,
    proveedor); si el censo trae dos cuantizaciones para ese par, `ambigua:a|b`.
    """
    global _censo_cache
    if not upstream:
        return None
    d = declarado(model_id)
    if d and d["provider_name"].lower() == upstream.lower():
        return d["cuantizacion"]
    if _censo_cache is None:
        try:
            _censo_cache = json.loads((ROOT / "docs" / "data" / "censo_proveedores.json")
                                      .read_text(encoding="utf-8")).get("modelos", {})
        except FileNotFoundError:
            _censo_cache = {}
    qs = sorted({e.get("cuantizacion") or "unknown"
                 for m in _censo_cache.values() if m.get("id") == model_id
                 for e in m.get("endpoints", [])
                 if (e.get("proveedor") or "").lower() == upstream.lower()})
    if not qs:
        return None
    return qs[0] if len(qs) == 1 else "ambigua:" + "|".join(qs)


def _apto(e: dict, necesita: set[str]) -> bool:
    return (e.get("status") == 0 and necesita <= set(e.get("supported_parameters") or [])
            and (e.get("context_length") or 0) >= CONTEXTO_MIN
            and not VARIANTE_DE_SERVICIO.search(e.get("tag") or ""))


def _precio(e: dict) -> float:
    p = e.get("pricing") or {}
    try:
        return float(p.get("prompt") or 0) + 4 * float(p.get("completion") or 0)
    except ValueError:
        return float("inf")


def elegir(model_id: str, endpoints: list[dict], runs: Counter,
           necesita: set[str]) -> tuple[dict | None, str]:
    """(endpoint elegido o None, motivo). Función pura: la prueban los unitarios."""
    aptos = [e for e in endpoints if _apto(e, necesita)]
    if not aptos:
        return None, f"ningún endpoint declara {sorted(necesita)} con status 0"
    con_aire = [e for e in aptos if (e.get("max_completion_tokens") or SALIDA_MIN) >= SALIDA_MIN]
    if con_aire:
        aptos = con_aire
    # DECISIONES 4-nov-2026: «la cuantización más alta disponible, o la que publica el
    # autor si no la hay sin cuantizar».
    pref = AUTOR.get(model_id.split("/")[0])
    sin_cuantizar = [e for e in aptos if CUANT_RANGO.get(e.get("quantization"), 0) >= SIN_CUANTIZAR]
    del_autor = [e for e in aptos if pref and (e.get("tag") or "").split("/")[0] == pref]
    if sin_cuantizar:
        aptos, motivo = sin_cuantizar, "sin cuantizar"
    elif del_autor:
        aptos, motivo = del_autor, "autor"
    else:
        motivo = "cuantización más alta"
    top = max(CUANT_RANGO.get(e.get("quantization"), 0) for e in aptos)
    aptos = [e for e in aptos if CUANT_RANGO.get(e.get("quantization"), 0) == top]
    aptos.sort(key=lambda e: (-runs.get(e.get("provider_name"), 0), _precio(e), e.get("tag")))
    return aptos[0], motivo


def _abiertos() -> list[tuple[str, dict]]:
    sys.path.insert(0, str(ROOT))
    from benchmarks.models import MODELS
    d = json.loads((ROOT / "docs" / "data" / "models.json").read_text())
    return [(m["key"], MODELS[m["key"]]) for m in d["models"]
            if m.get("ranked") and m.get("open_source")
            and MODELS[m["key"]].get("provider", "openrouter") == "openrouter"]


def _runs_por_proveedor() -> dict:
    sys.path.insert(0, str(AQUI))
    from benchmarks.export_for_pages import load_all_results
    _, por_id_nombre = load_all_results()
    return {k: Counter(r.get("upstream_provider") for r in v if r.get("upstream_provider"))
            for k, v in por_id_nombre.items()}


def _bajar(mid: str) -> list[dict]:
    with urllib.request.urlopen(ENDPOINTS_API.format(id=mid), timeout=30) as r:
        return json.load(r)["data"]["endpoints"]


def declarar() -> dict:
    sys.path.insert(0, str(ROOT))
    from benchmarks import effort
    abiertos = _abiertos()
    runs = _runs_por_proveedor()
    with ThreadPoolExecutor(8) as ex:
        eps = dict(zip([k for k, _ in abiertos], ex.map(lambda kc: _bajar(kc[1]["id"]), abiertos)))
    modelos, sin = {}, {}
    for k, c in abiertos:
        # Quien no recibe `tools` nativas (las mide por prompt, o se puntúa sin ellas) no
        # necesita un endpoint que las declare.
        sin_nativas = c.get("sin_tools") or c.get("prompt_tools")
        necesita = {"max_tokens"} if sin_nativas else {"tools", "max_tokens"}
        if effort.clase(c["id"]) == "interruptor":
            necesita.add("reasoning")
        e, motivo = elegir(c["id"], eps[k], runs.get((c["id"], c["name"]), Counter()), necesita)
        if e is None:
            sin[k] = motivo
            continue
        modelos[k] = {"id": c["id"], "tag": e["tag"], "provider_name": e["provider_name"],
                      "cuantizacion": e.get("quantization") or "unknown",
                      "contexto": e.get("context_length"), "motivo": motivo,
                      "techo_salida": e.get("max_completion_tokens"),
                      "precio_in_por_M": round(float(e["pricing"]["prompt"]) * 1e6, 4),
                      "precio_out_por_M": round(float(e["pricing"]["completion"]) * 1e6, 4)}
    return {"tomada": date.today().isoformat(), "fuente": ENDPOINTS_API,
            "criterio": "apto (status 0, tools, max_tokens, reasoning si hay interruptor, sin "
                        "variante de servicio) → salida ≥ SALIDA_MIN si existe → sin cuantizar → autor → cuantización más "
                        "alta → más runs nuestros → más barato",
            "modelos": modelos, "sin_endpoint_apto": sin}


def main() -> int:
    ap = argparse.ArgumentParser(description="Proveedor fijo por modelo abierto.")
    ap.add_argument("modelo", nargs="?")
    ap.add_argument("--declarar", action="store_true")
    ap.add_argument("--harbor", action="store_true",
                    help="escribe el yaml de mini-swe-agent y muestra el --ak para Harbor")
    a = ap.parse_args()
    if a.declarar:
        d = declarar()
        tmp = DECLARADOS.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                       encoding="utf-8")
        tmp.replace(DECLARADOS)
        print(f"declarados: {len(d['modelos'])} · sin endpoint apto: {len(d['sin_endpoint_apto'])}")
        for k, m in sorted(d["sin_endpoint_apto"].items()):
            print(f"  ⚠ {k}: {m}")
        return 0
    if not a.modelo:
        ap.error("pasar un model_id o --declarar")
    if a.harbor:
        ruta = yaml_harbor(a.modelo)
        print(f"--ak config_file={ruta}" if ruta else "(sin proveedor fijo: ruteo libre)")
        return 0
    print(declarado(a.modelo), ruteo(a.modelo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
