#!/usr/bin/env python3
"""
Guardrail de la calculadora: que sus supuestos no se separen de los datos.

POR QUÉ EXISTE
--------------
La calculadora (`docs/app.js` + `docs/index.html`) es **código escrito a mano** que
consume `docs/data/models.json`, que sí es generado. Cuando cambia la forma del dato,
nadie le avisa al código — y el 13-ago-2026 eso costó dos rondas de bugs invisibles:

  · Los 11 umbrales de calidad estaban calibrados para la escala z-scoreada (0,50–8,48).
    Al pasar a escala absoluta (7,26–8,65), **ninguno bajo 7,26 filtraba a nadie**: el
    default dejaba pasar los 82 y el usuario no tenía forma de notarlo.
  · El filtro "sólo con tool calling" usaba `m.tool_calling`, un flag de capacidad
    DECLARADA que declaran los 82 rankeados. Era un checkbox decorativo.
  · El selector ofrecía "score global" — el número que el README había dejado de
    publicar. Sitio y docs contaban historias distintas.

Ninguno rompía nada: la página cargaba, la tabla se dibujaba, los tests pasaban. Es
exactamente la clase de fallo que este repo documenta una y otra vez — **una regla sin
instrumento que la haga cumplir**. Este script es el instrumento.

QUÉ VERIFICA
------------
C1. Todo umbral de calidad del JS cae dentro del rango real de `score_calidad`. Un
    umbral fuera de rango no filtra a nadie (o filtra a todos) en silencio.
C2. El slider de calidad abarca el rango real de la población.
C3. Los campos que el JS lee existen en el JSON (`score_calidad`, `pareto`, …). Si el
    export deja de emitir uno, la UI muestra `undefined` sin quejarse.
C4. Los filtros por capacidad discriminan de verdad: si un filtro deja pasar al 100%
    de los rankeados, es decorativo.
C5. **La dirección inversa**: ¿la data ganó un eje que la calculadora ignora? C1-C4
    preguntan si la calculadora se ROMPIÓ; C5 pregunta si quedó INCOMPLETA, que es más
    silencioso — no hay error, hay una columna que nadie ve porque nunca se agregó.

Uso:
    python benchmarks/check_calculator.py          # exit 1 si algo derivó
    python benchmarks/check_calculator.py -v       # detalle
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APP_JS = ROOT / "docs" / "app.js"
INDEX = ROOT / "docs" / "index.html"
MODELS_JSON = ROOT / "docs" / "data" / "models.json"

# Campos que la UI lee del JSON y que el export tiene que seguir emitiendo.
CAMPOS_REQUERIDOS = [
    "score_calidad", "score_global", "quality_avg", "cost_score_avg",
    "speed_score_avg", "latency_score_avg", "tool_calling_score_avg",
    "cost_per_1k_calls_usd", "pareto", "ranked", "runs",
]

fallos: list[str] = []
avisos: list[str] = []


def fallo(codigo: str, msg: str) -> None:
    fallos.append(f"{codigo} · {msg}")


def aviso(codigo: str, msg: str) -> None:
    avisos.append(f"{codigo} · {msg}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    if not MODELS_JSON.exists():
        print(f"✗ falta {MODELS_JSON}. Corré export_for_pages.py primero.")
        return 1

    data = json.loads(MODELS_JSON.read_text())
    ranked = [m for m in data.get("models", []) if m.get("ranked")]
    if not ranked:
        print("✗ no hay modelos rankeados en models.json")
        return 1

    cal = [m["score_calidad"] for m in ranked if m.get("score_calidad") is not None]
    lo, hi = min(cal), max(cal)
    js = APP_JS.read_text(encoding="utf-8")
    html = INDEX.read_text(encoding="utf-8")

    # ── C1 · umbrales dentro del rango real ──────────────────────────────────
    umbrales = [float(x) for x in re.findall(r"quality:\s*(\d+(?:\.\d+)?)\s*,", js)]
    # `weights: { quality: 70, ... }` también matchea: son pesos 0-100, no umbrales.
    umbrales = [u for u in umbrales if u <= 10]
    muertos = [u for u in umbrales if u < lo]
    techo = [u for u in umbrales if u > hi]
    if muertos:
        fallo("C1", f"{len(muertos)} umbral(es) de calidad bajo el mínimo real ({lo:.2f}): "
                    f"{sorted(set(muertos))} — no filtran a NADIE, el usuario ve el catálogo entero")
    if techo:
        fallo("C1", f"umbral(es) sobre el máximo real ({hi:.2f}): {sorted(set(techo))} — "
                    f"la lista sale SIEMPRE vacía")
    if args.verbose and not muertos and not techo:
        print(f"  ✅ C1 · los {len(umbrales)} umbrales caen dentro de [{lo:.2f}, {hi:.2f}]")

    # ── C2 · el slider abarca la población ───────────────────────────────────
    m = re.search(r'id="quality"[^>]*min="([\d.]+)"[^>]*max="([\d.]+)"', html)
    if not m:
        aviso("C2", "no encontré el slider de calidad en index.html")
    else:
        smin, smax = float(m.group(1)), float(m.group(2))
        if smin > lo or smax < hi:
            fallo("C2", f"el slider va de {smin} a {smax} pero la población va de "
                        f"{lo:.2f} a {hi:.2f}: hay modelos que el usuario no puede alcanzar")
        elif smax - smin > (hi - lo) * 4:
            aviso("C2", f"el slider ({smin}–{smax}) es mucho más ancho que la población "
                        f"({lo:.2f}–{hi:.2f}): casi todo su recorrido no cambia nada")
        elif args.verbose:
            print(f"  ✅ C2 · slider {smin}–{smax} cubre la población {lo:.2f}–{hi:.2f}")

    # ── C3 · los campos que lee el JS siguen existiendo ──────────────────────
    faltan = [c for c in CAMPOS_REQUERIDOS
              if f'"{c}"' in json.dumps(ranked[0]) or c in ranked[0]]
    ausentes = [c for c in CAMPOS_REQUERIDOS if c not in ranked[0]]
    usados = [c for c in ausentes if re.search(rf"\b{re.escape(c)}\b", js)]
    if usados:
        fallo("C3", f"el JS lee campos que el export ya NO emite: {usados} — "
                    f"la UI los muestra como undefined sin quejarse")
    elif args.verbose:
        print(f"  ✅ C3 · los {len(faltan)} campos que usa la UI están en el export")

    # ── C4 · los filtros por capacidad discriminan ───────────────────────────
    n = len(ranked)
    tool_min = re.search(r"TOOL_CALLING_MIN\s*=\s*([\d.]+)", js)
    if tool_min:
        umbral = float(tool_min.group(1))
        pasan = sum(1 for m_ in ranked if (m_.get("tool_calling_score_avg") or 0) >= umbral)
        if pasan == n:
            fallo("C4", f"el filtro de tool calling (≥{umbral}) deja pasar a los {n} "
                        f"rankeados: es decorativo, no filtra nada")
        elif args.verbose:
            print(f"  ✅ C4 · el filtro de tool calling deja fuera a {n - pasan} de {n}")
    pareto = sum(1 for m_ in ranked if m_.get("pareto"))
    if pareto in (0, n):
        fallo("C4", f"la frontera de Pareto marca a {pareto} de {n}: no discrimina")
    elif args.verbose:
        print(f"  ✅ C4 · la frontera marca a {pareto} de {n}")

    # ── C5 · ¿la DATA ganó algo que la calculadora ignora? ──────────────────
    #
    # POR QUÉ (15-ago-2026). Cristian: *"pero ya te había pedido un guardrail para que la
    # calculadora estuviera al día"*. Tenía razón, y el hueco era de dirección: C1-C4
    # preguntan **«¿se rompió la calculadora porque cambió la data?»** — todos miran de
    # JS hacia JSON. Ninguno preguntaba lo contrario.
    #
    # Y eso fue exactamente lo que pasó: se midieron ejes nuevos (`agent_long_horizon`,
    # `tool_calling_adversarial`, `agentic_quality`), el JSON los trajo, la calculadora
    # los ignoró, y los cuatro chequeos dieron verde. No se rompió nada: quedó incompleta,
    # que es un fallo distinto y más silencioso — no hay error, hay una columna que nadie
    # ve porque nunca se agregó.
    js = APP_JS.read_text(errors="replace") if APP_JS.exists() else ""

    # 5a · toda suite medida en la mitad o más de los rankeados debería poder elegirse
    from collections import Counter
    cob = Counter()
    for m_ in ranked:
        for suite in (m_.get("score_by_suite") or {}):
            cob[suite] += 1
    # Suites que respaldan una DIMENSIÓN publicada aparte: exigir además la suite sería
    # pedir la misma información dos veces. `prompt_injection_es` se publica como
    # `security_score`, `niah_es` como `effective_context`.
    RESPALDAN_DIMENSION = {"prompt_injection_es": "security_score",
                           "niah_es": "effective_context",
                           "agent_long_horizon": "agentic_quality"}
    for suite, veces in sorted(cob.items()):
        if veces < n * 0.5:
            continue                      # cobertura baja: todavía no corresponde exigirla
        dim = RESPALDAN_DIMENSION.get(suite)
        if dim and dim in js:
            continue                      # ya visible por su dimensión
        if f'"{suite}"' not in js:
            aviso("C5", f"`{suite}` está medida en {veces}/{n} rankeados y la calculadora "
                        f"NO la ofrece: es un eje que existe en los datos y nadie puede ver")

    # 5b · dimensiones de primer nivel que deciden una elección
    DIMENSIONES = {
        "agentic_quality": "calidad en tareas multi-paso",
        "security_score": "resistencia a fuga de datos",
        "effective_context": "contexto que de verdad usa",
        "sirve_para_agentes": "si corre dentro de un agente",
        "multiturno_score": "sostener un hilo largo",
    }
    for campo, para_que in DIMENSIONES.items():
        con = sum(1 for m_ in ranked if m_.get(campo) is not None)
        if con >= n * 0.5 and campo not in js:
            fallo("C5", f"`{campo}` ({para_que}) está en {con}/{n} rankeados y la "
                        f"calculadora no lo usa en ninguna parte")

    print()
    for a in avisos:
        print(f"    ⚠️  {a}")
    for f in fallos:
        print(f"    ❌ {f}")
    if fallos:
        print(f"\n  ❌ La calculadora derivó de los datos ({len(fallos)} problema/s).")
        print("     Se rompe en silencio: la página carga igual y los filtros mienten.")
        return 1
    print("  ✅ La calculadora sigue alineada con los datos que sirve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
