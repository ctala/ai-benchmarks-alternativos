#!/usr/bin/env python3
"""
Sincroniza counts (modelos, tests, lotes) en archivos MD/HTML del repo
desde docs/data/models.json (single source of truth).

Idea: evita la deriva entre docs. Corre:
    python benchmarks/sync_doc_counts.py
y reescribe README.md, AGENTS.md, INSIGHTS.md, ARQUITECTURA.md, MODELOS.md,
los agentes y las landing pages SEO con los counts actuales.

Soporta dos modos de marcado:
1. Marcadores explícitos: <!-- AUTO:total_models -->88<!-- /AUTO -->
2. Patrones canónicos via regex (legacy, para textos ya escritos)

Para evitar pisar valores históricos (blogs con fecha, INSIGHTS al día X),
respeta archivos en blog/ y archivos con marker `# nosync` en la primera línea.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
MODELS_JSON = ROOT / "docs" / "data" / "models.json"


def load_counts():
    data = json.loads(MODELS_JSON.read_text())
    total = data["total_models"]
    tested = data["tested_count"]  # >= 50 runs
    with_runs = sum(1 for m in data["models"] if m.get("runs", 0) > 0)
    total_runs = sum(m.get("runs", 0) for m in data["models"])

    # "Lotes" = archivos benchmark_*.json con >=100 runs (excluye smoke tests).
    # Un lote canónico tiene ≥4 modelos × 91 tests ≈ 364 runs, pero relajamos
    # a 100 para no perder lotes parciales/cortados.
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
        # Marketing-friendly rounding
        "tests_marketing": _round_marketing(total_runs),
        "models_marketing": tested,
    }


def _round_marketing(n: int) -> str:
    """7223 -> '7,000+', 12500 -> '12,000+'."""
    if n < 1000:
        return f"{n}"
    floor_k = (n // 1000) * 1000
    return f"{floor_k:,}+".replace(",", ",")


# Patrones legacy → reemplazo dinámico desde counts
def build_substitutions(c: dict) -> list[tuple[re.Pattern, str]]:
    return [
        # "53 modelos" / "56 modelos" / "45 modelos" → "{tested} modelos"
        (re.compile(r"\b(45|53|56|61)\s+modelos\b"), f"{c['tested_count']} modelos"),
        # "5,000+ tests" / "7,500+ tests" → marketing rounded
        (re.compile(r"\b(?:5,000\+|7,500\+|6,000\+|7,000\+|5K)\s+tests\s+reales"),
         f"{c['tests_marketing']} tests reales"),
        (re.compile(r"\b(?:5,000\+|7,500\+|6,000\+|7,000\+|5K)\s+tests"),
         f"{c['tests_marketing']} tests"),
        # "7 lotes" / "10 lotes" / "15 lotes" → "{lotes} lotes"
        # (cualquier dígito 1-2 cifras antes de "lotes consolidados/del/etc")
        (re.compile(r"\b\d{1,2}\s+lotes\b"), f"{c['lotes']} lotes"),
        # "45 modelos × 91 tests = 4095 runs" → recalculado
        (re.compile(r"\b\d+\s+modelos\s+×\s+91\s+tests\s*=\s*\d+\s+runs"),
         f"{c['tested_count']} modelos × 91 tests = {c['tested_count'] * 91:,} runs"),
        # "53 modelos × 91 tests" (sin =) → "{tested} modelos × 91 tests"
        (re.compile(r"\b(?:45|53|56|61)\s+modelos\s+×\s+91\s+tests"),
         f"{c['tested_count']} modelos × 91 tests"),
    ]


# Marcadores explícitos para nuevos archivos:
# <!-- AUTO:KEY -->valor<!-- /AUTO -->
def build_marker_substitutions(c: dict) -> list[tuple[re.Pattern, str]]:
    keys = {
        "total_models": str(c["total_models"]),
        "tested_count": str(c["tested_count"]),
        "with_runs": str(c["with_runs"]),
        "total_runs": f"{c['total_runs']:,}",
        "tests_marketing": c["tests_marketing"],
        "lotes": str(c["lotes"]),
    }
    subs = []
    for key, value in keys.items():
        pattern = re.compile(
            rf"<!-- AUTO:{key} -->.*?<!-- /AUTO -->", re.DOTALL
        )
        replacement = f"<!-- AUTO:{key} -->{value}<!-- /AUTO -->"
        subs.append((pattern, replacement))
    return subs


# Archivos a actualizar (relativos a ROOT)
TARGET_GLOBS = [
    "README.md",
    "AGENTS.md",
    "INSIGHTS.md",
    "ARQUITECTURA.md",
    "MODELOS.md",
    ".claude/agents/*.md",
    ".claude/agents/README.md",
    "docs/alternativas-*/index.html",
    "docs/modelos-*/index.html",
]

# Archivos que NUNCA se tocan (históricos/dated)
EXCLUDED = {
    "blog/",
    "CHANGELOG.md",  # histórico, las versiones reflejan estado al momento del release
}


def should_skip(path: Path) -> bool:
    rel = str(path.relative_to(ROOT))
    if any(rel.startswith(p) for p in EXCLUDED):
        return True
    # Skip si tiene marker `<!-- nosync -->` en las primeras 5 líneas
    try:
        with path.open() as f:
            head = "".join(f.readline() for _ in range(5))
            if "<!-- nosync -->" in head or "# nosync" in head:
                return True
    except Exception:
        return True
    return False


def update_file(path: Path, subs: list, marker_subs: list) -> tuple[bool, int]:
    """Aplica substituciones. Devuelve (changed, n_replacements)."""
    original = path.read_text()
    text = original
    n = 0
    for pattern, repl in marker_subs + subs:
        new_text, count = pattern.subn(repl, text)
        if count > 0:
            n += count
            text = new_text
    if text != original:
        path.write_text(text)
        return True, n
    return False, 0


def main():
    counts = load_counts()
    print(f"Counts actuales: {counts}")
    print()

    subs = build_substitutions(counts)
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
    total_replacements = 0
    for path in targets:
        changed, n = update_file(path, subs, marker_subs)
        if changed:
            print(f"  ✓ {path.relative_to(ROOT)} ({n} reemplazos)")
            changed_files += 1
            total_replacements += n

    print()
    print(f"Total: {changed_files} archivos actualizados, {total_replacements} reemplazos")
    return 0 if changed_files >= 0 else 1


if __name__ == "__main__":
    sys.exit(main())
