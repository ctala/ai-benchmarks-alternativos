#!/usr/bin/env python3
"""
Compara diferentes métodos de calcular el score global:
1. Promedio por test (actual)
2. Promedio por suite (normaliza por suite)
3. Promedio por pilar
4. Solo tests comunes a todos
"""
import json
import glob
import math
import statistics
from collections import defaultdict
from pathlib import Path

RESULTS_DIR = Path(__file__).parent / "results"


def load_all():
    by_model = defaultdict(list)
    for fn in sorted(RESULTS_DIR.glob("benchmark_*.json")):
        try:
            data = json.loads(fn.read_text())
        except Exception:
            continue
        results = data if isinstance(data, list) else data.get("results", [])
        for r in results:
            if not r.get("success"):
                continue
            key = (r.get("model_id", "?"), r.get("model", "?"))
            by_model[key].append(r)
    return by_model


def cost_score_log(c):
    if c <= 1e-6:
        return 10.0
    return max(0.0, min(10.0, 8.0 - 3.0 * math.log10(c / 0.001)))


def main():
    by_model = load_all()

    # Modelos con cobertura ≥50 tests generales
    models = {}
    for (mid, mname), runs in by_model.items():
        general = [r for r in runs if not str(r.get("suite", "")).startswith(("niah", "prompt_injection"))]
        if len(general) >= 50:
            models[mname] = {"id": mid, "runs": general}

    # Tests comunes a todos
    all_keys = [{(r.get("suite"), r.get("test_name")) for r in m["runs"]} for m in models.values()]
    common_keys = set.intersection(*all_keys)

    # Métricas por modelo bajo distintos métodos
    rows = []
    for mname, info in models.items():
        runs = info["runs"]

        # Método 1: promedio por test
        q_test = statistics.mean(r.get("quality", 0) for r in runs)
        f_test = statistics.mean(r.get("final", 0) for r in runs)

        # Método 2: promedio por suite
        by_suite = defaultdict(list)
        for r in runs:
            by_suite[r.get("suite")].append(r.get("final", 0))
        suite_avgs = [sum(v)/len(v) for v in by_suite.values()]
        f_suite = sum(suite_avgs)/len(suite_avgs) if suite_avgs else 0

        # Método 3: solo tests comunes
        common_runs = [r for r in runs if (r.get("suite"), r.get("test_name")) in common_keys]
        f_common = statistics.mean(r.get("final", 0) for r in common_runs) if common_runs else 0
        q_common = statistics.mean(r.get("quality", 0) for r in common_runs) if common_runs else 0

        # Componentes para z-score
        speeds = [r.get("tokens_per_second", 0) for r in runs if r.get("tokens_per_second")]
        latencies = [r.get("latency_total", 0) for r in runs if r.get("latency_total")]
        costs = [r.get("cost_usd", 0) for r in runs]
        avg_speed = sum(speeds)/len(speeds) if speeds else 0
        avg_lat = sum(latencies)/len(latencies) if latencies else 0
        avg_cost = sum(costs)/len(costs) if costs else 0

        rows.append({
            "name": mname,
            "runs": len(runs),
            "q_test": q_test,
            "f_test": f_test,
            "f_suite": f_suite,
            "f_common": f_common,
            "q_common": q_common,
            "speed": avg_speed,
            "lat": avg_lat,
            "cost": avg_cost,
        })

    # Calcular z-score con método por suite (más robusto)
    tested = [r for r in rows]
    cols = {
        "q_test": ([r["q_test"] for r in tested], 0.60),
        "cost": ([cost_score_log(r["cost"]) for r in tested], 0.20),
        "speed": ([r["speed"] for r in tested], 0.10),
        "lat": ([-r["lat"] for r in tested], 0.10),  # latencia negativa: menor es mejor
    }
    stats = {}
    for c, (vals, w) in cols.items():
        mu = statistics.mean(vals)
        sd = statistics.pstdev(vals)
        stats[c] = (mu, sd, w)

    for r in rows:
        z = 0
        for c, (mu, sd, w) in stats.items():
            val = r["q_test"] if c == "q_test" else (cost_score_log(r["cost"]) if c == "cost" else (r["speed"] if c == "speed" else -r["lat"]))
            z += w * ((val - mu) / sd if sd > 0 else 0)
        r["z_suite"] = max(0.0, min(10.0, 5.5 + 3.3 * z))

    print("=== COMPARACIÓN DE MÉTODOS DE SCORE GLOBAL ===\n")
    print(f"{'Modelo':40s} | test | suite | común | z-suite")
    print("-" * 80)
    for r in sorted(rows, key=lambda x: -x["z_suite"])[:30]:
        print(f"{r['name']:40s} | {r['f_test']:4.2f} | {r['f_suite']:5.2f} | {r['f_common']:5.2f} | {r['z_suite']:7.2f}")

    print("\n=== Kimi K2.7 Code en contexto ===")
    for r in rows:
        if r["name"] == "Kimi K2.7 Code":
            print(f"{r['name']:40s} | {r['f_test']:4.2f} | {r['f_suite']:5.2f} | {r['f_common']:5.2f} | {r['z_suite']:7.2f}")
            print(f"  Quality promedio por test: {r['q_test']:.2f}")
            print(f"  Costo promedio por test: ${r['cost']:.5f}")
            print(f"  Velocidad: {r['speed']:.0f} tok/s, latencia: {r['lat']:.2f}s")


if __name__ == "__main__":
    main()
