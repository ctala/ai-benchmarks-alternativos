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
    python benchmarks/check_espanol_neutro.py                     # docs/ y los generadores
    python benchmarks/check_espanol_neutro.py --dist sitio/dist   # lo compilado

PÁGINAS LEÍDAS (11-nov-2026, motor-sitio 2.3): lee cada `index.html` del árbol, a cualquier
profundidad, y falla si no leyó todas las páginas que el registro publica. Antes buscaba en
`docs/*/index.html`, un solo nivel: las 132 fichas de `docs/modelo/` nunca se revisaron.
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
GENERADORES = ["benchmarks/generate_*.py"]


def archivos(base: Path, con_generadores: bool) -> list[Path]:
    """Las páginas (todo `index.html`, a cualquier profundidad), `app.js` y, si se revisa la
    fuente, los generadores."""
    fs = sorted(base.rglob("index.html"))
    if (base / "app.js").exists():
        fs.append(base / "app.js")
    if con_generadores:
        fs += [f for pat in GENERADORES for f in sorted(ROOT.glob(pat))]
    return fs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", type=Path, help="revisar lo compilado en vez de docs/")
    ap.add_argument("--docs", type=Path, default=ROOT / "docs", help="otro docs/ (para el sabotaje)")
    a = ap.parse_args()
    sys.path.insert(0, str(ROOT / "benchmarks"))
    import paginas_leidas as pl
    base = (a.dist or a.docs).resolve()
    patron = re.compile(r"\b(" + "|".join(VOSEO + LOCALISMOS) + r")\b", re.I)
    hallazgos, leidas = [], set()
    fs = archivos(base, con_generadores=not a.dist)
    for f in fs:
        txt = f.read_text(errors="ignore")
        if f.name == "index.html":
            leidas.add(pl.url_de(base, f))
        if f.suffix in (".py", ".js"):
            # fuera comentarios y docstrings: son notas internas, no audiencia
            txt = re.sub(r'"""[\s\S]*?"""', "", txt)
            txt = re.sub(r"^\s*(#|//).*$", "", txt, flags=re.M)
        for m in patron.finditer(txt):
            t = m.group(1).lower()
            if t in PERMITIDAS:
                continue
            linea = txt[:m.start()].count("\n") + 1
            ctx = re.sub(r"\s+", " ", txt[max(0, m.start() - 45):m.end() + 35]).strip()
            donde = f.relative_to(base) if base in f.parents else f.relative_to(ROOT)
            hallazgos.append((donde, linea, t, ctx))

    print(f"ESPAÑOL NEUTRO — {len(fs)} archivo(s) publicables revisados en {base.name}/\n")
    ciego = pl.exigir("check_espanol_neutro", leidas, pl.esperadas())
    for c in ciego:
        print(f"  ❌ {c}")
    if not hallazgos:
        if ciego:
            return 1
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
