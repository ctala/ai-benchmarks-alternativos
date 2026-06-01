#!/usr/bin/env python3
"""Recalcula cost_usd, cost_score y final de los runs históricos usando el
precio POR-PROVEEDOR del config (`models.py`) — fuente única de verdad.

Por qué existe: el costo de un modelo **depende del proveedor** por el que se
accede (OpenRouter vs Groq vs NIM gratis vs suscripción). El runner viejo
costeaba con un dict global keyed por id (`PRICING`), ambiguo cuando el mismo id
corre en varios proveedores (ej. Kimi K2.5 pago en OpenRouter vs $0 en NIM).
Este script alinea el costo guardado con el precio declarado en cada entrada del
config, identificando la entrada por el NOMBRE del modelo (único por proveedor,
es lo que el runner guarda en `model`). Así una corrección de precio se refleja
en TODOS los artefactos (calculadora, MDs por modelo, tabla MODELOS) sin
re-correr el benchmark.

NO toca quality, tokens, latencia, tool_calling ni respuestas. Solo los 3 campos
derivados de precio: cost_usd, cost_score, final. Idempotente.

Uso:
    python benchmarks/rescore_costs.py            # aplica in-place
    python benchmarks/rescore_costs.py --dry-run  # solo reporta, no escribe
"""
import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean

sys.path.insert(0, str(Path(__file__).parent.parent))
from benchmarks.models import MODELS, OLLAMA_MODELS
from benchmarks.scoring import PRICING, compute_final_score


def build_price_map():
    """name -> (cost_input, cost_output) desde el config. name es único por
    proveedor (el runner guarda model_config['name'] en cada run)."""
    by_name = {}
    collisions = set()
    for cfg in {**MODELS, **OLLAMA_MODELS}.values():
        name = cfg.get("name")
        ci, co = cfg.get("cost_input"), cfg.get("cost_output")
        if name is None or ci is None or co is None:
            continue
        if name in by_name and by_name[name] != (float(ci), float(co)):
            collisions.add(name)
        by_name[name] = (float(ci), float(co))
    return by_name, collisions


def price_for(run, by_name):
    name = run.get("model")
    if name in by_name:
        return by_name[name]
    mid = run.get("model_id")
    if mid in PRICING:
        return PRICING[mid]
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", default=None,
                    help="Lista de nombres de modelo (coma-separada) a rescorear. "
                         "Si se omite, rescorea TODOS (rescore provider-aware total).")
    args = ap.parse_args()

    only_set = None
    if args.only:
        only_set = {n.strip() for n in args.only.split(",") if n.strip()}
        print(f"Scoped a {len(only_set)} modelos: {sorted(only_set)}")

    by_name, collisions = build_price_map()
    if collisions:
        print(f"WARN nombres con precio ambiguo (último gana): {sorted(collisions)}")

    results_dir = Path(__file__).parent / "results"
    files = sorted(results_dir.glob("benchmark_*.json"))

    total = changed = unmatched = no_tokens = 0
    unmatched_names = set()
    before = defaultdict(list)
    after = defaultdict(list)

    for fn in files:
        data = json.loads(fn.read_text())
        runs = data if isinstance(data, list) else data.get("results", [])
        file_changed = False
        for r in runs:
            if not r.get("success") or r.get("quality") is None:
                continue
            name = r.get("model", "?")
            if only_set is not None and name not in only_set:
                continue
            total += 1
            old_final = r.get("final")
            if old_final is not None:
                before[name].append(old_final)

            prices = price_for(r, by_name)
            it = r.get("input_tokens", 0) or 0
            ot = r.get("output_tokens", 0) or 0
            if prices is None or not (it or ot):
                if prices is None:
                    unmatched += 1
                    unmatched_names.add(name)
                else:
                    no_tokens += 1
                if old_final is not None:
                    after[name].append(old_final)
                continue

            new_cost = (it / 1_000_000) * prices[0] + (ot / 1_000_000) * prices[1]
            sc = compute_final_score(
                r["quality"], r.get("speed", 0) or 0, r.get("latency", 0) or 0,
                r.get("tool_calling", 0) or 0, new_cost,
            )
            after[name].append(sc["final"])

            if (round(r.get("cost_usd", -1), 6) != sc["cost_usd"]
                    or round(r.get("cost_score", -1), 2) != sc["cost_score"]
                    or round(old_final if old_final is not None else -1, 2) != sc["final"]):
                r["cost_usd"] = sc["cost_usd"]
                r["cost_score"] = sc["cost_score"]
                r["final"] = sc["final"]
                changed += 1
                file_changed = True

        if file_changed and not args.dry_run:
            fn.write_text(json.dumps(data, indent=2, ensure_ascii=False))

    mode = "DRY-RUN" if args.dry_run else "APLICADO"
    print(f"[{mode}] runs evaluados: {total} · cambiados: {changed} · "
          f"sin precio (match): {unmatched} · sin tokens: {no_tokens}")
    if unmatched_names:
        print(f"  nombres sin match en config (usan PRICING/stored): "
              f"{sorted(unmatched_names)}")

    deltas = []
    for name in after:
        b, a = before.get(name), after.get(name)
        if b and a and len(a) >= 20:
            deltas.append((mean(a) - mean(b), name, mean(b), mean(a), len(a)))
    deltas.sort(key=lambda x: -abs(x[0]))
    print("\nTop deltas de avg final por modelo (>=20 runs, |delta|>=0.01):")
    for d, name, b, a, n in deltas:
        if abs(d) >= 0.01:
            print(f"  {d:+.3f}  {name}: {b:.2f} -> {a:.2f}  (n={n})")


if __name__ == "__main__":
    main()
