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
- **frontera** (11-nov-2026, Cristian): se recorre de menor a mayor costo por punto; un modelo
  entra solo si supera al último de la frontera por MÁS del ruido: diferencia pareada test a
  test mayor que 2 errores estándar. Si no, es «≈» y gana el más barato. Antes bastaba con una
  nota mayor, y la frontera coronaba diferencias de 0,02 que eran ruido.
- **piso de Eco**: un modelo queda bajo el piso si rinde peor que el redactor principal de Eco
  (`PISO_REF`, DeepSeek V4.1 Flash) por más del ruido, con la misma prueba pareada.

Escribe `sitio/legado/img/eco-redaccion.svg` y la tabla de la frontera dentro de OCASIONES.md, entre
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
SVG = ROOT / "sitio" / "legado" / "img" / "eco-redaccion.svg"
DOC = ROOT / "OCASIONES.md"
INI, FIN = "<!-- ECO-REDACCION-START -->", "<!-- ECO-REDACCION-END -->"
SUITE = "noticias_redaccion"
VENTANA = "benchmark_20261109_v61c"
# Los redactores de Eco hoy (inventario de Eco, 9-nov-2026): se señalan siempre, con su rol.
ECO = {"deepseek-v4.1-flash": "DeepSeek V4.1 Flash", "qwen3.7-flash": "Qwen 3.7 Flash"}
ROL_ECO = {"deepseek-v4.1-flash": "redactor principal de Eco", "qwen3.7-flash": "respaldo de Eco"}
# El piso: no rendir peor que el redactor PRINCIPAL de Eco por más del ruido. Hasta el 11-nov se
# calculó contra Qwen 3.7 Flash, que es el respaldo (DECISIONES, 11-nov-2026: corrección).
PISO_REF = "deepseek-v4.1-flash"

# Colores del Manual de Marca v2 (check_paleta): nada inventado. Verde neón para la frontera y
# cian para Eco: validate_palette.js da PASS en daltonismo (ΔE 27), visión normal (30) y contraste
# sobre #0a0a1a; la banda de luminosidad falla porque los neones son brillantes por diseño, y la
# identidad nunca es solo color: cada punto destacado lleva su etiqueta. El resto, muted.
AZUL, NARANJA, GRIS = "#39ff14", "#00d4ff", "#b0b0b0"
TINTA, TINTA2, FONDO, GRILLA = "#ffffff", "#b0b0b0", "#0a0a1a", "#1a1a2e"


def puntos() -> list[dict]:
    data = json.loads((ROOT / "sitio" / "legado" / "data" / "models.json").read_text(encoding="utf-8"))
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
        por_test: dict[str, list] = {}
        for r in rs:
            por_test.setdefault(r["test_name"], []).append(r["quality"])
        out.append({"key": k, "name": rank[k]["name"], "nota": round(nota, 2), "n": len(rs),
                    "costo_1k": round(costo, 4), "cpp": costo / nota,
                    "tests": {t: st.mean(v) for t, v in por_test.items()}})
    out.sort(key=lambda p: (p["cpp"], -p["nota"]))
    marcar(out)
    return out


def delta(a: dict, b: dict) -> tuple[float, float]:
    """Diferencia pareada test a test (a − b) y su margen de ruido (2 errores estándar)."""
    comun = [t for t in a["tests"] if t in b["tests"]]
    d = [a["tests"][t] - b["tests"][t] for t in comun]
    if len(d) < 2:
        return (st.mean(d) if d else 0.0), float("inf")
    return st.mean(d), 2 * st.stdev(d) / len(d) ** 0.5


def marcar(out: list[dict]) -> None:
    """Frontera con margen de ruido y piso de Eco. `out` viene ordenado por costo por punto."""
    if not out:
        return
    campeon, mejor_nota = out[0], out[0]["nota"]
    for p in out:
        p["frontera"], p["empata_con"], p["delta"], p["en_lugar_de"] = p is campeon, None, None, None
    for i, p in enumerate(out[1:], 1):
        md, margen = delta(p, campeon)
        coronaba = p["nota"] > mejor_nota          # la regla vieja: cualquier nota mayor
        mejor_nota = max(mejor_nota, p["nota"])
        if md > margen and md > 0:
            # 11-nov-2026 (Cristian): «≈ gana el más barato» también dentro de la frontera. Si
            # un modelo más barato que `p` (y más caro que el campeón) empata con `p`, el lugar
            # es suyo: lo que `p` le gana al campeón lo consigue igual, a menor costo.
            # El sustituto tiene que empatar con `p` Y estar por encima del campeón en nota: un
            # modelo peor que el campeón no hereda el salto solo porque su ruido es grande.
            igual = next((q for q in out[out.index(campeon) + 1:i]
                          if q["nota"] > campeon["nota"]
                          and abs(delta(p, q)[0]) <= delta(p, q)[1]), None)
            if igual is not None:
                dq = delta(p, igual)
                p["empata_con"], p["delta"] = igual["name"], (dq[0], dq[1], igual["name"])
                if not igual["frontera"]:
                    igual["frontera"], igual["empata_con"] = True, None
                    igual["delta"] = (*delta(igual, campeon), campeon["name"])
                    igual["en_lugar_de"] = (p["name"], campeon["name"])
                campeon = igual
                continue
            p["frontera"], p["delta"] = True, (md, margen, campeon["name"])
            campeon = p
        elif coronaba:
            # Con la regla vieja entraba; ahora es un empate y gana el más barato.
            p["empata_con"], p["delta"] = campeon["name"], (md, margen, campeon["name"])
    ref = next((q for q in out if q["key"] == PISO_REF), None)
    for p in out:
        p["bajo_piso"] = False
        if ref is not None and p is not ref:
            md, margen = delta(p, ref)
            p["bajo_piso"] = md < -margen


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
         f'<desc id="d">{len(ps)} modelos rankeados, ventana v6.1. Frontera costo/calidad en verde '
         f'(entra solo quien supera al anterior por más del ruido); redactores de Eco en cian; '
         f'los que rinden peor que el redactor principal de Eco, como anillo vacío.</desc>',
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
        if p["bajo_piso"]:
            tip += " · bajo el piso de Eco"
            # Segunda codificación, no solo color: bajo el piso es un anillo vacío.
            e.append(f'<circle cx="{X(p["cpp"]):.1f}" cy="{Y(p["nota"]):.1f}" r="{r - 0.75}" '
                     f'fill="{FONDO}" stroke="{color}" stroke-width="1.5"><title>{tip}</title></circle>')
            continue
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
    leyenda = ((AZUL, "Frontera costo/calidad", False), (NARANJA, "Redactor de Eco (principal y respaldo)", False),
               (GRIS, "Resto de los rankeados", False),
               (GRIS, f"Bajo el piso (peor que {ECO[PISO_REF]})", True))
    for i, (c, t, anillo) in enumerate(leyenda):
        y = H - mb - 68 + i * 16
        e.append(f'<circle cx="{lx}" cy="{y}" r="4.5" fill="{FONDO}" stroke="{c}" stroke-width="1.5"/>'
                 if anillo else f'<circle cx="{lx}" cy="{y}" r="5" fill="{c}"/>')
        e.append(f'<text x="{lx + 10}" y="{y + 4}" font-size="11" fill="{TINTA}">{t}</text>')
    e.append("</svg>")
    return "\n".join(e) + "\n"


def bloque(ps: list[dict]) -> str:
    f = lambda v: f"{v:.2f}".replace(".", ",")
    f3 = lambda v: f"{v:.3f}".replace(".", ",")
    filas = [p for p in ps if p["frontera"] or p["empata_con"] or p["key"] in ECO]
    lin = [INI, "",
           "![Redacción de noticias: nota contra costo por punto](sitio/legado/img/eco-redaccion.svg)", "",
           "| Modelo | Nota de redacción | US$ por 1.000 llamadas | US$ por 1.000 llamadas por punto "
           "| Diferencia pareada | |",
           "|---|---|---|---|---|---|"]
    for p in filas:
        d = p["delta"]
        dif = (f"{f(d[0]) if d[0] < 0 else '+' + f(d[0])} ± {f(d[1])} contra {d[2]}" if d else "—")
        marca = " · ".join(x for x in (
            ("frontera" + (f", en lugar de {p['en_lugar_de'][0]} (que supera a {p['en_lugar_de'][1]}"
                           " y empata con este, más barato)" if p["en_lugar_de"] else ""))
            if p["frontera"] else "",
            f"≈ {p['empata_con']}: gana el más barato" if p["empata_con"] else "",
            ROL_ECO.get(p["key"], ""),
            "bajo el piso de Eco" if p["bajo_piso"] else "") if x)
        lin.append(f"| {p['name']} | {f(p['nota'])} | {f(p['costo_1k'])} | {f3(p['cpp'])} | {dif} "
                   f"| {marca} |")
    bajo = sorted((p for p in ps if p["bajo_piso"]), key=lambda p: -p["nota"])
    lin += ["", "**Margen de ruido:** la diferencia pareada test a test en los 25 tests de "
            "`noticias_redaccion` (un run por test), con un margen de 2 errores estándar. Un modelo "
            "entra a la frontera solo si supera al anterior por más que ese margen; si no, es «≈» y "
            "gana el más barato. Lo mismo dentro de la frontera: si el que supera al anterior empata "
            "con uno más barato que también está por encima en nota, el lugar es del más barato.", "",
            f"**Bajo el piso de Eco** (rinde peor que {ECO[PISO_REF]}, el redactor principal, por más "
            f"del ruido): {len(bajo)} de {len(ps)} — "
            + ", ".join(f"{p['name']} ({f(p['nota'])})" for p in bajo) + ".",
            "", f"Generado por `generate_eco_redaccion.py` sobre {len(ps)} rankeados, runs de la "
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
