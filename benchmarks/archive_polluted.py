#!/usr/bin/env python3
"""Archiva los runs que contaminan la quality cruda: E1 (vacíos-basura), E2 (fórmula
obsoleta marcada), E3 (sin procedencia). Solo suites GENERALES (no niah/seguridad/tool).

Por qué: el quality_avg crudo global mezcla runs de procedencia incompatible. Los que
no se pueden usar (fórmula desconocida / no-respuesta) se archivan — es lo mismo que
caducarlos — y los huecos se re-miden limpio. Reversible (mueve a _archive, respalda).

KEEP: runs limpios (success + no-vacío + fórmula actual) · empty_persistent (silencio
intencional) · TODO niah/prompt_injection/tool_calling (fuera de esta pasada) · fallidos.

Uso:  python benchmarks/archive_polluted.py            # dry-run
      python benchmarks/archive_polluted.py --apply
"""
import argparse
import json
import shutil
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import benchmarks.export_for_pages as E

RESULTS = Path(__file__).parent / "results"
ARCHIVE = RESULTS / "_archive-polluted-20260716"
APARTE = ("niah", "prompt_injection")


def _empty(r):
    return not (r.get("response_preview") or "").strip()


def _polluted(r):
    if not r.get("success"):
        return None
    if r.get("empty_persistent"):
        return None
    s = str(r.get("suite", ""))
    if s.startswith(APARTE) or s == "tool_calling":
        return None
    if _empty(r):
        return "E1"                       # vacío-basura
    if not E._misma_formula(r):
        return "E2" if r.get("scoring") else "E3"  # obsoleta marcada / sin procedencia
    return None                            # limpio


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    afect, total = 0, 0
    clase = Counter()
    plan = []
    for f in sorted(RESULTS.glob("benchmark_*.json")):
        try:
            data = json.loads(f.read_text())
        except Exception:  # noqa: BLE001
            continue
        rows = data if isinstance(data, list) else data.get("results", [])
        rm, keep = [], []
        for r in rows:
            c = _polluted(r) if isinstance(r, dict) else None
            if c:
                rm.append(r); clase[c] += 1
            else:
                keep.append(r)
        if rm:
            afect += 1; total += len(rm)
            plan.append((f, data, keep, rm))

    print(f"  archivos afectados: {afect}")
    print(f"  runs a archivar: {total}  ·  por clase: {dict(clase)}")
    if not args.apply:
        print("\n  (dry-run — correr con --apply para ejecutar)")
        return 0

    ARCHIVE.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    for f, data, keep, rm in plan:
        if not (ARCHIVE / f.name).exists():
            shutil.copy(f, ARCHIVE / f.name)
        (ARCHIVE / f"REMOVED__{f.name}").write_text(
            json.dumps({"archived_at": stamp, "reason": "polluted_E1_E2_E3_general_suites",
                        "runs": rm}, ensure_ascii=False, indent=2))
        if isinstance(data, list):
            out = keep
        else:
            data["results"] = keep
            data.setdefault("metadata", {})["polluted_cleanup"] = {"at": stamp, "removed": len(rm)}
            out = data
        f.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"\n  ✅ {total} runs archivados en {ARCHIVE.name}/ (originales respaldados ahí)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
