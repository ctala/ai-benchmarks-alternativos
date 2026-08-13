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


# ── Estimación PROSPECTIVA ────────────────────────────────────────────────────
# Por qué existe (12-ago-2026): la Regla 0.5 del RUNBOOK ya decía que multi-turno
# dispara los tokens "muy por encima del promedio". Estaba escrita, y aun así
# estimé Grupo A en $15,09 cuando iba a costar ~$32 — el doble.
#
# La causa es aritmética y no se ve promediando: `agent_long_horizon` reenvía la
# conversación entera en cada turno, así que un test de 13 turnos paga el
# contexto 13 veces, creciendo. Medido en Claude Opus 5 Fast: 25.837 tokens de
# input por run contra ~300 de una suite normal — **86×**. Esa suite se llevó el
# 44% del costo del modelo en el 7,5% de los runs.
#
# Estimar con un promedio global de $/run reparte ese pico entre 192 runs y lo
# esconde. Por eso este estimador proyecta **por suite**, nunca en bloque.
def estimar(modelo_ref: str, precio_in: float, precio_out: float, results_dir: str):
    """Proyecta el costo del examen completo usando el consumo real por suite
    de un examen ya medido (`modelo_ref`), aplicado a otro precio."""
    import glob
    from collections import defaultdict

    runs = []
    for f in glob.glob(os.path.join(results_dir, "*.json")):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        # algunos JSONs históricos son una lista pelada de runs, no {"results": [...]}
        items = d if isinstance(d, list) else d.get("results", [])
        for r in items:
            if not isinstance(r, dict):
                continue
            if r.get("model_id") == modelo_ref or r.get("model") == modelo_ref:
                if r.get("success"):
                    runs.append(r)
    if not runs:
        print(f"✗ no hay runs de '{modelo_ref}' para usar como referencia")
        return 1

    por = defaultdict(lambda: [0, 0, 0])  # suite -> [n, tok_in, tok_out]
    for r in runs:
        s = r.get("suite", "?")
        por[s][0] += 1
        por[s][1] += r.get("input_tokens") or 0
        por[s][2] += r.get("output_tokens") or 0

    print(f"Referencia: {modelo_ref} · {len(runs)} runs · {len(por)} suites")
    print(f"Precio objetivo: ${precio_in}/M in · ${precio_out}/M out\n")
    print(f"  {'suite':<24} {'runs':>5} {'tok-in/run':>11} {'$/run':>8} {'$ suite':>9}")
    total = 0.0
    for s, (n, ti, to) in sorted(por.items(), key=lambda x: -(x[1][1] / max(x[1][0], 1))):
        c = (ti / 1_000_000) * precio_in + (to / 1_000_000) * precio_out
        total += c
        marca = "  ⚠ multi-turno" if ti / max(n, 1) > 5000 else ""
        print(f"  {s:<24} {n:>5} {ti/max(n,1):>11,.0f} {c/max(n,1):>8.3f} {c:>9.2f}{marca}")
    print(f"\n  TOTAL examen completo ≈ ${total:.2f}")
    # Si la referencia es un examen a medias, el total sale corto EN SILENCIO —
    # el mismo modo de falla que este estimador vino a evitar. Que grite.
    if len(runs) < 170:
        falta = 192 - len(runs)
        print(f"  ⚠️  REFERENCIA INCOMPLETA: {len(runs)}/192 runs. Faltan ~{falta} y el "
              f"total de arriba NO los incluye.\n"
              f"     Si los que faltan son de una suite multi-turno, el costo real es "
              f"bastante mayor. Usá una referencia completa.")
    caras = {s: v for s, v in por.items() if v[1] / max(v[0], 1) > 5000}
    if caras:
        cc = sum((v[1]/1_000_000)*precio_in + (v[2]/1_000_000)*precio_out for v in caras.values())
        nn = sum(v[0] for v in caras.values())
        print(f"  de los cuales {', '.join(caras)}: ${cc:.2f} "
              f"({cc/total*100:.0f}% del costo en {nn/len(runs)*100:.0f}% de los runs)")
    return 0


def gastado(prefijo: str, results_dir: str):
    """Cuánto se gastó DE VERDAD en un lote, separando lo pagado de lo nocional.

    Por qué existe (13-ago-2026): reporté $40,45 de gasto y la key de OpenRouter
    marcaba $77,32. No mentí un total: sumé a mano solo los modelos que estaba
    mirando en los reportes de avance y me salté siete archivos, entre ellos uno de
    $17,69. **No había instrumento que sumara todo** — el mismo patrón que el resto
    del repo documenta cinco veces.

    Y separa lo nocional porque si no, sobra: las variantes de suscripción
    (`provider: claude_code`) se costean al precio de OpenRouter para que la
    comparación sea justa, pero **no se pagan**. Sumadas al total daban $95,66
    contra $77,32 de la key. Descontadas: $77,57. Cuadra con 25 centavos de
    diferencia por redondeo.

    Uso:  python benchmarks/calculate_costs.py --gastado 20260812
    """
    import glob
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from benchmarks.models import MODELS, OLLAMA_MODELS
    catalogo = {**MODELS, **OLLAMA_MODELS}
    nocionales = {c.get("id") for c in catalogo.values()
                  if c.get("provider") in ("claude_code",)}

    pagado = nocional = 0.0
    filas = []
    for f in sorted(glob.glob(os.path.join(results_dir, f"benchmark_{prefijo}*.json"))):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        items = d if isinstance(d, list) else d.get("results", [])
        c_pag = c_noc = 0.0
        for r in items:
            if not isinstance(r, dict):
                continue
            c = r.get("cost_usd") or 0
            if r.get("model_id") in nocionales:
                c_noc += c
            else:
                c_pag += c
        if c_pag or c_noc:
            filas.append((c_pag, c_noc, len(items), os.path.basename(f)))
        pagado += c_pag
        nocional += c_noc

    filas.sort(key=lambda x: -(x[0] + x[1]))
    print(f"  {'pagado':>9} {'nocional':>9} {'runs':>6}  archivo")
    for cp, cn, k, f in filas:
        marca = "  ← suscripción, NO se paga" if cn > cp else ""
        print(f"  {cp:>9.2f} {cn:>9.2f} {k:>6}  {f[:44]}{marca}")
    print(f"\n  GASTO REAL (lo que cobra el proveedor): ${pagado:.2f}")
    if nocional:
        print(f"  nocional por suscripción (comparabilidad): ${nocional:.2f}")
        print(f"  suma de cost_usd, que NO es el gasto:      ${pagado + nocional:.2f}")
    print("\n  Contrastá contra el dashboard del proveedor. Si no cuadra, falta un archivo.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--markdown", action="store_true", help="Emitir tabla en formato Markdown")
    ap.add_argument("--results-dir", default="benchmarks/results", help="Carpeta con JSONs")
    ap.add_argument("--estimar", metavar="MODELO",
                    help="Proyectar el costo de un examen completo ANTES de lanzarlo, "
                         "por suite. Requiere --precio-in/--precio-out del modelo objetivo "
                         "y usa MODELO (ya medido) como referencia de consumo.")
    ap.add_argument("--precio-in", type=float, help="USD por millón de tokens de input")
    ap.add_argument("--precio-out", type=float, help="USD por millón de tokens de output")
    ap.add_argument("--gastado", metavar="PREFIJO",
                    help="Cuánto se gastó de verdad en un lote (ej. 20260812), separando "
                         "lo pagado de lo nocional por suscripción. Contrastar con la key.")
    args = ap.parse_args()

    if args.gastado:
        sys.exit(gastado(args.gastado, args.results_dir))

    if args.estimar:
        if args.precio_in is None or args.precio_out is None:
            ap.error("--estimar requiere --precio-in y --precio-out")
        sys.exit(estimar(args.estimar, args.precio_in, args.precio_out, args.results_dir))

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
