#!/usr/bin/env python3
"""¿Alguna página corona a un ganador que su propia tabla no sostiene?

POR QUÉ EXISTE (19-ago-2026)
----------------------------
Cristian, sobre `/mejor-llm-para-agentes/`: *"no entiendo, ¿por qué gana DeepSeek si no
tiene el mejor puesto? Esto es lo que te decía, tiene que quedar claro para cualquiera"*.
La página decía «DeepSeek V3.2 encabeza la tabla» y la tabla lo ponía **#73 con 7,4**.

Se arregló, y entonces preguntó lo único que importaba: **«¿lo mismo no nos pasa en
otras páginas?»**. Sí pasaba, en otra forma. La auditoría encontró que las páginas de
variantes coronaban por columna:

    Gana 4.20      con  [8,80 · 9,20 · 9,20 · 9,20]   ← tres idénticos, corona a uno
    Gana Luna Pro  con  [9,00 · 9,20 · 8,40 · 9,20]
    Gana Terra     con  [9,63 · 9,33 · 10,00 · 10,00]

La causa era distinta de la del veredicto, pero el efecto para el lector es el mismo:
**la tabla muestra números iguales y el texto nombra a uno**.

LA REGLA QUE UNIFICA LAS DOS
----------------------------
No se corona a nadie por una diferencia que no publicamos. Si las celdas salen con dos
decimales, dos valores a menos de 0,005 se ven iguales y no se pueden separar; si el
ranking se lee por posición, el que el texto nombre primero tiene que ser el #1.

Este chequeo cubre las dos formas:
  G1  el veredicto de una página de ranking recomienda a alguien del grupo de cabeza
  G2  ninguna fila con «Gana X» tiene un empate visible en la cima

EL GRUPO DE CABEZA (6-nov-2026, DECISIONES)
-------------------------------------------
El top 20 del índice v5 cabe en 0,19 puntos: coronar al #1 es publicar ruido. Las
páginas de ranking publican el GRUPO que el benchmark no separa del mejor
(`data-grupo-cabeza`, calculado con `bands.py`) y, dentro del grupo, el precio manda.
  G3  cada página de ranking publica su grupo, y es el que sale de models.json HOY
      (`generate_rankings.cabeza` sobre los rankeados); con más de uno en el grupo, el
      texto no corona a nadie («lidera», «encabeza la tabla», «la opción a vencer»)
  G4  cada modelo que nombra un veredicto está RANKEADO. Dos landings coronaban a
      Claude Fable 5, del histórico, como «la mejor calidad medida» de v5
  G5  en las comparaciones «X vs Y», el ganador de cada pilar, los empates y el cuadro
      «Resumen: quién gana» nombran solo a rankeados. El 7-nov-2026 /claude-vs-chatgpt/
      coronaba en sus cuatro pilares a modelos del histórico, medidos con otro examen
  G6  en una comparación con versión en el título («Fable 5 vs Opus 4.8»), todo modelo de
      la tabla o coronado está nombrado en el título, y una foto histórica no corona a
      nadie. El 8-nov-2026 las páginas de Fable 5 coronaban a Fable 5.1, porque el
      generador elegía por familia («fable») y no por key

Uso:
    python benchmarks/check_ganadores.py
"""

import argparse
import glob
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
sys.path.insert(0, str(ROOT / "benchmarks"))
sys.path.insert(0, str(ROOT))

GRUPO = re.compile(r'data-grupo-cabeza="([^"]*)"')
# Lo que corona a uno solo. Con un grupo de más de uno, ninguna de estas puede aparecer.
CORONAS = ("lidera", "encabeza la tabla", "la opción a vencer", "#1:")

# La resolución con la que se publican los números de tabla. Es el piso del empate:
# por debajo de esto, dos modelos se ven iguales y declarar un ganador es inventarlo.
TOL = 0.005

FILA_1 = re.compile(r"<tr><td>1</td><td>(?:<a[^>]*>)?(?:<strong>)?([^<]+)")
CARD = re.compile(r'<span class="verdict-tag">([^<]*)</span>\s*<strong>([^<]*)</strong>', re.S)
FILA = re.compile(r"<tr[^>]*>(.*?)</tr>", re.S)
CELDA = re.compile(r"<t[dh][^>]*>(.*?)</t[dh]>", re.S)
_limpio = lambda x: re.sub(r"<[^>]+>", "", x).strip()


_GANA = re.compile(r"gana <strong>([^<]+)</strong>")
_EMPATE = re.compile(r"Empate técnico en calidad: <strong>([^<]+)</strong> y <strong>([^<]+)</strong>")
_RESUMEN = re.compile(r"Resumen: quién gana según tu caso</h2>.*?</table>", re.S)


def g5_coronados(h: str, permitidos: set, catalogo: set) -> tuple[list, int]:
    """(nombres coronados que no están permitidos, cuántos coronados se leyeron) en una
    página de comparación. Función pura. `permitidos` son los rankeados más los modelos de
    un lado SIN ningún rankeado (ahí la página corona al mejor medido y lo dice con
    `_nota_campeon`). Un nombre que no está en el catálogo no se juzga."""
    import html as _html
    nombres = [n for n in _GANA.findall(h)]
    for a, b in _EMPATE.findall(h):
        nombres += [a, b]
    res = _RESUMEN.search(h)
    if res:
        for celda in re.findall(r"<td><strong>([^<]+)</strong>", res.group(0)):
            celda = re.sub(r"\s*\((?:por calidad|\$[^)]*|\d+ tok/s)\)\s*$", "", celda.strip())
            celda = celda.removeprefix("Empate — ")
            # el empate pone «A o B»: se parte solo si ambos lados son modelos del catálogo
            partes = celda.split(" o ")
            if len(partes) == 2 and all(_html.unescape(x.strip()) in catalogo for x in partes):
                nombres += partes
            else:
                nombres.append(celda)
    nombres = [_html.unescape(n.strip()) for n in nombres]
    malos = sorted({n for n in nombres if n in catalogo and n not in permitidos})
    return malos, len(nombres)



_TITLE = re.compile(r"<title>([^<]*)</title>")
_TABLA_PRINCIPAL = re.compile(r'<section class="results">.*?<tbody>(.*?)</tbody>', re.S)
_FILA_MODELO = re.compile(r"<tr><td>\d+</td><td>(.*?)</td>", re.S)


def g6_fuera_del_titulo(h: str, catalogo: set) -> tuple[list, int]:
    """(problemas, nombres leídos) de UNA comparación. Función pura.

    Lee el título que publica la página, no la config: si el generador vuelve a elegir por
    familia, lo que se caza es la página que lo muestra."""
    import html as _html
    sys.path.insert(0, str(ROOT / "benchmarks"))
    from generate_comparison import (etiquetas_titulo, nombrado_en_titulo,
                                     titulo_con_version, MARCA_FOTO)
    t = _TITLE.search(h)
    if not t:
        return ["la página no tiene <title>: G6 no puede leer qué compara"], 0
    titulo = _html.unescape(t.group(1))
    if not titulo_con_version(titulo):
        return [], 0                       # página de familia: compara familias a propósito
    etiquetas = etiquetas_titulo(titulo)
    nombres = []
    tabla = _TABLA_PRINCIPAL.search(h)
    if tabla:
        for celda in _FILA_MODELO.findall(tabla.group(1)):
            celda = re.sub(r'<span class="row-badge[^"]*"[^>]*>.*?</span>', "", celda)
            nombres.append(_html.unescape(re.sub(r"<[^>]+>", "", celda)).strip())
    coronados_fuera, n_cor = g5_coronados(h, set(), catalogo)  # todos los coronados del catálogo
    problemas = [f"compara a «{n}», que no está en el título «{titulo}»"
                 for n in dict.fromkeys(nombres) if not nombrado_en_titulo(n, etiquetas)]
    problemas += [f"corona a «{n}», que no está en el título «{titulo}»"
                  for n in coronados_fuera if not nombrado_en_titulo(n, etiquetas)]
    if MARCA_FOTO in h and n_cor:
        problemas.append(f"es una foto histórica y corona a {n_cor} nombre(s): una foto no elige ganador")
    return problemas, len(nombres)


def main() -> int:
    argparse.ArgumentParser().parse_args()
    fallos = []
    g1 = g2 = 0

    import json as _json
    import html as _html
    from generate_rankings import RANKINGS, rank_models, cabeza
    modelos = _json.loads((DOCS / "data" / "models.json").read_text())["models"]
    por_nombre = {m["name"]: m for m in modelos}
    rankeados = {m["name"] for m in modelos if m.get("ranked")}
    if not rankeados:
        print("❌ G0 models.json no trae rankeados: el chequeo está ciego")
        return 1
    g3 = g4 = 0

    # ── G3 · el grupo publicado es el de hoy, y con grupo no se corona a nadie ──
    grupos = {}
    for cfg in RANKINGS:
        f = DOCS / cfg["slug"] / "index.html"
        if not f.exists():
            continue
        h = f.read_text(errors="ignore")
        g = GRUPO.search(h)
        if not g:
            fallos.append(f"{cfg['slug']}: no publica su grupo de cabeza (`data-grupo-cabeza`)")
            continue
        g3 += 1
        publicado = [k for k in _html.unescape(g.group(1)).split(",") if k]
        esperado = [m["key"] for m in cabeza(cfg, rank_models(modelos, cfg))]
        grupos[cfg["slug"]] = set(publicado)
        if set(publicado) != set(esperado):
            fallos.append(f"{cfg['slug']}: publica un grupo de cabeza de {len(publicado)} y "
                          f"models.json da {len(esperado)} — la página quedó vieja o se escribió a mano")
        if len(publicado) > 1:
            texto = re.sub(r"<script.*?</script>", "", h, flags=re.S)
            texto = re.sub(r"<table.*?</table>", "", texto, flags=re.S)
            texto = texto + " ".join(re.findall(r'<meta name="description" content="([^"]*)"', h))
            for c in CORONAS:
                if c in texto:
                    fallos.append(f"{cfg['slug']}: el benchmark no separa a {len(publicado)} de la "
                                  f"cima y el texto dice «{c}»")

    # ── G1 + G4 · el veredicto recomienda a alguien del grupo, y solo rankeados ──
    for cfg in RANKINGS:
        f = DOCS / cfg["slug"] / "index.html"
        if not f.exists() or cfg["slug"] not in grupos:
            continue
        h = f.read_text(errors="ignore")
        for lab, nom in CARD.findall(h):
            nom = _html.unescape(_limpio(nom))
            g4 += 1
            if nom not in rankeados:
                fallos.append(f"{cfg['slug']}: el veredicto nombra a «{nom}», que no está rankeado")
                continue
            if any(x in lab.lower() for x in ("mejor", "grupo", "calidad")):
                g1 += 1
                if por_nombre[nom]["key"] not in grupos[cfg["slug"]]:
                    fallos.append(f"{cfg['slug']}: el veredicto recomienda a «{nom}» y no está "
                                  f"en el grupo de cabeza que publica la página")

    # ── G2 · «Gana X» sobre un empate visible ────────────────────────────────
    for f in sorted(DOCS.glob("*/index.html")):
        h = f.read_text(errors="ignore")
        if "Gana " not in h:
            continue
        for fila in FILA.findall(h):
            celdas = [_limpio(c) for c in CELDA.findall(fila)]
            gana = [c for c in celdas if c.startswith("Gana ")]
            nums = [float(c) for c in celdas if re.fullmatch(r"\d+\.\d+", c)]
            if not gana or len(nums) < 2:
                continue
            g2 += 1
            mx = max(nums)
            if sum(1 for v in nums if v >= mx - TOL) > 1:
                fallos.append(
                    f"{f.parent.name}: «{gana[0]}» sobre {[f'{v:.2f}' for v in nums]} — "
                    f"hay más de uno en el máximo y la tabla los muestra iguales")

    # ── G5 · las comparaciones coronan solo a rankeados ──────────────────────
    from generate_comparison import COMPARISONS, family
    catalogo = {m["name"] for m in modelos}
    g5 = 0
    for cfg in COMPARISONS:
        f = DOCS / cfg["slug"] / "index.html"
        if not f.exists():
            continue
        permitidos = set(rankeados)
        for lado in ("a", "b"):
            fam = family(modelos, cfg[lado])
            if not any(m.get("ranked") for m in fam):
                permitidos |= {m["name"] for m in fam}
        malos, n = g5_coronados(f.read_text(errors="ignore"), permitidos, catalogo)
        g5 += n
        for nom in malos:
            fallos.append(f"{cfg['slug']}: corona a «{nom}», que no está rankeado")
    if g5 == 0:
        fallos.append("G5 no leyó ningún coronado en las comparaciones: el chequeo está ciego")

    # ── G6 · la comparación muestra a los modelos de SU título ───────────────
    g6 = g6_paginas = 0
    for cfg in COMPARISONS:
        f = DOCS / cfg["slug"] / "index.html"
        if not f.exists():
            continue
        problemas, n = g6_fuera_del_titulo(f.read_text(errors="ignore"), catalogo)
        if n:
            g6_paginas += 1
        g6 += n
        fallos += [f"{cfg['slug']}: {x}" for x in problemas]
    if g6 == 0:
        fallos.append("G6 no leyó ningún modelo en las comparaciones con versión: el chequeo está ciego")

    print("GANADORES — ¿la página sostiene a quien corona?\n")
    print(f"  G1 · recomendaciones de veredicto contra su grupo: {g1}")
    print(f"  G2 · filas con «Gana X»: {g2}")
    print(f"  G3 · páginas de ranking con su grupo de cabeza: {g3}")
    print(f"  G4 · modelos nombrados en veredictos: {g4}")
    print(f"  G5 · coronados en comparaciones: {g5}")
    print(f"  G6 · modelos de comparaciones con versión, contra su título: {g6} en {g6_paginas} página(s)")
    if g3 == 0:
        fallos.append("G3 no leyó ninguna página de ranking: el chequeo está ciego")
    if not fallos:
        print(f"\n  ✅ los {g1 + g2} coinciden con lo que muestra su propia tabla.")
        return 0
    print(f"\n  ❌ {len(fallos)} contradicción(es):\n")
    for x in fallos:
        print(f"     {x}")
    print(f"\n     No se corona a nadie por una diferencia menor a {TOL} — que es la")
    print("     resolución con la que publicamos el número.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
