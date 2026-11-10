#!/usr/bin/env python3
"""Redacción para Eco: nota contra costo por punto, con la frontera. (10-nov-2026)

POR QUÉ EXISTE
--------------
La regresión de Eco (filtro, extracción, traducción, verificación) quedó decidida en OCASIONES:
ahí casi todos aciertan y sirve el más barato. **Redacción no**: separa modelos (55 % de runs
perfectos, sd 0,85) y es donde está el ahorro grande. La fila del 10-nov de DECISIONES dejó el
criterio: costo/calidad, no «el más barato que pase». Este generador lo aplica a la suite
`noticias_redaccion` de la ventana v6.1, sobre los rankeados.

QUÉ CALCULA
-----------
- **nota**: la media de `quality` de los 25 tests de `noticias_redaccion`, solo runs de la
  ventana (`benchmark_20261109_v61c*`), con éxito.
- **costo por punto**: US$ por 1.000 llamadas (media de `cost_usd`, el precio del proveedor
  declarado) dividido por la nota. Un modelo el doble de caro con la misma nota cuesta el doble
  por punto.
- **frontera**: los modelos que nadie supera en nota a un costo por punto menor o igual.

Escribe `docs/img/eco-redaccion.svg` y la tabla de la frontera dentro de OCASIONES.md, entre
`<!-- ECO-REDACCION-START -->` y `<!-- ECO-REDACCION-END -->`. Nada de esto se edita a mano.

Uso:
    python benchmarks/generate_eco_redaccion.py           # escribe
    python benchmarks/generate_eco_redaccion.py --check   # falla si el SVG o el bloque caducaron
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import statistics as st
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SVG = ROOT / "docs" / "img" / "eco-redaccion.svg"
DOC = ROOT / "OCASIONES.md"
INI, FIN = "<!-- ECO-REDACCION-START -->", "<!-- ECO-REDACCION-END -->"
SUITE = "noticias_redaccion"
VENTANA = "benchmark_20261109_v61c"
# Los redactores de Eco hoy (OCASIONES, «Redacción»): se señalan siempre.
ECO = {"deepseek-v4.1-flash": "DeepSeek V4.1 Flash", "qwen3.7-flash": "Qwen 3.7 Flash"}

# Colores del Manual de Marca v2 (check_paleta): nada inventado. Verde neón para la frontera y
# cian para Eco: validate_palette.js da PASS en daltonismo (ΔE 27), visión normal (30) y contraste
# sobre #0a0a1a; la banda de luminosidad falla porque los neones son brillantes por diseño, y la
# identidad nunca es solo color: cada punto destacado lleva su etiqueta. El resto, muted.
AZUL, NARANJA, GRIS = "#39ff14", "#00d4ff", "#b0b0b0"
TINTA, TINTA2, FONDO, GRILLA = "#ffffff", "#b0b0b0", "#0a0a1a", "#1a1a2e"


def puntos() -> list[dict]:
    data = json.loads((ROOT / "docs" / "data" / "models.json").read_text(encoding="utf-8"))
    rank = {m["key"]: m for m in data["models"] if m.get("ranked")}
    from benchmarks.models import MODELS  # noqa: PLC0415
    por_id = {}
    for k in rank:
        por_id.setdefault(MODELS[k]["id"], k)
    runs: dict[str, list] = {}
    for f in sorted(glob.glob(str(ROOT / "benchmarks" / "results" / f"{VENTANA}*.json"))):
        for r in json.loads(Path(f).read_text(encoding="utf-8"))["results"]:
            k = por_id.get(r.get("model_id"))
            if k and r.get("suite") == SUITE and r.get("success") and r.get("quality") is not None:
                runs.setdefault(k, []).append(r)
    out = []
    for k, rs in runs.items():
        nota = st.mean(r["quality"] for r in rs)
        costo = 1000 * st.mean(r.get("cost_usd") or 0 for r in rs)
        if nota <= 0 or costo <= 0:
            continue
        out.append({"key": k, "name": rank[k]["name"], "nota": round(nota, 2), "n": len(rs),
                    "costo_1k": round(costo, 4), "cpp": costo / nota})
    out.sort(key=lambda p: (p["cpp"], -p["nota"]))
    mejor = -1.0
    for p in out:
        p["frontera"] = p["nota"] > mejor
        mejor = max(mejor, p["nota"])
    return out


def svg(ps: list[dict]) -> str:
    W, H, ml, mr, mt, mb = 760, 460, 64, 24, 48, 56
    xs = [math.log10(p["cpp"]) for p in ps]
    x0, x1 = math.floor(min(xs)), math.ceil(max(xs))
    y0 = math.floor(min(p["nota"] for p in ps)) - 0.5
    y1 = 10.0
    X = lambda v: ml + (math.log10(v) - x0) / (x1 - x0) * (W - ml - mr)
    Y = lambda v: mt + (y1 - v) / (y1 - y0) * (H - mt - mb)
    e = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'font-family="Inter, system-ui, sans-serif" role="img" aria-labelledby="t d">',
         '<title id="t">Redacción de noticias: nota contra costo por punto</title>',
         f'<desc id="d">{len(ps)} modelos rankeados, ventana v6.1. Frontera en azul; redactores de '
         f'Eco en naranja.</desc>',
         f'<rect width="{W}" height="{H}" fill="{FONDO}"/>',
         f'<text x="{ml}" y="22" font-size="15" font-weight="700" font-family="JetBrains Mono, ui-monospace, monospace" fill="{TINTA}">Redacción de noticias: '
         f'nota contra costo por punto</text>',
         f'<text x="{ml}" y="38" font-size="11.5" fill="{TINTA2}">{len(ps)} rankeados · 25 tests · '
         f'ventana v6.1 · más arriba y más a la izquierda es mejor</text>']
    for d in range(x0, x1 + 1):
        x = X(10 ** d)
        e.append(f'<line x1="{x:.1f}" y1="{mt}" x2="{x:.1f}" y2="{H - mb}" stroke="{GRILLA}"/>')
        etiqueta = f"{10 ** d:g}".replace(".", ",")
        e.append(f'<text x="{x:.1f}" y="{H - mb + 16}" font-size="11" fill="{TINTA2}" '
                 f'text-anchor="middle">${etiqueta}</text>')
    v = math.ceil(y0)
    while v <= y1:
        y = Y(v)
        e.append(f'<line x1="{ml}" y1="{y:.1f}" x2="{W - mr}" y2="{y:.1f}" stroke="{GRILLA}"/>')
        e.append(f'<text x="{ml - 8}" y="{y + 4:.1f}" font-size="11" fill="{TINTA2}" '
                 f'text-anchor="end">{v}</text>')
        v += 1
    e.append(f'<text x="{(ml + W - mr) / 2}" y="{H - 14}" font-size="11.5" fill="{TINTA2}" '
             f'text-anchor="middle">US$ por 1.000 llamadas, por punto de nota (escala log)</text>')
    e.append(f'<text x="16" y="{(mt + H - mb) / 2}" font-size="11.5" fill="{TINTA2}" text-anchor="middle" '
             f'transform="rotate(-90 16 {(mt + H - mb) / 2})">Nota de redacción</text>')
    fr = [p for p in ps if p["frontera"]]
    e.append('<polyline fill="none" stroke="%s" stroke-width="2" points="%s"/>' % (
        AZUL, " ".join(f"{X(p['cpp']):.1f},{Y(p['nota']):.1f}" for p in fr)))
    orden = sorted(ps, key=lambda p: (p["key"] in ECO, p["frontera"]))
    for p in orden:
        color = NARANJA if p["key"] in ECO else AZUL if p["frontera"] else GRIS
        r = 6 if p["key"] in ECO or p["frontera"] else 4.5
        tip = escape(f"{p['name']}: nota {p['nota']:.2f}, US$ {p['costo_1k']:.3f} por 1.000 llamadas")
        tenue = ' fill-opacity="0.55"' if color == GRIS else ""
        e.append(f'<circle cx="{X(p["cpp"]):.1f}" cy="{Y(p["nota"]):.1f}" r="{r}" fill="{color}" '
                 f'stroke="{FONDO}" stroke-width="2"{tenue}><title>{tip}</title></circle>')
    # Etiquetas sin choques: cada una prueba posiciones (derecha, izquierda y después bajando en
    # escalones) y toma la primera cuya caja no pisa a otra etiqueta ni a un punto rotulado.
    # Si quedó lejos de su punto, una línea guía la une.
    cajas: list[tuple[float, float, float, float]] = []
    rot = [p for p in ps if p["key"] in ECO or p["frontera"]]
    for p in sorted(rot, key=lambda p: -p["nota"]):
        x, y = X(p["cpp"]), Y(p["nota"])
        cajas.append((x - 7, y - 7, x + 7, y + 7))
    choca = lambda b: any(not (b[2] < c[0] or b[0] > c[2] or b[3] < c[1] or b[1] > c[3]) for c in cajas)
    for p in sorted(rot, key=lambda p: (-p["nota"], p["cpp"])):
        x, y = X(p["cpp"]), Y(p["nota"])
        ancho = 6.3 * len(p["name"]) * (1.06 if p["key"] in ECO else 1)
        elegida = None
        for dy in (0, 16, 30, 44, 58, 72, 86):
            for lado in ((1, -1) if x < W * 0.7 else (-1, 1)):
                bx = x + 10 if lado > 0 else x - 10 - ancho
                b = (bx, y + dy - 6, bx + ancho, y + dy + 7)
                if b[0] >= ml and b[2] <= W - mr and not choca(b):
                    elegida = (b, lado, dy)
                    break
            if elegida:
                break
        if not elegida:
            continue
        b, lado, dy = elegida
        cajas.append(b)
        peso = ' font-weight="600"' if p["key"] in ECO else ""
        if dy:
            e.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{(b[0] if lado > 0 else b[2]):.1f}" '
                     f'y2="{y + dy:.1f}" stroke="{TINTA2}" stroke-width="1"/>')
        e.append(f'<text x="{b[0]:.1f}" y="{y + dy + 4:.1f}" font-size="11" fill="{TINTA}"{peso}>'
                 f'{escape(p["name"])}</text>')
    lx = W - mr - 190
    for i, (c, t) in enumerate(((AZUL, "Frontera costo/calidad"), (NARANJA, "Redactor de Eco hoy"),
                                (GRIS, "Resto de los rankeados"))):
        y = H - mb - 52 + i * 16
        e.append(f'<circle cx="{lx}" cy="{y}" r="5" fill="{c}"/>')
        e.append(f'<text x="{lx + 10}" y="{y + 4}" font-size="11" fill="{TINTA}">{t}</text>')
    e.append("</svg>")
    return "\n".join(e) + "\n"


def bloque(ps: list[dict]) -> str:
    f = lambda v: f"{v:.2f}".replace(".", ",")
    f3 = lambda v: f"{v:.3f}".replace(".", ",")
    filas = [p for p in ps if p["frontera"] or p["key"] in ECO]
    lin = [INI, "",
           "![Redacción de noticias: nota contra costo por punto](docs/img/eco-redaccion.svg)", "",
           "| Modelo | Nota de redacción | US$ por 1.000 llamadas | US$ por 1.000 llamadas por punto | |",
           "|---|---|---|---|---|"]
    for p in filas:
        marca = " · ".join(x for x in ("frontera" if p["frontera"] else "",
                                         "redactor de Eco" if p["key"] in ECO else "") if x)
        lin.append(f"| {p['name']} | {f(p['nota'])} | {f(p['costo_1k'])} | {f3(p['cpp'])} | {marca} |")
    lin += ["", f"Generado por `generate_eco_redaccion.py` sobre {len(ps)} rankeados, runs de la "
            "ventana v6.1. No se edita a mano.", "", FIN]
    return "\n".join(lin)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    sys.path.insert(0, str(ROOT))
    ps = puntos()
    nuevo_svg, nuevo_bloque = svg(ps), bloque(ps)
    doc = DOC.read_text(encoding="utf-8")
    if INI not in doc or FIN not in doc:
        print(f"❌ OCASIONES.md no tiene el bloque {INI} … {FIN}")
        return 1
    nuevo_doc = doc.split(INI)[0] + nuevo_bloque + doc.split(FIN, 1)[1]
    if a.check:
        malo = []
        if not SVG.exists() or SVG.read_text(encoding="utf-8") != nuevo_svg:
            malo.append(str(SVG.relative_to(ROOT)))
        if doc != nuevo_doc:
            malo.append("OCASIONES.md (bloque de redacción)")
        for m in malo:
            print(f"❌ caducado: {m} — correr generate_eco_redaccion.py")
        if not malo:
            print("✅ redacción de Eco: el gráfico y la tabla salen de los runs de hoy")
        return 1 if malo else 0
    SVG.parent.mkdir(parents=True, exist_ok=True)
    SVG.write_text(nuevo_svg, encoding="utf-8")
    DOC.write_text(nuevo_doc, encoding="utf-8")
    print(f"✓ {SVG.relative_to(ROOT)} · {len(ps)} modelos · frontera: "
          + ", ".join(p["name"] for p in ps if p["frontera"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
