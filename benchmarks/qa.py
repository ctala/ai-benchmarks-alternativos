#!/usr/bin/env python3
"""EL comando de QA. Uno solo, para todo lo que publicamos.

POR QUÉ EXISTE (16-ago-2026)
----------------------------
Cristian: *"El QA es para páginas, calculadora, wizards, tests, cuando agregamos nuevos
modelos, etc. Son muchas cosas para que no te queden perdidas. Ojalá lo más automatizado
posible, antes de mergear deberíamos correrlos."*

Las piezas existían y estaban **sueltas**: había que acordarse de cinco comandos, y
acordarse es justo lo que falla. Esta sesión lo probó tres veces en un día — el wizard
recomendando un modelo que falla, la calculadora coronando a uno sin herramientas, y una
página ordenando por un criterio con correlación negativa. Ninguno rompía nada.

    python benchmarks/qa.py            # todo, agrupado por área
    python benchmarks/qa.py --rapido   # lo que corre en segundos (pre-commit)
    python benchmarks/qa.py --area calculadora
    python benchmarks/qa.py --pre-merge  # lo que DEBE pasar antes de mergear

LAS SEIS ÁREAS
--------------
Cubren lo que el usuario nombró, y cada chequeo dice a qué área pertenece para que no se
pierda ninguna cuando se agregue algo nuevo:

  datos        el dataset y sus invariantes (precio $0, `:free`, duplicados, umbrales)
  suites       el registro de ejes: una sola lista, todos con nombre humano
  calculadora  el `app.js` REAL contra los datos reales, incluido el wizard
  paginas      las 71 publicadas: ¿lo que dicen lo sostiene la data?
  guardrails   que cada guardrail falle cuando debe (si no, no es un guardrail)
  version      las 7 superficies que declaran la versión, + tag y CHANGELOG

QUÉ CUENTA COMO «PASA»
----------------------
Un chequeo `bloqueante` que falla impide mergear. Uno `informativo` reporta deuda conocida
(por ejemplo variantes PRO citadas en prosa) y no frena: bloquear por deuda convierte al
QA en algo que se saltea, y un QA que se saltea no existe.
"""

import argparse
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = str(ROOT / ".venv" / "bin" / "python")

# área · qué prueba · comando · bloqueante · rápido (< ~5 s)
CHEQUEOS = [
    ("datos", "invariantes del dataset y funciones puras del núcleo",
     [PY, "-m", "pytest", "benchmarks/test_unitarios.py", "-q"], True, True),
    ("datos", "los docs vivos no citan un score que ya no existe",
     [PY, "benchmarks/check_consistency.py"], True, True),
    ("suites", "el registro de ejes es UNO y nadie lo copió a mano",
     [PY, "benchmarks/check_suites.py"], True, True),
    ("calculadora", "el app.js real contra los datos reales, wizard incluido",
     ["node", "benchmarks/qa_calculadora.mjs"], True, True),
    ("calculadora", "sus filtros y umbrales siguen alineados con lo que sirve",
     [PY, "benchmarks/check_calculator.py"], True, True),
    ("paginas", "lo que publican las 71 páginas lo sostiene la data",
     [PY, "benchmarks/auditar_paginas.py", "--duro"], True, False),
    ("paginas", "los cortes por eje coinciden con models.json",
     [PY, "benchmarks/check_cortes.py"], True, True),
    ("paginas", "ningún doc vivo contradice una decisión vigente",
     [PY, "benchmarks/check_claims.py"], True, True),
    ("guardrails", "cada guardrail falla cuando debe",
     [PY, "benchmarks/test_guardrails.py"], True, False),
    ("guardrails", "nadie mide por fuera del runner",
     [PY, "benchmarks/check_caminos.py"], True, True),
    ("version", "las 7 superficies declaran lo mismo, con tag y CHANGELOG",
     [PY, "benchmarks/check_version.py"], True, True),
    ("datos", "cobertura del núcleo sobre el piso",
     [PY, "benchmarks/cobertura.py", "--duro"], False, False),
]

AREAS = ["datos", "suites", "calculadora", "paginas", "guardrails", "version"]


def main() -> int:
    ap = argparse.ArgumentParser(description="QA unificado del benchmark")
    ap.add_argument("--area", choices=AREAS, help="solo un área")
    ap.add_argument("--rapido", action="store_true", help="solo lo que corre en segundos")
    ap.add_argument("--pre-merge", action="store_true", help="solo lo bloqueante (para el hook)")
    ap.add_argument("-v", "--verbose", action="store_true", help="mostrar la salida completa")
    a = ap.parse_args()

    sel = [c for c in CHEQUEOS
           if (not a.area or c[0] == a.area)
           and (not a.rapido or c[4])
           and (not a.pre_merge or c[3])]

    print(f"\n  QA · {len(sel)} chequeos"
          + (f" · área {a.area}" if a.area else "")
          + (" · modo rápido" if a.rapido else "")
          + (" · pre-merge" if a.pre_merge else "") + "\n")

    fallos, area_actual, t0 = [], None, time.monotonic()
    for area, que, cmd, bloqueante, _ in sel:
        if area != area_actual:
            print(f"  ── {area.upper()}")
            area_actual = area
        t = time.monotonic()
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        dt = time.monotonic() - t
        ok = r.returncode == 0
        marca = "✅" if ok else ("❌" if bloqueante else "⚠️ ")
        print(f"     {marca} {que}  ({dt:.1f}s)")
        if not ok:
            (fallos if bloqueante else []).append((area, que, r))
            if a.verbose or bloqueante:
                salida = (r.stdout or "") + (r.stderr or "")
                for ln in salida.strip().splitlines()[-14:]:
                    print(f"          {ln}")

    print(f"\n  {'─'*66}")
    if fallos:
        print(f"  ❌ {len(fallos)} chequeo(s) bloqueante(s) fallando · "
              f"{time.monotonic()-t0:.0f}s")
        print(f"     No mergees: lo que falla no rompe la página, la hace mentir.")
        return 1
    print(f"  ✅ los {len(sel)} chequeos pasan · {time.monotonic()-t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
