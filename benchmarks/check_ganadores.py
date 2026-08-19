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
  G1  el veredicto de una página de ranking corona al #1 de su tabla
  G2  ninguna fila con «Gana X» tiene un empate visible en la cima

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

# La resolución con la que se publican los números de tabla. Es el piso del empate:
# por debajo de esto, dos modelos se ven iguales y declarar un ganador es inventarlo.
TOL = 0.005

FILA_1 = re.compile(r"<tr><td>1</td><td>(?:<a[^>]*>)?(?:<strong>)?([^<]+)")
CARD = re.compile(r'<span class="verdict-tag">([^<]*)</span>\s*<strong>([^<]*)</strong>', re.S)
FILA = re.compile(r"<tr[^>]*>(.*?)</tr>", re.S)
CELDA = re.compile(r"<t[dh][^>]*>(.*?)</t[dh]>", re.S)
_limpio = lambda x: re.sub(r"<[^>]+>", "", x).strip()


def main() -> int:
    argparse.ArgumentParser().parse_args()
    fallos = []
    g1 = g2 = 0

    # ── G1 · el veredicto corona al #1 de su tabla ───────────────────────────
    for f in sorted(DOCS.glob("*/index.html")):
        h = f.read_text(errors="ignore")
        if "verdict-tag" not in h:
            continue
        m1 = FILA_1.search(h)
        if not m1:
            continue
        lider = None
        for lab, nom in CARD.findall(h):
            if "calidad" in lab.lower() or "el mejor" in lab.lower():
                lider = _limpio(nom)
        if not lider:
            continue          # veredictos que no coronan (p. ej. «no logra separar»)
        g1 += 1
        primero = m1.group(1).strip()
        if primero not in lider and lider not in primero:
            fallos.append(f"{f.parent.name}: el veredicto corona a «{lider}» y el #1 de "
                          f"la tabla es «{primero}» — dos criterios en una página")

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

    print("GANADORES — ¿la página sostiene a quien corona?\n")
    print(f"  G1 · veredictos que nombran un líder: {g1}")
    print(f"  G2 · filas con «Gana X»: {g2}")
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
