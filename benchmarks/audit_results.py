#!/usr/bin/env python3
"""
Auditoría de comparabilidad de resultados del benchmark.

Objetivos:
1. Detectar modelos medidos con distintas suites/versiones.
2. Comparar score_global lineal vs z-scoreado.
3. Ver impacto de incluir/excluir long-context (niah) y seguridad (prompt_injection).
4. Ver estabilidad de modelos con múltiples runs.
5. Detectar inconsistencias juez/no juez.
"""
import json
import glob
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


def main():
    by_model = load_all()
    print(f"Modelos/variantes con resultados: {len(by_model)}")

    # 1. Cobertura por modelo
    print("\n=== COBERTURA (runs generales: excluyendo niah y prompt_injection) ===")
    coverage = []
    for (mid, mname), runs in by_model.items():
        general = [r for r in runs if not str(r.get("suite", "")).startswith(("niah", "prompt_injection"))]
        niah = [r for r in runs if str(r.get("suite", "")).startswith("niah")]
        sec = [r for r in runs if str(r.get("suite", "")).startswith("prompt_injection")]
        coverage.append({
            "name": mname,
            "id": mid,
            "general": len(general),
            "niah": len(niah),
            "security": len(sec),
        })

    for c in sorted(coverage, key=lambda x: -x["general"])[:30]:
        marker = "✅" if c["general"] >= 50 else "⚠️"
        print(f"{marker} {c['name']:45s} general={c['general']:4d} niah={c['niah']:4d} sec={c['security']:4d}")

    # 2. Suites disponibles por modelo
    print("\n=== SUITES POR MODELO (top modelos por cobertura) ===")
    for (mid, mname), runs in sorted(by_model.items(), key=lambda x: -len([r for r in x[1] if not str(r.get('suite','')).startswith(('niah','prompt_injection'))]))[:10]:
        general = [r for r in runs if not str(r.get("suite", "")).startswith(("niah", "prompt_injection"))]
        suites = sorted(set(r.get("suite") for r in general))
        print(f"\n{mname}: {len(general)} runs, {len(suites)} suites")
        print(", ".join(suites))

    # 3. Score lineal vs z-score (simulado)
    print("\n=== SCORE LINEAL (promedio de final recalc) VS RANKING ===")
    model_scores = []
    for (mid, mname), runs in by_model.items():
        general = [r for r in runs if not str(r.get("suite", "")).startswith(("niah", "prompt_injection"))]
        if len(general) < 50:
            continue
        finals = [r.get("final", 0) for r in general if r.get("final") is not None]
        qualities = [r.get("quality") for r in general if r.get("quality") is not None]
        speeds = [r.get("tokens_per_second", 0) for r in general if r.get("tokens_per_second")]
        latencies = [r.get("latency_total", 0) for r in general if r.get("latency_total")]
        costs = [r.get("cost_usd", 0) for r in general]
        judge = [r.get("judge_score") for r in general if r.get("judge_score") is not None]
        model_scores.append({
            "name": mname,
            "runs": len(general),
            "final_avg": sum(finals)/len(finals),
            "quality_avg": sum(qualities)/len(qualities),
            "judge_avg": sum(judge)/len(judge) if judge else None,
            "toks": sum(speeds)/len(speeds),
            "lat": sum(latencies)/len(latencies),
            "cost": sum(costs)/len(costs),
        })

    # z-score simple sobre quality/cost/speed/latency (simulando export_for_pages)
    # Asumimos cost_score logarítmico aproximado para el análisis
    import math
    def cost_score_log(c):
        if c <= 1e-6:
            return 10.0
        return max(0.0, min(10.0, 8.0 - 3.0 * math.log10(c / 0.001)))

    def normalize(vals):
        mu = statistics.mean(vals)
        sd = statistics.pstdev(vals)
        return mu, sd

    tested = [m for m in model_scores if m["runs"] >= 50]
    q_mu, q_sd = normalize([m["quality_avg"] for m in tested])
    c_mu, c_sd = normalize([cost_score_log(m["cost"]) for m in tested])
    s_mu, s_sd = normalize([m["toks"] for m in tested])
    l_mu, l_sd = normalize([m["lat"] for m in tested])

    weights = {"q": 0.60, "c": 0.20, "s": 0.10, "l": 0.10}
    for m in tested:
        zq = (m["quality_avg"] - q_mu) / q_sd
        zc = (cost_score_log(m["cost"]) - c_mu) / c_sd
        zs = (m["toks"] - s_mu) / s_sd
        zl = (m["lat"] - l_mu) / l_sd
        z_comp = weights["q"]*zq + weights["c"]*zc + weights["s"]*zs + weights["l"]*zl
        # Nota: en el export real, speed/latency son scores normalizados, no raw.
        # Aquí usamos raw para mostrar la sensibilidad; el orden no es exacto.
        m["zscore"] = max(0.0, min(10.0, 5.5 + 3.3 * z_comp))

    print("\nTop 20 por score lineal (promedio final):")
    for i, m in enumerate(sorted(tested, key=lambda x: -x["final_avg"])[:20], 1):
        print(f"{i:2d}. {m['name']:40s} final={m['final_avg']:.2f} quality={m['quality_avg']:.2f} cost=${m['cost']:.5f} tok/s={m['toks']:.0f}")

    print("\nTop 20 por z-score aproximado:")
    for i, m in enumerate(sorted(tested, key=lambda x: -x["zscore"])[:20], 1):
        print(f"{i:2d}. {m['name']:40s} zscore={m['zscore']:.2f} final={m['final_avg']:.2f} quality={m['quality_avg']:.2f}")

    # 4. Estabilidad de modelos con múltiples lotes
    print("\n=== ESTABILIDAD (modelos con ≥2 archivos distintos) ===")
    by_model_file = defaultdict(lambda: defaultdict(list))
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
            by_model_file[key][fn.name].append(r)

    for (mid, mname), files in sorted(by_model_file.items(), key=lambda x: -sum(len(v) for v in x[1].values())):
        if len(files) < 2:
            continue
        avgs = []
        for fname, runs in files.items():
            general = [r for r in runs if not str(r.get("suite", "")).startswith(("niah", "prompt_injection"))]
            if general:
                avgs.append((fname, sum(r.get("quality", 0) for r in general)/len(general)))
        if len(avgs) >= 2:
            vals = [a[1] for a in avgs]
            print(f"\n{mname}: quality por lote (std={statistics.pstdev(vals):.2f})")
            for fname, q in avgs:
                print(f"  {fname}: {q:.2f}")


if __name__ == "__main__":
    main()
