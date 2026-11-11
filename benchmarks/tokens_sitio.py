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
        if MANUAL.exists() and COPIA.exists() and MANUAL.read_bytes() != COPIA.read_bytes():
            fallos.append("sitio/brand.json difiere del manual: correr tokens_sitio.py --sincronizar")
        for f in fallos:
            print(f"  ❌ {f}")
        if not fallos:
            print("  ✅ tokens del sitio: salen de brand.json")
        return 1 if fallos else 0
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(css, encoding="utf-8")
    print(f"✓ {SALIDA.relative_to(ROOT)} · {len(css.splitlines()) - 3} tokens · fuente {fuente()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
