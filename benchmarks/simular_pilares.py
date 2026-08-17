#!/usr/bin/env python3
"""Simula meter al promedio de su pilar las suites que hoy quedan afuera.

POR QUÉ EXISTE (16-ago-2026)
----------------------------
`check_suites.py` avisa que tres suites están medidas, tienen pilar natural y **no suman
al promedio**: `agent_long_horizon` (91 modelos), `tool_calling_adversarial` (82) y
`content_verificable` (92). No fue una decisión — el mapeo viejo simplemente no las tenía
y `export_for_pages` las salteaba en silencio.

Meterlas es un cambio de **presentación**, y la regla del repo es clara: la presentación
se simula ANTES contra los runs en disco, cuesta minutos y $0, y se decide con el
resultado a la vista (`PLAN-ESTABILIDAD.md` R1). Este script es esa simulación.

Lo que hay que responder no es "¿cambia?" —va a cambiar—, sino:

  1. ¿Cuánto se mueve cada pilar, y en qué dirección?
  2. ¿Cuántos modelos cambian de puesto DENTRO del pilar, y cuánto?
  3. ¿A quién castiga? Una suite nueva en el promedio castiga al que no la rindió — y si
     los que no la rindieron son un grupo con algo en común (un proveedor, una época),
     el promedio deja de medir calidad y empieza a medir quién se midió primero.

El punto 3 es el que decide. Es la misma trampa que ya está documentada para
`integridad_idioma`: entrar al promedio con 17 de 138 mediría el sesgo de la muestra.

Uso:  python benchmarks/simular_pilares.py
      python benchmarks/simular_pilares.py --aplicar   # solo tras leer el reporte
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from benchmarks import suites as suites_reg  # noqa: E402
from benchmarks import validate_suite  # noqa: E402  (los umbrales de saturación)
from benchmarks.export_for_pages import MIN_SUITE_COVERAGE as COBERTURA_MINIMA  # noqa: E402

CANDIDATAS = [k for k, s in suites_reg.SUITES.items()
              if s["pilar"] and not s["en_promedio"]]


def _export_con(candidatas_dentro: set[str]) -> dict:
    """Corre el export con esas suites sumando a su pilar. No escribe nada a disco."""
    import importlib
    for k in CANDIDATAS:
        suites_reg.SUITES[k]["en_promedio"] = k in candidatas_dentro
    suites_reg.SUITE_TO_PILLAR = {k: s["pilar"] for k, s in suites_reg.SUITES.items()
                                  if s["pilar"] and s["en_promedio"]}
    import benchmarks.export_for_pages as exp
    importlib.reload(exp)
    return exp.build_export()


def _pilares(d: dict) -> dict:
    """{key: {pilar: score}} solo de los rankeados."""
    return {m["key"]: (m.get("score_by_pillar") or {})
            for m in d["models"] if m.get("ranked")}


def _puestos(pil_map: dict, pilar: str) -> dict:
    vals = [(k, p.get(pilar)) for k, p in pil_map.items() if p.get(pilar) is not None]
    vals.sort(key=lambda x: -x[1])
    return {k: i + 1 for i, (k, _) in enumerate(vals)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--aplicar", action="store_true",
                    help="escribe en_promedio: True en suites.py (leer el reporte antes)")
    a = ap.parse_args()

    if not CANDIDATAS:
        print("  ✅ ninguna suite medida quedó fuera del promedio de su pilar.")
        return 0

    d = json.loads((ROOT / "docs" / "data" / "models.json").read_text())
    nombres = {m["key"]: m["name"] for m in d["models"]}

    print(f"\nSimulando {len(CANDIDATAS)} suite(s) entrando al promedio de su pilar:\n")
    for k in CANDIDATAS:
        s = suites_reg.SUITES[k]
        n = sum(1 for m in d["models"] if k in (m.get("score_by_suite") or {}))
        rank = sum(1 for m in d["models"]
                   if m.get("ranked") and k in (m.get("score_by_suite") or {}))
        tot = sum(1 for m in d["models"] if m.get("ranked"))
        print(f"  · {k:<26} → {s['pilar']:<13} {n:>3} medidos · "
              f"{rank}/{tot} rankeados ({rank / tot:.0%} de cobertura)")

    # ── 3 · ¿a quién castiga la que NO rindió? ──────────────────────────────
    print("\n" + "─" * 74)
    print("QUIÉN NO LA RINDIÓ (lo que decide: si es un grupo, el promedio mide la muestra)")
    print("─" * 74)
    for k in CANDIDATAS:
        faltan = [m for m in d["models"] if m.get("ranked")
                  and k not in (m.get("score_by_suite") or {})]
        if not faltan:
            print(f"\n  {k}: la rindieron TODOS los rankeados — entra sin castigar a nadie.")
            continue
        print(f"\n  {k}: {len(faltan)} rankeados NO la rindieron")
        provs = {}
        for m in faltan:
            provs[m.get("provider") or "openrouter"] = provs.get(m.get("provider") or "openrouter", 0) + 1
        print(f"     por proveedor: " +
              " · ".join(f"{p} {n}" for p, n in sorted(provs.items(), key=lambda x: -x[1])[:6]))
        q = [m.get("score_calidad") for m in faltan if m.get("score_calidad") is not None]
        todos = [m.get("score_calidad") for m in d["models"]
                 if m.get("ranked") and m.get("score_calidad") is not None]
        if q and todos:
            print(f"     calidad media de los que faltan: {sum(q)/len(q):.2f} "
                  f"· del total rankeado: {sum(todos)/len(todos):.2f}")
        print(f"     ejemplos: " + ", ".join(nombres.get(m['key'], m['key']) for m in faltan[:5]))

    # ── 1 y 2 · cuánto se mueve ─────────────────────────────────────────────
    print("\n" + "─" * 74)
    print("EFECTO EN LOS PILARES (mismo dato, con y sin ellas)")
    print("─" * 74)
    antes = _export_con(set())
    despues = _export_con(set(CANDIDATAS))
    pa, pd = _pilares(antes), _pilares(despues)

    afectados = sorted({suites_reg.SUITES[k]["pilar"] for k in CANDIDATAS})
    for pilar in afectados:
        ra, rd = _puestos(pa, pilar), _puestos(pd, pilar)
        deltas = [(k, ra[k], rd.get(k), (pd[k].get(pilar) or 0) - (pa[k].get(pilar) or 0))
                  for k in ra if k in rd]
        movidos = [x for x in deltas if x[1] != x[2]]
        dmax = sorted(deltas, key=lambda x: -abs(x[3]))[:5]
        print(f"\n  {pilar}: {len(movidos)} de {len(deltas)} modelos cambian de puesto")
        print(f"     mayores cambios de nota:")
        for k, p1, p2, dv in dmax:
            flecha = "=" if p1 == p2 else (f"↑{p1 - p2}" if p2 < p1 else f"↓{p2 - p1}")
            print(f"       {nombres.get(k, k)[:34]:<36} {pa[k].get(pilar):.2f} → "
                  f"{pd[k].get(pilar):.2f}  ({dv:+.2f})  puesto {p1}→{p2} {flecha}")
        saltos = sorted(deltas, key=lambda x: -abs(x[1] - (x[2] or x[1])))[:5]
        print(f"     mayores saltos de puesto:")
        for k, p1, p2, dv in saltos:
            if p1 == p2:
                continue
            print(f"       {nombres.get(k, k)[:34]:<36} {p1} → {p2} "
                  f"({'sube' if p2 < p1 else 'baja'} {abs(p1 - p2)})")

    if not a.aplicar:
        print("\n  (simulación — nada se escribió. `--aplicar` tras leer el reporte)")
        return 0

    # ── el gate: `--aplicar` NO puede aplicar lo que este mismo reporte descartó ──
    #
    # Bug real, 17-ago-2026: marcó las tres candidatas `en_promedio: True` mientras su
    # propio reporte decía que dos tenían 10% de cobertura y habían fallado la validación
    # por saturación. Marcarlas no las metía al score hoy (el export excluye <80% de
    # cobertura) — las metía **el día que subieran de cobertura**, sin que nadie decidiera.
    # Una suite saturada entrando sola a un pilar es exactamente lo que `validate_suite.py`
    # existe para impedir.
    #
    # Es el patrón de siempre en este repo: la regla estaba escrita y no tenía instrumento.
    # El reporte la enunciaba en pantalla y el código de abajo no la leía.
    califican, rechazadas = [], []
    for k in CANDIDATAS:
        rank = sum(1 for m in d["models"]
                   if m.get("ranked") and k in (m.get("score_by_suite") or {}))
        tot = sum(1 for m in d["models"] if m.get("ranked"))
        notas = [(m.get("score_by_suite") or {}).get(k) for m in d["models"]
                 if m.get("ranked") and k in (m.get("score_by_suite") or {})]
        notas = [x for x in notas if x is not None]
        cob = rank / tot if tot else 0.0
        perf = (sum(1 for x in notas if x >= 9.9) / len(notas)) if notas else 1.0
        if cob < COBERTURA_MINIMA:
            rechazadas.append((k, f"{cob:.0%} de cobertura (mínimo {COBERTURA_MINIMA:.0%}): "
                                  f"entraría castigando al que la rindió primero"))
        elif perf >= validate_suite.SATURACION_MUERTA:
            rechazadas.append((k, f"{perf:.0%} de notas perfectas: saturada, no discrimina. "
                                  f"Endurecela y re-validá antes de sumarla al pilar"))
        else:
            califican.append(k)

    if rechazadas:
        print("\n  ⛔ NO se aplican (el reporte de arriba ya decía por qué):")
        for k, motivo in rechazadas:
            print(f"       · {k} — {motivo}")

    if not califican:
        print("\n  Ninguna candidata califica. Nada se escribió.")
        return 1

    src = (ROOT / "benchmarks" / "suites.py").read_text()
    for k in califican:
        i = src.index(f'"{k}": {{')
        j = src.index('"en_promedio": False', i)
        src = src[:j] + '"en_promedio": True' + src[j + len('"en_promedio": False'):]
    (ROOT / "benchmarks" / "suites.py").write_text(src)
    print(f"\n  ✅ {len(califican)} suite(s) marcadas `en_promedio: True`: "
          f"{', '.join(califican)}.")
    print(f"     Escribí el motivo en su `nota` de suites.py y corré regenerate_all.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
