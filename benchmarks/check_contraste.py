#!/usr/bin/env python3
"""Contraste WCAG 2 AA de lo compilado, con axe, en cada tipo de página (12-nov-2026, motor-sitio 2.6).

POR QUÉ EXISTE
--------------
Ningún guardrail medía contraste. Al pasar el sitio a claro (2.2) el magenta de alerta quedó
como color de texto sobre fondo claro: 3,1 a 3,5:1, bajo el 4,5:1 de AA, en la etiqueta
«thinking» de la calculadora, los valores de riesgo y el aviso de prompt injection de las fichas.
Nada falló porque nada lo medía. Cristian pidió un chequeo bloqueante sobre lo compilado, con al
menos una página de cada tipo.

Elige del registro las dos primeras URLs de cada tipo de página destino (home, ficha, comparación,
ranking, landing, variantes, proveedores) y la ficha de un modelo retirado, que lleva su aviso, y
corre `sitio/pruebas/contraste.mjs` (axe, a 390 y a 1280 px):
  K0  axe corre y caza un gris claro sobre blanco en una página de control;
  K1  ningún texto bajo el contraste AA.
Falla también si alguno de esos tipos no aporta páginas: un verde sobre un tipo que no se midió
no vale.

Mide `sitio/dist`. Si está más viejo que sus fuentes, primero compila (`npm run build`, cuyo
postbuild ya corre este mismo chequeo).

Uso:
    python benchmarks/check_contraste.py
    python benchmarks/check_contraste.py --dist <dir> --sin-compilar
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITIO = ROOT / "sitio"
SCRIPT = SITIO / "pruebas" / "contraste.mjs"
sys.path.insert(0, str(Path(__file__).resolve().parent))

TIPOS = ("home", "ficha", "comparacion", "ranking", "landing", "variantes", "proveedores")


def elegir(regs: list[dict], retirados: set[str], por_tipo: int = 2) -> tuple[list[str], list[str]]:
    """(URLs a medir, tipos sin páginas). Función pura."""
    d = defaultdict(list)
    for e in regs:
        if not e["redirect_a"]:
            d[e["tipo"]].append(e["url"])
    urls = [u for t in TIPOS for u in sorted(d.get(t, []))[:por_tipo]]
    ret = next((u for u in sorted(d.get("ficha", [])) if u.strip("/").split("/")[-1] in retirados), None)
    if ret and ret not in urls:
        urls.append(ret)
    return urls, [t for t in TIPOS if not d.get(t)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", type=Path, default=SITIO / "dist")
    ap.add_argument("--sin-compilar", action="store_true", help="medir el dist tal cual está")
    a = ap.parse_args()
    import registro_paginas as rp
    import check_movil

    if not shutil.which("node") or not (SITIO / "node_modules" / "axe-core").is_dir():
        print("  ❌ falta Node o axe-core: correr `npm ci` en sitio/")
        return 1
    if not a.sin_compilar:
        motivo = check_movil.viejo(a.dist)
        if motivo:
            print(f"  · {motivo}: compilo con `npm run build` (su postbuild mide el contraste)", flush=True)
            r = subprocess.run(["npm", "run", "build"], cwd=SITIO, capture_output=True, text=True)
            if r.returncode != 0:
                print("  ❌ el build falló:")
                print("\n".join("     " + x for x in (r.stdout + r.stderr).strip().splitlines()[-15:]))
                return 1
            tramo = (r.stdout or "").split("CONTRASTE WCAG", 1)
            print("CONTRASTE WCAG" + tramo[1].rstrip() if len(tramo) == 2 else "  ✅ el build midió el contraste y pasó")
            return 0

    datos = json.loads((SITIO / "legado" / "data" / "models.json").read_text(encoding="utf-8"))
    retirados = {m["key"] for m in datos["models"] if m.get("retired")}
    urls, vacios = elegir(rp.paginas(), retirados)
    if vacios:
        print(f"  ❌ el registro no tiene páginas de {', '.join(vacios)}: ese tipo no se mediría")
        return 1
    cmd = ["node", str(SCRIPT), "--dist", str(a.dist)] + [x for u in urls for x in ("--url", u)]
    r = subprocess.run(cmd, cwd=SITIO)
    if r.returncode == 2:
        print("  ❌ no se pudo medir (ver arriba): un chequeo que no midió no es un verde")
        return 1
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
