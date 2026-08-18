#!/usr/bin/env python3
"""¿Alguna nota publicada es en realidad una respuesta cortada a la mitad?

POR QUÉ EXISTE (17-ago-2026)
----------------------------
Cristian, al ver a Claude Opus 5 en el puesto #79 de 83: *"me llama mucho la atención
lo de Opus 5"*. Y después, al ver la causa: **"eso lo debió detectar el QA, no?"**.

Sí. Y no lo detectó, porque **todos los detectores del repo cazan AUSENCIA** y esto es
lo contrario. La cadena entera está construida para lo que falta:

    E1  respuestas vacías          falta contenido
    E3  runs sin procedencia       falta el proveedor
    E4  tasa de fallo alta         faltan runs exitosos
    E5  rutas muertas              falta el endpoint
    E6  precio $0                  falta el precio

Un run truncado no le falta nada. Tiene contenido, tiene forma válida, tiene
`success=True`, pasa `validate.py` y el juez le pone una nota — más baja, porque la
respuesta se corta a la mitad de la frase. Lo que hay es un techo de más.

Medido el día que se escribió esto:

    Claude Opus 5 Fast   33% de 167 runs cortados
    Claude Opus 5        31% de 173      → publicado #79 de 83
    Gemini 3.6 Flash     30% de 174
    Claude Sonnet 5      15% de 222

La misma familia por suscripción —otra ruta, sin el techo— saca **0,81 más de calidad**
en Opus 5 y 0,82 en Sonnet 5, sobre una población que entera abarca 1,4 puntos. El
ranking publicaba a los modelos frontier de Anthropic al fondo de la tabla por un
`max_tokens` nuestro.

La causa raíz se arregla en `providers/adapters.py` (entrar a `THINKING_MODELS` da
`max_tokens × 4` y piso de 8192). Este archivo existe para lo otro: **que la próxima vez
que un modelo nuevo razone y nadie lo anote en esa lista, el pipeline lo diga en vez de
publicarlo**.

CÓMO LEER EL UMBRAL
-------------------
Truncar no siempre es un fallo. Un test que pide un artículo largo puede tocar el techo
en cualquier modelo, y eso es parte del examen —el límite es el mismo para todos—. Lo que
NO es normal es que un tercio del examen termine cortado: ahí el techo dejó de ser una
restricción compartida y pasó a ser una propiedad del modelo, que es exactamente lo que
no puede pasar en una comparación.

El umbral duro (12%) sale de la distribución real: de 83 modelos rankeados, la enorme
mayoría está bajo 5%, y los cuatro que lo cruzaban eran los cuatro que razonaban sin
estar declarados. No es un número redondo elegido a ojo: es donde la población se parte.

Uso:
    python benchmarks/check_truncamiento.py            # reporte
    python benchmarks/check_truncamiento.py --duro     # exit 1 si alguno cruza el umbral
"""

import argparse
import glob
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "benchmarks" / "results"
MODELS_JSON = ROOT / "docs" / "data" / "models.json"

# Dónde se parte la población. Ver el docstring: no es redondo, es medido.
UMBRAL = 0.12
# Bajo esta cantidad de runs el porcentaje es ruido, no señal.
MIN_RUNS = 40


def recolectar() -> dict:
    """% de `finish_reason == "length"` por modelo, sobre todos los runs en disco."""
    st = defaultdict(Counter)
    for f in glob.glob(str(RESULTS / "*.json")):
        try:
            d = json.loads(Path(f).read_text())
        except Exception:
            continue
        rs = d.get("results") if isinstance(d, dict) else d
        if not isinstance(rs, list):
            continue
        for r in rs:
            if isinstance(r, dict) and r.get("model"):
                st[r["model"]][r.get("finish_reason") or "?"] += 1
    return st


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--duro", action="store_true", help="exit 1 si algún rankeado cruza el umbral")
    # 18-ago-2026: ANTES esto era `--todos` y por defecto miraba SOLO los rankeados.
    # Ese default dejó pasar el peor caso que hubo: once de trece modelos NUEVOS
    # truncando (Seed 2.1 Turbo al 73%), invisibles porque todavía no rankeaban.
    #
    # Estaba exactamente al revés. Un modelo nuevo es donde MÁS importa: su nota se
    # publica por primera vez y no hay histórico con qué contrastarla. Un rankeado
    # que empieza a truncar, en cambio, se nota porque su score se mueve.
    ap.add_argument("--solo-rankeados", action="store_true",
                    help="mirar sólo los ya rankeados (era el default hasta el 18-ago)")
    a = ap.parse_args()

    st = recolectar()
    try:
        mj = json.loads(MODELS_JSON.read_text())
        rankeados = {m["name"] for m in mj["models"] if m.get("ranked")}
    except Exception:
        print("⚠️  no se pudo leer models.json — se revisa todo lo que haya en disco")
        rankeados = set(st)

    malos, ok = [], 0
    for m, c in st.items():
        tot = sum(c.values())
        if tot < MIN_RUNS:
            continue
        if a.solo_rankeados and m not in rankeados:
            continue
        p = c.get("length", 0) / tot
        if p >= UMBRAL:
            malos.append((p, m, c.get("length", 0), tot))
        else:
            ok += 1
    malos.sort(reverse=True)

    print(f"TRUNCAMIENTO — respuestas cortadas por el techo de tokens "
          f"(umbral {UMBRAL:.0%}, mínimo {MIN_RUNS} runs)\n")
    if not malos:
        print(f"  ✅ ninguno de los {ok} modelos con muestra suficiente cruza el umbral.")
        return 0

    print(f"  {'% cortado':>10}  {'cortados/total':>15}  modelo")
    for p, m, L, t in malos:
        print(f"  {p:>9.0%}  {f'{L}/{t}':>15}  {m}")
    print(f"\n  {len(malos)} modelo(s) publican una nota construida sobre respuestas a medias.")
    print("  Fix: agregar su patrón de id a THINKING_MODELS en providers/adapters.py")
    print("       (da max_tokens × 4 y piso de 8192) y RE-MEDIR — los runs viejos no")
    print("       son comparables con los nuevos, así que se archivan, no se mezclan.")
    return 1 if a.duro else 0


if __name__ == "__main__":
    sys.exit(main())
