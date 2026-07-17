#!/usr/bin/env python3
"""
Genera la imagen Open Graph (1200x630) de la calculadora/benchmark a partir de
docs/data/models.json — representativa del producto (ranking real top-5 + stats),
no del logo personal. Marca synthwave (cyan/verde/oro, JetBrains Mono).

Salida: docs/og-benchmark.png  (referenciada en docs/index.html og:image/twitter:image)

Regenerar tras cada lote (la incluyo en el pipeline de auto-generación):
    python benchmarks/generate_og_image.py
"""
import json, os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_JSON = os.path.join(ROOT, "docs", "data", "models.json")
OUT = os.path.join(ROOT, "docs", "og-benchmark.png")

W, H = 1200, 630
# Marca
BG      = (10, 10, 26)       # #0a0a1a
GREEN   = (57, 255, 20)      # #39ff14
CYAN    = (0, 212, 255)      # #00d4ff
GOLD    = (255, 215, 0)      # #ffd700
ORANGE  = (255, 170, 0)      # #ffaa00
PINK    = (255, 0, 110)      # #ff006e
WHITE   = (255, 255, 255)
GRAY    = (176, 176, 176)    # #b0b0b0
PANEL   = (22, 22, 42)
GRID    = (30, 40, 70)

FONT_DIR = os.path.expanduser("~/.local/share/fonts")

# Cadena de fallback de fuentes, en orden de preferencia.
#
# BUG (12-jul-2026): la unica ruta era ~/.local/share/fonts (Linux, el Spark). Al
# generar la OG desde el Mac, ninguna existia -> caia a ImageFont.load_default(),
# que es una fuente BITMAP sin acentos. La tarjeta social del sitio decia
# "Eleg[]el mejor para TU caso" y "espa[]ol". Es la primera imagen que ve alguien
# al compartir el link, con la marca al lado.
#
# Ahora: JetBrains Mono (la de marca) si esta; si no, un mono del sistema que SI
# tenga los glifos latinos. Nunca load_default().
_CANDIDATES = [
    os.path.join(FONT_DIR, "JetBrainsMono-Medium.ttf"),          # marca (Linux/Spark)
    os.path.expanduser("~/Library/Fonts/JetBrainsMono-Medium.ttf"),  # marca (macOS)
    "/System/Library/Fonts/Menlo.ttc",                            # macOS mono
    "/System/Library/Fonts/SFNSMono.ttf",                         # macOS mono
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",        # Linux
    "/usr/lib/python3/dist-packages/reportlab/fonts/DejaVuSansMono.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",               # ultimo recurso
]


def _font(size, bold=False):
    for p in _CANDIDATES:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    # Si llegamos acá la OG saldría sin acentos: mejor fallar ruidoso que publicar
    # una tarjeta social rota con la marca al lado.
    raise SystemExit(
        "ERROR: no encontré ninguna fuente con glifos latinos.\n"
        "La OG saldría con los acentos rotos (á, í, ñ como cuadrados).\n"
        f"Probé: {chr(10).join('  - ' + c for c in _CANDIDATES)}"
    )

def _text_w(draw, txt, font):
    b = draw.textbbox((0, 0), txt, font=font)
    return b[2] - b[0]

def main():
    d = json.load(open(MODELS_JSON))
    models = d.get("models", [])
    # RANKEABLES (>=50 runs), no `tested` (>=20). Es la imagen que se ve al compartir
    # el sitio: con `tested` coronaba a MiniMax M2.7 — que tiene 39 runs y NO entra al
    # ranking. La tarjeta social mostraba un #1 que el propio sitio no reconoce.
    n_tested = d.get("ranked_count", len([m for m in models if m.get("ranked")]))
    ms = [m for m in models if m.get("ranked")]
    ms.sort(key=lambda m: -m.get("score_global", 0))
    top = [m for m in ms if m.get("score_global")][:5]
    if not top and ms:
        top = ms[:5]

    suite_keys = set()
    for m in ms:
        suite_keys.update((m.get("score_by_suite") or {}).keys())
    n_suites = len(suite_keys)

    img = Image.new("RGB", (W, H), BG)
    dr = ImageDraw.Draw(img)

    # --- grid de fondo (synthwave) ---
    for x in range(0, W, 48):
        dr.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(0, H, 48):
        dr.line([(0, y), (W, y)], fill=GRID, width=1)
    # borde superior de acento
    dr.rectangle([0, 0, W, 6], fill=GREEN)

    PAD = 60
    # --- header ---
    f_tag = _font(22)
    dr.ellipse([PAD, 40, PAD + 14, 54], fill=GREEN)
    dr.text((PAD + 24, 36), "benchmarks.cristiantala.com", font=f_tag, fill=GREEN)
    tag_r = f"{d.get('scoring_version', 'v4.0')} · quality 70% · cost 15% · speed/latency 7.5%"
    dr.text((W - PAD - _text_w(dr, tag_r, f_tag), 36), tag_r, font=f_tag, fill=GRAY)

    # --- título ---
    f_title = _font(60)
    dr.text((PAD, 84), "Benchmark de Modelos IA", font=f_title, fill=WHITE)
    f_sub = _font(28)
    dr.text((PAD, 158), "Elige el mejor para TU caso — no el que está de moda", font=f_sub, fill=CYAN)

    # --- stat strip ---
    f_stat = _font(24)
    stats = f"{n_tested} modelos analizados   ·   {n_suites} suites   ·   tests reales en español"
    dr.text((PAD, 206), stats, font=f_stat, fill=GRAY)

    # --- panel ranking top-5 ---
    panel_y0 = 256
    dr.rounded_rectangle([PAD, panel_y0, W - PAD, H - 70], radius=16, fill=PANEL)
    f_hdr = _font(22)
    dr.text((PAD + 28, panel_y0 + 18), "TOP 5  ·  score global ponderado", font=f_hdr, fill=GOLD)

    rows_y0 = panel_y0 + 58
    row_h = 46
    bar_x0 = PAD + 360
    bar_x1 = W - PAD - 120
    max_score = max((m.get("score_global", 0) for m in top), default=10) or 10
    f_rank = _font(26)
    f_name = _font(24)
    f_score = _font(28)
    medal = {0: GOLD, 1: (200, 200, 210), 2: ORANGE}
    for i, m in enumerate(top):
        y = rows_y0 + i * row_h
        cy = y + row_h // 2
        col = medal.get(i, CYAN)
        # rank
        dr.text((PAD + 28, y + 8), f"#{i+1}", font=f_rank, fill=col)
        # nombre: sacar el provider entre paréntesis y recortar para no chocar la barra
        name = m["name"].split("(")[0].strip()
        name_x = PAD + 86
        while _text_w(dr, name, f_name) > (bar_x0 - name_x - 18) and len(name) > 4:
            name = name[:-2].rstrip() + "…" if not name.endswith("…") else name[:-2].rstrip() + "…"
        dr.text((name_x, y + 10), name, font=f_name, fill=WHITE)
        # barra proporcional al líder
        frac = m.get("score_global", 0) / max_score
        bx1 = bar_x0 + int((bar_x1 - bar_x0) * frac)
        dr.rounded_rectangle([bar_x0, cy - 11, bar_x1, cy + 11], radius=6, fill=(34, 34, 54))
        # relleno gradiente simple verde→cyan por pasos
        steps = max(1, (bx1 - bar_x0) // 6)
        for s in range(steps):
            t = s / max(1, steps - 1)
            r = int(GREEN[0] + (CYAN[0] - GREEN[0]) * t)
            g = int(GREEN[1] + (CYAN[1] - GREEN[1]) * t)
            b = int(GREEN[2] + (CYAN[2] - GREEN[2]) * t)
            sx0 = bar_x0 + s * 6
            dr.rounded_rectangle([sx0, cy - 11, min(sx0 + 7, bx1), cy + 11], radius=6, fill=(r, g, b))
        # score
        dr.text((bar_x1 + 16, y + 8), f"{m.get('score_global', 0):.2f}", font=f_score, fill=col)

    # --- footer ---
    f_foot = _font(22)
    foot = "Para agentes N8N · Hermes · contenido · uso personal     |     open source · MIT"
    dr.text((PAD, H - 44), foot, font=f_foot, fill=GRAY)

    img.save(OUT, "PNG")
    print(f"OK: {OUT} ({W}x{H}) — top1 {top[0]['name']} {top[0]['score_global']}, {n_tested} modelos")

if __name__ == "__main__":
    main()
