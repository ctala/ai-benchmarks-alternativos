#!/usr/bin/env python3
"""
Sincroniza counts (modelos, tests, lotes) en archivos MD/HTML del repo
desde docs/data/models.json (single source of truth).

Uso:
    python benchmarks/sync_doc_counts.py              # aplica cambios
    python benchmarks/sync_doc_counts.py --dry-run    # solo muestra

Solo reemplaza marcadores explícitos:
    <!-- AUTO:total_models -->88<!-- /AUTO -->
    <!-- AUTO:tested_count -->45<!-- /AUTO -->
    <!-- AUTO:with_runs -->87<!-- /AUTO -->
    <!-- AUTO:total_runs -->8,000<!-- /AUTO -->
    <!-- AUTO:tests_marketing -->7,000+<!-- /AUTO -->
    <!-- AUTO:lotes -->15<!-- /AUTO -->

Para proteger bloques históricos o ejemplos de agentes, envolver en:
    <!-- nosync-start -->
    ... texto que NO se toca ...
    <!-- nosync-end -->

Archivos excluidos: blog/, CHANGELOG.md (histórico por definición).
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
MODELS_JSON = ROOT / "docs" / "data" / "models.json"

# Marcadores soportados
COUNT_KEYS = [
    "total_models",
    "tested_count",
    "with_runs",
    "total_runs",
    "tests_marketing",
    "lotes",
]

# Archivos a actualizar (relativos a ROOT)
TARGET_GLOBS = [
    "README.md",
    "AGENTS.md",
    "INSIGHTS.md",
    "ARQUITECTURA.md",
    "MODELOS.md",
    "ESTADO_SESION.md",
    "ROADMAP.md",
    ".claude/agents/*.md",
    "docs/alternativas-*/index.html",
    "docs/modelos-*/index.html",
]

# Archivos/directorios que NUNCA se tocan
EXCLUDED = {
    "blog/",
    "CHANGELOG.md",
}


def load_counts():
    data = json.loads(MODELS_JSON.read_text())
    total = data["total_models"]
    tested = data["tested_count"]
    with_runs = sum(1 for m in data["models"] if m.get("runs", 0) > 0)
    total_runs = sum(m.get("runs", 0) for m in data["models"])

    results_dir = ROOT / "benchmarks" / "results"
    lotes = 0
    for f in results_dir.glob("benchmark_*.json"):
        try:
            d = json.loads(f.read_text())
            runs = d if isinstance(d, list) else d.get("results", [])
            if len(runs) >= 100:
                lotes += 1
        except Exception:
            pass

    return {
        "total_models": total,
        "tested_count": tested,
        "with_runs": with_runs,
        "total_runs": total_runs,
        "lotes": lotes,
        # "tests reales" = total de ejecuciones medidas (campo canónico total_runs_measured,
        # incluye descartadas); fallback al conteo por-modelo. Consistente con los
        # generadores pSEO y llms.txt, y dinámico para no volver a quedar stale.
        "tests_marketing": _round_marketing(data.get("total_runs_measured") or total_runs),
    }


def _round_marketing(n: int) -> str:
    """7223 -> '7,000+', 12500 -> '12,000+'."""
    if n < 1000:
        return f"{n}"
    floor_k = (n // 1000) * 1000
    return f"{floor_k:,}+"


def build_marker_substitutions(c: dict) -> dict[str, tuple[re.Pattern, str]]:
    """Devuelve dict {key: (pattern, replacement)}."""
    values = {
        "total_models": str(c["total_models"]),
        "tested_count": str(c["tested_count"]),
        "with_runs": str(c["with_runs"]),
        "total_runs": f"{c['total_runs']:,}",
        "tests_marketing": c["tests_marketing"],
        "lotes": str(c["lotes"]),
    }
    subs = {}
    for key, value in values.items():
        pattern = re.compile(
            rf"<!-- AUTO:{re.escape(key)} -->.*?<!-- /AUTO -->", re.DOTALL
        )
        replacement = f"<!-- AUTO:{key} -->{value}<!-- /AUTO -->"
        subs[key] = (pattern, replacement)
    return subs


def should_skip(path: Path) -> bool:
    rel = str(path.relative_to(ROOT))
    if any(rel.startswith(p) for p in EXCLUDED):
        return True
    try:
        with path.open() as f:
            head = "".join(f.readline() for _ in range(5))
            if "<!-- nosync -->" in head or "# nosync" in head:
                return True
    except Exception:
        return True
    return False


def split_nosync_blocks(text: str) -> list[tuple[str, bool]]:
    """
    Divide el texto en segmentos (texto, is_sync).
    Los bloques entre <!-- nosync-start --> y <!-- nosync-end --> son is_sync=False.
    """
    pattern = re.compile(r"<!-- nosync-start -->.*?<!-- nosync-end -->", re.DOTALL)
    segments = []
    last_end = 0
    for m in pattern.finditer(text):
        if m.start() > last_end:
            segments.append((text[last_end:m.start()], True))
        segments.append((m.group(), False))
        last_end = m.end()
    if last_end < len(text):
        segments.append((text[last_end:], True))
    return segments


def update_file(path: Path, marker_subs: dict[str, tuple], dry_run: bool = False) -> tuple[bool, dict[str, int]]:
    """Aplica substituciones solo en segmentos sync. Devuelve (changed, counts_por_key)."""
    original = path.read_text()
    segments = split_nosync_blocks(original)
    changed = False
    key_counts = {}
    new_segments = []

    for seg_text, is_sync in segments:
        if not is_sync:
            new_segments.append(seg_text)
            continue
        new_text = seg_text
        for key, (pattern, replacement) in marker_subs.items():
            new_text, count = pattern.subn(replacement, new_text)
            if count:
                key_counts[key] = key_counts.get(key, 0) + count
                changed = True
        new_segments.append(new_text)

    if changed and not dry_run:
        path.write_text("".join(new_segments))
    return changed, key_counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="Muestra cambios sin escribir")
    args = ap.parse_args()

    counts = load_counts()
    print(f"Counts actuales: {counts}")
    print()

    marker_subs = build_marker_substitutions(counts)

    targets = []
    for glob in TARGET_GLOBS:
        if "*" in glob:
            targets.extend(ROOT.glob(glob))
        else:
            p = ROOT / glob
            if p.exists():
                targets.append(p)

    targets = [p for p in sorted(set(targets)) if not should_skip(p)]

    changed_files = 0
    for path in targets:
        changed, key_counts = update_file(path, marker_subs, dry_run=args.dry_run)
        if changed:
            changed_files += 1
            detail = ", ".join(f"{k}={v}" for k, v in key_counts.items())
            action = "[dry-run]" if args.dry_run else "✓"
            print(f"  {action} {path.relative_to(ROOT)} ({detail})")

    print()
    if args.dry_run:
        print(f"Dry-run: {changed_files} archivos se modificarían")
    else:
        print(f"Total: {changed_files} archivos actualizados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
