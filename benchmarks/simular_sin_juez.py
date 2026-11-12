#!/usr/bin/env python3
"""Simula SACAR AL JUEZ del índice de calidad, contra los runs en disco ($0).

POR QUÉ EXISTE (3-nov-2026)
---------------------------
Cristian: *"no me molesta cambiar el cómo puntuamos y cómo medimos, mientras se mantenga
lo de qué medimos"* y *"no me importa dejar de hacer suites si estandarizamos"*. El estándar
propuesto: toda prueba es una lista de checks verificables; la calidad es la fracción que
pasa; sin juez en el titular. Antes de tocar nada, se simula (PLAN-ESTABILIDAD R1).

Hoy el índice mezcla tres formas de puntuar, marcadas en cada run por `scoring`:
  · `verificable`   → quality = answer_score (la trampa se cazó o no)
  · `juez-30-70`    → quality = auto*0.3 + juez*0.7 (no hay verdad contra qué verificar)
  · `solo-rubrica-SIN-JUEZ` / sin marca → quality = auto (rúbrica de formato, sin juez)

Escenarios:
  E0  hoy (control: debe reproducir lo publicado o el script se niega a simular)
  S1  juez a peso CERO: los runs juzgados valen lo que dice su rúbrica automática
      (mismo número de tests → aísla cuánto aporta el juez)
  S2  SOLO VERIFICABLE: fuera del índice todo run juzgado o de rúbrica sin verdad objetiva.
      Las suites que quedan vacías se jubilan solas; las mixtas conservan sus tests con check.
      (menos tests → el IC95 sube; es el precio del estándar antes de convertir suites)
  S3  S2 + las suites de prosa que no admiten trampa (creativity) fuera

MÉTODO: reutiliza `aggregate_metrics` (la función real del export), como
`simular_jubilacion.py`. Uso:  python benchmarks/simular_sin_juez.py
"""

import json
import statistics as st
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from benchmarks.export_for_pages import (  # noqa: E402
    MIN_SUITE_COVERAGE, MODELS, aggregate_metrics, load_all_results, suite_coverage,
)
from benchmarks.simular_jubilacion import _low_coverage, _runs_de, _spearman  # noqa: E402
from benchmarks.suites import SUITES  # noqa: E402

MODELS_JSON = ROOT / "sitio" / "legado" / "data" / "models.json"
TOL_MEDIANA, TOL_MAX = 0.005, 0.05
JUZGADO = {"juez-30-70"}
SIN_VERDAD = {"juez-30-70", "solo-rubrica-SIN-JUEZ", "sin-marca"}
PROSA_SIN_TRAMPA = {"creativity"}


def _marca(r):
    return r.get("scoring") or ("juez-30-70" if (r.get("judge_score") or -1) >= 0 else "sin-marca")


def _auto(r):
    if r.get("auto_quality") is not None:
        return float(r["auto_quality"])
    c = float(r.get("content_score") or 0.0)
    a = r.get("answer_score")
    return c * 0.4 + float(a) * 0.6 if a not in (None, 0.0) else c


def _escenario(rs, modo):
    """Devuelve (runs transformados, suites a jubilar además de las de baja cobertura)."""
    if modo == "E0":
        return rs, set()
    if modo == "S1":
        out = []
        for r in rs:
            if _marca(r) in JUZGADO:
                r = dict(r); r["quality"] = _auto(r)
            out.append(r)
        return out, set()
    keep = [r for r in rs if _marca(r) not in SIN_VERDAD]
    extra = set(PROSA_SIN_TRAMPA) if modo == "S3" else set()
    return keep, extra


def main() -> int:
    d = json.loads(MODELS_JSON.read_text())
    R = [m for m in d["models"] if m.get("ranked")]
    by_id, by_name, low = _low_coverage()
    idx = {s for s, v in SUITES.items() if v.get("en_promedio")}

    print("=" * 78); print(" FASE 1 · CONTROL — ¿reproduzco el quality_avg PUBLICADO de hoy?"); print("=" * 78)
    runs_por_modelo, err_q, err_ci = {}, [], []
    for m in R:
        rs = _runs_de(m, by_id, by_name)
        runs_por_modelo[m["key"]] = rs
        met = aggregate_metrics(rs, low)
        if met.get("quality_avg") is not None and m.get("quality_avg") is not None:
            err_q.append(abs(met["quality_avg"] - m["quality_avg"]))
        if met.get("quality_ci95") is not None and m.get("quality_ci95") is not None:
            err_ci.append(abs(met["quality_ci95"] - m["quality_ci95"]))
    if not err_q:
        print("  ❌ CONTROL EN ROJO: no se recalculó ni un modelo."); return 1
    med, mx = st.median(err_q), max(err_q)
    print(f"  modelos recalculados: {len(err_q)}/{len(R)} · error quality_avg mediana {med:.4f} máx {mx:.4f}"
          f" · error ci95 mediana {st.median(err_ci):.4f} máx {max(err_ci):.4f}")
    if med > TOL_MEDIANA or mx > TOL_MAX:
        print("  ❌ CONTROL EN ROJO: el método no reproduce lo publicado. NO se simula."); return 1
    print("  ✅ CONTROL VERDE.\n")

    # Qué parte del índice decide el juez hoy, por suite (runs de los rankeados, suites del índice)
    c = defaultdict(Counter)
    for rs in runs_por_modelo.values():
        for r in rs:
            if r.get("suite") in idx and r.get("suite") not in low:
                c[r["suite"]][_marca(r)] += 1
    print("=" * 78); print(" QUIÉN PUNTÚA HOY CADA SUITE DEL ÍNDICE (runs de los rankeados)"); print("=" * 78)
    print(f" {'suite':26} {'verificable':>11} {'juez':>8} {'rúbrica':>8}   queda en S2")
    tot_v = tot_j = tot_r = 0
    for s in sorted(c, key=lambda s: -(c[s]['juez-30-70'] + c[s]['solo-rubrica-SIN-JUEZ'] + c[s]['sin-marca'])):
        v, j = c[s]["verificable"], c[s]["juez-30-70"]
        rb = c[s]["solo-rubrica-SIN-JUEZ"] + c[s]["sin-marca"]
        tot_v += v; tot_j += j; tot_r += rb
        print(f" {s:26} {v:11d} {j:8d} {rb:8d}   {'sí (' + str(v) + ')' if v else 'NO: se jubila'}")
    print(f" {'TOTAL':26} {tot_v:11d} {tot_j:8d} {tot_r:8d}   juez = {100*tot_j/(tot_v+tot_j+tot_r):.0f}% de los runs del índice\n")

    hoy = {m["key"]: m["quality_avg"] for m in R if m.get("quality_avg") is not None}
    nombre = {m["key"]: m["name"] for m in R}
    pos_hoy = {k: i for i, k in enumerate(sorted(hoy, key=lambda x: -hoy[x]), 1)}
    tabla, resultados = [], {}

    for modo, etiqueta in [("E0", "E0 · hoy (control)"), ("S1", "S1 · juez a peso cero, mismos tests"),
                           ("S2", "S2 · solo verificable (el estándar)"), ("S3", "S3 · S2 sin creativity")]:
        qs, cis, ntests = {}, {}, Counter()
        for m in R:
            rs, extra = _escenario(runs_por_modelo[m["key"]], modo)
            met = aggregate_metrics(rs, low | extra)
            if met.get("quality_avg") is not None:
                qs[m["key"]] = met["quality_avg"]; cis[m["key"]] = met.get("quality_ci95")
                ntests[m["key"]] = len({(r.get("suite"), r.get("test_name")) for r in rs
                                        if r.get("suite") in idx and r.get("suite") not in (low | extra)})
        orden = sorted(qs, key=lambda k: -qs[k]); lider = orden[0]
        solapan = sum(1 for k in qs if qs[k] + (cis[k] or 0) >= qs[lider] - (cis[lider] or 0))
        sd_entre = st.pstdev(list(qs.values()))
        ci_medio = st.mean([v for v in cis.values() if v is not None])
        movs = {k: pos_hoy[k] - i for i, k in enumerate(orden, 1) if k in pos_hoy}
        resultados[modo] = (qs, orden, movs)
        print("=" * 78); print(f" {etiqueta}"); print("=" * 78)
        print(f"  tests por modelo (mediana): {st.median(ntests.values()):.0f}   ·   modelos con nota: {len(qs)}")
        print(f"  dispersión entre modelos: {sd_entre:.3f}   ·   IC95 medio: {ci_medio:.3f}"
              f"   ·   señal/ruido: {sd_entre/ci_medio:.2f}")
        print(f"  se solapan con el #1 en IC95: {solapan} de {len(qs)}")
        print(f"  movimiento de puesto: mediana {st.median(abs(v) for v in movs.values()):.0f}"
              f" · máximo {max(abs(v) for v in movs.values())}   ·   Spearman vs hoy: {_spearman(hoy, qs):.4f}")
        print("  TOP 12:")
        for i, k in enumerate(orden[:12], 1):
            dlt = movs.get(k, 0)
            print(f"    {i:2d}. {nombre[k]:34} {qs[k]:5.2f}" + (f"  ({dlt:+d})" if dlt else "   (=)"))
        if modo != "E0":
            sube = sorted(movs.items(), key=lambda kv: -kv[1])[:5]
            baja = sorted(movs.items(), key=lambda kv: kv[1])[:5]
            print("  más suben:  " + " · ".join(f"{nombre[k]} ({v:+d})" for k, v in sube if v > 0))
            print("  más bajan:  " + " · ".join(f"{nombre[k]} ({v:+d})" for k, v in baja if v < 0))
        print()
        tabla.append((etiqueta, st.median(ntests.values()), sd_entre, ci_medio, sd_entre / ci_medio, solapan, len(qs)))

    print("=" * 78); print(" COMPARACIÓN"); print("=" * 78)
    print(f" {'escenario':40} {'tests':>5} {'sigma':>6} {'IC95':>6} {'señal/ruido':>12} {'solapan #1':>11}")
    for et, nt, sd, ci, sr, sol, tot in tabla:
        print(f" {et:40} {nt:5.0f} {sd:6.3f} {ci:6.3f} {sr:12.2f} {sol:6d}/{tot:<3d}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
