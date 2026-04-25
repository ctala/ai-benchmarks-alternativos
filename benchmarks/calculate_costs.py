#!/usr/bin/env python3
"""
Calcula costos totales del benchmark sumando cost_usd, tokens y runs por lote.

Usa los archivos JSON de benchmarks/results/ que el runner ya genera con
cost_usd embebido por test, pero **recalcula con el dict PRICING actual** (más
fiable que el cost_usd guardado, que puede estar desactualizado para corridas
viejas hechas antes de agregar precios al dict).

Notas importantes:
- Los modelos faltantes en PRICING usan fallback (1.0, 3.0).
- Reasoning tokens de thinking models pueden NO estar en output_tokens (varía
  por proveedor) — el costo real puede ser 1.5-2× lo calculado en thinking.
- El número definitivo siempre es el dashboard de OpenRouter / OpenAI.

Uso:
    python benchmarks/calculate_costs.py            # tabla a stdout
    python benchmarks/calculate_costs.py --markdown # formato MD para pegar
"""

import argparse
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from benchmarks.scoring import PRICING


def recalc_cost(model: str, tin: int, tout: int) -> float:
    if model in PRICING:
        ci, co = PRICING[model]
    else:
        ci, co = 1.0, 3.0  # fallback conservador
    return (tin / 1_000_000) * ci + (tout / 1_000_000) * co

# Lotes históricos en orden cronológico. (label, archivo, descripción).
# Los archivos no presentes se omiten silenciosamente.
LOTES = [
    ("Pre-v2.1 (sin Phi-4)", None, "16 sesiones 11-15 abril, JSONs no preservados — ~$3 estimado"),
    ("Agent capabilities (smoke)", "benchmark_20260422_062137.json", "13 modelos, 5 tests"),
    ("Kimi K2.6 vs Claude Opus", "benchmark_20260422_082319.json", "3 modelos × 91 tests"),
    ("Lote 1 v2.1 (Phi-4 oficial)", "benchmark_20260422_204025.json", "8 modelos × 91 tests"),
    ("Lote 2 v2.1", "benchmark_20260423_051248.json", "9 modelos × 91 tests"),
    ("Lote 3 v2.2 (10 modelos nuevos)", "benchmark_20260424_053942.json", "10 modelos × 91 tests"),
    ("Smoke Ollama Cloud", "benchmark_20260424_071523.json", "qwen3.5:397b-cloud, 3 tests"),
    ("Lote 4 GPT-5.5 (+retries)", "benchmark_20260425_052724.json", "GPT-5.5 + retries timeouts/empties"),
]

PRE_V21_ESTIMATE_USD = 3.0  # rough estimate for early v1.x runs not preserved


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--markdown", action="store_true", help="Emitir tabla en formato Markdown")
    ap.add_argument("--results-dir", default="benchmarks/results", help="Carpeta con JSONs")
    args = ap.parse_args()

    rows = []
    total_cost = 0.0
    total_tokens_in = 0
    total_tokens_out = 0
    total_runs = 0
    total_runs_ok = 0
    models_seen = set()

    for label, fname, desc in LOTES:
        if fname is None:
            rows.append((label, None, desc, 0, 0, 0, 0, PRE_V21_ESTIMATE_USD))
            total_cost += PRE_V21_ESTIMATE_USD
            continue
        path = Path(args.results_dir) / fname
        if not path.exists():
            continue
        try:
            data = json.loads(path.read_text())
        except Exception:
            continue
        cost = 0.0
        tin = 0
        tout = 0
        for r in data.get("results", []):
            mid = r.get("model_id") or r.get("model") or "?"
            ri = r.get("input_tokens", 0) or 0
            ro = r.get("output_tokens", 0) or 0
            tin += ri
            tout += ro
            cost += recalc_cost(mid, ri, ro)
        n = len(data.get("results", []))
        ok = sum(1 for r in data.get("results", []) if r.get("success"))
        for r in data.get("results", []):
            mid = r.get("model_id") or r.get("model")
            if mid:
                models_seen.add(mid)
        rows.append((label, fname, desc, n, ok, tin, tout, cost))
        total_cost += cost
        total_tokens_in += tin
        total_tokens_out += tout
        total_runs += n
        total_runs_ok += ok

    if args.markdown:
        print("| Lote | Runs | OK | In tokens | Out tokens | Costo USD |")
        print("|---|---:|---:|---:|---:|---:|")
        for label, fname, desc, n, ok, tin, tout, cost in rows:
            label_md = label
            if fname:
                label_md = f"{label} (`{fname}`)"
            n_str = f"{n:,}" if n else "—"
            ok_str = f"{ok:,}" if ok else "—"
            tin_str = f"{tin:,}" if tin else "—"
            tout_str = f"{tout:,}" if tout else "—"
            cost_str = f"${cost:.3f}" if cost else "—"
            print(f"| {label_md} | {n_str} | {ok_str} | {tin_str} | {tout_str} | {cost_str} |")
        print(f"| **TOTAL** | **{total_runs:,}** | **{total_runs_ok:,}** | **{total_tokens_in:,}** | **{total_tokens_out:,}** | **${total_cost:.2f}** |")
        print()
        print(f"**Modelos únicos**: {len(models_seen)}")
    else:
        print(f"{'Lote':<35} {'Runs':>6} {'OK':>6} {'In':>10} {'Out':>10} {'Costo':>9}")
        print("-" * 80)
        for label, fname, desc, n, ok, tin, tout, cost in rows:
            print(f"{label[:35]:<35} {n:>6} {ok:>6} {tin:>10,} {tout:>10,} ${cost:>7.3f}")
        print("-" * 80)
        print(f"{'TOTAL':<35} {total_runs:>6} {total_runs_ok:>6} {total_tokens_in:>10,} {total_tokens_out:>10,} ${total_cost:>7.2f}")
        print()
        print(f"Modelos únicos cubiertos: {len(models_seen)}")


if __name__ == "__main__":
    main()
