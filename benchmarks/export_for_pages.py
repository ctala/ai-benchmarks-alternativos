#!/usr/bin/env python3
"""
Genera docs/data/models.json para la calculadora HTML en GitHub Pages.

Consolida:
- Metadata desde benchmarks/config.py (MODELS dict): tier, pricing, license, provider, notas
- Métricas desde benchmarks/results/*.json (todos los lotes): score promedio,
  tok/s, latencia, tasa de éxito por suite/pilar
- Recalcula costo con PRICING actualizado (más fiable que cost_usd guardado)

El JSON resultante se commitea con el repo y se sirve estáticamente desde
GitHub Pages en https://benchmarks.cristiantala.com/data/models.json

Uso:
    python benchmarks/export_for_pages.py
"""

import json
import os
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from benchmarks.config import MODELS
from benchmarks.scoring import PRICING


# Mapeo suite → pilar (mismo orden que en generate_tests_md.py)
SUITE_TO_PILLAR = {
    "reasoning": "Razonamiento",
    "deep_reasoning": "Razonamiento",
    "hallucination": "Razonamiento",
    "strategy": "Razonamiento",
    "code_generation": "Coding",
    "structured_output": "Coding",
    "string_precision": "Coding",
    "ocr_extraction": "Coding",
    "content_generation": "Contenido",
    "summarization": "Contenido",
    "presentation": "Contenido",
    "startup_content": "Contenido",
    "creativity": "Contenido",
    "news_seo_writing": "Contenido",
    "sales_outreach": "Contenido",
    "translation": "Contenido",
    "tool_calling": "Agentes",
    "task_management": "Agentes",
    "customer_support": "Agentes",
    "orchestration": "Agentes",
    "multi_turn": "Agentes",
    "policy_adherence": "Agentes",
    "agent_capabilities": "Agentes",
}


def load_all_results():
    """Carga y consolida todos los runs exitosos de benchmark JSONs."""
    results_dir = Path(__file__).parent / "results"
    by_model = defaultdict(list)

    for fn in sorted(os.listdir(results_dir)):
        if not (fn.startswith("benchmark_") and fn.endswith(".json")):
            continue
        try:
            data = json.loads((results_dir / fn).read_text())
        except Exception:
            continue
        results = data if isinstance(data, list) else data.get("results", [])
        for r in results:
            if not r.get("success"):
                continue
            mid = r.get("model_id") or r.get("model") or "?"
            by_model[mid].append(r)
    return by_model


def aggregate_metrics(runs):
    """Reduce lista de runs a métricas: score, latencia, tok/s, por pilar."""
    scores = [r.get("final", 0) for r in runs if r.get("final") is not None]
    judge_scores = [r.get("judge_score") for r in runs if r.get("judge_score") is not None]
    speeds = [r.get("tokens_per_second", 0) for r in runs if r.get("tokens_per_second", 0) > 0]
    latencies = [r.get("latency_total", 0) for r in runs if r.get("latency_total", 0) > 0]
    in_tokens = sum(r.get("input_tokens", 0) or 0 for r in runs)
    out_tokens = sum(r.get("output_tokens", 0) or 0 for r in runs)

    # Score por pilar
    by_pillar = defaultdict(list)
    for r in runs:
        suite = r.get("suite", "")
        pillar = SUITE_TO_PILLAR.get(suite)
        if pillar and r.get("final") is not None:
            by_pillar[pillar].append(r["final"])
    pillars = {p: round(sum(s) / len(s), 2) for p, s in by_pillar.items() if s}

    return {
        "runs": len(runs),
        "score_global": round(sum(scores) / len(scores), 2) if scores else None,
        "score_by_pillar": pillars,
        "judge_score_avg": round(sum(judge_scores) / len(judge_scores), 2) if judge_scores else None,
        "tokens_per_second": round(sum(speeds) / len(speeds), 1) if speeds else None,
        "latency_avg_s": round(sum(latencies) / len(latencies), 2) if latencies else None,
        "total_input_tokens": in_tokens,
        "total_output_tokens": out_tokens,
    }


def build_export():
    by_model = load_all_results()
    models_export = []

    for cfg_key, cfg in MODELS.items():
        model_id = cfg["id"]
        runs = by_model.get(model_id, [])
        # Si el id de OpenRouter difiere, intentar matching loose
        if not runs:
            runs = by_model.get(cfg_key, [])

        metrics = aggregate_metrics(runs) if runs else {
            "runs": 0,
            "score_global": None,
            "score_by_pillar": {},
            "judge_score_avg": None,
            "tokens_per_second": None,
            "latency_avg_s": None,
            "total_input_tokens": 0,
            "total_output_tokens": 0,
        }

        # Costo por 1000 calls asumiendo 300 input + 1500 output tokens/call
        ci = cfg.get("cost_input", 0) or 0
        co = cfg.get("cost_output", 0) or 0
        cost_per_1k_calls = (300_000 * ci + 1_500_000 * co) / 1_000_000

        models_export.append({
            "key": cfg_key,
            "id": model_id,
            "name": cfg.get("name", cfg_key),
            "tier": cfg.get("tier", "?"),
            "provider": cfg.get("provider", "openrouter"),
            "open_source": cfg.get("open_source", False),
            "license": cfg.get("license", ""),
            "cost_input_per_M": ci,
            "cost_output_per_M": co,
            "cost_per_1k_calls_usd": round(cost_per_1k_calls, 3),
            "notes": cfg.get("notes", ""),
            "tested": metrics["runs"] >= 50,  # >= 50 runs = cobertura completa
            **metrics,
        })

    # Sort: tested first, then by score desc
    models_export.sort(key=lambda m: (not m["tested"], -(m.get("score_global") or 0)))

    return {
        "generated_at": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
        "total_models": len(models_export),
        "tested_count": sum(1 for m in models_export if m["tested"]),
        "tokens_per_call_assumption": {"input": 300, "output": 1500},
        "models": models_export,
    }


def main():
    out_path = Path(__file__).parent.parent / "docs" / "data" / "models.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    export = build_export()
    out_path.write_text(json.dumps(export, indent=2, ensure_ascii=False))
    print(f"OK escrito: {out_path}")
    print(f"  Total modelos: {export['total_models']}")
    print(f"  Con cobertura (≥50 runs): {export['tested_count']}")


if __name__ == "__main__":
    main()
