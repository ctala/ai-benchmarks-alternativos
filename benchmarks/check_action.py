#!/usr/bin/env python3
"""¿El Action compila el sitio nuevo, con Node fijado y en el orden que funciona? (11-nov-2026, motor-sitio 2.5)

POR QUÉ EXISTE
--------------
El Action es el seguro del repo y ya estuvo 40 días en rojo por una dependencia que no
instalaba (`openai`, después `dirhash` y `pytest`). Con el sitio en Astro le suman Node, sus
paquetes y Chrome, y cada uno puede faltar de la misma forma. El orden también importa:
`test_guardrails` prueba `check_movil`, que necesita `node_modules`, y el `package.json` del
sitio llama a `../.venv/bin/python`, que en el runner no existe si nadie lo crea.

`check_ci` mira si el Action está en rojo, pero depende de la red y es informativo: un paso
que falta se vería recién cuando el Action ya falló en `main`. Esto lee el YAML del repo,
sin red, y es bloqueante.

  A1  Node se instala con `actions/setup-node` y su versión sale de `sitio/.nvmrc`, que
      cumple el `engines` del `package.json`.
  A2  el venv `.venv` se crea antes del build y queda en el PATH: el `package.json` corre
      `../.venv/bin/python`.
  A3  `npm ci` en `sitio/` corre antes del build y antes de `test_guardrails`.
  A4  `npm run build` en `sitio/` corre después de regenerar `models.json`.
  A5  `check_datos_dist.py --dist sitio/dist` corre después del build.
  A6  `publicar_dist.py` copia dist a docs/ después del build (12-nov-2026, motor-sitio 2.6).
  A7  el paso que commitea verifica `publicar_dist.py --check` antes de su `git add`, y
      ningún otro paso hace `git add`: en docs/ solo se commitea lo que salió del build.

Uso:
    python benchmarks/check_action.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
YAML = ROOT / ".github" / "workflows" / "regenerate-auto-artifacts.yml"
SITIO = ROOT / "sitio"


def _texto(paso: dict) -> str:
    return " ".join(str(paso.get(k, "")) for k in ("uses", "run", "working-directory", "with"))


def _en_sitio(paso: dict) -> bool:
    return paso.get("working-directory") == "sitio" or "cd sitio" in str(paso.get("run", ""))


def revisar(flujo: dict, nvmrc: str | None, engines: str) -> list[str]:
    """Fallos A1-A5 de un workflow ya parseado. Función pura."""
    pasos = [p for j in (flujo.get("jobs") or {}).values() for p in (j.get("steps") or [])]

    def primero(cond) -> int | None:
        return next((i for i, p in enumerate(pasos) if cond(p)), None)

    fallos = []
    node = primero(lambda p: str(p.get("uses", "")).startswith("actions/setup-node"))
    if node is None:
        fallos.append("A1 · no hay paso con actions/setup-node")
    elif (pasos[node].get("with") or {}).get("node-version-file") != "sitio/.nvmrc":
        fallos.append("A1 · setup-node no toma la versión de sitio/.nvmrc (una sola autoridad)")
    m = re.search(r">=\s*(\d+)\s*<\s*(\d+)", engines)
    if not nvmrc:
        fallos.append("A1 · falta sitio/.nvmrc")
    elif not m or not (int(m.group(1)) <= int(nvmrc.split(".")[0]) < int(m.group(2))):
        fallos.append(f"A1 · sitio/.nvmrc dice {nvmrc} y el package.json pide {engines}")

    venv = primero(lambda p: "venv .venv" in str(p.get("run", "")) and "GITHUB_PATH" in str(p.get("run", "")))
    ci = primero(lambda p: _en_sitio(p) and re.search(r"\bnpm ci\b", str(p.get("run", ""))))
    build = primero(lambda p: _en_sitio(p) and "npm run build" in str(p.get("run", "")))
    export = primero(lambda p: "export_for_pages.py" in str(p.get("run", "")))
    guard = primero(lambda p: "test_guardrails.py" in str(p.get("run", "")))
    datos = primero(lambda p: re.search(r"check_datos_dist\.py\s+--dist\s+sitio/dist", str(p.get("run", ""))))

    if venv is None:
        fallos.append("A2 · no se crea el venv .venv ni se pone en el PATH")
    elif build is not None and venv > build:
        fallos.append("A2 · el venv .venv se crea después del build")
    if ci is None:
        fallos.append("A3 · no hay `npm ci` en sitio/")
    else:
        if build is not None and ci > build:
            fallos.append("A3 · `npm ci` corre después del build")
        if guard is not None and ci > guard:
            fallos.append("A3 · `npm ci` corre después de test_guardrails (check_movil lo necesita)")
    if build is None:
        fallos.append("A4 · no hay `npm run build` en sitio/")
    elif export is not None and build < export:
        fallos.append("A4 · el build corre antes de regenerar models.json")
    if datos is None:
        fallos.append("A5 · no se verifica el sha de models.json en sitio/dist")
    elif build is not None and datos < build:
        fallos.append("A5 · el sha se verifica antes del build")

    copia = primero(lambda p: re.search(r"publicar_dist\.py\s*$", str(p.get("run", "")).strip().splitlines()[-1] if p.get("run") else ""))
    if copia is None:
        fallos.append("A6 · ningún paso copia dist a docs/ (python benchmarks/publicar_dist.py)")
    elif build is not None and copia < build:
        fallos.append("A6 · la copia a docs/ corre antes del build")
    con_add = [i for i, p in enumerate(pasos) if re.search(r"\bgit add\b", str(p.get("run", "")))]
    if len(con_add) != 1:
        fallos.append(f"A7 · {len(con_add)} pasos hacen `git add`: tiene que ser uno, el del commit")
    else:
        run = str(pasos[con_add[0]].get("run", ""))
        chk = run.find("publicar_dist.py --check")
        if chk < 0 or chk > run.find("git add"):
            fallos.append("A7 · el commit no verifica `publicar_dist.py --check` antes de su `git add`")
        if copia is not None and con_add[0] < copia:
            fallos.append("A7 · el commit corre antes de la copia a docs/")
    return fallos


def main() -> int:
    flujo = yaml.safe_load(YAML.read_text(encoding="utf-8"))
    nv = SITIO / ".nvmrc"
    nvmrc = nv.read_text(encoding="utf-8").strip() if nv.exists() else None
    engines = json.loads((SITIO / "package.json").read_text(encoding="utf-8")).get("engines", {}).get("node", "")
    fallos = revisar(flujo, nvmrc, engines)
    print(f"EL ACTION Y EL SITIO — {YAML.relative_to(ROOT)}")
    if fallos:
        for x in fallos:
            print(f"  ❌ {x}")
        print(f"\n  ❌ {len(fallos)} problema(s): el Action no compilaría el sitio, o lo haría con lo que no es.")
        return 1
    print(f"  ✅ Node {nvmrc} desde sitio/.nvmrc, venv, npm ci, build, sha de models.json y copia a docs/, "
          "en ese orden; el commit verifica la copia antes de su git add")
    return 0


if __name__ == "__main__":
    sys.exit(main())
