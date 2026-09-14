#!/usr/bin/env python3
"""Qué esfuerzo de razonamiento se le manda a cada modelo — la regla vive acá, una vez.

POR QUÉ EXISTE (14-sep-2026)
----------------------------
El 2-sep (v4.12.0) se decidió mandar `reasoning: {effort: medium}` a todo thinking model
por OpenRouter, para que el examen fuera explícito y reproducible. OpenRouter declara en
`/api/v1/models`, por modelo, qué niveles soporta (`supported_efforts`) y cuál usa si no
se le pide nada (`default_effort`). Cruzado con los 100 rankeados el 14-sep:

  · `medium` NO está entre los niveles de 10 thinking rankeados: DeepSeek V4 (×4),
    GLM 5.2 / 5.3 / 5.3 Flash, Hy3, Hy4 y Kimi K3. GLM 5.3 con `medium` reportó 0 tokens
    de razonamiento en 4 de 5 preguntas; con su default (`max`), 619 de mediana
    (`results/experimento_effort_por_proveedor_20260902.json`). Otro examen, sin aviso.
  · Los niveles no son equivalentes entre proveedores: en 3 de 5 modelos medidos el
    razonamiento ni siquiera crece de `low` a `high`. «El mismo effort para todos»
    iguala el string, no el esfuerzo.
  · El histórico entero se midió SIN el parámetro, o sea al default. Los runs posteriores
    a v4.12.0 son canarios: el `medium` nunca midió un examen rankeado.

Cristian: *"ser lo más eficiente posible y ojalá no tener que remedir todo"* e *"incluso
podría ser sin effort si crees conveniente"*.

LA REGLA: EL EXAMEN ES EL DEFAULT, Y SE SABE CUÁL ES
----------------------------------------------------
**Sin pedido explícito no se manda effort.** Cada modelo rinde en su configuración por
defecto, que es:

  · lo que recibe quien llama a la API sin configurar nada — el caso de la audiencia;
  · lo único comparable entre proveedores, porque sus niveles no son equivalentes;
  · el examen que ya rindió el histórico: cero re-medición, por construcción.

Lo que buscaba la decisión del 2-sep —saber en qué modo rinde cada modelo— se cumple sin
mandar el string: la foto versiona el default declarado, cada run guarda la etiqueta
(«default:max», «apagado_por_defecto», «sin_niveles») y `--vivo` avisa cuando un
proveedor lo cambia. Recién ahí se decide si ese modelo se re-mide.

Mandar el default explícito parecía equivalente y no lo es del todo: en los tests con
herramientas el adapter activa `require_parameters`, y un parámetro más en el request
puede sacar del ruteo a proveedores que sirven al modelo pero no declaran `reasoning`.

Un test PUEDE pedir un nivel (`"reasoning_effort"` en su dict) y `BENCH_REASONING_EFFORT`
lo pide para un lote entero: es para experimentos, no para el índice. Si el modelo no
soporta el nivel pedido no se manda nada y la etiqueta lo dice. Al pedir más, recordar
que el effort REPARTE el presupuesto de salida (~50% `medium`, ~80% `high`): con los
techos de `suites.PRESUPUESTO_SALIDA`, `high` dejaría sin espacio a la respuesta en el
1,11% de los runs y en el 7,6% de `agent_long_horizon`.

POR QUÉ ACÁ Y NO EN EL ADAPTER
------------------------------
El adapter importa el SDK de OpenAI; esto no importa nada. Así la regla la verifica
`check_effort.py` sin red ni SDK, y los tests la prueban sin mockear un cliente.

LA FOTO
-------
`benchmarks/reasoning_openrouter.json` guarda esa metadata el día que se tomó y va en git.
Un proveedor que cambia su default cambia el examen en silencio: sólo se ve comparando la
foto contra la API (`--vivo`).

Uso:
    python benchmarks/effort.py --actualizar          # rehace la foto desde OpenRouter
    python benchmarks/effort.py --vivo                # foto vs API; exit 1 si algo cambió
    python benchmarks/effort.py z-ai/glm-5.3 [nivel]  # qué se le mandaría
"""
import argparse
import json
import sys
import urllib.request
from datetime import date
from pathlib import Path

AQUI = Path(__file__).resolve().parent
FOTO = AQUI / "reasoning_openrouter.json"
OR_API = "https://openrouter.ai/api/v1/models"

# Niveles que aparecen en los `supported_efforts` de OpenRouter (14-sep-2026). Un test que
# declare otro string tiene un error de tipeo, y el resolver lo trataría como no soportado.
NIVELES = ("none", "minimal", "low", "medium", "high", "xhigh", "max")

# Lo que se guarda de `reasoning`. El resto no decide nada del request.
CAMPOS = ("mandatory", "default_enabled", "supported_efforts", "default_effort",
          "supports_max_tokens")

_foto_cache: dict | None = None


def cargar_foto() -> dict:
    global _foto_cache
    if _foto_cache is None:
        try:
            _foto_cache = json.loads(FOTO.read_text(encoding="utf-8"))
        except FileNotFoundError:
            _foto_cache = {"modelos": {}, "ausentes": []}
    return _foto_cache


def resolver(model_id: str, pedido: str | None = None,
             foto: dict | None = None) -> tuple[str | None, str]:
    """(effort a mandar —None: no se manda nada—, etiqueta que queda en el run)."""
    modelos = (foto if foto is not None else cargar_foto()).get("modelos", {})
    if model_id not in modelos:
        return None, "sin_foto"
    rz = modelos[model_id] or {}
    niveles = rz.get("supported_efforts") or []
    if not niveles:
        return None, "sin_niveles" if rz else "sin_metadata"
    if rz.get("default_enabled") is False:
        return None, "apagado_por_defecto"
    default = rz.get("default_effort") or "sin_declarar"
    pedido = (pedido or "").strip().lower() or None
    if pedido is None:
        return None, f"default:{default}"
    if pedido in niveles:
        return pedido, f"pedido:{pedido}"
    return None, f"pedido:{pedido}→default:{default}"


def _ids_openrouter() -> set[str]:
    sys.path.insert(0, str(AQUI.parent))
    from benchmarks.models import MODELS
    return {c["id"] for c in MODELS.values()
            if c.get("id") and c.get("provider", "openrouter") == "openrouter"}


def foto_desde_api(ids: set[str]) -> dict:
    with urllib.request.urlopen(OR_API, timeout=30) as r:
        por_id = {m["id"]: m for m in json.load(r)["data"]}
    modelos, ausentes = {}, []
    for mid in sorted(ids):
        if mid not in por_id:
            ausentes.append(mid)
            continue
        rz = por_id[mid].get("reasoning")
        modelos[mid] = {k: rz[k] for k in CAMPOS if k in rz} if rz else None
    return {"tomada": date.today().isoformat(), "fuente": OR_API,
            "modelos": modelos, "ausentes": ausentes}


def diferencias(foto: dict, viva: dict) -> list[str]:
    """Cambios que alteran el examen: niveles, default, o si razona por defecto."""
    out = []
    for mid, rz in foto.get("modelos", {}).items():
        if mid not in viva["modelos"]:
            out.append(f"{mid}: ya no aparece en OpenRouter")
            continue
        a, b = rz or {}, viva["modelos"][mid] or {}
        for k in ("supported_efforts", "default_effort", "default_enabled"):
            if a.get(k) != b.get(k):
                out.append(f"{mid}: {k} {a.get(k)!r} → {b.get(k)!r}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Effort de razonamiento por modelo.")
    ap.add_argument("modelo", nargs="?", help="model_id de OpenRouter")
    ap.add_argument("nivel", nargs="?", help="nivel pedido por un test (opcional)")
    ap.add_argument("--actualizar", action="store_true", help="rehace la foto desde la API")
    ap.add_argument("--vivo", action="store_true", help="compara la foto contra la API")
    a = ap.parse_args()

    if a.actualizar or a.vivo:
        viva = foto_desde_api(_ids_openrouter())
        if a.vivo:
            difs = diferencias(cargar_foto(), viva)
            for d in difs:
                print(f"  ⚠ {d}")
            print(f"{len(difs)} cambio(s) contra la foto del {cargar_foto().get('tomada')}")
            return 1 if difs else 0
        FOTO.write_text(json.dumps(viva, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                        encoding="utf-8")
        con = sum(1 for v in viva["modelos"].values() if v and v.get("supported_efforts"))
        print(f"foto escrita: {len(viva['modelos'])} modelos ({con} con niveles declarados), "
              f"{len(viva['ausentes'])} ausentes de OpenRouter")
        return 0

    if not a.modelo:
        ap.error("pasar un model_id, --actualizar o --vivo")
    print(resolver(a.modelo, a.nivel))
    return 0


if __name__ == "__main__":
    sys.exit(main())
