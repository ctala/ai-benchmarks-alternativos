#!/usr/bin/env python3
"""Los tokens del sitio salen de `brand.json`, no de una hoja de estilos. (11-nov-2026)

POR QUÉ EXISTE
--------------
El motor del sitio (change `motor-sitio`, DECISIONES 11-nov-2026) usa el tema claro del nivel
Cercano del manual. Cristian lo pidió así: «ningún color fuera de los tokens». El manual vive
en `~/Playground/brand-manuals/cristian-tala/tokens/brand.json`. Si el CSS copiara sus valores
a mano, se desviaría como pasó en agosto, cuando el sitio llegó a tener 30 hex y 22 eran
inventados (`check_paleta.py`). Por eso este script ESCRIBE `sitio/src/styles/tokens.css` y
`check_paleta` P4 exige que el archivo sea igual a lo que sale de `brand.json`.

Lo que sale: cada rol de `themes.light` como `--color-<rol>`; las familias de `typography`;
`radius`, `spacing` y `motion`; y la sombra destacada en claro de `extensions.sombras`.

LEGADO (motor-sitio 2.2, 11-nov-2026; Cristian eligió «claro ya»): las páginas que todavía salen de
Python (fichas, landings, home, proveedores) usan `docs/style.css` con sus propias variables
(`--bg`, `--green`, `--white`…). Su `:root` también se genera acá, entre marcadores, mapeando
cada variable a un rol del mismo tema (`MAPEO_LEGADO`). Así el claro llega al sitio entero el
día del corte y ningún color del legado queda escrito a mano. `--check` verifica los dos.

El repo es público y `brand.json` vive fuera de él. Si no está (en el CI, por ejemplo), se usa
la copia versionada `sitio/brand.json`. `--sincronizar` la refresca y P4 avisa si difieren.

Uso:
    python benchmarks/tokens_sitio.py                 # escribe tokens.css
    python benchmarks/tokens_sitio.py --check         # falla si tokens.css no sale de brand.json
    python benchmarks/tokens_sitio.py --sincronizar   # copia brand.json del manual al repo
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANUAL = Path.home() / "Playground" / "brand-manuals" / "cristian-tala" / "tokens" / "brand.json"
COPIA = ROOT / "sitio" / "brand.json"
SALIDA = ROOT / "sitio" / "src" / "styles" / "tokens.css"
TEMA = "light"     # nivel Cercano, claro por defecto (DECISIONES 11-nov-2026); el oscuro, en el 1b
LEGADO = ROOT / "docs" / "style.css"
INICIO_LEGADO = "/* AUTO-TOKENS-LEGADO-START · generado por benchmarks/tokens_sitio.py desde brand.json; no se edita a mano */"
FIN_LEGADO = "/* AUTO-TOKENS-LEGADO-END */"
# Variable del legado → rol del tema. Los nombres vienen del tema oscuro (`--green` era el primario,
# `--white` el texto fuerte); lo que se conserva es el ROL, no el color.
MAPEO_LEGADO = {
    "bg": "base-100",            # fondo de página
    "bg-grid": "base-200",       # inset: code blocks y fondos alternativos
    "bg-card": "base-200",       # cards y superficies de lectura
    "green": "primary",          # primario: headings, CTAs
    "cyan": "link",              # secundario: links y badges
    "purple": "accent",          # acento: glow y grid
    "magenta": "warning",        # alertas, uso escaso
    "white": "titulo",           # texto fuerte
    "prose": "base-content",     # prosa
    "gray": "muted",             # captions
    "gray-dark": "muted",        # UI apagada
    "muted": "muted",            # se usaba sin declararse (caía al color heredado)
    "border": "decorative-line", # bordes y líneas
}


def fuente() -> Path:
    return MANUAL if MANUAL.exists() else COPIA


def generar(marca: dict) -> str:
    tema = marca["themes"][TEMA]
    tipo = marca["typography"]
    lin = ["/* Generado por benchmarks/tokens_sitio.py desde brand.json "
           f"(v{marca['brand']['version']}, tema {TEMA}, nivel Cercano). No se edita a mano. */",
           ":root {"]
    lin += [f"  --color-{rol}: {hexa.lower()};" for rol, hexa in tema.items()]
    for nombre, t in tipo.items():
        lin.append(f"  --font-{nombre}: \"{t['family']}\", {t['fallback']};")
    lin += [f"  --radius-{k}: {v};" for k, v in marca["radius"].items()]
    lin += [f"  --space-{i}: {v}px;" for i, v in enumerate(marca["spacing"], 1)]
    lin += [f"  --motion-{k}: {v}ms;" for k, v in marca["motion"].items()]
    sombras = (marca.get("extensions") or {}).get("sombras") or {}
    for nombre in ("destacada", "destacada-2"):
        if nombre in sombras:
            lin.append(f"  --shadow-{nombre}: {sombras[nombre]['claro']};")
    lin.append("}")
    return "\n".join(lin) + "\n"


def generar_legado(marca: dict) -> str:
    """El bloque `:root` de `docs/style.css`, con sus marcadores."""
    tema = marca["themes"][TEMA]
    lin = [INICIO_LEGADO, ":root {"]
    lin += [f"  --{var}: {tema[rol].lower()};   /* {rol} */" for var, rol in MAPEO_LEGADO.items()]
    lin += ["}", FIN_LEGADO]
    return "\n".join(lin)


def con_legado(css: str, bloque: str) -> str:
    """`docs/style.css` con su bloque de tokens reemplazado. Falla si faltan los marcadores."""
    if INICIO_LEGADO not in css or FIN_LEGADO not in css:
        raise SystemExit(f"❌ faltan los marcadores de tokens en {LEGADO.relative_to(ROOT)}")
    i, j = css.index(INICIO_LEGADO), css.index(FIN_LEGADO) + len(FIN_LEGADO)
    return css[:i] + bloque + css[j:]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--sincronizar", action="store_true")
    a = ap.parse_args()
    if a.sincronizar:
        if not MANUAL.exists():
            print(f"❌ no está el manual en {MANUAL}")
            return 1
        shutil.copyfile(MANUAL, COPIA)
        print(f"✓ {COPIA.relative_to(ROOT)} ← {MANUAL}")
    marca = json.loads(fuente().read_text(encoding="utf-8"))
    css = generar(marca)
    if a.check:
        fallos = []
        if not SALIDA.exists() or SALIDA.read_text(encoding="utf-8") != css:
            fallos.append(f"{SALIDA.relative_to(ROOT)} no sale de brand.json: correr tokens_sitio.py")
        if LEGADO.exists():
            actual = LEGADO.read_text(encoding="utf-8")
            if INICIO_LEGADO not in actual or con_legado(actual, generar_legado(marca)) != actual:
                fallos.append(f"{LEGADO.relative_to(ROOT)}: su :root no sale de brand.json: correr tokens_sitio.py")
        if MANUAL.exists() and COPIA.exists() and MANUAL.read_bytes() != COPIA.read_bytes():
            fallos.append("sitio/brand.json difiere del manual: correr tokens_sitio.py --sincronizar")
        for f in fallos:
            print(f"  ❌ {f}")
        if not fallos:
            print("  ✅ tokens del sitio: salen de brand.json")
        return 1 if fallos else 0
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(css, encoding="utf-8")
    if LEGADO.exists():
        actual = LEGADO.read_text(encoding="utf-8")
        nuevo = con_legado(actual, generar_legado(marca))
        if nuevo != actual:
            LEGADO.write_text(nuevo, encoding="utf-8")
            print(f"✓ {LEGADO.relative_to(ROOT)} · :root del legado regenerado (correr sync_cachebust.py)")
    print(f"✓ {SALIDA.relative_to(ROOT)} · {len(css.splitlines()) - 3} tokens · fuente {fuente()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
