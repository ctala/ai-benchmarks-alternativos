#!/usr/bin/env python3
"""Ninguna página muestra una entidad HTML como texto. (11-nov-2026, motor-sitio)

POR QUÉ EXISTE
--------------
`/alternativas-gemini/` mostraba «contexto &gt;128K» en vez de «contexto >128K». El texto de
la FAQ venía escrito como `&gt;128K` en `generate_manual_landings.py` y `faq_html` lo volvía
a escapar: en el HTML quedaba `&amp;gt;`, que el navegador pinta como `&gt;`. Y el JSON-LD,
que no se escapa, publicaba `&gt;128K` como texto literal. Nadie lo vio: la página cargaba bien.

  E1  el texto visible de una página no trae `&amp;gt;`, `&amp;lt;`, `&amp;amp;` ni otra
      entidad escapada dos veces (fuera de <script> y <style>).
  E2  ningún texto del JSON-LD trae una entidad HTML (`&gt;`, `&amp;`, `&#39;`…): el JSON-LD
      no se interpreta como HTML, así que Google la lee tal cual.
  E3  regla de páginas leídas: un árbol que no se lee no da verde.

Uso:
    python benchmarks/check_escapes.py                    # sitio/legado/
    python benchmarks/check_escapes.py --dist sitio/dist  # lo que compila Astro
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

ENTIDAD = r"(?:gt|lt|amp|quot|apos|nbsp|#\d+|#x[0-9a-fA-F]+|[a-z]{2,8})"
DOBLE = re.compile(rf"&amp;{ENTIDAD};")
LITERAL = re.compile(rf"&{ENTIDAD};")
JSONLD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)


def revisar_pagina(html: str) -> list[str]:
    """Fallos E1/E2 de UNA página. Función pura."""
    fallos = []
    visible = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    visible = re.sub(r"<[^>]+>", " ", visible)
    for m in DOBLE.finditer(visible):
        ctx = re.sub(r"\s+", " ", visible[max(0, m.start() - 30):m.end() + 15]).strip()
        fallos.append(f"E1 · muestra «&{m.group(0)[5:]}» como texto (escapado dos veces): «{ctx}»")
    for b in JSONLD.findall(html):
        for m in LITERAL.finditer(b):
            ctx = re.sub(r"\s+", " ", b[max(0, m.start() - 30):m.end() + 15]).strip()
            fallos.append(f"E2 · el JSON-LD trae la entidad «{m.group(0)}» como texto: «{ctx}»")
    return fallos


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", type=Path, default=None, help="revisar lo que compila Astro (sitio/dist)")
    a = ap.parse_args()
    base = a.dist or ROOT / "sitio" / "legado"
    import paginas_leidas as pl

    fallos, leidas = [], set()
    for f in sorted(base.rglob("index.html")):
        h = f.read_text(encoding="utf-8", errors="ignore")
        if 'http-equiv="refresh"' in h:
            continue
        url = pl.url_de(base, f)
        leidas.add(url)
        fallos += [f"{url}: {x}" for x in revisar_pagina(h)]
    print(f"ENTIDADES COMO TEXTO — {len(leidas)} página(s) de {base}")
    fallos += pl.exigir("E3", leidas, pl.esperadas())
    if fallos:
        for x in fallos[:40]:
            print(f"  ❌ {x}")
        print(f"\n  ❌ {len(fallos)} entidad(es) HTML que la página muestra como texto: se arreglan en el generador.")
        return 1
    print("  ✅ ninguna página muestra una entidad HTML como texto, ni en lo visible ni en su JSON-LD")
    return 0


if __name__ == "__main__":
    sys.exit(main())
