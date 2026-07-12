#!/usr/bin/env python3
"""
Mide si una suite DISCRIMINA — o sea, si sirve para algo.

LA PREGUNTA QUE RESPONDE
------------------------
Una suite no vale por ser difícil, ni por ser bonita: vale si **separa a los modelos**.
Si un 8B y Opus sacan la misma nota, esa suite no está midiendo nada — solo está
gastando plata en tokens y metiendo ruido en el ranking.

El benchmark tenía este problema y no lo sabía: en `content_generation` la nota media
del juez es 4.73/5 con desviación 0.25. Le pone casi lo mismo a todo el mundo. Con esa
señal, el ranking se ordena por ruido.

QUE MIRA
--------
- **Spread**: cuánto separa al mejor del peor. Si es <1 punto sobre 10, la suite no
  distingue y hay que rediseñarla o tirarla.
- **Señal/ruido**: la separación entre modelos comparada con la variación DENTRO de un
  mismo modelo entre tests. Si el ruido supera a la señal, el orden es azar.
- **Por test**: cuáles tests separan y cuáles los aprueba todo el mundo. Un test que
  todos pasan no aporta información: hay que endurecerlo o sacarlo.

Uso:
    python benchmarks/analyze_discrimination.py --suite business_audit
    python benchmarks/analyze_discrimination.py --suite business_audit --compare content_generation
"""
import argparse
import glob
import json
import statistics as st
from collections import defaultdict


def load(suite, only_file=None):
    """{modelo: {test: quality}} de la suite pedida."""
    per = defaultdict(dict)
    files = [only_file] if only_file else glob.glob("benchmarks/results/benchmark_*.json")
    for f in files:
        try:
            d = json.load(open(f))
        except Exception:
            continue
        rows = d.get("results", []) if isinstance(d, dict) else d
        for r in rows:
            if not isinstance(r, dict) or not r.get("success"):
                continue
            if r.get("suite") != suite:
                continue
            q = r.get("quality")
            if q is None:
                continue
            per[r.get("model", "?")][r.get("test_name")] = float(q)
    return per


def report(suite, per):
    if not per:
        print(f"  (sin runs de `{suite}`)")
        return None

    means = {m: st.mean(v.values()) for m, v in per.items() if v}
    order = sorted(means, key=lambda m: -means[m])

    print(f"\n=== SUITE: {suite} ===")
    print(f"{'modelo':<34}{'media':>8}{'peor test':>11}{'mejor test':>12}{'n':>4}")
    for m in order:
        v = list(per[m].values())
        print(f"  {m[:32]:<34}{means[m]:>8.2f}{min(v):>11.2f}{max(v):>12.2f}{len(v):>4}")

    spread = means[order[0]] - means[order[-1]]
    # Señal = dispersión ENTRE modelos. Ruido = dispersión DENTRO de un modelo.
    signal = st.pstdev(list(means.values())) if len(means) > 1 else 0
    noise = st.median([st.pstdev(list(v.values())) for v in per.values() if len(v) > 1] or [0])

    print(f"\n  spread (mejor − peor):        {spread:.2f} puntos")
    print(f"  señal (std entre modelos):    {signal:.2f}")
    print(f"  ruido (std dentro de uno):    {noise:.2f}")
    if noise:
        ratio = signal / noise
        print(f"  señal/ruido:                  {ratio:.2f}", end="  ")
        print("✅ discrimina" if ratio >= 0.5 else "❌ el ruido domina: no discrimina")

    print(f"\n  --- por test (¿cuáles separan?) ---")
    tests = sorted({t for v in per.values() for t in v})
    for t in tests:
        vals = [v[t] for v in per.values() if t in v]
        if len(vals) < 2:
            continue
        rng = max(vals) - min(vals)
        flag = "✅ separa" if rng >= 2.0 else ("· plano" if rng < 1.0 else "~ débil")
        print(f"    {t:<40} rango {rng:>5.2f}  (media {st.mean(vals):.2f})  {flag}")
    return {"spread": spread, "signal": signal, "noise": noise}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", required=True)
    ap.add_argument("--compare", help="Suite de referencia (p.ej. content_generation)")
    ap.add_argument("--file", help="Analizar solo este JSON de resultados")
    args = ap.parse_args()

    a = report(args.suite, load(args.suite, args.file))
    if args.compare:
        b = report(args.compare, load(args.compare))
        if a and b and b["spread"]:
            print(f"\n>>> `{args.suite}` separa {a['spread'] / b['spread']:.1f}× más que "
                  f"`{args.compare}` ({a['spread']:.2f} vs {b['spread']:.2f} puntos de spread)")


if __name__ == "__main__":
    main()
