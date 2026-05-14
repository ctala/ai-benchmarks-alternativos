"""Análisis de varianza intra-model — 5 runs del mismo prompt en top N modelos.

Mide qué tan estable es el score de un modelo cuando se le hace el mismo prompt
N veces a temperatura 0.7. Output: stdev de quality_score por (model, prompt)
y stdev overall por modelo.

Pregunta: ¿el ranking top 10 es estadísticamente significativo, o el delta entre
posiciones está dentro del ruido intra-model?

Uso:
    python benchmarks/variance_analysis.py --reps 5 --models top5

Output:
    benchmarks/results/variance_<timestamp>.json
"""

import argparse
import json
import statistics
import time
from datetime import datetime
from pathlib import Path

from benchmarks.config import (
    OPENROUTER_API_KEY, GROQ_API_KEY, GROQ_BASE_URL,
    XIAOMI_API_KEY, XIAOMI_BASE_URL, MODELS,
)
from benchmarks.llm_judge import LLMJudge, judge_score_to_10
from benchmarks.tests.reasoning import TESTS as REASONING_TESTS
from benchmarks.tests.code_generation import TESTS as CODE_TESTS
from benchmarks.tests.startup_content import TESTS as STARTUP_TESTS
from benchmarks.tests.tool_calling import TESTS as TOOL_TESTS
from benchmarks.tests.niah_es_lite import TESTS as NIAH_TESTS
from providers.adapters import UnifiedProvider

RESULTS_DIR = Path("benchmarks/results")


def pick_test(suite, name):
    for t in suite:
        if t["name"] == name:
            return t
    raise ValueError(f"Test {name} no encontrado en suite")


VARIANCE_PROMPTS = [
    ("razonamiento", pick_test(REASONING_TESTS, "multi_constraint_decision")),
    ("coding", pick_test(CODE_TESTS, "sql_query_complex")),
    ("contenido", pick_test(STARTUP_TESTS, "blog_actualidad_startup")),
    ("agentes", pick_test(TOOL_TESTS, "single_tool_calendar")),
    ("niah_es", pick_test(NIAH_TESTS, "niah_es_discount_code_4000_p50")),
]


TOP_MODELS_BY_KEY = [
    "groq-llama-4-scout",
    "groq-llama-3.1-8b",
    "devstral",
    "mistral-small-4",
    "groq-gpt-oss-20b",
]


def provider_for(model_key, model_cfg):
    provider_name = model_cfg.get("provider", "openrouter")
    if provider_name == "groq_direct":
        return UnifiedProvider("groq", GROQ_API_KEY, GROQ_BASE_URL)
    if provider_name == "xiaomi_direct":
        return UnifiedProvider("xiaomi", XIAOMI_API_KEY, XIAOMI_BASE_URL)
    return UnifiedProvider("openrouter", OPENROUTER_API_KEY, "https://openrouter.ai/api/v1")


def run_variance(reps: int, model_keys: list[str], output_path: Path):
    judge = LLMJudge(
        api_key="ollama", base_url="http://localhost:11434/v1",
        judge_model="phi4:latest", provider="ollama",
    )

    out = {
        "started_at": datetime.now().isoformat(),
        "reps": reps,
        "model_keys": model_keys,
        "prompts": [{"pilar": p, "name": t["name"], "suite": t.get("suite", "")} for p, t in VARIANCE_PROMPTS],
        "runs": [],
    }

    total = len(model_keys) * len(VARIANCE_PROMPTS) * reps
    done = 0
    for model_key in model_keys:
        cfg = MODELS.get(model_key)
        if not cfg:
            print(f"⚠️  Modelo {model_key} no encontrado en MODELS, skip")
            continue
        provider = provider_for(model_key, cfg)
        model_id = cfg["id"]

        for pilar, test in VARIANCE_PROMPTS:
            for rep_i in range(reps):
                done += 1
                t0 = time.time()
                try:
                    result = provider.chat(
                        model=model_id, messages=test["messages"], tools=None,
                        temperature=0.7, max_tokens=2048, timeout=120,
                    )
                    response = result.response or ""
                    latency = result.latency_total
                    judge_result = judge.evaluate(response, test, suite_name=pilar) if response else {"score_final": -1}
                    score_10 = judge_score_to_10(judge_result)
                except Exception as e:
                    response, latency, score_10 = "", 0, -1
                    judge_result = {"score_final": -1, "error": str(e)}

                out["runs"].append({
                    "model_key": model_key, "pilar": pilar, "test_name": test["name"],
                    "rep": rep_i, "score_10": score_10,
                    "response_chars": len(response), "latency_s": latency,
                    "judge_score_raw": judge_result.get("score_final", -1),
                })
                # Guardado incremental
                output_path.write_text(json.dumps(out, indent=2, ensure_ascii=False))
                print(f"[{done}/{total}] {model_key} | {pilar} | rep={rep_i} | score={score_10:.2f} | {time.time()-t0:.1f}s")

    # Estadísticas
    by_key = {}
    for r in out["runs"]:
        key = (r["model_key"], r["pilar"])
        by_key.setdefault(key, []).append(r["score_10"])

    stats = []
    for (model_key, pilar), scores in by_key.items():
        valid = [s for s in scores if s >= 0]
        if len(valid) >= 2:
            stats.append({
                "model_key": model_key, "pilar": pilar, "n": len(valid),
                "mean": round(statistics.mean(valid), 2),
                "stdev": round(statistics.stdev(valid), 3),
                "min": round(min(valid), 2), "max": round(max(valid), 2),
                "range": round(max(valid) - min(valid), 2),
            })

    out["stats_per_model_pilar"] = stats

    # Overall stdev por modelo (todos los pilares juntos)
    by_model = {}
    for r in out["runs"]:
        if r["score_10"] >= 0:
            by_model.setdefault(r["model_key"], []).append(r["score_10"])
    out["overall_per_model"] = [
        {"model_key": k, "n": len(v), "mean": round(statistics.mean(v), 2),
         "stdev_pooled": round(statistics.stdev(v), 3) if len(v) >= 2 else 0.0}
        for k, v in by_model.items()
    ]

    out["finished_at"] = datetime.now().isoformat()
    output_path.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reps", type=int, default=5)
    parser.add_argument("--models", type=str, default="top5",
                        help="top5 (default) o csv de model_keys")
    args = parser.parse_args()

    if args.models == "top5":
        model_keys = TOP_MODELS_BY_KEY
    else:
        model_keys = [k.strip() for k in args.models.split(",")]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output = RESULTS_DIR / f"variance_{timestamp}.json"
    print(f"Variance analysis: {len(model_keys)} modelos × {len(VARIANCE_PROMPTS)} prompts × {args.reps} reps = {len(model_keys)*len(VARIANCE_PROMPTS)*args.reps} runs")
    print(f"Output: {output}")
    result = run_variance(args.reps, model_keys, output)
    print(f"\nDone. {len(result['runs'])} runs guardados.")
    print(f"\nOverall stdev por modelo:")
    for s in sorted(result["overall_per_model"], key=lambda x: x["stdev_pooled"]):
        print(f"  {s['model_key']:30} mean={s['mean']:.2f} stdev={s['stdev_pooled']:.3f} (n={s['n']})")


if __name__ == "__main__":
    main()
