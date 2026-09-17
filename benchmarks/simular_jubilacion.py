#!/usr/bin/env python3
"""Simula JUBILAR DEL ÍNDICE las suites que ya no separan modelos.

Jubilar no es borrar: la suite se sigue corriendo y se sigue reportando aparte —como
`niah_es` y `prompt_injection_es` hoy—, sólo deja de promediar en el número que encabeza
el ranking. Cristian, 17-sep-2026: *"lo saturado igual son tareas que se deberían hacer"*.

POR QUÉ EXISTE (17-sep-2026)
----------------------------
94 de 107 modelos rankeados se solapan con el #1 dentro de su IC95, y 16 de 34 suites no
separan a nadie. La salida obvia —sacar del promedio las suites saturadas— es un cambio de
PRESENTACIÓN, y la regla del repo es que la presentación se simula ANTES contra los runs en
disco, cuesta minutos y $0 (`PLAN-ESTABILIDAD.md` R1). Este script es esa simulación.

Y el resultado contradijo la propuesta que lo motivó. Jubilar **empeora** la discriminación:

    escenario                         suites  sigma   IC95   señal/ruido   solapan con #1
    hoy                                   29  0.257  0.376      0.68           94/107
    sin las que no separan (sigma<0.6)    18  0.303  0.522      0.58          102/107
    sólo las 12 más discriminantes        12  0.394  0.736      0.54           99/107

La dispersión entre modelos sí sube (+53%), pero el IC95 sube más rápido (+96%) porque el
índice pierde tests y la incertidumbre crece con 1/raíz(n). Quitar tareas fáciles no crea
señal: tira muestra. Lo que separa modelos es AGREGAR tareas difíciles.

Y de paso destapó que el índice declarado no es el que promedia — ver `check_suites.py` S6.

MÉTODO (por qué se le puede creer)
----------------------------------
No reimplementa el cálculo: reutiliza `aggregate_metrics`, la MISMA función que produce
`quality_avg` y `quality_ci95` en `docs/data/models.json`. Jubilar una suite = pasarla en
`low_coverage_suites`, el conjunto que `general` ya excluye del quality.

La fase 1 reproduce el quality_avg PUBLICADO de los 107 rankeados y **se niega a simular si
no lo logra**: un método que no puede recalcular el presente no tiene derecho a opinar sobre
el futuro. Es la regla del repo de exigir verde de control antes de sabotear nada.

Uso:  python benchmarks/simular_jubilacion.py
"""

import json
import statistics as st
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from benchmarks.export_for_pages import (  # noqa: E402
    MIN_SUITE_COVERAGE, MODELS, aggregate_metrics, load_all_results, suite_coverage,
)
from benchmarks.runner import ALL_TEST_SUITES as TS  # noqa: E402

MODELS_JSON = ROOT / "docs" / "data" / "models.json"

# Tolerancias del control. Cero en la práctica (se reutiliza la función real); el margen
# existe para no romperse por un redondeo si el export cambia de formato.
TOL_MEDIANA, TOL_MAX = 0.005, 0.05

# Umbrales de saturación, explícitos para que se puedan discutir:
SD_NO_SEPARA = 0.60     # desviación entre modelos: por debajo, la suite no ordena a nadie
PERF_TECHO = 70         # % de notas >= 9.5: por encima, la suite satura por techo


def _low_coverage():
    """Las suites que hoy no puntúan por cobertura, calculadas como en el export."""
    by_id, by_name = load_all_results()
    muertos = {(c["id"], c.get("name", k)) for k, c in MODELS.items()
               if c.get("retired") or c.get("provider_variant")}
    nombres_muertos = {n for _, n in muertos}

    def compite(key):
        if isinstance(key, tuple):
            return key not in muertos and key[1] not in nombres_muertos
        return True

    cov = suite_coverage(by_name if by_name else by_id, compite)
    return by_id, by_name, {s for s, c in cov.items() if c < MIN_SUITE_COVERAGE}


def _runs_de(m, by_id, by_name):
    """El mismo emparejamiento runs↔modelo que hace el export."""
    cfg = next((c for c in MODELS.values()
                if c["id"] == m["id"] and c.get("name") == m["name"]), None)
    compartido = [c["id"] for c in MODELS.values()].count(m["id"]) > 1
    if (cfg and cfg.get("force_reasoning")) or compartido:
        return by_name.get((m["id"], m["name"]), [])
    rs = [r for r in by_id.get(m["id"], []) if "(thinking)" not in (r.get("model") or "")]
    return rs or by_name.get((m["id"], m["name"]), [])


def _spearman(a: dict, b: dict) -> float:
    comunes = [k for k in a if k in b]
    n = len(comunes)
    ra = {k: i for i, k in enumerate(sorted(comunes, key=lambda k: -a[k]))}
    rb = {k: i for i, k in enumerate(sorted(comunes, key=lambda k: -b[k]))}
    d2 = sum((ra[k] - rb[k]) ** 2 for k in comunes)
    return 1 - 6 * d2 / (n * (n * n - 1))


def main() -> int:
    d = json.loads(MODELS_JSON.read_text())
    R = [m for m in d["models"] if m.get("ranked")]
    by_id, by_name, low = _low_coverage()

    # ── FASE 1 · CONTROL ───────────────────────────────────────────────────────
    print("=" * 78)
    print(" FASE 1 · CONTROL — ¿reproduzco el quality_avg PUBLICADO de hoy?")
    print("=" * 78)
    print(f"  fuera por cobertura (<{MIN_SUITE_COVERAGE:.0%}): {sorted(low) or 'ninguna'}")

    runs_por_modelo, err_q, err_ci, base = {}, [], [], {}
    for m in R:
        rs = _runs_de(m, by_id, by_name)
        runs_por_modelo[m["key"]] = rs
        met = aggregate_metrics(rs, low)
        base[m["key"]] = met.get("quality_avg")
        if met.get("quality_avg") is not None and m.get("quality_avg") is not None:
            err_q.append(abs(met["quality_avg"] - m["quality_avg"]))
        if met.get("quality_ci95") is not None and m.get("quality_ci95") is not None:
            err_ci.append(abs(met["quality_ci95"] - m["quality_ci95"]))

    if not err_q:
        print("  ❌ CONTROL EN ROJO: no se recalculó ni un modelo. NO se simula.")
        return 1
    med, mx = st.median(err_q), max(err_q)
    print(f"  modelos recalculados: {len(err_q)}/{len(R)}")
    print(f"  error en quality_avg  → mediana {med:.4f} · máx {mx:.4f}")
    print(f"  error en quality_ci95 → mediana {st.median(err_ci):.4f} · máx {max(err_ci):.4f}")
    if med > TOL_MEDIANA or mx > TOL_MAX:
        print("\n  ❌ CONTROL EN ROJO: el método no reproduce lo publicado. NO se simula.")
        for m in sorted(R, key=lambda m: -abs((base[m["key"]] or 0) - (m["quality_avg"] or 0)))[:5]:
            print(f"     {m['name']:30} publicado {m['quality_avg']} vs simulado {base[m['key']]}")
        return 1
    print("  ✅ CONTROL VERDE: reproduce el ranking publicado. Se puede simular.\n")

    # ── Señales de saturación, suite por suite ─────────────────────────────────
    universo = {r.get("suite", "") for rs in runs_por_modelo.values() for r in rs}
    universo = {s for s in universo
                if s and not s.startswith("niah") and not s.startswith("prompt_injection")
                and s != "tool_calling" and s not in low}

    señales = {}
    for s in universo:
        vals = [m["quality_by_suite"][s] for m in R
                if m.get("quality_by_suite", {}).get(s) is not None]
        if len(vals) < 10:
            continue
        señales[s] = {"n": len(vals), "media": st.mean(vals), "sd": st.pstdev(vals),
                      "perf": 100 * sum(1 for v in vals if v >= 9.5) / len(vals),
                      "tests": len(TS.get(s, []))}

    print("=" * 78)
    print(" LO QUE HOY PROMEDIA EN EL TITULAR")
    print("=" * 78)
    print(f" {'suite':26} {'tests':>5} {'media':>6} {'sigma':>6} {'%perf':>6}   veredicto")
    for s, v in sorted(señales.items(), key=lambda kv: kv[1]["sd"]):
        ver = ("TECHO (casi todos 10)" if v["perf"] >= PERF_TECHO
               else "no separa" if v["sd"] < SD_NO_SEPARA else "")
        print(f" {s:26} {v['tests']:5d} {v['media']:6.2f} {v['sd']:6.2f} {v['perf']:5.0f}%   {ver}")

    techo = {s for s, v in señales.items() if v["perf"] >= PERF_TECHO}
    no_separa = {s for s, v in señales.items() if v["sd"] < SD_NO_SEPARA}
    conservador = {s for s, v in señales.items() if v["sd"] < 0.45}
    discriminantes = {s for s, _ in sorted(señales.items(), key=lambda kv: -kv[1]["sd"])[:12]}

    escenarios = [
        ("E0 · hoy (control)", set()),
        ("E1 · jubilar las de TECHO", techo),
        ("E2 · corte conservador (sigma < 0.45)", conservador),
        ("E3 · jubilar las que NO SEPARAN (sigma < 0.60)", no_separa),
        ("E4 · E1 + E3", techo | no_separa),
        ("E5 · sólo las 12 más discriminantes", set(señales) - discriminantes),
    ]

    hoy = {m["key"]: m["quality_avg"] for m in R if m.get("quality_avg") is not None}
    nombre = {m["key"]: m["name"] for m in R}
    pos_hoy = {k: i for i, k in enumerate(sorted(hoy, key=lambda x: -hoy[x]), 1)}
    tabla = []

    for etiqueta, jubiladas in escenarios:
        qs, cis = {}, {}
        for m in R:
            met = aggregate_metrics(runs_por_modelo[m["key"]], low | jubiladas)
            if met.get("quality_avg") is not None:
                qs[m["key"]] = met["quality_avg"]
                cis[m["key"]] = met.get("quality_ci95")
        if not qs:
            continue
        orden = sorted(qs, key=lambda k: -qs[k])
        lider = orden[0]
        solapan = sum(1 for k in qs if qs[k] + (cis[k] or 0) >= qs[lider] - (cis[lider] or 0))
        sd_entre = st.pstdev(list(qs.values()))
        ci_medio = st.mean([c for c in cis.values() if c is not None])
        movs = [abs(pos_hoy[k] - i) for i, k in enumerate(orden, 1) if k in pos_hoy]
        quedan = [s for s in señales if s not in jubiladas]

        print("\n" + "=" * 78)
        print(f" {etiqueta}")
        print("=" * 78)
        if jubiladas:
            print(f"  jubiladas ({len(jubiladas)}): {', '.join(sorted(jubiladas))}")
        print(f"  quedan {len(quedan)} suites · {sum(señales[s]['tests'] for s in quedan)} tests")
        print(f"  dispersión entre modelos: {sd_entre:.3f}   ·   IC95 medio: {ci_medio:.3f}"
              f"   ·   señal/ruido: {sd_entre / ci_medio:.2f}")
        print(f"  se solapan con el #1 en IC95: {solapan} de {len(qs)}")
        print(f"  movimiento de puesto: mediana {st.median(movs):.0f} · máximo {max(movs)}")
        print(f"  Spearman contra el ranking de hoy: {_spearman(hoy, qs):.4f}")
        print("  TOP 10:")
        for i, k in enumerate(orden[:10], 1):
            delta = pos_hoy.get(k, i) - i
            print(f"    {i:2d}. {nombre[k]:32} {qs[k]:5.2f}" +
                  (f"  ({delta:+d})" if delta else "   (=)"))
        tabla.append((etiqueta, len(quedan), sd_entre, sd_entre / ci_medio, solapan, len(qs)))

    print("\n" + "=" * 78)
    print(" COMPARACIÓN — más suites jubiladas NO es más discriminación")
    print("=" * 78)
    print(f" {'escenario':48} {'suites':>6} {'sigma':>6} {'señal/ruido':>12} {'solapan':>9}")
    for et, ns, sd, sr, sol, tot in tabla:
        print(f" {et:48} {ns:6d} {sd:6.3f} {sr:12.2f} {sol:5d}/{tot:<3d}")
    print("\n  Leer la columna señal/ruido, no la de sigma: jubilar sube la dispersión ENTRE"
          "\n  modelos, pero sube más rápido el error de cada uno (menos tests). El ranking"
          "\n  no se vuelve más nítido — se vuelve más ruidoso.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
