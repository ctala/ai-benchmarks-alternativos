#!/usr/bin/env python3
"""Instala el hook `pre-push` que corre el QA antes de que nada llegue a GitHub.

POR QUÉ EXISTE (16-ago-2026)
----------------------------
Cristian: *"antes de mergear deberíamos correrlos"*.

`pre-push` y no `pre-commit`: commitear a mitad de un arreglo es normal y frenar ahí
molesta sin proteger nada — lo que no puede pasar es que llegue a `main`. Y no
`pre-merge`, porque git no tiene ese hook: el push es el último punto donde todavía es
nuestro.

Corre `qa.py --pre-merge`, que son solo los chequeos bloqueantes (~5 s). La deuda conocida
—variantes PRO citadas en prosa, cobertura bajo el piso— reporta pero no frena: un QA que
frena por deuda es un QA que se saltea con `--no-verify`, y entonces no existe.

Uso:
    python benchmarks/instalar_hooks.py          # instala
    python benchmarks/instalar_hooks.py --check  # ¿está instalado y al día?
"""

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HOOK = """#!/bin/sh
# Generado por benchmarks/instalar_hooks.py — no editar a mano.
#
# Corre el QA bloqueante antes de empujar. Si falla, lo que se estaba por publicar no
# rompe ninguna página: la hace mentir, que es peor y no se nota.
#
# Para saltearlo a propósito (y solo a propósito):  git push --no-verify
exec "$(git rev-parse --show-toplevel)/.venv/bin/python" \\
     "$(git rev-parse --show-toplevel)/benchmarks/qa.py" --pre-merge
"""


def _ruta_hook() -> Path:
    d = subprocess.run(["git", "rev-parse", "--git-path", "hooks"],
                       cwd=ROOT, capture_output=True, text=True).stdout.strip()
    return (ROOT / d).resolve() / "pre-push"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="solo verificar")
    a = ap.parse_args()

    h = _ruta_hook()
    al_dia = h.exists() and h.read_text() == HOOK

    if a.check:
        if al_dia:
            print(f"  ✅ hook pre-push instalado y al día ({h})")
            return 0
        print(f"  ❌ el hook pre-push {'está desactualizado' if h.exists() else 'no está instalado'}.")
        print("     Corré: python benchmarks/instalar_hooks.py")
        return 1

    h.parent.mkdir(parents=True, exist_ok=True)
    h.write_text(HOOK)
    h.chmod(0o755)
    print(f"  ✅ hook pre-push instalado en {h}")
    print("     Antes de cada push corre `qa.py --pre-merge` (~5 s).")
    print("     Para saltearlo a propósito: git push --no-verify")
    return 0


if __name__ == "__main__":
    sys.exit(main())
