#!/usr/bin/env python3
"""Extrae los resultados de Harbor a un JSON versionado en git.

POR QUÉ EXISTE (14-ago-2026)
----------------------------
Harbor escribe cada corrida en `jobs/<fecha>/<tarea>__<id>/`, y `jobs/` está en
`.gitignore` a propósito: las trayectorias completas de un agente pesan y contienen la
salida cruda del modelo. El problema es que **ese era el único lugar donde vivían los
resultados**. Un `rm -rf jobs/` —o cualquier limpieza de disco— borraba 222 corridas y
US$ 2,68 sin dejar rastro, y no había forma de reconstruirlas salvo volver a pagar.

Es el mismo agujero que el runner ya tenía tapado desde siempre (`results/*.json` va a
git) y que la tarea agéntica, por venir de un harness externo, no heredó.

QUÉ GUARDA, Y QUÉ NO
--------------------
Guarda el **resultado y su procedencia**: reward por intento, media, piso, causa de los
ceros, `task_checksum` (la huella de la tarea: dos corridas del mismo checksum son
comparables, dos de checksums distintos NO), agente, harness y costo.

NO guarda las trayectorias: son el equivalente de los haystacks de `niah` — enormes,
regenerables pagando, y sin valor comparativo. Quedan en `jobs/` mientras exista.

LA CAUSA DEL CERO NO SE ESCRIBE A MANO
--------------------------------------
Un reward 0 tiene al menos tres causas distintas y **no significan lo mismo**:

    sin_herramientas → no existe endpoint con tool use. El modelo nunca corrió.
    rompe_bucle      → tiene herramientas y no sostiene el formato. Sí corrió, y falló.
    hizo_mal_la_tarea→ corrió, entregó, y lo entregado está mal.

La primera NO es culpa del modelo como razonador; la tercera sí. Confundirlas es el
error que ya cometí una vez publicando un 0,0 que era del harness. Por eso la causa se
DERIVA de la traza, acá, con reglas explícitas — no se decide leyendo a ojo.

Uso:
    python benchmarks/export_harbor.py            # escribe tareas-agente/resultados.json
    python benchmarks/export_harbor.py --dry-run
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JOBS = ROOT / "jobs"
SALIDA = ROOT / "tareas-agente" / "resultados.json"
ARCHIVO = ROOT / "tareas-agente" / "archivo_condiciones_mezcladas.json"

# Firmas en la traza del agente → causa del cero. En orden de precedencia: la primera
# que aparece manda, porque "no hay endpoint" ocurre ANTES de cualquier intento.
FIRMAS = [
    ("sin_herramientas", re.compile(r"No endpoints found that support tool use", re.I),
     "no existe endpoint con tool use — el modelo nunca llegó a correr"),
    ("rompe_bucle", re.compile(r"RepeatedFormatError", re.I),
     "tiene herramientas pero no sostiene el formato de tool call"),
    ("sin_credencial", re.compile(r"AuthenticationError|invalid[_ ]api[_ ]key", re.I),
     "falta la credencial del proveedor — no es un fallo del modelo"),
    ("limite_de_pasos", re.compile(r"LimitsExceeded|step limit", re.I),
     "se quedó sin pasos antes de terminar"),
    # Descubierto el 14-ago en `harbor-ruteo`: deepseek-chat entró en un bucle
    # degenerado repitiendo la misma frase, y su traza llegó a 676 KB contra un entorno
    # de 7,6 KB — reventó su PROPIA ventana de contexto (180.517 tokens pedidos contra
    # 163.840). No es la tarea ni el harness: es el modelo llenándose de su propia
    # salida. Sin esta firma quedaba como `hizo_mal_la_tarea`, que sugiere que entendió
    # mal el trabajo cuando en realidad nunca llegó a hacerlo.
    ("desbordo_su_contexto", re.compile(
        r"maximum context length is \d+ tokens|context_length_exceeded", re.I),
     "entró en un bucle degenerado y reventó su propia ventana de contexto"),
]


def _causa(traza: str) -> tuple[str | None, str | None]:
    for clave, patron, detalle in FIRMAS:
        if patron.search(traza):
            return clave, detalle
    return None, None


_PRECIOS: dict[str, tuple[float, float]] | None = None


def _precio(modelo: str) -> tuple[float, float] | None:
    """USD por millón (entrada, salida) del catálogo, por id de OpenRouter: el mismo precio
    con que el runner costea sus runs, para que Harbor y el índice se lean igual."""
    global _PRECIOS
    if _PRECIOS is None:
        sys.path.insert(0, str(ROOT / "benchmarks"))
        from models import MODELS, OLLAMA_MODELS
        _PRECIOS = {}
        for cfg in {**OLLAMA_MODELS, **MODELS}.values():
            if cfg.get("id") and cfg.get("cost_input") is not None:
                _PRECIOS.setdefault(cfg["id"], (cfg["cost_input"], cfg.get("cost_output") or 0))
    return _PRECIOS.get(modelo)


def _costo(trayectoria: str, modelo: str) -> tuple[float | None, str | None]:
    """El costo de un intento y de dónde salió.

    4-nov-2026 · ANTES leía el acumulado que mini-swe-agent IMPRIME en la traza,
    `(step N, $0.01)`, y ese número viene **redondeado a dos decimales**: un intento de
    $0,0029 quedaba en $0,00 y uno de $0,0093 en $0,01. De paso, `instance_cost` de la
    trayectoria es 0 en 807 de 1.229 intentos porque litellm no conoce el precio de esos
    modelos. Resultado: `resultados.json` decía $0 para casi todo, la única prueba aceptaba
    cualquier float o None, y el dimensionamiento de la ventana de v5 tuvo que recalcular
    a mano. Un verde vacío.

    Ahora: tokens de la trayectoria × precio del catálogo (`tokens_x_precio`); si no hay
    precio, `instance_cost` cuando es > 0; si no hay ninguno, None — **nunca 0**, que se
    lee como «gratis» y no como «no se sabe»."""
    pi = sum(int(x) for x in re.findall(r'"prompt_tokens":\s*(\d+)', trayectoria))
    po = sum(int(x) for x in re.findall(r'"completion_tokens":\s*(\d+)', trayectoria))
    precio = _precio(modelo)
    if precio and (pi or po):
        return round(pi / 1e6 * precio[0] + po / 1e6 * precio[1], 6), "tokens_x_precio"
    m = re.search(r'"instance_cost":\s*([0-9.eE-]+)', trayectoria)
    if m and float(m.group(1)) > 0:
        return float(m.group(1)), "instance_cost"
    return None, None


def _checksum_vigente() -> dict[str, str]:
    """Por tarea, el checksum MAYORITARIO — el de la versión con la que se corrió el lote.

    Harbor calcula un hash de la tarea entera (consigna + entorno + tests). Si edité un
    test entre corridas, el hash cambia y **las dos corridas ya no son el mismo examen**.
    Es `prompt_sha` con otro nombre, y la regla del repo es la misma: no se promedian
    resultados de versiones distintas. Medido acá: 2 de 231 corridas venían de versiones
    viejas de `harbor-cotizar` y habrían entrado al promedio sin decir nada.
    """
    conteo: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    mtimes: dict[str, dict[str, float]] = defaultdict(dict)
    for trial in JOBS.glob("*/*__*"):
        p = trial / "result.json"
        if not p.exists():
            continue
        try:
            ck = json.loads(p.read_text()).get("task_checksum")
        except Exception:
            continue
        if ck:
            tarea = trial.name.split("__")[0]
            conteo[tarea][ck] += 1
            mtimes[tarea][ck] = max(mtimes[tarea].get(ck, 0), p.stat().st_mtime)
    # El vigente es el de la corrida MÁS RECIENTE, no el mayoritario.
    #
    # La v1 usaba mayoría, y eso funciona cuando quedan unos pocos rezagados viejos —
    # pero se rompe justo cuando la tarea cambia a propósito: el 14-ago le agregué
    # `politica.md` a `harbor-reunion` y quedaron **204 corridas de la versión vieja
    # contra 1 de la nueva**. Por mayoría, el extractor habría descartado la corrida
    # correcta y publicado las 204 obsoletas como si fueran de la tarea actual. El bug
    # más peligroso posible: reportar en verde la versión equivocada.
    vigente = {}
    for t, c in conteo.items():
        if not c:
            continue
        recientes = sorted(mtimes[t].items(), key=lambda kv: -kv[1])
        vigente[t] = recientes[0][0]
    return vigente


_PROVEEDOR = re.compile(r'"provider"\s*:\s*"([^"]+)"')


def _proveedores(trayectoria: str) -> list[str]:
    """Quién sirvió cada paso del intento, según la trayectoria (corte-v5 6.4).

    mini-swe-agent guarda `"provider"` por llamada y el export lo tiraba: un intento de
    10 pasos podía repartirse entre tres endpoints sin que nada lo dijera.
    """
    return sorted(set(_PROVEEDOR.findall(trayectoria)))


def es_de_ventana(agente_cfg: dict) -> bool:
    """¿El intento corrió en la ventana de v5, con proveedor fijo? (DECISIONES, 5-nov-2026)

    El config de mini-swe-agent con el proveedor fijo vive en `jobs/_proveedor_fijo/`."""
    return "_proveedor_fijo" in json.dumps(agente_cfg.get("kwargs") or {})


def solo_ventana(por_modelo: dict) -> tuple[dict, dict]:
    """En un par (tarea, modelo) con intentos de la ventana, quedan solo ésos; los demás van
    al archivo con su marca de condiciones mezcladas, como el «antes» de corte-v5 6.9.
    Función pura: devuelve (por_modelo filtrado, archivo)."""
    filtrado, archivo = {}, {}
    for par, intentos in por_modelo.items():
        nuevos = [i for i in intentos if i.get("ventana")]
        if nuevos and len(nuevos) < len(intentos):
            archivo[f"{par[0]}::{par[1]}"] = {
                "marca": "condiciones_mezcladas",
                "intentos": [i for i in intentos if not i.get("ventana")]}
        filtrado[par] = nuevos or intentos
    return filtrado, archivo


def recolectar() -> dict:
    por_modelo: dict[tuple[str, str], list[dict]] = defaultdict(list)
    meta_tarea: dict[str, dict] = {}
    vigente = _checksum_vigente()
    descartadas: dict[str, int] = defaultdict(int)

    for trial in sorted(JOBS.glob("*/*__*")):
        cfg_p = trial / "config.json"
        if not cfg_p.exists():
            continue
        # `harbor check` deja corridas de validación de la rúbrica, no de modelos.
        if trial.name.startswith("check-"):
            continue
        try:
            cfg = json.loads(cfg_p.read_text())
        except Exception:
            continue

        agente_cfg = cfg.get("agent") or {}
        modelo = (agente_cfg.get("model_name") or "").replace("openrouter/", "")
        agente = agente_cfg.get("name")
        tarea = trial.name.split("__")[0]
        if not modelo:
            continue

        rw = trial / "verifier" / "reward.txt"
        reward = None
        if rw.exists():
            try:
                reward = float(rw.read_text().strip())
            except ValueError:
                pass

        traza_p = trial / "agent" / "mini-swe-agent.txt"
        traza = traza_p.read_text(errors="replace") if traza_p.exists() else ""
        # La causa se deriva de TODA corrida en cero, aunque el modelo promedie bien.
        #
        # POR QUÉ (14-ago-2026, lo pidió Cristian: *"revisa si los inestables son culpa
        # nuestra"*). Antes, un modelo con 2 corridas perfectas y una en cero quedaba
        # etiquetado `inestable` a secas, y la causa de ESA corrida se perdía. Pero
        # «a veces rompe el bucle de herramientas» y «a veces hace mal la tarea» son
        # riesgos distintos: el primero no se arregla con una instrucción mejor.
        # Medido: grok-4.20 promedia 0,67 y su cero fue `rompe_bucle`; llama-3.3-70b
        # promedia 0,62 y el suyo fue JSON malformado. Misma etiqueta, causas opuestas.
        causa, detalle = _causa(traza) if (reward in (None, 0.0)) else (None, None)

        res_p = trial / "result.json"
        checksum = None
        if res_p.exists():
            try:
                checksum = json.loads(res_p.read_text()).get("task_checksum")
            except Exception:
                pass

        if checksum and vigente.get(tarea) and checksum != vigente[tarea]:
            descartadas[tarea] += 1
            continue

        if tarea not in meta_tarea and checksum:
            meta_tarea[tarea] = {"task_checksum": checksum, "agente": agente}

        tray_p = trial / "agent" / "mini-swe-agent.trajectory.json"
        tray = tray_p.read_text(errors="replace") if tray_p.exists() else ""
        costo, fuente = _costo(tray, modelo)
        por_modelo[(tarea, modelo)].append(
            {"reward": reward, "causa": causa, "detalle": detalle,
             "costo_usd": costo, "costo_fuente": fuente, "checksum": checksum,
             "proveedores": _proveedores(tray),
             "ventana": es_de_ventana(agente_cfg)})

    por_modelo, archivo = solo_ventana(por_modelo)
    datos = _resumir(por_modelo, meta_tarea, descartadas)
    datos["_archivo_condiciones_mezcladas"] = archivo
    return datos


def _resumir(por_modelo, meta_tarea, descartadas) -> dict:
    tareas: dict[str, dict] = {}
    for (tarea, modelo), intentos in sorted(por_modelo.items()):
        rewards = [i["reward"] for i in intentos if i["reward"] is not None]
        causas = [i["causa"] for i in intentos if i["causa"]]
        costos = [i["costo_usd"] for i in intentos if i["costo_usd"] is not None]

        # El estado NO sale del promedio: sale de la causa cuando la hay, y del piso
        # cuando no. Un modelo que promedia 0,56 con un piso en 0 es INESTABLE, y eso
        # es información distinta de "saca 0,56 siempre".
        if causas and all(r == 0.0 for r in rewards or [0.0]):
            estado = max(set(causas), key=causas.count)
        elif not rewards:
            estado = "sin_datos"
        elif min(rewards) == 0.0:
            estado = "inestable"
        elif min(rewards) == 1.0:
            estado = "ok_siempre"
        else:
            estado = "ok_parcial"

        fila = {
            "media": round(sum(rewards) / len(rewards), 4) if rewards else None,
            "piso": min(rewards) if rewards else None,
            "techo": max(rewards) if rewards else None,
            "intentos": len(intentos),
            "rewards": rewards,
            "estado": estado,
            "costo_usd": round(sum(costos), 4) if costos else None,
            # Cuántos intentos tienen costo conocido: un total sobre 1 de 3 no es el total.
            "costo_intentos": len(costos),
            # Proveedores que sirvieron los intentos. Más de uno = examen mezclado (6.5).
            "proveedores": sorted({p for i in intentos for p in i.get("proveedores") or []}),
        }
        detalle = next((i["detalle"] for i in intentos if i["detalle"]), None)
        if detalle:
            fila["motivo"] = detalle
        # Causas de las corridas en cero de un modelo que NO es uniformemente cero.
        # Sin esto, `inestable` es una etiqueta sin diagnóstico.
        ceros = [i["causa"] or "hizo_mal_la_tarea" for i in intentos if i["reward"] == 0.0]
        if ceros and estado not in ("sin_herramientas", "rompe_bucle", "sin_credencial"):
            fila["causas_de_los_ceros"] = sorted(set(ceros))

        tareas.setdefault(tarea, {"modelos": {}, **meta_tarea.get(tarea, {})})
        tareas[tarea]["modelos"][modelo] = fila

    for tarea, d in tareas.items():
        mods = d["modelos"]
        medias = [m["media"] for m in mods.values() if m["media"] is not None]
        d["resumen"] = {
            "modelos": len(mods),
            "corridas": sum(m["intentos"] for m in mods.values()),
            "perfectos": sum(1 for m in mods.values() if m["media"] == 1.0),
            "ceros": sum(1 for m in mods.values() if m["media"] == 0.0),
            "media_global": round(sum(medias) / len(medias), 4) if medias else None,
            "costo_usd": round(sum(m["costo_usd"] or 0 for m in mods.values()), 2),
            "descartadas_por_checksum": descartadas.get(tarea, 0),
        }
    return {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "harness": "harbor",
        "nota": ("Reward de tareas agénticas. NO entra al índice de calidad: es una "
                 "dimensión aparte, como tool calling y seguridad. Ver DECISIONES.md."),
        "tareas": tareas,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    if not JOBS.exists():
        print(f"❌ no existe {JOBS} — ¿corriste alguna tarea de Harbor?")
        return 1

    datos = recolectar()
    if not datos["tareas"]:
        print("❌ no se encontró ninguna corrida con reward en jobs/")
        return 1

    for tarea, d in datos["tareas"].items():
        r = d["resumen"]
        desc = r["descartadas_por_checksum"]
        print(f"  {tarea:<24} {r['modelos']:>3} modelos · {r['corridas']:>4} corridas · "
              f"{r['perfectos']} perfectos · {r['ceros']} ceros · ${r['costo_usd']}"
              + (f"  ⚠️  {desc} descartadas (versión vieja de la tarea)" if desc else ""))

    arch = datos.get("_archivo_condiciones_mezcladas", {})
    print(f"\n  archivo de condiciones mezcladas: {len(arch)} pares, "
          f"{sum(len(v['intentos']) for v in arch.values())} intentos")
    if a.dry_run:
        print("\n(dry-run: no se escribió nada)")
        return 0

    archivo = datos.pop("_archivo_condiciones_mezcladas", {})
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(json.dumps(datos, indent=2, ensure_ascii=False) + "\n",
                      encoding="utf-8")
    ARCHIVO.write_text(json.dumps({
        "por_que": "Intentos anteriores a la ventana de v5 en pares re-medidos con proveedor "
                   "fijo (DECISIONES, 5-nov-2026). No entran al índice; son el antes de 6.9.",
        "pares": archivo}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"  ✅ {ARCHIVO.relative_to(ROOT)} · {len(archivo)} pares, "
          f"{sum(len(v['intentos']) for v in archivo.values())} intentos archivados")
    print(f"\n  ✅ {SALIDA.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
