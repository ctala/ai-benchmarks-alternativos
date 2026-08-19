#!/usr/bin/env python3
"""¿La nota de un modelo es del MODELO, o de dónde le tocó correr?

POR QUÉ EXISTE (19-ago-2026)
----------------------------
Cristian, mirando el ruido antes de publicar contenido sobre Qwen 3.8: *"me preocupa que
aún tengamos ruido en mediciones ya terminadas que puedan afectar el ranking, en especial
en modelos nuevos como los de qwen 3.8 ya que queremos generar contenido relacionado"*.

LA PRIMERA VERSIÓN DE ESTE CHEQUEO ESTABA MAL, Y CONVIENE CONTARLO
-----------------------------------------------------------------
Comparaba la media de cada proveedor a secas, y daba alarmas enormes:

    Kimi K2.5      3,33   (Venice 9,04 ↔ SiliconFlow 5,71)
    Qwen 3.8 2.4T  1,53   (DeepInfra 9,38 ↔ DigitalOcean 7,85)

Con la población entera abarcando ~1,4 puntos, eso decía que el proveedor pesa más que
el modelo. Era **falso**: al mirar QUÉ tests había rendido cada proveedor, los tests
COMUNES entre ellos eran **cero**. OpenRouter rutea run por run, así que a cada proveedor
le tocan tests distintos — y comparar sus medias es comparar exámenes distintos, que es
exactamente el error que este repo ya había pagado («MiniMax audita mejor que Opus 4.8»,
con MiniMax habiendo rendido 4 de los 10 tests).

El 10,00 de Kimi K2.5 en Venice no dice que Venice sirva mejor: dice que a Venice le
tocaron los tests fáciles.

Por eso ahora la comparación es SOBRE TESTS COMUNES, y cuando no los hay el veredicto es
«no comparable» — que es información, no una alarma. La doctrina «Endpoint ≠ modelo»
sigue siendo cierta y el riesgo del ruteo sigue existiendo; lo que no había era evidencia
de su tamaño, y este chequeo existe para producirla bien.

EL REPO YA TENÍA LA MITAD
-------------------------
La doctrina estaba escrita («Endpoint ≠ modelo») y la instrumentación también: cada run
guarda `upstream_provider` desde julio. Lo que faltaba era **la política** — nadie decidía
qué hacer cuando el mismo id rinde 1,5 puntos distinto según dónde caiga. Este chequeo no
inventa la regla: pone número al problema y deja la lista de qué re-medir con proveedor
fijo (`provider.order` en OpenRouter).

QUÉ NO ES
---------
No es lo mismo que `provider_variant`. Ése cubre el caso deliberado —medir Qwen en NIM y
en Ollama Cloud como filas distintas— donde la comparación ES el objetivo. Acá el ruteo
lo decide OpenRouter sin avisar, y el resultado se promedia como si fuera un solo modelo.

Uso:
    python benchmarks/check_dispersion_proveedor.py            # reporte
    python benchmarks/check_dispersion_proveedor.py --duro     # exit 1 si alguno pasa el umbral
    python benchmarks/check_dispersion_proveedor.py --plan     # qué re-medir y con qué proveedor
"""

import argparse
import glob
import json
import statistics as st
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from benchmarks.suites import SUITES  # noqa: E402

RESULTS = ROOT / "benchmarks" / "results"
# Umbral: la mitad del rango de la población. Por debajo, la dispersión compite con el
# ruido normal entre runs; por encima, el proveedor pesa más que el modelo.
UMBRAL = 0.5
MIN_TESTS_PROV = 10   # tests distintos que un proveedor debe haber rendido
MIN_COMUNES = 5       # tests comunes mínimos para que la comparación signifique algo


def recolectar():
    """modelo → proveedor → test → [quality]. Por TEST, para poder comparar lo comparable."""
    pil = {s for s, v in SUITES.items() if v.get("en_promedio")}
    d = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for f in glob.glob(str(RESULTS / "*.json")):
        if "_archive" in f:
            continue
        try:
            dd = json.loads(Path(f).read_text())
        except Exception:
            continue
        rs = dd.get("results") if isinstance(dd, dict) else dd
        if not isinstance(rs, list):
            continue
        for r in rs:
            if not isinstance(r, dict) or not r.get("success"):
                continue
            if r.get("quality") is None or r.get("suite") not in pil:
                continue
            p = r.get("upstream_provider")
            if p and r.get("model") and r.get("test_name"):
                d[r["model"]][p][r["test_name"]].append(r["quality"])
    return d


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--duro", action="store_true")
    ap.add_argument("--plan", action="store_true", help="qué re-medir y con qué proveedor")
    a = ap.parse_args()

    filas, incomparables = [], []
    for m, pv in recolectar().items():
        grandes = [p for p, t in pv.items() if len(t) >= MIN_TESTS_PROV]
        if len(grandes) < 2:
            continue
        # SOLO tests que TODOS rindieron. Sin esto se comparan exámenes distintos.
        comunes = set.intersection(*[set(pv[p]) for p in grandes])
        if len(comunes) < MIN_COMUNES:
            incomparables.append((m, len(grandes), len(comunes)))
            continue
        ps = [(st.mean([st.mean(pv[p][t]) for t in comunes]), p, len(comunes))
              for p in grandes]
        ps.sort(reverse=True)
        qs = [x[0] for x in ps]
        filas.append((max(qs) - min(qs), m, ps))
    filas.sort(reverse=True)
    malos = [f for f in filas if f[0] >= UMBRAL]

    print(f"DISPERSIÓN ENTRE PROVEEDORES · umbral {UMBRAL} · "
          f"{len(filas)} modelos con ≥2 proveedores medidos\n")
    if incomparables:
        print("  ⚠️  NO COMPARABLES — cada proveedor rindió tests distintos:\n")
        for m, n, c in sorted(incomparables, key=lambda x: -x[1])[:8]:
            print(f"      {m:<34} {n} proveedores · {c} tests en común")
        print("\n      No es una alarma: es que el ruteo de OpenRouter reparte run por run,")
        print("      así que no hay base para comparar. Para medirlo de verdad hay que")
        print("      fijar `provider.order` y correr el MISMO examen en cada uno.\n")
    if not malos:
        print("  ✅ ningún modelo con tests comunes muestra dispersión sobre el umbral.")
        return 0

    for dsp, m, ps in malos:
        print(f"  Δ {dsp:.2f}  {m}")
        for q, p, n in ps:
            print(f"          {q:>5.2f}  ({n:>3} runs)  {p}")

    print(f"\n  {len(malos)} modelo(s) cuya nota depende del proveedor más de lo que")
    print("  la población entera se separa entre sí. Su número publicado es el promedio")
    print("  de cómo los enrutó OpenRouter, no una propiedad del modelo.")

    if a.plan:
        print("\n  PLAN — re-medir con `provider.order` fijo:\n")
        for dsp, m, ps in malos:
            mejor = ps[0]
            print(f"    {m:<34} fijar en «{mejor[1]}» "
                  f"(el de más muestra limpia: {mejor[2]} runs, {mejor[0]:.2f})")
        print("\n    Ojo: fijar el MEJOR proveedor sesga hacia arriba. Lo defendible es")
        print("    fijar el que un usuario obtendría por defecto, o declarar cuál se usó.")
    return 1 if a.duro else 0


if __name__ == "__main__":
    sys.exit(main())
