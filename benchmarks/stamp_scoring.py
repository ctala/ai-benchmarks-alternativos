#!/usr/bin/env python3
"""
Estampa la PROCEDENCIA del scoring en los runs históricos.

POR QUÉ EXISTE
--------------
Un run no guardaba con qué fórmula se calculó su `quality`. Eso suena menor y es la causa
raíz de una familia entera de bugs: al mezclar runs de distintas épocas en un promedio se
sumaban **escalas incompatibles** sin que nadie lo notara.

En julio de 2026 el dataset tenía tres fórmulas conviviendo:

    juez-30-70            quality = auto*0.3 + juez*0.7      (42% de los runs)
    verificable           quality = answer_score             (35%)
    solo-rubrica          el juez falló y se degradó         (17%)

Y 24 suites promediaban dos o más de esas escalas **en un mismo número**. `business_audit`
mezclaba las tres.

Peor: sin la marca no se puede ni AUDITAR. Yo mismo intenté deducir la fórmula comparando
`quality` con `auto_quality`, y deduje mal — conté como obsoletos los runs que el runner
nuevo ya había puntuado bien.

QUÉ HACE
--------
Recorre los runs y les pone `scoring` según lo que se puede deducir con certeza:

    rescored_by presente      → "verificable"        (lo puso rescore_all)
    quality != auto_quality   → "juez-30-70"         (hubo juez: la fórmula lo delata)
    quality == auto_quality   → "solo-rubrica-SIN-JUEZ"  (el juez falló; NO comparable)

Lo que NO hace: adivinar. Un run que no se puede clasificar con certeza queda sin marca,
y el export lo descarta. **Preferimos perder muestra a publicar un promedio de peras y
manzanas.**

Uso:
    python benchmarks/stamp_scoring.py --dry-run
    python benchmarks/stamp_scoring.py
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

RESULTS = ROOT / "benchmarks" / "results"


def _es_verificable(suite: str) -> bool:
    from benchmarks.runner import ALL_TEST_SUITES
    if not suite:
        return False
    if suite.startswith("niah"):
        return True
    tests = ALL_TEST_SUITES.get(suite, [])
    return bool(tests) and all(t.get("expected_answer") for t in tests)


def clasificar(r: dict) -> str | None:
    """Con qué fórmula se puntuó este run. None si NO se puede saber con certeza.

    OJO CON LA HEURÍSTICA. Comparar `quality` con `auto_quality` NO distingue las dos
    fórmulas modernas:

        verificable   quality = answer_score              → quality != auto_quality
        juez-30-70    quality = auto*0.3 + juez*0.7       → quality != auto_quality

    Las dos dan lo mismo al compararlas. Mi primer intento clasificó como "juez" runs
    verificables, y el validador reventó con una contradicción que había creado yo.

    Por eso: en una suite VERIFICABLE, un run viejo sin marca NO se puede clasificar.
    Se descarta. Adivinar la fórmula es cómo se llegó al problema original.
    """
    if r.get("scoring"):
        return r["scoring"]          # ya marcado (runner nuevo o rescore_all)
    if r.get("rescored_by"):
        return "verificable"

    q, a = r.get("quality"), r.get("auto_quality")
    if q is None or a is None:
        return None

    if _es_verificable(r.get("suite", "")):
        # No hay forma de saber si esta nota salió del answer_score o del juez.
        # Si tiene respuesta guardada, rescore_all la arregla. Si no, se descarta.
        return None

    # Suite BLANDA: la fórmula no cambió (30/70). Acá la heurística sí sirve.
    if abs(q - a) > 0.01:
        return "juez-30-70"          # hubo juez
    return "solo-rubrica-SIN-JUEZ"   # el juez falló: degradado, NO comparable


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cuenta = Counter()
    archivos = 0

    for f in sorted(RESULTS.glob("benchmark_*.json")):
        try:
            data = json.loads(f.read_text())
        except Exception:  # noqa: BLE001
            continue
        rows = data if isinstance(data, list) else data.get("results", [])
        tocado = False
        for r in rows:
            if not isinstance(r, dict) or not r.get("success"):
                continue
            if r.get("scoring"):
                cuenta["ya marcado"] += 1
                continue
            m = clasificar(r)
            cuenta[m or "SIN CLASIFICAR (se descarta)"] += 1
            if m and not args.dry_run:
                r["scoring"] = m
                tocado = True
        if tocado and not args.dry_run:
            f.write_text(json.dumps(data, ensure_ascii=False, indent=2))
            archivos += 1

    tot = sum(cuenta.values())
    print(f"\n  {tot} runs\n")
    for k, n in cuenta.most_common():
        print(f"    {k:<28} {n:>6} ({n / tot:>5.1%})")

    sin = cuenta["SIN CLASIFICAR (se descarta)"]
    roto = cuenta["solo-rubrica-SIN-JUEZ"]
    print(f"\n  ⚠️  {sin + roto} runs NO son comparables:")
    print(f"       · {sin} sin procedencia deducible")
    print(f"       · {roto} puntuados con el juez caído (fórmula degradada)")
    print(f"     El export los descarta. Perder muestra es mejor que promediar escalas distintas.")

    if args.dry_run:
        print("\n  (correr sin --dry-run para estampar)")
    else:
        print(f"\n  ✅ {archivos} archivos actualizados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
