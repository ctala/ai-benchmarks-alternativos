#!/usr/bin/env python3
"""¿El sitio compilado salió del `models.json` de ahora? (11-nov-2026, motor-sitio 2.5)

POR QUÉ EXISTE
--------------
Astro compila desde `sitio/src/datos/`, que `exportar_sitio.py` escribe desde
`sitio/legado/data/models.json`. Si alguien re-exporta los datos (un lote nuevo, un modelo retirado)
y no recompila, `sitio/dist` sigue mostrando el ranking de ayer, y en el corte eso es lo que
se copia a `sitio/legado/`. Ninguna página se ve rota: cada cifra cuadra con los datos con los que se
compiló, que ya no son los publicados.

Cada página de Astro lleva `<meta name="datos-sha">`, la huella del `models.json` con el que
se compiló (`exportar_sitio.models_sha`). Este chequeo la compara con la de ahora.

  D1  cada página de Astro del registro (sin los redirects) declara su `datos-sha`.
  D2  ese sha es el del `models.json` de ahora: si no, hay que recompilar.
  D3  regla de páginas leídas: las páginas de Astro de `dist` son las que el registro declara.

Corre al final del `postbuild`, en `regenerate_all.py` después del build y en el Action.

Uso:
    python benchmarks/check_datos_dist.py --dist sitio/dist
    python benchmarks/check_datos_dist.py --dist <dir> --models <models.json>
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

SHA = re.compile(r'<meta name="datos-sha" content="([0-9a-f]*)"')


def revisar(dist: Path, esperado: str, astro: set[str]) -> tuple[list[str], set[str]]:
    """(fallos D1-D2, URLs de Astro leídas). Función pura sobre el árbol dado."""
    import paginas_leidas as pl
    fallos, leidas = [], set()
    for f in sorted(dist.rglob("index.html")):
        url = pl.url_de(dist, f)
        if url not in astro:
            continue
        leidas.add(url)
        m = SHA.search(f.read_text(encoding="utf-8", errors="ignore"))
        if not m:
            fallos.append(f"D1 · {url}: no declara con qué models.json se compiló (datos-sha)")
        elif m.group(1) != esperado:
            fallos.append(f"D2 · {url}: se compiló con models.json {m.group(1)} y el de ahora es {esperado}")
    return fallos, leidas


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", type=Path, required=True, help="el sitio compilado (sitio/dist)")
    ap.add_argument("--models", type=Path, default=ROOT / "sitio" / "legado" / "data" / "models.json")
    a = ap.parse_args()
    import paginas_leidas as pl
    import registro_paginas as rp
    from exportar_sitio import models_sha

    esperado = models_sha(a.models)
    astro = {e["url"] for e in rp.paginas() if e["motor"] == "astro" and not e["redirect_a"]}
    fallos, leidas = revisar(a.dist, esperado, astro)
    print(f"DATOS DEL SITIO COMPILADO — {len(leidas)} página(s) de Astro en {a.dist}")
    fallos += pl.exigir("D3", leidas, astro)
    if fallos:
        for x in fallos[:40]:
            print(f"  ❌ {x}")
        print(f"\n  ❌ {len(fallos)} problema(s): recompila con `npm run build` en sitio/.")
        return 1
    print(f"  ✅ cada página de Astro se compiló con el models.json de ahora ({esperado})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
