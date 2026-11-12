#!/usr/bin/env python3
"""La vista de teléfono del sitio compilado, medida en el QA (11-nov-2026, change `motor-sitio`).

POR QUÉ EXISTE
--------------
La revisión a 390 px se hacía a mano con Chrome sin interfaz, y mintió dos veces: con
`--window-size=390` Chrome dibuja a ~500 px y recorta, así que mostró un desborde que no
existía. Una revisión a mano tampoco vuelve a correr cuando cambia el CSS. Cristian pidió
que quede repetible en el QA.

Esto llama a `sitio/pruebas/movil.mjs`, que emula un teléfono con Playwright (390×844,
`isMobile`, táctil, DPR 3) sobre cada página compilada que no es un redirect y exige:
  M1  que el ancho de diseño sea 390 (si la emulación no corrió, la medición no vale);
  M2  que nada desborde a lo ancho (una tabla ancha se desplaza dentro de su caja);
  M3  que en cada tabla el primer valor de cada fila se vea sin desplazar (12-nov-2026).

Mide `sitio/dist`. Si falta, o si es más viejo que las fuentes del sitio o que `models.json`,
primero compila (`npm run build`, que además corre el registro y la paridad): un verde sobre
un `dist` viejo miraría el CSS de ayer. Sin `node_modules` o sin Chrome da rojo con la
instrucción, nunca un verde por omisión.

Uso:
    python benchmarks/check_movil.py                       # compila si hace falta y mide
    python benchmarks/check_movil.py --capturas <dir>      # además guarda capturas por tramos
    python benchmarks/check_movil.py --dist <dir> --sin-compilar   # mide ese dist tal cual
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITIO = ROOT / "sitio"
SCRIPT = SITIO / "pruebas" / "movil.mjs"


def _mtime_max(base: Path, excluir: tuple[str, ...] = ()) -> float:
    m = 0.0
    for f in base.rglob("*"):
        if f.is_file() and not any(x in f.parts for x in excluir):
            m = max(m, f.stat().st_mtime)
    return m


def viejo(dist: Path) -> str | None:
    """Por qué hay que compilar antes de medir, o None si el dist está al día."""
    paginas = list(dist.rglob("index.html")) if dist.is_dir() else []
    if not paginas:
        return "no hay build"
    # La hora del build sale de lo que Astro escribe siempre de nuevo (`_astro/`): las páginas del
    # legado se copian con su fecha de `sitio/legado/` (copy2) y harían parecer viejo cualquier build.
    astro = [f for f in (dist / "_astro").rglob("*") if f.is_file()] if (dist / "_astro").is_dir() else []
    hecho = min(f.stat().st_mtime for f in (astro or paginas))
    # 12-nov-2026: `sitio/legado/` también es fuente del build (copiar_legado lo pasa a dist).
    fuentes = max(_mtime_max(SITIO / "src", excluir=("datos",)), _mtime_max(SITIO / "legado"),
                  (ROOT / "sitio" / "legado" / "data" / "models.json").stat().st_mtime)
    return "el build es más viejo que las fuentes" if fuentes > hecho else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", type=Path, default=SITIO / "dist")
    ap.add_argument("--capturas", type=Path, default=None)
    ap.add_argument("--sin-compilar", action="store_true", help="medir el dist tal cual está")
    a = ap.parse_args()

    if not shutil.which("node"):
        print("  ❌ falta Node: la vista de teléfono se mide con Playwright (sitio/pruebas/movil.mjs)")
        return 1
    if not (SITIO / "node_modules" / "playwright").is_dir():
        print("  ❌ falta Playwright: correr `npm ci` en sitio/")
        return 1

    if not a.sin_compilar:
        motivo = viejo(a.dist)
        if motivo:
            print(f"  · {motivo}: compilo con `npm run build` (también corre registro y paridad)",
                  flush=True)
            r = subprocess.run(["npm", "run", "build"], cwd=SITIO, capture_output=True, text=True)
            if r.returncode != 0:
                print("  ❌ el build falló (registro, paridad o la vista de teléfono):")
                print("\n".join("     " + x for x in (r.stdout + r.stderr).strip().splitlines()[-15:]))
                return 1
            if not a.capturas:
                # El `postbuild` ya corrió `movil.mjs` sobre este mismo dist: no se mide dos veces.
                tramo = (r.stdout or "").split("VISTA DE TELÉFONO", 1)
                print("VISTA DE TELÉFONO" + tramo[1].rstrip() if len(tramo) == 2 else
                      "  ✅ el build midió la vista de teléfono y pasó")
                return 0

    cmd = ["node", str(SCRIPT), "--dist", str(a.dist)]
    if a.capturas:
        cmd += ["--capturas", str(a.capturas)]
    r = subprocess.run(cmd, cwd=SITIO)
    if r.returncode == 2:
        print("  ❌ no se pudo medir (ver arriba): un chequeo que no midió no es un verde")
        return 1
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
