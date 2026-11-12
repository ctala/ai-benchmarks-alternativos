#!/usr/bin/env python3
"""Lo que Astro todavía no compila se copia tal cual desde `sitio/legado/` a `dist`. (11-nov-2026, tarea 2.2)

POR QUÉ EXISTE
--------------
El corte del change `motor-sitio` reemplaza `sitio/legado/` por `dist`. Astro compila hoy las
comparaciones, los rankings, las variantes y los redirects. Las fichas, las landings, la home con
la calculadora y la página de proveedores siguen saliendo de Python (`motor: legado`) hasta el 1b.
Si `dist` no las llevara, el corte borraría 143 páginas. Además están los archivos que no son
páginas: `data/` (el JSON público), `app.js`, `style.css`, `img/`, `CNAME`, `robots.txt`,
`sitemap.xml`, `llms.txt` y la verificación de IndexNow.

Regla: se copia todo lo de `sitio/legado/` **salvo** las carpetas de las páginas que el registro declara en
Astro, porque esas las compila Astro. Si algo copiado choca con un archivo que Astro ya escribió,
falla: dos motores escribiendo la misma ruta es justo lo que el registro existe para impedir.

Uso:
    python benchmarks/copiar_legado.py --dist sitio/dist
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))


def copiar(docs: Path, dist: Path, regs: list[dict]) -> tuple[int, list[str]]:
    """(archivos copiados, choques). No copia las carpetas de las páginas que compila Astro."""
    de_astro = {e["slug"] for e in regs if e["motor"] == "astro" and e["slug"]}
    n, choques = 0, []
    for origen in sorted(docs.rglob("*")):
        if not origen.is_file():
            continue
        rel = origen.relative_to(docs)
        if rel.parts[0] in de_astro:
            continue
        destino = dist / rel
        if destino.exists():
            choques.append(str(rel))
            continue
        destino.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(origen, destino)
        n += 1
    return n, choques


def main() -> int:
    import registro_paginas as rp

    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", type=Path, default=ROOT / "sitio" / "dist")
    ap.add_argument("--docs", type=Path, default=ROOT / "sitio" / "legado")
    a = ap.parse_args()
    if not a.dist.is_dir():
        print(f"  ❌ no existe {a.dist}: primero `astro build`")
        return 1
    n, choques = copiar(a.docs, a.dist, rp.paginas())
    if choques:
        print(f"  ❌ {len(choques)} archivo(s) del legado chocan con lo que compiló Astro:")
        for c in choques[:20]:
            print(f"     · {c}")
        return 1
    print(f"  ✓ legado: {n} archivos copiados de sitio/legado/ a dist (fichas, landings, home, proveedores y archivos)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
