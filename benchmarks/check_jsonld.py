#!/usr/bin/env python3
"""El JSON-LD de cada página es válido y dice lo que la página muestra. (11-nov-2026, motor-sitio 2.3)

POR QUÉ EXISTE
--------------
El JSON-LD es lo que leen Google y los buscadores con IA, y nadie lo mira: no se ve en la
página. Ningún chequeo lo validaba. El corte cambia el motor de 61 páginas: si una plantilla
emite un bloque mal formado, sin fecha o con una FAQ que la página no muestra, el sitio sigue
cargando y el error solo aparece semanas después en Search Console. Google exige que el
contenido de una FAQPage sea visible en la página; una FAQ invisible es una acción manual.

  J1  cada bloque `application/ld+json` parsea como JSON.
  J2  cada tipo trae sus campos: Article (headline, datePublished, dateModified, author),
      Dataset (name, description, url), FAQPage (al menos una pregunta, cada una con su
      respuesta), SoftwareApplication (name).
  J3  las fechas son ISO (AAAA-MM-DD) y dateModified no es anterior a datePublished.
  J4  una FAQPage solo si cada pregunta y cada respuesta se ven en el texto de la página.
  J5  la `url` de un Article o un Dataset de página es su canonical.
  J6  toda página con contenido del registro publica al menos un bloque (regla de páginas
      leídas: un árbol que no se lee no tiene JSON-LD que objetar).

J4 BLOQUEA EN TODO EL SITIO DESDE EL 11-NOV
-------------------------------------------
Al nacer, J4 encontró 8 casos, todos del legado: la home, escrita a mano, traía en su JSON-LD
otra versión de 6 respuestas y una pregunta que la página ya no mostraba, y
`/alternativas-gemini/` mostraba `&amp;gt;` por un doble escape. Como un chequeo que nace en
rojo no puede ser bloqueante, J4 avisaba en el legado. Se arreglaron en la fuente el mismo día
(la FAQPage de la home la genera `generate_home_jsonld.py` desde la FAQ visible; el doble
escape, en `generate_manual_landings.py`) y J4 quedó en verde en todo el sitio: desde
entonces bloquea en todo el sitio, igual que J1, J2, J3, J5 y J6.

Uso:
    python benchmarks/check_jsonld.py                    # docs/
    python benchmarks/check_jsonld.py --dist sitio/dist  # lo que compila Astro
"""
from __future__ import annotations

import argparse
import html as _h
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

BLOQUE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
CANONICAL = re.compile(r'<link rel="canonical" href="([^"]*)"')
FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}")
REQUERIDOS = {
    "Article": ("headline", "datePublished", "dateModified", "author"),
    "Dataset": ("name", "description", "url"),
    "FAQPage": ("mainEntity",),
    "SoftwareApplication": ("name",),
}


def _texto(html: str) -> str:
    """El texto visible de la página, sin espacios: quitar etiquetas deja «Phi-4 ,» donde la página
    muestra «Phi-4,», y esa diferencia no es de contenido."""
    t = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    return _sin_espacios(re.sub(r"<[^>]+>", " ", t))


def _sin_espacios(s: str) -> str:
    return re.sub(r"\s+", "", _h.unescape(s or ""))


def _norm(s: str) -> str:
    """Una pregunta o respuesta de la FAQ, legible (para el mensaje)."""
    return re.sub(r"\s+", " ", _h.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def revisar_pagina(html: str) -> tuple[list[str], int]:
    """(fallos, bloques leídos) de UNA página. Función pura."""
    fallos, n = [], 0
    visible = None
    canon = CANONICAL.search(html)
    for b in BLOQUE.findall(html):
        n += 1
        try:
            d = json.loads(b)
        except json.JSONDecodeError as e:
            fallos.append(f"J1 · un bloque no parsea: {e.msg} (línea {e.lineno})")
            continue
        items = d.get("@graph", [d]) if isinstance(d, dict) else d
        for it in items:
            t = it.get("@type")
            for campo in REQUERIDOS.get(t, ()):
                if not it.get(campo):
                    fallos.append(f"J2 · {t} sin `{campo}`")
            if t in ("Article", "Dataset"):
                pub, mod = it.get("datePublished"), it.get("dateModified")
                for nombre, v in (("datePublished", pub), ("dateModified", mod)):
                    if v and not FECHA.match(str(v)):
                        fallos.append(f"J3 · {t}.{nombre} no es ISO: «{v}»")
                if pub and mod and FECHA.match(str(pub)) and FECHA.match(str(mod)) and str(mod)[:10] < str(pub)[:10]:
                    fallos.append(f"J3 · {t}: dateModified {mod} es anterior a datePublished {pub}")
                url = it.get("url")
                if url and canon and "@id" not in it and url != canon.group(1):
                    fallos.append(f"J5 · {t}.url «{url}» no es el canonical «{canon.group(1)}»")
            if t == "FAQPage":
                visible = visible if visible is not None else _texto(html)
                qs = it.get("mainEntity") or []
                for q in qs:
                    nombre = _norm(q.get("name"))
                    resp = _norm((q.get("acceptedAnswer") or {}).get("text"))
                    if not nombre or not resp:
                        fallos.append("J2 · una pregunta de la FAQ sin texto o sin respuesta")
                        continue
                    if _sin_espacios(nombre) not in visible:
                        fallos.append(f"J4 · la FAQ declara «{nombre[:60]}» y la página no la muestra")
                    elif _sin_espacios(resp)[:80] not in visible:
                        fallos.append(f"J4 · la respuesta a «{nombre[:50]}» no se ve en la página")
    return fallos, n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", type=Path, default=None, help="revisar lo que compila Astro (sitio/dist)")
    a = ap.parse_args()
    base = a.dist or ROOT / "docs"
    import paginas_leidas as pl

    fallos, leidas, bloques = [], set(), 0
    for f in sorted(base.rglob("index.html")):
        h = f.read_text(encoding="utf-8", errors="ignore")
        if 'http-equiv="refresh"' in h:
            continue                     # un redirect no publica contenido ni JSON-LD
        url = pl.url_de(base, f)
        fs, n = revisar_pagina(h)
        if n:
            leidas.add(url)
        bloques += n
        fallos += [f"{url}: {x}" for x in fs]
    print(f"JSON-LD — {bloques} bloque(s) en {len(leidas)} página(s) de {base}")
    fallos += pl.exigir("J6", leidas, pl.esperadas())
    if fallos:
        for x in fallos[:40]:
            print(f"  ❌ {x}")
        print(f"\n  ❌ {len(fallos)} problema(s) en el JSON-LD: es lo que leen Google y los buscadores con IA.")
        return 1
    print("  ✅ cada bloque parsea, trae sus campos y fecha bien, y su FAQ se ve en la página")
    return 0


if __name__ == "__main__":
    sys.exit(main())
