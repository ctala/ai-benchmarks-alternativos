#!/usr/bin/env python3
"""Barrido SISTEMÁTICO de anomalías que afectan el ranking del benchmark.

No es un parche por síntoma: enumera CADA clase de problema de integridad de datos
sobre TODO el dataset, cuánto pesa, y qué modelos rankeados toca. Es el detector que
debió correr antes de andar arreglando de a uno. Complementa validate.py (que ya cubre
procedencia/fórmula/duplicados de archivo) con las clases que le faltaban.

Uso:  python benchmarks/audit_anomalies.py
"""
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import benchmarks.export_for_pages as E

RESULTS = Path(__file__).parent / "results"


def load_runs():
    runs = []
    for f in sorted(RESULTS.glob("benchmark_*.json")):
        try:
            d = json.loads(f.read_text())
        except Exception:  # noqa: BLE001
            continue
        for r in (d if isinstance(d, list) else d.get("results", [])):
            if isinstance(r, dict):
                r["_file"] = f.name
                runs.append(r)
    return runs


def _empty(r):
    return not (r.get("response_preview") or "").strip()


def main():
    runs = load_runs()
    exp = E.build_export()
    ranked = {m["name"] for m in exp["models"] if m.get("ranked")}
    # runs por modelo (nombre) que ENTRAN a quality general (success, no-pilar-aparte)
    def in_quality(r):
        s = str(r.get("suite", ""))
        return (r.get("success") and not s.startswith("niah")
                and not s.startswith("prompt_injection") and s != "tool_calling")

    success = [r for r in runs if r.get("success")]
    print(f"\n{'='*72}\n  AUDITORÍA DE ANOMALÍAS — {len(runs)} runs · {len(success)} success · "
          f"{len(ranked)} rankeados\n{'='*72}\n")

    def report(code, title, bad_runs, extra=""):
        # cuántos tocan quality general + qué modelos RANKEADOS
        inq = [r for r in bad_runs if in_quality(r)]
        by_ranked = Counter(r.get("model") for r in inq if r.get("model") in ranked)
        print(f"── {code} · {title}")
        print(f"     runs afectados: {len(bad_runs)}  ·  que entran a quality: {len(inq)}  ·  "
              f"en modelos RANKEADOS: {sum(by_ranked.values())}")
        if extra:
            print(f"     {extra}")
        if by_ranked:
            top = ", ".join(f"{m}({n})" for m, n in by_ranked.most_common(8))
            print(f"     top rankeados: {top}")
        print()
        return by_ranked

    affected = defaultdict(set)  # modelo rankeado -> set de códigos

    # E1 · vacíos-basura: success + respuesta vacía + sin empty_persistent → no-medición puntuada
    e1 = [r for r in success if _empty(r) and not r.get("empty_persistent")]
    q = [r.get("quality") for r in e1 if r.get("quality") is not None]
    br = report("E1", "Vacíos-basura (no-respuesta puntuada como baja calidad)", e1,
                f"quality media de esos: {sum(q)/len(q):.2f} (basura)" if q else "")
    for m in br: affected[m].add("E1")

    # E2 · fórmula obsoleta MARCADA en quality cruda (scoring != esperada, pero cuenta en raw)
    e2 = [r for r in success if r.get("scoring") and not E._misma_formula(r)]
    persuite = Counter(r.get("suite") for r in e2 if in_quality(r))
    br = report("E2", "Fórmula obsoleta marcada (en quality cruda global)", e2,
                "por suite: " + ", ".join(f"{s}({n})" for s, n in persuite.most_common(6)))
    for m in br: affected[m].add("E2")

    # E3 · sin procedencia: ningún marcador scoring → escala desconocida, en quality cruda
    e3 = [r for r in success if not r.get("scoring")]
    br = report("E3", "Sin procedencia (scoring ausente, escala desconocida)", e3)
    for m in br: affected[m].add("E3")

    # E4 · modelos con alta tasa de FALLO (subset success sesgado)
    tot = Counter(r.get("model") for r in runs)
    fail = Counter(r.get("model") for r in runs if not r.get("success"))
    print("── E4 · Modelos con alta tasa de fallo (success = subset sesgado)")
    high = [(m, fail[m], tot[m]) for m in tot if tot[m] >= 20 and fail[m] / tot[m] > 0.20]
    high.sort(key=lambda x: -x[1] / x[2])
    for m, fl, tt in high[:12]:
        flag = " ← RANKEADO" if m in ranked else ""
        codes = Counter(str(r.get("error"))[:12] for r in runs
                        if r.get("model") == m and not r.get("success"))
        print(f"     {m:38} {fl}/{tt} fallan ({100*fl/tt:.0f}%){flag}  {dict(codes)}")
        if m in ranked: affected[m].add("E4")
    print()

    # E5 · rutas muertas: muchos 403 (forbidden) → modelo ya no disponible en su ruta
    print("── E5 · Rutas posiblemente muertas (403 forbidden)")
    d403 = Counter(r.get("model") for r in runs if "403" in str(r.get("error", "")))
    for m, n in d403.most_common(8):
        flag = " ← RANKEADO" if m in ranked else ""
        print(f"     {m:38} {n}× 403{flag}")
        if m in ranked: affected[m].add("E5")
    if not d403: print("     (ninguno)")
    print()

    # E6 · precio $0 en modelo rankeado (regla: nunca gratis como precio)
    print("── E6 · Precio $0 en modelo RANKEADO (regla: nunca gratis como precio)")
    z = [m for m in exp["models"] if m.get("ranked") and (
        (m.get("cost_input_per_M") in (0, 0.0)) or (m.get("cost_output_per_M") in (0, 0.0)))]
    for m in z:
        print(f"     {m['name']:38} in={m.get('cost_input_per_M')} out={m.get('cost_output_per_M')}")
        affected[m["name"]].add("E6")
    if not z: print("     (ninguno)")
    print()

    # RESUMEN: modelos rankeados tocados por ≥1 anomalía
    print(f"{'='*72}\n  RESUMEN — modelos RANKEADOS con ≥1 anomalía: {len(affected)}/{len(ranked)}\n{'='*72}")
    for m, codes in sorted(affected.items(), key=lambda x: -len(x[1])):
        print(f"   {m:40} {sorted(codes)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
