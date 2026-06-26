#!/usr/bin/env python3
"""
Auditoría de comparabilidad: qué tests son comunes entre modelos y
qué tanto distorsiona comparar scores globales cuando la cobertura difiere.
"""
import json
import glob
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

    # Tests generales (no niah, no prompt_injection)
    general_tests_by_model = {}
    for (mid, mname), runs in by_model.items():
        general = [r for r in runs if not str(r.get("suite", "")).startswith(("niah", "prompt_injection"))]
        if len(general) >= 50:
            general_tests_by_model[mname] = {
                "id": mid,
                "runs": general,
                "keys": {(r.get("suite"), r.get("test_name")) for r in general},
            }

    print(f"Modelos con cobertura ≥50 tests generales: {len(general_tests_by_model)}")

    # Conjunto de tests comunes a TODOS los modelos con cobertura
    all_keys = [m["keys"] for m in general_tests_by_model.values()]
    common_keys = set.intersection(*all_keys) if all_keys else set()
    print(f"Tests generales comunes a todos estos modelos: {len(common_keys)}")

    # Tests totales presentes en al menos un modelo
    union_keys = set.union(*all_keys) if all_keys else set()
    print(f"Tests generales distintos en total (unión): {len(union_keys)}")

    # Matriz de cobertura
    print("\n=== MATRIZ DE COBERTURA POR MODELO ===")
    print(f"{'Modelo':40s} | total | comunes | faltantes | %común")
    print("-" * 80)
    rows = []
    for mname, info in general_tests_by_model.items():
        total = len(info["keys"])
        common = len(info["keys"] & common_keys)
        missing = total - common
        pct = common / total * 100 if total else 0
        rows.append((mname, total, common, missing, pct))
    for row in sorted(rows, key=lambda x: -x[4]):
        print(f"{row[0]:40s} | {row[1]:5d} | {row[2]:7d} | {row[3]:9d} | {row[4]:5.1f}%")

    # Score promedio solo en tests comunes
    print("\n=== SCORE PROMEDIO EN TESTS COMUNES ===")
    print(f"{'Modelo':40s} | quality común | final común | #runs")
    print("-" * 80)
    scores_common = []
    for mname, info in general_tests_by_model.items():
        common_runs = [r for r in info["runs"] if (r.get("suite"), r.get("test_name")) in common_keys]
        if not common_runs:
            continue
        q = sum(r.get("quality", 0) for r in common_runs) / len(common_runs)
        f = sum(r.get("final", 0) for r in common_runs) / len(common_runs)
        scores_common.append((mname, q, f, len(common_runs)))
    for mname, q, f, n in sorted(scores_common, key=lambda x: -x[2])[:25]:
        print(f"{mname:40s} | {q:13.2f} | {f:11.2f} | {n:5d}")

    # Tests no comunes (novedades) y quién los tiene
    print("\n=== TESTS NO COMUNES (presentes en algunos modelos, no en todos) ===")
    non_common = union_keys - common_keys
    by_test = defaultdict(list)
    for mname, info in general_tests_by_model.items():
        for suite, test in info["keys"] - common_keys:
            by_test[(suite, test)].append(mname)
    for (suite, test), models in sorted(by_test.items(), key=lambda x: -len(x[1])):
        print(f"  {suite}/{test}: {len(models)} modelos")
        if len(models) <= 5:
            print(f"    {', '.join(models)}")


if __name__ == "__main__":
    main()
