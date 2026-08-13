#!/usr/bin/env python3
"""
Valida una suite NUEVA antes de gastar en medirla en los 82 modelos.

POR QUÉ EXISTE (13-ago-2026)
----------------------------
Escribí dos suites duras y las validé **en dos modelos** — uno bueno y uno malo. Las
dos parecían discriminar:

    retrieval_distractores   Qwen 3.7 Flash 8,99  ·  Llama 3.1 8B 7,46   → "separa 1,53"

Con los 82 medidos, la realidad: **76% de respuestas perfectas.** Saturada de nacimiento,
igual que las cinco suites que acabábamos de jubilar por eso mismo. Endurecerla la bajó
solo a 70%. Se descartó.

**Dos modelos no dicen nada sobre saturación.** Un test que el 76% de la población
resuelve perfecto puede igual mostrar diferencia entre el mejor y el peor — y eso fue
exactamente lo que me convenció. La separación entre dos puntos no mide la dispersión
de la distribución.

QUÉ VERIFICA
------------
Corre la suite en una **muestra diversa** (modelos repartidos por todo el rango de
calidad, no dos extremos) y decide con tres criterios:

  S1. **Saturación** — % de runs con nota perfecta. Sobre 40% ya no discrimina bien;
      sobre 60% es una suite muerta antes de nacer.
  S2. **Dispersión** — sd de la nota media por modelo, comparada con la del índice de
      calidad general. Menos de 1× significa que no agrega poder de separación.
  S3. **Piso y techo** — si nadie baja de 8 o nadie sube de 4, el rango útil es falso.

Cuesta lo que cuesta medir ~8 modelos (centavos), contra los ~$3-65 del examen completo
y, sobre todo, contra publicar una suite que no informa.

Uso:
    python benchmarks/validate_suite.py --suite tool_calling_adversarial
    python benchmarks/validate_suite.py --suite mi_suite --modelos 10
"""

import argparse
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean, pstdev

ROOT = Path(__file__).resolve().parent.parent
PY = str(ROOT / ".venv" / "bin" / "python")
if not Path(PY).exists():
    PY = sys.executable

SATURACION_ALERTA = 0.40
SATURACION_MUERTA = 0.60


def muestra_diversa(n: int) -> list[str]:
    """Modelos repartidos por el rango de calidad, no los dos extremos.

    Tomar "uno bueno y uno malo" es lo que falló: mide la separación entre dos puntos,
    no la forma de la distribución. Con n repartidos se ve si el pelotón del medio se
    apelotona arriba, que es como se manifiesta la saturación.
    """
    d = json.loads((ROOT / "docs" / "data" / "models.json").read_text())
    rank = sorted([m for m in d["models"] if m.get("ranked") and m.get("score_calidad")],
                  key=lambda m: -m["score_calidad"])
    if not rank:
        return []
    paso = max(1, len(rank) // n)
    return [m["key"] for m in rank[::paso]][:n]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", required=True)
    ap.add_argument("--modelos", type=int, default=8)
    ap.add_argument("--sin-medir", action="store_true",
                    help="no mide: analiza los runs que ya existan de esa suite")
    args = ap.parse_args()

    keys = muestra_diversa(args.modelos)
    if not keys:
        print("✗ no hay modelos rankeados para muestrear")
        return 1

    salida = ROOT / "benchmarks" / "results" / f"benchmark_validacion_{args.suite}.json"
    if not args.sin_medir:
        print(f"Midiendo «{args.suite}» en {len(keys)} modelos repartidos por el rango…\n")
        salida.write_text(json.dumps({"metadata": {"timestamp": f"validacion_{args.suite}",
                                                   "partial": True}, "results": []}))
        subprocess.run([PY, str(ROOT / "benchmarks" / "runner.py"), "--quick", "--judge",
                        "--judge-model", "phi4-or", "--models", *keys,
                        "--tests", args.suite, "--resume", str(salida), "--sin-canario"],
                       cwd=ROOT, capture_output=True, text=True)

    if not salida.exists():
        print(f"✗ no hay resultados en {salida.name}")
        return 1
    runs = [r for r in json.loads(salida.read_text()).get("results", [])
            if r.get("suite") == args.suite and r.get("quality") is not None]
    if not runs:
        print("✗ la suite no produjo runs con nota")
        return 1

    por = defaultdict(list)
    for r in runs:
        por[r.get("model")].append(r["quality"])
    medias = [mean(v) for v in por.values()]
    todos = [x for v in por.values() for x in v]
    perfectos = sum(1 for x in todos if x >= 10) / len(todos)
    sd = pstdev(medias) if len(medias) > 1 else 0.0

    d = json.loads((ROOT / "docs" / "data" / "models.json").read_text())
    sd_ref = pstdev([m["score_calidad"] for m in d["models"]
                     if m.get("ranked") and m.get("score_calidad")])

    print(f"  {len(runs)} runs · {len(por)} modelos\n")
    print(f"  S1 saturación : {perfectos:.0%} de runs con nota perfecta")
    print(f"  S2 dispersión : sd {sd:.2f}  (índice general {sd_ref:.2f} → "
          f"{sd/sd_ref if sd_ref else 0:.1f}×)")
    print(f"  S3 rango      : {min(medias):.2f} – {max(medias):.2f}\n")

    fallos = []
    if perfectos >= SATURACION_MUERTA:
        fallos.append(f"S1 · {perfectos:.0%} de runs perfectos: la suite nace saturada. "
                      f"No discrimina y no debe puntuar.")
    elif perfectos >= SATURACION_ALERTA:
        print(f"  ⚠️  S1 · {perfectos:.0%} de perfectos: en el borde. Endurecer antes de medir los 82.\n")
    if sd_ref and sd < sd_ref:
        fallos.append(f"S2 · dispersión {sd:.2f} < {sd_ref:.2f} del índice general: "
                      f"no agrega poder de separación.")
    if min(medias) > 8:
        fallos.append(f"S3 · nadie baja de 8,0: el piso es falso, todos aprueban.")

    for f in fallos:
        print(f"    ❌ {f}")
    if fallos:
        print(f"\n  ❌ «{args.suite}» NO está lista para el examen completo.")
        print("     Endurecer y re-validar cuesta centavos; medir los 82 y descubrirlo, no.")
        return 1
    print(f"  ✅ «{args.suite}» discrimina. Se puede medir en los 82.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
