#!/usr/bin/env python3
"""
Elige juez con datos, no con intuición.

POR QUÉ EXISTE
--------------
El juez del benchmark era phi-4 (14B) por una razón correcta: Microsoft no tiene modelos
en el benchmark, así que no puede auto-preferirse. Pero "sin conflicto de interés" no
alcanza — **también tiene que discriminar**, y phi-4 no lo hace: sobre 15 respuestas
reales de `business_audit` le puso 5/5 a las 15, incluidas las que fallaron la trampa
aritmética plantada. Desviación 0.00. Correlación con la verdad objetiva: 0.00.

Un juez que aprueba a todos no es un juez blando. Es ruido con 70% del peso.

CÓMO SE ELIGE
-------------
`business_audit` da algo raro y valioso: **verdad objetiva**. Cada test esconde un error
verificable (un P&L cuyos costos suman 9.150 y no 7.400, un churn que mezcla usuarios
gratis con pagados). Sabemos, sin opinar, quién lo cazó y quién no.

Así que el candidato se mide contra esa verdad:

  · **techo**  — % de respuestas a las que les pone la nota máxima. Alto = satura = inútil.
  · **corr**   — correlación con el rúbrico objetivo. Un juez que sirve castiga a quien
                 falló la trampa. Si su correlación es ~0, está puntuando otra cosa
                 (largo, tono, seguridad aparente) y no la calidad del análisis.
  · **desv**   — si es 0, todos empatan y el juez no aporta orden.

Sesgo: se descartan de entrada todos los vendors que TIENEN modelos en el benchmark
(derivado de los IDs reales, no de una lista a mano — Cohere ya se coló una vez así).

Uso:
    python benchmarks/judge_bakeoff.py
    python benchmarks/judge_bakeoff.py --suite business_audit --n 15
"""
import argparse
import random
import re
import statistics as st
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

# Candidatos: vendors SIN modelos en el benchmark (cero auto-preferencia), baratos
# (el juez corre miles de veces) y que devuelvan JSON parseable — los modelos "thinking"
# (OLMo 3 Think, Ring) escupen razonamiento antes del JSON y el parser los rechaza.
CANDIDATOS = [
    ("phi-4 14B (el actual)",     "microsoft/phi-4"),
    ("Hunyuan 3 (Tencent)",       "tencent/hy3"),
    ("Solar Pro 3 (Upstage)",     "upstage/solar-pro-3"),
    ("Ling 2.6 1T (InclusionAI)", "inclusionai/ling-2.6-1t"),
    ("Virtuoso Large (Arcee)",    "arcee-ai/virtuoso-large"),
    ("Nova Pro (Amazon)",         "amazon/nova-pro-v1"),
    ("Cogito v2.1 671B",          "deepcogito/cogito-v2.1-671b"),
]


def corr(a, b):
    if len(a) < 3:
        return 0.0
    ma, mb = st.mean(a), st.mean(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    den = (sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b)) ** 0.5
    return num / den if den else 0.0


def cargar_casos(suite, responses_dir):
    from benchmarks.runner import ALL_TEST_SUITES
    idx = {(s, t["name"]): t for s, ts in ALL_TEST_SUITES.items() for t in ts}
    casos = []
    for f in Path(responses_dir).glob("*.md"):
        partes = f.stem.split("__")
        if len(partes) != 3:
            continue
        _, s, test = partes
        if s != suite:
            continue
        t = idx.get((s, test))
        txt = f.read_text(encoding="utf-8")
        m = re.search(r"quality:\s*([\d.]+)", txt)
        if not t or not m or "## Respuesta completa\n" not in txt:
            continue
        casos.append({
            "rub": float(m.group(1)),
            "resp": txt.split("## Respuesta completa\n", 1)[1].strip(),
            "test": t, "suite": s,
        })
    return casos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", default="business_audit")
    ap.add_argument("--n", type=int, default=15, help="Muestra (múltiplo de 3)")
    ap.add_argument("--responses", default="benchmarks/results/responses/20260713_083709_82198")
    args = ap.parse_args()

    from benchmarks.config import OPENROUTER_API_KEY
    from benchmarks.llm_judge import LLMJudge

    casos = cargar_casos(args.suite, args.responses)
    if len(casos) < args.n:
        sys.exit(f"Solo encontré {len(casos)} respuestas de {args.suite}")

    # Muestra ESTRATIFICADA: un tercio de los que fallaron la trampa, un tercio del medio,
    # un tercio de los que la cazaron. Si el juez sirve, tiene que separar estos grupos.
    casos.sort(key=lambda c: c["rub"])
    n3 = args.n // 3
    t = len(casos)
    random.seed(11)
    muestra = (random.sample(casos[:t // 3], n3)
               + random.sample(casos[t // 3:2 * t // 3], n3)
               + random.sample(casos[2 * t // 3:], n3))

    g = [st.mean([c["rub"] for c in muestra[i * n3:(i + 1) * n3]]) for i in range(3)]
    print(f"\n  {len(muestra)} respuestas reales de {args.suite}, estratificadas por la verdad objetiva:")
    print(f"    fallaron la trampa: rúbrico {g[0]:.1f}   ·   medio: {g[1]:.1f}   ·   la cazaron: {g[2]:.1f}\n")
    print(f"  {'juez':<28} {'media':>6} {'desv':>6} {'techo':>6} {'corr':>6}   veredicto")
    print("  " + "─" * 76)

    filas = []
    for nombre, mid in CANDIDATOS:
        J = LLMJudge(api_key=OPENROUTER_API_KEY, base_url="https://openrouter.ai/api/v1",
                     judge_model=mid, provider="openrouter")
        ss, rr = [], []
        for c in muestra:
            try:
                s = J.evaluate(c["resp"], c["test"], c["suite"]).get("score_final", -1)
            except Exception:  # noqa: BLE001
                s = -1
            if s >= 0:
                ss.append(s)
                rr.append(c["rub"])
        if len(ss) < len(muestra) * 0.7:
            print(f"  {nombre:<28} — no parsea ({len(ss)}/{len(muestra)})", flush=True)
            continue
        techo = sum(1 for x in ss if x >= 4.9) / len(ss)
        c = corr(ss, rr)
        if techo >= 0.5:
            v = "SATURA — aprueba a todos"
        elif c > 0.4:
            v = "✅ sigue la verdad objetiva"
        elif c > 0.15:
            v = "flojo pero ordena algo"
        else:
            v = "no correlaciona — puntúa otra cosa"
        filas.append((c, techo, nombre, mid))
        print(f"  {nombre:<28} {st.mean(ss):>6.2f} {st.pstdev(ss):>6.2f} "
              f"{techo:>5.0%} {c:>6.2f}   {v}", flush=True)

    buenos = [f for f in filas if f[0] > 0.4 and f[1] < 0.5]
    print()
    if buenos:
        buenos.sort(reverse=True)
        c, _, nombre, mid = buenos[0]
        print(f"  Mejor candidato: {nombre} ({mid}) — correlación {c:.2f} con la verdad objetiva.")
    else:
        print("  NINGÚN juez correlaciona con la verdad objetiva en esta suite.")
        print("  Conclusión: para suites con trampa verificable, el rúbrico ES la medición;")
        print("  el juez LLM sobra. (Es lo que ya hace niah_es.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
