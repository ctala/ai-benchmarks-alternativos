#!/usr/bin/env python3
"""¿El sitio publica voseo o localismos, en vez de español neutro?

POR QUÉ EXISTE (21-ago-2026)
----------------------------
El estándar del proyecto es **español neutro para todo lo publicable**, y el motivo no
es de estilo: la audiencia es LATAM + España, y el voseo rioplatense o un localismo
chileno excluyen a la mayoría de quien lee. Está escrito en las preferencias globales
desde hace meses.

Y el sitio lo rompía en su página principal: **«¿Querés ir más a fondo?»** como
encabezado de sección, y «Si querés que el precio pese, movés los pesos vos» en el
bloque que explica la metodología. Siete casos en cinco archivos, algunos en
generadores —o sea, replicados en decenas de páginas—. Nadie los escribió a propósito:
se cuelan al redactar rápido, y una vez publicados nadie los vuelve a leer.

Es el patrón de siempre acá: una regla correcta, escrita, y sin nada que la verifique.

QUÉ NO HACE
-----------
No corrige gramática ni tono. Sólo busca las formas verbales del voseo y un puñado de
localismos que el estándar prohíbe explícitamente. Un falso positivo se silencia
agregando el término a `PERMITIDAS` con su razón — por ejemplo, citar textualmente a
alguien que vosea.

Uso:
    python benchmarks/check_espanol_neutro.py
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Voseo: 2ª persona con acento en la última sílaba, e imperativos rioplatenses.
VOSEO = [
    "querés", "tenés", "podés", "hacés", "sabés", "elegís", "movés", "ajustás",
    "recortás", "mirás", "llamás", "usás", "buscás", "pagás", "necesitás", "vivís",
    "decís", "venís", "salís", "escribís", "seguís", "medís", "corrés", "ponés",
    "fijate", "acordate", "mirá", "dale", "andá", "tomá", "vení", "poné", "sos",
]
# Localismos que el estándar nombra: chilenos, mexicanos y peninsulares exclusivos.
LOCALISMOS = ["cachái", "po'", "weá", "órale", "wey", "chido", "vale que", "vosotros", "tío"]

# Excepciones declaradas, con su razón. Vacío hoy: si aparece una, va acá y no en el
# texto — así la excepción queda a la vista y no se convierte en costumbre.
PERMITIDAS: dict[str, str] = {}

# Dónde mirar: lo que se publica y lo que lo genera. Los comentarios de código quedan
# fuera —no los lee nadie de la audiencia— pero el texto dentro de generadores SÍ entra,
# porque termina en decenas de páginas.
OBJETIVOS = ["docs/index.html", "docs/app.js", "benchmarks/generate_*.py",
             "docs/*/index.html"]


def main() -> int:
    argparse.ArgumentParser().parse_args()
    patron = re.compile(r"\b(" + "|".join(VOSEO + LOCALISMOS) + r")\b", re.I)
    hallazgos = []
    vistos = 0
    for pat in OBJETIVOS:
        for f in sorted(ROOT.glob(pat)):
            txt = f.read_text(errors="ignore")
            if f.suffix in (".py", ".js"):
                # fuera comentarios y docstrings: son notas internas, no audiencia
                txt = re.sub(r'"""[\s\S]*?"""', "", txt)
                txt = re.sub(r"^\s*(#|//).*$", "", txt, flags=re.M)
            vistos += 1
            for m in patron.finditer(txt):
                t = m.group(1).lower()
                if t in PERMITIDAS:
                    continue
                linea = txt[:m.start()].count("\n") + 1
                ctx = re.sub(r"\s+", " ", txt[max(0, m.start() - 45):m.end() + 35]).strip()
                hallazgos.append((f.relative_to(ROOT), linea, t, ctx))

    print(f"ESPAÑOL NEUTRO — {vistos} archivo(s) publicables revisados\n")
    if not hallazgos:
        print("  ✅ sin voseo ni localismos: se lee igual en México, Chile, España o Perú.")
        return 0
    print(f"  ❌ {len(hallazgos)} uso(s) que excluyen a parte de la audiencia:\n")
    for f, l, t, ctx in hallazgos[:20]:
        print(f"     {str(f)}:{l}  «{t}»")
        print(f"        …{ctx}…")
    if len(hallazgos) > 20:
        print(f"     … y {len(hallazgos) - 20} más")
    print("\n     El estándar es español neutro para TODO lo publicable: la audiencia es")
    print("     LATAM + España, y el voseo excluye a la mayoría de quien lee.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
