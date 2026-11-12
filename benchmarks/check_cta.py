#!/usr/bin/env python3
"""Un solo CTA a la comunidad, al go-link, sin `skool.com` ni «gratis». (11-nov-2026, motor-sitio 2.4)

POR QUÉ EXISTE
--------------
Desde el 28-sep-2026 CAR es de pago y desde el 27-oct está cerrada a nuevos miembros: todo
enlace público va por `go.aprenderepite.com/<slug>` a la lista de espera. Al 11-nov, 204
páginas del benchmark enlazaban a `skool.com` y ninguna al go-link, y varias decían «Entrar es
gratis» o «curso gratis». Era la tarea 1.4.d de `corte-v5-1`, que pasó al motor.

  C1  ninguna página enlaza a `skool.com`.
  C2  todo enlace a `go.aprenderepite.com` va a `/benchmark`, el slug del benchmark.
  C3  a lo más un bloque de CTA a la comunidad por página (un enlace con clase `cta` o
      `cta-primary` al go-link). Los enlaces de la cabecera y del pie no son bloques.
  C4  nada dice «gratis» en el bloque que contiene un enlace a la comunidad (el `section`, `nav`,
      `header`, `footer`, `li`, `aside` o `details` más cercano): «Entrar es gratis» iba en el
      mismo bloque del CTA, en otro párrafo.
  C5  regla de páginas leídas.

Uso:
    python benchmarks/check_cta.py                    # docs/
    python benchmarks/check_cta.py --dist sitio/dist  # lo que compila Astro
"""
from __future__ import annotations

import argparse
import html as _h
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

GO = "https://go.aprenderepite.com/benchmark"
ENLACE = re.compile(r"<a\b([^>]*)>", re.I)
HREF = re.compile(r'href="([^"]*)"')
CLASE = re.compile(r'class="([^"]*)"')
BLOQUES = {"section", "nav", "header", "footer", "li", "aside", "details"}


class _Bloques(HTMLParser):
    """Para cada enlace a la comunidad, el texto del bloque más cercano que lo contiene."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pila: list[list] = [["raiz", [], False]]   # [etiqueta, textos, ¿contiene enlace?]
        self.textos_marcados: list[str] = []
        self.ignorar = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.ignorar += 1
        if tag in BLOQUES:
            self.pila.append([tag, [], False])
        if tag == "a" and "go.aprenderepite.com" in (dict(attrs).get("href") or ""):
            self.pila[-1][2] = True

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.ignorar:
            self.ignorar -= 1
        if tag in BLOQUES and len(self.pila) > 1 and self.pila[-1][0] == tag:
            etiqueta, textos, marcado = self.pila.pop()
            texto = " ".join(textos)
            self.pila[-1][1].append(texto)
            if marcado:
                self.textos_marcados.append(texto)

    def handle_data(self, data):
        if not self.ignorar:
            self.pila[-1][1].append(data)

    def cerrar(self) -> list[str]:
        self.close()
        while len(self.pila) > 1:
            self.handle_endtag(self.pila[-1][0])
        if self.pila[0][2]:
            self.textos_marcados.append(" ".join(self.pila[0][1]))
        return self.textos_marcados


def revisar_pagina(html: str) -> list[str]:
    """Fallos C1-C4 de UNA página. Función pura."""
    fallos, bloques = [], 0
    cuerpo = re.sub(r"<head\b.*?</head>", lambda m: " " * len(m.group(0)), html, flags=re.S | re.I)
    for m in ENLACE.finditer(cuerpo):
        href = (HREF.search(m.group(1)) or [None, ""])[1]
        clases = (CLASE.search(m.group(1)) or [None, ""])[1].split()
        if "skool.com" in href:
            fallos.append(f"C1 · enlaza a skool.com ({href[:60]}): CAR está cerrada, va al go-link")
            continue
        if "go.aprenderepite.com" not in href:
            continue
        if _h.unescape(href) != GO:
            fallos.append(f"C2 · enlaza a {href}: el benchmark usa {GO}")
        if {"cta", "cta-primary"} & set(clases):
            bloques += 1
    p = _Bloques()
    p.feed(cuerpo)
    for texto in p.cerrar():
        m = re.search(r"[^.]{0,60}\bgratis\b[^.]{0,30}", texto, re.I)
        if m:
            frase = " ".join(m.group(0).split())
            fallos.append(f"C4 · dice «gratis» en el bloque del enlace a la comunidad: «{frase}»")
    if bloques > 1:
        fallos.append(f"C3 · {bloques} bloques de CTA a la comunidad: va uno solo")
    return sorted(set(fallos))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", type=Path, default=None, help="revisar lo que compila Astro (sitio/dist)")
    a = ap.parse_args()
    base = a.dist or ROOT / "docs"
    import paginas_leidas as pl

    fallos, leidas = [], set()
    for f in sorted(base.rglob("index.html")):
        h = f.read_text(encoding="utf-8", errors="ignore")
        if 'http-equiv="refresh"' in h:
            continue
        url = pl.url_de(base, f)
        leidas.add(url)
        fallos += [f"{url}: {x}" for x in revisar_pagina(h)]
    print(f"CTA A LA COMUNIDAD — {len(leidas)} página(s) de {base}")
    fallos += pl.exigir("C5", leidas, pl.esperadas())
    if fallos:
        for x in fallos[:40]:
            print(f"  ❌ {x}")
        print(f"\n  ❌ {len(fallos)} problema(s) en el CTA: CAR está cerrada y es de pago.")
        return 1
    print(f"  ✅ un solo CTA a la comunidad por página, al go-link, sin skool.com ni «gratis»")
    return 0


if __name__ == "__main__":
    sys.exit(main())
