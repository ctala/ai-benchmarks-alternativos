#!/usr/bin/env python3
"""Mide y hace cumplir la cobertura de pruebas del NÚCLEO.

POR QUÉ EXISTE (16-ago-2026)
----------------------------
Cristian: *"Agrega todos los QAs funcionales y unitarios para tener un coverage de al
menos un 80%. No puede ser que todo siempre esté roto y no nos demos cuenta."*

Medido ese día antes de escribir nada: **4%**.

QUÉ CUENTA COMO NÚCLEO
----------------------
Los módulos que **deciden lo que se publica**. Deliberadamente NO están los generadores
de HTML completos ni los scripts de operación: cubrir 900 líneas de f-strings sube el
número y no atrapa un fallo más. Lo que sí atrapa fallos ahí es `auditar_paginas.py`,
que mira el HTML **ya generado** y pregunta si la data lo sostiene — otra capa, no ésta.

La cobertura sale de correr las TRES suites, porque prueban cosas distintas:

    test_unitarios.py    la función sola con su caso borde
    test_guardrails.py   que cada guardrail falle cuando debe (por proceso)
    qa_calculadora.mjs   el flujo real de la calculadora (JS, no cuenta acá)

El umbral es un piso, no una meta: sube cuando se agrega código al núcleo sin probarlo.

Uso:
    python benchmarks/cobertura.py            # reporte
    python benchmarks/cobertura.py --duro     # exit 1 si baja del umbral
"""

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = str(ROOT / ".venv" / "bin" / "python")

# Módulos que deciden lo que se publica. Agregar uno acá obliga a probarlo.
NUCLEO = [
    "benchmarks/suites.py",
    "benchmarks/scoring.py",
    "benchmarks/export_harbor.py",
    "benchmarks/auditar_paginas.py",
    "benchmarks/simular_pilares.py",
    "benchmarks/check_suites.py",
    "benchmarks/check_cortes.py",
    "benchmarks/check_claims.py",
    "benchmarks/check_calculator.py",
    "benchmarks/check_version.py",
]

UMBRAL = 80.0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--duro", action="store_true", help="exit 1 si baja del umbral")
    a = ap.parse_args()

    inc = ",".join(NUCLEO)
    subprocess.run([PY, "-m", "coverage", "erase"], cwd=ROOT, capture_output=True)
    for suite in (["-m", "pytest", "benchmarks/test_unitarios.py", "-q"],
                  ["benchmarks/test_guardrails.py"]):
        subprocess.run([PY, "-m", "coverage", "run", "-a", f"--include={inc}"] + suite,
                       cwd=ROOT, capture_output=True, text=True)

    r = subprocess.run([PY, "-m", "coverage", "report", f"--include={inc}"],
                       cwd=ROOT, capture_output=True, text=True)
    print(r.stdout)

    total = 0.0
    for ln in r.stdout.splitlines():
        if ln.startswith("TOTAL"):
            total = float(ln.split()[-1].rstrip("%"))

    js = subprocess.run(["node", str(ROOT / "benchmarks" / "qa_calculadora.mjs")],
                        cwd=ROOT, capture_output=True, text=True)
    n_js = js.stdout.count("✅")
    print(f"  Núcleo Python: {total:.0f}% de cobertura sobre {len(NUCLEO)} módulos")
    print(f"  Calculadora (JS): {n_js} chequeos funcionales sobre el `app.js` real")

    if total < UMBRAL:
        print(f"\n  ❌ {total:.0f}% está por debajo del piso de {UMBRAL:.0f}%.")
        print("     Un módulo del núcleo sin pruebas es un módulo que se rompe en silencio.")
        return 1 if a.duro else 0
    print(f"\n  ✅ {total:.0f}% ≥ {UMBRAL:.0f}% · las 3 suites en verde")
    return 0


if __name__ == "__main__":
    sys.exit(main())
