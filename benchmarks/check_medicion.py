#!/usr/bin/env python3
"""Lo que una página dice de la medición, dónde y cuándo, sale del dato. (11-nov-2026, motor-sitio 2.4)

  M1  cada comparación de Astro dice, por cada modelo de su tabla, dónde se midió: el proveedor
      que sirvió la mayoría de los runs (y qué parte, si no fueron todos), la cuantización y el
      razonamiento. La línea es la que calcula `exportar_sitio.linea_medido_en` desde
      `models.json`, ni más ni menos. «Endpoint ≠ modelo»: el mismo modelo rinde distinto según
      quién lo sirva (era la 1.4.c de `corte-v5-1`).
  T1  un año en un título (`<title>`, `og:title`, `<h1>`, `headline` del JSON-LD) es el de la
      medición: `medido_hasta` de `models.json`, o el de su modelo en una ficha. «(2026)» estaba
      escrito a mano en 141 líneas de los generadores.
  T2  un mes en un título va con su año y es el de la medición.
  M0  regla de páginas leídas (M1 sobre las comparaciones vivas de Astro; T1 sobre todas).

Uso:
    python benchmarks/check_medicion.py --dist sitio/dist
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
MODELS = ROOT / "docs" / "data" / "models.json"

ANIO = re.compile(r"(?<!\d)(20\d{2})(?!\d)")
TITULOS = (re.compile(r"<title>(.*?)</title>", re.S),
           re.compile(r'<meta property="og:title" content="([^"]*)"'),
           re.compile(r"<h1\b[^>]*>(.*?)</h1>", re.S),
           re.compile(r'"headline":\s*"([^"]*)"'))
ITEM = re.compile(r'<li data-medido-en="([^"]+)">(.*?)</li>', re.S)
TABLA = re.compile(r'<table class="results-table">(.*?)</table>', re.S)
FILA_MODELO = re.compile(r'data-modelo="([^"]+)"')


def _texto(s: str) -> str:
    return " ".join(_h.unescape(re.sub(r"<[^>]+>", "", s)).split())


def titulos(html: str) -> list[str]:
    return [_texto(m) for r in TITULOS for m in r.findall(html)]


def revisar_titulos(html: str, medicion: str) -> list[str]:
    """Fallos T1/T2 de una página, contra la fecha de medición que le toca. Función pura."""
    import fechas
    fallos = []
    for t in titulos(html):
        for a in ANIO.findall(t):
            if a != medicion[:4]:
                fallos.append(f"T1 · el título «{t[:70]}» dice {a} y la medición es de {medicion[:4]}")
        for i, mes in enumerate(fechas.MESES, 1):
            m = re.search(rf"\b{mes}\b(?:\s+de)?\s*(20\d{{2}})?", t, re.I)
            if m and (not m.group(1) or f"{m.group(1)}-{i:02d}" != medicion[:7]):
                fallos.append(f"T2 · el título «{t[:70]}» dice «{m.group(0)}» y la medición es de {medicion[:7]}")
    return fallos


def revisar_medido_en(html: str, por_key: dict) -> list[str]:
    """Fallos M1 de una comparación. Función pura."""
    from exportar_sitio import linea_medido_en
    fallos = []
    tabla = TABLA.search(html)
    filas = list(dict.fromkeys(FILA_MODELO.findall(tabla.group(1)))) if tabla else []
    items = {k: _texto(t) for k, t in ITEM.findall(html)}
    if not filas:
        return ["M1 · no encontré la tabla comparativa (¿cambió la plantilla?)"]
    for k in filas:
        m = por_key.get(k)
        if k not in items:
            fallos.append(f"M1 · {k} está en la tabla y no dice dónde se midió")
        elif m and items[k] != f"{m['name']}: {linea_medido_en(m)}":
            fallos.append(f"M1 · {k}: publica «{items[k]}» y el dato dice «{m['name']}: {linea_medido_en(m)}»")
    for k in set(items) - set(filas):
        fallos.append(f"M1 · {k} dice dónde se midió y no está en la tabla")
    return fallos


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", type=Path, required=True, help="el sitio compilado (sitio/dist)")
    a = ap.parse_args()
    import paginas_leidas as pl
    import registro_paginas as rp
    d = json.loads(MODELS.read_text(encoding="utf-8"))
    por_key = {m["key"]: m for m in d["models"]}
    global_ = d.get("medido_hasta") or ""
    regs = {e["url"]: e for e in rp.paginas()}

    fallos, leidas_t, leidas_m = [], set(), set()
    for f in sorted(a.dist.rglob("index.html")):
        h = f.read_text(encoding="utf-8", errors="ignore")
        if 'http-equiv="refresh"' in h:
            continue
        url = pl.url_de(a.dist, f)
        leidas_t.add(url)
        mf = re.match(r"/modelo/([^/]+)/$", url)
        medicion = ((por_key.get(mf.group(1)) or {}).get("medido_en") or {}).get("hasta") if mf else None
        fallos += [f"{url}: {x}" for x in revisar_titulos(h, medicion or global_)]
        e = regs.get(url) or {}
        if e.get("tipo") == "comparacion" and e.get("motor") == "astro" and not e.get("congelada"):
            fs = revisar_medido_en(h, por_key)
            if not any("no encontré la tabla" in x for x in fs):
                leidas_m.add(url)
            fallos += [f"{url}: {x}" for x in fs]
    print(f"LA MEDICIÓN EN LA PÁGINA — {len(leidas_t)} página(s) de {a.dist}")
    esperadas_m = {u for u, e in regs.items() if e["tipo"] == "comparacion" and e["motor"] == "astro"
                   and not e["redirect_a"] and not e.get("congelada")}
    fallos += pl.exigir("M0 (títulos)", leidas_t, pl.esperadas())
    fallos += pl.exigir("M0 (medido en)", leidas_m, esperadas_m)
    if fallos:
        for x in fallos[:40]:
            print(f"  ❌ {x}")
        print(f"\n  ❌ {len(fallos)} problema(s): lo que la página dice de la medición no es el dato.")
        return 1
    print(f"  ✅ cada comparación dice dónde se midió cada modelo, y cada año de un título es el de la medición ({global_[:4]})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
