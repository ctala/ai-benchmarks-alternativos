#!/usr/bin/env python3
"""La parte de la prueba de `check_gitleaks` que planta secretos en el árbol, con su candado.

POR QUÉ EXISTE (corte-v5 5.2.c, 8-nov-2026)
--------------------------------------------
El 4-nov la prueba de `check_gitleaks` en `test_guardrails` falló una vez dentro de `qa.py`
y pasó sola. `qa.py` corre `cobertura.py` en paralelo, y `cobertura.py` vuelve a correr
`test_guardrails`: dos copias de la prueba a la vez. Las dos plantan un secreto en el árbol
y `check_gitleaks` escanea el árbol ENTERO, así que el control verde de una ve lo que plantó
la otra. Nombres únicos por proceso no alcanzan, porque el escaneo no mira nombres.

El arreglo es un candado de archivo (`flock`) que serializa la prueba entre procesos de la
máquina. Vive en este módulo y no en `test_guardrails.py` porque ese archivo corre todas sus
pruebas al importarse: la prueba de la carrera necesita lanzar dos copias de ESTO solo.

Uso:
    python benchmarks/prueba_arbol_gitleaks.py                      # con el candado
    python benchmarks/prueba_arbol_gitleaks.py --sin-candado        # para reproducir la carrera
    python benchmarks/prueba_arbol_gitleaks.py --candado <ruta>     # otro archivo de candado
Sale con 0 si el control dio verde y los dos secretos plantados dieron rojo.
"""

import argparse
import contextlib
import secrets
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = sys.executable
CANDADO_ARBOL = Path(tempfile.gettempdir()) / "benchmark_guardrails_arbol.lock"


@contextlib.contextmanager
def candado_arbol(ruta: Path | None = None):
    """Exclusivo entre procesos: quien lo toma planta y borra antes de que otro escanee."""
    import fcntl  # noqa: PLC0415
    with open(ruta or CANDADO_ARBOL, "w") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)


def _gitleaks() -> int:
    """Exit code de `check_gitleaks`. Un 2 (argparse) es un fallo de la prueba, no un rojo."""
    r = subprocess.run([PY, str(ROOT / "benchmarks" / "check_gitleaks.py")],
                       capture_output=True, text=True, cwd=ROOT)
    if r.returncode == 2:
        raise RuntimeError("check_gitleaks salió con 2: la prueba no corrió el detector")
    return r.returncode


def plantar_y_verificar() -> bool:
    """Control verde, y rojo con cada uno de los dos secretos plantados. Sin candado."""
    if _gitleaks() != 0:
        return False  # control verde
    plantado = ROOT / "_prueba_gitleaks.md"
    try:
        plantado.write_text(f"config\n\nR2_SECRET_ACCESS_KEY={secrets.token_hex(32)}\n")
        if _gitleaks() == 0:
            return False
    finally:
        plantado.unlink(missing_ok=True)
    # Un JSON generado NUEVO con keys de modelos no está en las exclusiones: tiene que verse.
    copia = ROOT / "docs" / "data" / "_prueba_gitleaks_models.json"
    try:
        shutil.copy2(ROOT / "docs" / "data" / "models.json", copia)
        if _gitleaks() == 0:
            return False
    finally:
        copia.unlink(missing_ok=True)
    return True


def probar(con_candado: bool = True, ruta: Path | None = None) -> bool:
    if not con_candado:
        return plantar_y_verificar()
    with candado_arbol(ruta):
        return plantar_y_verificar()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sin-candado", action="store_true")
    ap.add_argument("--candado", type=Path, default=None)
    a = ap.parse_args()
    return 0 if probar(not a.sin_candado, a.candado) else 1


if __name__ == "__main__":
    sys.exit(main())
