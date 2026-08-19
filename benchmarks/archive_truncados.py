#!/usr/bin/env python3
"""Archiva los runs cortados por el techo de tokens. Reversible.

POR QUÉ (18-ago-2026)
---------------------
Un run con `finish_reason="length"` de un modelo que razonaba sin estar declarado en
`THINKING_MODELS` no es una medición baja: es **media medición**. La respuesta se cortó a
mitad de frase y el juez la puntuó igual, así que la nota que produce no es del modelo —
es del techo.

Mezclar esos runs con los de la re-medición sería lo peor de los dos mundos: el promedio
quedaría a medio camino entre el número falso y el verdadero, sin ser ninguno.

QUÉ SE ARCHIVA, Y QUÉ NO
------------------------
Sólo los runs con `finish_reason="length"` de los modelos afectados. **Un run del mismo
modelo y la misma época que NO se cortó es válido** —la respuesta cabía en el techo— y se
conserva: caducarlo sería tirar una medición buena y pagar por rehacerla.

Los runs archivados NO se borran: van a `_archive-truncados-<fecha>/`, con el JSON
original respaldado al lado. Siguen siendo evidencia de que esto pasó.

Después de archivar quedan huecos —tests sin ningún run válido— y el reporte los lista:
ésos son los que hay que re-medir, y sólo ésos.

Uso:  python benchmarks/archive_truncados.py           # dry-run, no toca nada
      python benchmarks/archive_truncados.py --apply
"""

import argparse
import glob
import json
import shutil
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "benchmarks" / "results"
ARCHIVE = RESULTS / f"_archive-truncados-{date.today().isoformat().replace('-','')}"
UMBRAL = 0.12
MIN_RUNS = 40


def afectados() -> dict:
    """Modelos cuyo % de runs cortados cruza el umbral. Mismo criterio que
    `check_truncamiento.py` — si divergieran, uno de los dos mentiría."""
    st = defaultdict(lambda: [0, 0])
    for f in glob.glob(str(RESULTS / "*.json")):
        try:
            d = json.loads(Path(f).read_text())
        except Exception:
            continue
        rs = d.get("results") if isinstance(d, dict) else d
        if not isinstance(rs, list):
            continue
        for r in rs:
            if isinstance(r, dict) and r.get("model"):
                st[r["model"]][1] += 1
                if r.get("finish_reason") == "length":
                    st[r["model"]][0] += 1
    return {m: (L, t) for m, (L, t) in st.items() if t >= MIN_RUNS and L / t >= UMBRAL}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="ejecutar (si no, dry-run)")
    ap.add_argument("--excluir", nargs="*", default=[],
                    help="modelos a dejar intactos (ej. los que aún no tienen fix)")
    a = ap.parse_args()

    objetivo = {m: v for m, v in afectados().items() if m not in a.excluir}
    if not objetivo:
        print("  ✅ ningún modelo con truncamiento sobre el umbral.")
        return 0

    print(f"{'MODO: APLICAR' if a.apply else 'MODO: DRY-RUN (no toca nada)'}\n")
    print(f"  {len(objetivo)} modelo(s) afectados:")
    for m, (L, t) in sorted(objetivo.items(), key=lambda x: -x[1][0] / x[1][1]):
        print(f"     {L/t:>5.0%}  {L:>4}/{t:<5}  {m}")
    if a.excluir:
        print(f"\n  excluidos a propósito: {', '.join(a.excluir)}")

    movidos = 0
    tocados = []
    huecos = defaultdict(set)      # (modelo) -> tests que quedan sin run válido
    conservados = defaultdict(set)  # (modelo) -> tests con al menos un run bueno

    for f in sorted(glob.glob(str(RESULTS / "*.json"))):
        p = Path(f)
        if "_archive" in str(p):
            continue
        try:
            d = json.loads(p.read_text())
        except Exception:
            continue
        if not isinstance(d, dict) or not isinstance(d.get("results"), list):
            continue
        quedan, fuera = [], []
        for r in d["results"]:
            malo = (isinstance(r, dict) and r.get("model") in objetivo
                    and r.get("finish_reason") == "length")
            (fuera if malo else quedan).append(r)
            if isinstance(r, dict) and r.get("model") in objetivo and r.get("test_name"):
                clave = (r["model"], r.get("suite"), r["test_name"])
                if malo:
                    huecos[clave[0]].add(clave[1:])
                elif r.get("success"):
                    conservados[clave[0]].add(clave[1:])
        if not fuera:
            continue
        movidos += len(fuera)
        tocados.append((p.name, len(fuera), len(quedan)))
        if a.apply:
            ARCHIVE.mkdir(exist_ok=True)
            shutil.copy2(p, ARCHIVE / f"ORIGINAL__{p.name}")
            (ARCHIVE / f"TRUNCADOS__{p.name}").write_text(
                json.dumps({"metadata": {**d.get("metadata", {}),
                                         "archivado": date.today().isoformat(),
                                         "motivo": "finish_reason=length · techo de tokens"},
                            "results": fuera}, ensure_ascii=False))
            d["results"] = quedan
            p.write_text(json.dumps(d, ensure_ascii=False))

    print(f"\n  {movidos} runs cortados en {len(tocados)} archivo(s)")
    for n, f_, q in sorted(tocados, key=lambda x: -x[1])[:8]:
        print(f"     {f_:>4} fuera / {q:>4} quedan   {n}")
    if len(tocados) > 8:
        print(f"     … y {len(tocados)-8} archivos más")

    print("\n  TESTS A RE-MEDIR (quedaron sin ningún run válido):")
    tot = 0
    for m in sorted(objetivo):
        faltan = huecos[m] - conservados[m]
        tot += len(faltan)
        if faltan:
            print(f"     {m:<26} {len(faltan):>3} tests")
    print(f"     {'TOTAL':<26} {tot:>3}")

    if not a.apply:
        print("\n  (dry-run: no se movió nada. Correr con --apply)")
    else:
        print(f"\n  ✅ archivado en {ARCHIVE.name}/ — con el original respaldado al lado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
