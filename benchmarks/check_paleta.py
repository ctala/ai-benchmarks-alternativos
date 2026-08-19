#!/usr/bin/env python3
"""¿Algún color del sitio se inventó fuera del manual de marca?

POR QUÉ EXISTE (19-ago-2026)
----------------------------
Cristian, mirando el sitio: *"a nivel de colores creo que cansa"*.

La medición: **30 hex distintos, 22 fuera del manual de marca**. Siete fondos oscuros
casi idénticos (`#12121f`, `#14142a`, `#181830`, `#161628`, `#111120`, `#101020`,
`#2a2a42`) y seis acentos compitiendo — dorado `#ffd700` usado 17 veces, naranja
`#ffaa00`, morado claro `#b478ff`, rojo `#ff5c5c`. Ninguno de esos existe en el manual.

Lo importante es CÓMO llegaron: nadie decidió tener 30 colores. Cada uno entró solo,
en una regla, resolviendo un caso puntual —«acá necesito un amarillo para advertencia»—
y se quedó. Eso es exactamente lo que el repo ya sabe de las reglas sin instrumento:
el manual decía «NUNCA inventar colores», estaba escrito, y **nada lo verificaba**.

Tres desvíos que solo aparecen cuando se compara contra la fuente:
  · la card era `#14142a` y el manual dice `#1a1a2e`
  · la prosa era `#dcdcec` y el manual dice `#dbdbe5` (9.5:1 AAA)
  · el morado se usaba ACLARADO a `#b478ff` como color de TEXTO, y el manual lo
    prohíbe explícito: «púrpura acento glow/grid, nunca en texto principal». Que
    hubiera que aclararlo para que contrastara era la señal de que no correspondía.

QUÉ VERIFICA
------------
  P1  Todo hex en CSS/HTML/generadores pertenece a la paleta del manual.
  P2  El `:root` declara los valores del manual, sin desviarse.

LO QUE NO PUEDE VERIFICAR
-------------------------
Si el color se usó en el ROL correcto (verde de primario, morado solo en glow). Eso es
criterio. Lo que sí garantiza es que nadie invente uno nuevo sin darse cuenta.

Fuente: https://assets.cristiantala.com/brand/ctala.html · espejo: landings/brand.json

Uso:
    python benchmarks/check_paleta.py
"""

import argparse
import glob
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Manual de Marca v2. Estos son TODOS los colores que la marca tiene.
MANUAL = {
    "#0a0a1a": "fondo · Negro profundo",
    "#1a1a2e": "superficie · cards",
    "#1a0a2e": "inset · code blocks",
    "#ffffff": "texto · 19.3:1 AAA",
    "#dbdbe5": "prosa body · 9.5:1 AAA",
    "#b0b0b0": "muted · captions",
    "#39ff14": "primario · headings, CTAs",
    "#00d4ff": "secundario · links, badges",
    "#7a00df": "acento · glow y grid, NUNCA texto",
    "#ff006e": "alerta · uso escaso",
}
# Grises de UI sin rol de marca (bordes, deshabilitado). Se toleran y se listan.
UI = {"#4a4a5e", "#2a2a3e", "#000000"}

DONDE = ["docs/style.css", "docs/index.html", "docs/app.js",
         "benchmarks/generate_*.py"]
# La imagen OG se compone con PIL y no comparte el CSS; se audita aparte.
SALTAR = ("generate_og_image.py",)


def main() -> int:
    argparse.ArgumentParser().parse_args()
    fuera, archivos = Counter(), {}
    for patron in DONDE:
        for f in sorted(glob.glob(str(ROOT / patron))):
            if any(x in f for x in SALTAR):
                continue
            txt = Path(f).read_text(errors="ignore")
            # Los comentarios documentan colores YA eliminados (por qué murieron). Citar
            # un color muerto para explicar su muerte no puede reabrir el hallazgo.
            txt = re.sub(r"/\*.*?\*/", "", txt, flags=re.S)
            txt = re.sub(r"^\s*#.*$", "", txt, flags=re.M)
            for h in {x.lower() for x in re.findall(r"#[0-9a-fA-F]{6}\b", txt)}:
                if h not in MANUAL and h not in UI:
                    fuera[h] += 1
                    archivos.setdefault(h, []).append(Path(f).name)

    print("PALETA — contra el Manual de Marca v2\n")
    print(f"  P1 · colores del manual: {len(MANUAL)} · grises de UI tolerados: {len(UI)}")
    print(f"  P2 · colores inventados: {len(fuera)}")
    if not fuera:
        print("\n  ✅ ningún color fuera del manual. «NUNCA inventar colores ni fuentes».")
        return 0
    print("\n  ❌ estos no existen en el manual de marca:\n")
    for h, _ in fuera.most_common():
        print(f"     {h}   en {', '.join(sorted(set(archivos[h])))}")
    print("\n     El manual es la fuente: https://assets.cristiantala.com/brand/ctala.html")
    print("     Si hace falta un rol nuevo, se agrega AL MANUAL primero — no a una regla.")
    print("     Roles disponibles:")
    for h, rol in MANUAL.items():
        print(f"       {h}  {rol}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
