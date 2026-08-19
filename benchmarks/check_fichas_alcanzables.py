#!/usr/bin/env python3
"""¿Se puede LLEGAR a las fichas de modelo, o están publicadas y huérfanas?

POR QUÉ EXISTE (19-ago-2026)
----------------------------
Cristian, mirando la tabla de la home: *"desde acá deberíamos ser capaces de llegar al
card del modelo"*. Al ir a arreglarlo apareció que el problema era mucho mayor:

    16 de 16 páginas de ranking      sin un solo enlace a una ficha
    40 de 40 páginas de comparación  sin un solo enlace a una ficha

Se generaban **91 fichas por modelo** —con su ranking, su perfil por pilar, su
presupuesto de salida y su comparación contra los frontier— y no había forma de llegar
a ellas navegando. Trabajo publicado y enterrado.

LA CLASE DE FALLO QUE ES
------------------------
No es que algo esté roto: **es que la conexión no está hecha**. Y es la tercera vez en un
día que aparece la misma forma —el `piso` que el filtro del wizard no miraba, el campo
`page` que cuatro tareas tenían vacío, y esto—. Todos nuestros guardrails preguntaban
«¿esto está mal?»; ninguno preguntaba «¿esto está completo?».

Cristian: *"recuerda ir agregando todo lo que necesites a los estándares y a los
guardrails, la idea es no seguir cometiendo errores"*. Éste es de esa clase.

QUÉ VERIFICA
------------
  F1  cada modelo rankeado tiene su ficha en disco (si no, el enlace sería un 404)
  F2  cada página que LISTA modelos rankeados enlaza a sus fichas

No exige que TODO nombre sea un enlace: en prosa comparativa el enlace estorba. Exige
que la página que lista modelos ofrezca la salida hacia el detalle.

Uso:
    python benchmarks/check_fichas_alcanzables.py
    python benchmarks/check_fichas_alcanzables.py --duro
"""

import argparse
import glob
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
MODELS_JSON = DOCS / "data" / "models.json"

# Páginas que LISTAN modelos y por tanto deben ofrecer el camino al detalle.
LISTADOS = ("mejor-llm-*", "*-vs-*", "alternativas-*")


def main() -> int:
    # Sin `--duro`: este chequeo falla y punto.
    #
    # Nació en verde (las 5 páginas huérfanas se arreglaron en el mismo commit), así que
    # no hay deuda conocida que tolerar. Un `--duro` opcional acá sería una palanca
    # engañosa: `qa.py` lo declara bloqueante y lo invoca sin el flag, o sea que habría
    # dicho «bloqueante» y devuelto 0 para siempre. Es la misma clase de falso verde que
    # el `--todos` muerto en test_guardrails, encontrado el mismo día.
    argparse.ArgumentParser().parse_args()

    d = json.loads(MODELS_JSON.read_text())
    rankeados = [m for m in d["models"] if m.get("ranked")]

    # F1 · la ficha existe
    sin_ficha = [m["key"] for m in rankeados if not (DOCS / "modelo" / m["key"]).is_dir()]

    # F2 · las páginas que listan, enlazan
    huerfanas = []
    for pat in LISTADOS:
        for f in sorted(glob.glob(str(DOCS / pat / "index.html"))):
            s = Path(f).read_text(errors="ignore")
            if 'http-equiv="refresh"' in s:      # redirects: no listan nada
                continue
            # ¿lista modelos rankeados?
            listados = sum(1 for m in rankeados if m["name"] and m["name"] in s)
            if listados < 3:
                continue
            if 'href="/modelo/' not in s:
                huerfanas.append((Path(f).parent.name, listados))

    print("FICHAS ALCANZABLES\n")
    print(f"  F1 · rankeados con ficha en disco: {len(rankeados) - len(sin_ficha)}/{len(rankeados)}")
    print(f"  F2 · páginas que listan y NO enlazan: {len(huerfanas)}")
    if sin_ficha:
        print(f"\n  ❌ rankeados SIN ficha (su enlace sería 404): {sin_ficha[:6]}")
    if huerfanas:
        print("\n  ❌ publican modelos y no dejan llegar a su detalle:\n")
        for pg, n in huerfanas:
            print(f"     {pg:<44} lista {n} modelos rankeados")
        print("\n     Usá `enlace_ficha(m)` de generate_comparison — es el helper que")
        print("     resuelve el enlace y omite a los que no tienen ficha.")
    if not sin_ficha and not huerfanas:
        print("\n  ✅ toda ficha existe y toda página que lista modelos deja llegar a ella.")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
