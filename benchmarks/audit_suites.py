#!/usr/bin/env python3
"""
¿Cada suite y cada eje publicado MIDE lo que su nombre dice que mide?

POR QUÉ EXISTE
--------------
El 12-ago-2026 encontramos, de a uno y por sospecha del usuario, que:

  · `structured_output` publicaba **5,00 fijo** en los 117 modelos (varianza cero)
  · `orchestration` tenía correlación **−0,07** con elegir bien la herramienta
    y **+0,55** con la prosa: medía redacción, no orquestación
  · `agentic_score` —el eje que publicamos como "Agentes"— correlaciona **−0,26**
    con el tool calling real. Los peores usando herramientas encabezaban la página
    de agentes.

Los tres son la misma falla: **una métrica con un nombre que no le corresponde**. Y
los tres aparecieron por casualidad, encadenando dudas. Eso no escala: si hace falta
que alguien sospeche para encontrarlos, los que nadie sospeche siguen publicados.

Este script busca esa clase entera, sin lista escrita a mano.

QUÉ DETECTA
-----------
1. **Varianza cero o casi cero** → la suite no distingue modelos: no mide nada.
2. **La nota la manda una señal que no es la propia de la suite.** La señal esperada
   se INFIERE de los tests (si dan herramientas → tools; si tienen `expected_answer`
   → sustancia; si no → prosa/juez), no de una tabla que haya que mantener.
3. **Ejes publicados desalineados**: un eje cuyo nombre promete X y correlaciona ~0
   o negativo con X.
4. **Campos calculados y no persistidos**: si el runner lo computa y el JSON no lo
   guarda, la pregunta que ese campo responde no se puede auditar después.

Uso:
    python benchmarks/audit_suites.py            # reporte
    python benchmarks/audit_suites.py --strict   # exit 1 si hay problemas
"""
import argparse
import glob
import json
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean, pstdev

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

# Bajo esta desviación, una suite no distingue modelos.
MIN_STD = 0.35
# Bajo esta correlación, la señal propia de la suite NO manda su nota.
MIN_CORR_PROPIA = 0.30


def _corr(a, b):
    if len(a) < 20:
        return None
    ma, mb = mean(a), mean(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    den = (sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b)) ** 0.5
    return num / den if den else 0.0


def señal_esperada(tests: list) -> str:
    """Qué DEBERÍA mandar la nota de esta suite, inferido de sus propios tests."""
    if any(t.get("tools") or t.get("expected_tools") for t in tests):
        return "tool_calling"
    if any(t.get("expected_answer") for t in tests):
        return "answer_score"
    return "content_score"


def cargar_runs():
    por_suite = defaultdict(list)
    for f in glob.glob(str(ROOT / "benchmarks/results/benchmark_*.json")):
        d = json.loads(Path(f).read_text())
        rs = d if isinstance(d, list) else d.get("results", [])
        for r in rs:
            if r.get("success") and r.get("quality") is not None and r.get("suite"):
                por_suite[r["suite"]].append(r)
    return por_suite


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="exit 1 si hay problemas")
    args = ap.parse_args()

    from benchmarks.runner import ALL_TEST_SUITES
    from providers.adapters import BenchmarkResult
    import dataclasses

    runs = cargar_runs()
    problemas = []

    print("=" * 78)
    print("  ¿CADA SUITE MIDE LO QUE SU NOMBRE DICE?")
    print("=" * 78)
    print(f"\n{'SUITE':<24} {'n':>5} {'std':>6} {'señal propia':>14} {'corr':>7}  veredicto")
    for suite in sorted(runs):
        rs = runs[suite]
        q = [r["quality"] for r in rs]
        tests = ALL_TEST_SUITES.get(suite, [])
        esperada = señal_esperada(tests) if tests else "?"
        pares = [(r.get(esperada), r["quality"]) for r in rs if r.get(esperada) is not None]
        c = _corr([p[0] for p in pares], [p[1] for p in pares]) if len(pares) >= 20 else None
        std = pstdev(q) if len(q) > 1 else 0.0

        veredicto = "ok"
        if std < MIN_STD:
            veredicto = f"🔴 VARIANZA {std:.2f}: no distingue modelos"
            problemas.append((suite, veredicto))
        elif c is not None and c < MIN_CORR_PROPIA:
            # ¿qué manda entonces?
            alt = {}
            for k in ("content_score", "answer_score", "tool_calling", "judge_score"):
                p2 = [(r.get(k), r["quality"]) for r in rs if r.get(k) is not None]
                if len(p2) >= 20:
                    alt[k] = _corr([x[0] for x in p2], [x[1] for x in p2]) or 0
            manda = max(alt, key=lambda k: alt[k]) if alt else "?"
            if manda != esperada and alt.get(manda, 0) > (c or 0) + 0.2:
                veredicto = f"🔴 la manda `{manda}` ({alt[manda]:+.2f}), no `{esperada}`"
                problemas.append((suite, veredicto))
        print(f"  {suite:<22} {len(rs):>5} {std:>6.2f} {esperada:>14} "
              f"{(f'{c:+.2f}' if c is not None else '   —'):>7}  {veredicto}")

    # ── Ejes publicados ─────────────────────────────────────────────────────
    print("\n" + "=" * 78)
    print("  EJES PUBLICADOS — ¿el nombre corresponde con lo que correlaciona?")
    print("=" * 78)
    exp = json.loads((ROOT / "docs/data/models.json").read_text())
    SUITES_TOOLS = {"tool_calling", "customer_support", "orchestration", "agent_capabilities"}
    tc_real = defaultdict(list)
    for s in SUITES_TOOLS:
        for r in runs.get(s, []):
            if r.get("tool_calling") is not None:
                tc_real[r["model"]].append(r["tool_calling"])
    filas = [(mean(v), m["agentic_score"]) for m in exp["models"]
             if m.get("ranked") and m.get("agentic_score") is not None
             for v in [tc_real.get(m["name"], [])] if len(v) >= 10]
    if filas:
        c = _corr([f[0] for f in filas], [f[1] for f in filas])
        estado = "🔴 DESALINEADO" if (c is None or c < 0.3) else "ok"
        print(f"\n  `agentic_score` (se publica como «Agentes»)")
        print(f"     correlación con el tool calling REAL: {c:+.2f}  sobre {len(filas)} modelos  {estado}")
        if estado.startswith("🔴"):
            problemas.append(("agentic_score", f"correlación {c:+.2f} con tool calling"))
            print(f"     └ sale solo de `agent_long_horizon` (multi-turno, sin herramientas):")
            print(f"       mide coherencia conversacional, no capacidad agéntica.")

    # ── Campos que se calculan y no se guardan ──────────────────────────────
    print("\n" + "=" * 78)
    print("  AUDITABILIDAD — ¿se guarda lo que se calcula?")
    print("=" * 78)
    campos = {f.name for f in dataclasses.fields(BenchmarkResult)}
    guardados = set()
    for f in sorted(glob.glob(str(ROOT / "benchmarks/results/benchmark_*.json")))[-6:]:
        d = json.loads(Path(f).read_text())
        for r in (d if isinstance(d, list) else d.get("results", [])):
            guardados |= set(r.keys())
    # `prompt` y `response` viven en el .md a propósito; el resto debería estar.
    EN_MD = {"prompt", "response", "provider", "score"}
    faltan = sorted(campos - guardados - EN_MD)
    if faltan:
        print(f"\n  🔴 calculados y NO persistidos: {faltan}")
        print("     Un campo que no se guarda no puede auditarse después sin re-medir.")
        problemas.append(("persistencia", str(faltan)))
    else:
        print("\n  ✓ todo lo que se calcula se guarda (o vive en el .md a propósito)")

    # ── Endpoints :free ─────────────────────────────────────────────────────
    #
    # REGLA (Cristian, 12-ago-2026): **nunca medir en un endpoint `:free`.**
    #
    # Medido ese día: los runs contra ids `:free` fallan **69,2%** (651 de 941),
    # contra **10,9%** de los pagos — seis veces más. Un free tier tiene rate limits
    # agresivos, puede servirse con otra cuantización y puede desaparecer sin aviso.
    # Nada de eso es el modelo, y todo entra al número que publicamos.
    #
    # No siempre hay alternativa en OpenRouter: `nemotron-nano-9b-v2` y
    # `nemotron-3-nano-omni-...-reasoning` SOLO existen como `:free` ahí. Los dos están
    # en NVIDIA NIM, que es la ruta correcta para medirlos.
    print("\n" + "=" * 78)
    print("  ENDPOINTS `:free` — regla: nunca medir ahí")
    print("=" * 78)
    from benchmarks.models import MODELS as _M2, OLLAMA_MODELS as _O2
    libres = [(k, c) for k, c in {**_M2, **_O2}.items()
              if ":free" in str(c.get("id", "")) and not c.get("retired")]
    rank_names = {m["name"] for m in exp["models"] if m.get("ranked")}
    if libres:
        print()
        for k, c in libres:
            rk = "  ← RANKEADO" if c.get("name") in rank_names else ""
            print(f"     {k:<36} {c.get('id')}{rk}")
        rankeados = [k for k, c in libres if c.get("name") in rank_names]
        if rankeados:
            problemas.append((":free", f"{len(rankeados)} rankeados medidos en free tier: {rankeados}"))
        print(f"\n     {len(libres)} entradas con id `:free` · {len(rankeados)} de ellas RANKEADAS")
    else:
        print("\n  ✓ ninguna entrada usa un endpoint `:free`")

    print("\n" + "=" * 78)
    print(f"  PROBLEMAS DETECTADOS: {len(problemas)}")
    for s, v in problemas:
        print(f"     · {s}: {v}")
    print("=" * 78)
    return 1 if (problemas and args.strict) else 0


if __name__ == "__main__":
    sys.exit(main())
