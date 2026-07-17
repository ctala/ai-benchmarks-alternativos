#!/usr/bin/env python3
"""Archiva los runs agénticos OBSOLETOS (agent_long_horizon con scoring != verificable).

Por qué: la suite agéntica se puntúa re-corriendo la tarea multi-turno (no tiene
expected_answer), así que NO se puede re-puntuar offline. El backfill de jul-2026 ya
la re-corrió con la fórmula actual (`verificable`) cubriendo los 70 modelos ranked.
Los runs viejos rubric-only / sin-marca / juez-30-70 quedan superados: solo ensucian
la calidad cruda global mezclando fórmulas. Se MUEVEN a _archive (reversible), no se
borran. Los verificables (backfill + viejos verificables) quedan intactos.

Uso:  python benchmarks/archive_obsolete_agentic.py --apply
      (sin --apply = dry-run)
"""
import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

RESULTS = Path(__file__).parent / "results"
ARCHIVE = RESULTS / "_archive-obsolete-agentic-20260716"


def _is_agentic(r):
    return str(r.get("suite", "")).startswith("agent_long_horizon")


def _obsolete(r):
    return _is_agentic(r) and r.get("scoring") != "verificable"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Ejecuta (sin esto, dry-run)")
    args = ap.parse_args()

    afectados, total_rm, total_keep_ag = 0, 0, 0
    plan = []
    for f in sorted(RESULTS.glob("benchmark_*.json")):
        try:
            data = json.loads(f.read_text())
        except Exception:  # noqa: BLE001
            continue
        rows = data if isinstance(data, list) else data.get("results", [])
        rm = [r for r in rows if isinstance(r, dict) and _obsolete(r)]
        keep = [r for r in rows if not (isinstance(r, dict) and _obsolete(r))]
        keep_ag = [r for r in rows if isinstance(r, dict) and _is_agentic(r) and not _obsolete(r)]
        total_keep_ag += len(keep_ag)
        if rm:
            afectados += 1
            total_rm += len(rm)
            plan.append((f, data, rows, rm, keep))

    print(f"  archivos afectados: {afectados}")
    print(f"  runs obsoletos a archivar: {total_rm}")
    print(f"  runs agénticos verificables que QUEDAN: {total_keep_ag}")
    if not args.apply:
        print("\n  (dry-run — correr con --apply para ejecutar)")
        return 0

    ARCHIVE.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    for f, data, rows, rm, keep in plan:
        # 1) respaldo del original completo (una vez) + archivo de los runs removidos
        if not (ARCHIVE / f.name).exists():
            shutil.copy(f, ARCHIVE / f.name)
        (ARCHIVE / f"REMOVED__{f.name}").write_text(
            json.dumps({"archived_at": stamp, "reason": "obsolete_agentic_superseded_by_backfill",
                        "runs": rm}, ensure_ascii=False, indent=2))
        # 2) reescribir el original solo con los runs que quedan (preservando estructura)
        if isinstance(data, list):
            out = keep
        else:
            data["results"] = keep
            data.setdefault("metadata", {})["agentic_cleanup"] = {
                "at": stamp, "removed": len(rm),
                "note": "runs agénticos no-verificables archivados (superados por backfill)"}
            out = data
        f.write_text(json.dumps(out, ensure_ascii=False, indent=2))
        print(f"    {f.name[:50]:<52} -{len(rm)} runs")

    print(f"\n  ✅ {total_rm} runs archivados en {ARCHIVE.name}/ (originales respaldados ahí)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
