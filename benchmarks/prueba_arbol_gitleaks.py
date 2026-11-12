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

LA PRUEBA DE LA CARRERA ES DETERMINISTA (11-nov-2026)
-----------------------------------------------------
Hasta el 11-nov la segunda copia arrancaba tras un `sleep` calculado con el tiempo de un
escaneo × 1,3. Bajo la carga del QA completo un escaneo tardaba más que la medición previa y
la segunda copia llegaba tarde: la carrera no se reproducía y la prueba fallaba al azar (el
pre-push la tumbó una vez y pasó al reintento). Un guardrail que falla al azar enseña a
ignorarlo. Ahora las copias se coordinan con archivos de señal en `--sync <dir>`, sin tiempos:

  - `--rol primero`: planta el secreto, escribe `plantado` y NO lo borra hasta que exista
    `escaneado` (la segunda ya corrió su control) o `bloqueado` (la segunda intentó el
    candado sin esperar y lo encontró tomado).
  - `--rol segundo`: espera `plantado`; intenta el candado sin bloquear y, si está tomado,
    escribe `bloqueado` y espera su turno; corre el control y escribe `escaneado`.

Sin candado, el control de la segunda ve SIEMPRE el secreto de la primera (rojo). Con
candado, la segunda no escanea hasta que la primera borró (verde). Si el candado no
excluyera, la segunda escanearía con el secreto plantado y la prueba daría rojo: la
exigencia es la misma, solo que ya no depende del reloj.

Uso:
    python benchmarks/prueba_arbol_gitleaks.py                      # con el candado
    python benchmarks/prueba_arbol_gitleaks.py --sin-candado        # para reproducir la carrera
    python benchmarks/prueba_arbol_gitleaks.py --candado <ruta>     # otro archivo de candado
    ... --rol primero|segundo --sync <dir>                          # la carrera coordinada
Sale con 0 si el control dio verde y los dos secretos plantados dieron rojo.
"""

import argparse
import contextlib
import secrets
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = sys.executable
CANDADO_ARBOL = Path(tempfile.gettempdir()) / "benchmark_guardrails_arbol.lock"


ESPERA_MAX_S = 300  # red de seguridad contra un cuelgue; la coordinación no depende de esto


@contextlib.contextmanager
def candado_arbol(ruta: Path | None = None, al_esperar=None):
    """Exclusivo entre procesos: quien lo toma planta y borra antes de que otro escanee.
    `al_esperar` se llama si el candado ya estaba tomado, antes de quedarse esperando."""
    import fcntl  # noqa: PLC0415
    with open(ruta or CANDADO_ARBOL, "w") as f:
        try:
            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            if al_esperar:
                al_esperar()
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


def esperar(*senales: Path) -> None:
    """Espera a que exista alguna de las señales. Espera un EVENTO, no un tiempo."""
    tope = time.monotonic() + ESPERA_MAX_S
    while not any(s.exists() for s in senales):
        if time.monotonic() > tope:
            raise RuntimeError(f"nadie escribió {[s.name for s in senales]} en {ESPERA_MAX_S} s")
        time.sleep(0.02)


def plantar_y_verificar(tras_control=None, tras_plantar=None) -> bool:
    """Control verde, y rojo con cada uno de los dos secretos plantados. Sin candado.
    Los ganchos coordinan la carrera: `tras_control` corre después del control (pase o no),
    `tras_plantar` con el primer secreto ya en el árbol y antes de escanearlo."""
    control = _gitleaks()
    if tras_control:
        tras_control()
    if control != 0:
        return False  # control verde
    plantado = ROOT / "_prueba_gitleaks.md"
    try:
        plantado.write_text(f"config\n\nR2_SECRET_ACCESS_KEY={secrets.token_hex(32)}\n")
        if tras_plantar:
            tras_plantar()
        if _gitleaks() == 0:
            return False
    finally:
        plantado.unlink(missing_ok=True)
    # Un JSON generado NUEVO con keys de modelos no está en las exclusiones: tiene que verse.
    copia = ROOT / "sitio" / "legado" / "data" / "_prueba_gitleaks_models.json"
    try:
        shutil.copy2(ROOT / "sitio" / "legado" / "data" / "models.json", copia)
        if _gitleaks() == 0:
            return False
    finally:
        copia.unlink(missing_ok=True)
    return True


def probar(con_candado: bool = True, ruta: Path | None = None,
           rol: str | None = None, sync: Path | None = None) -> bool:
    ganchos, al_esperar = {}, None
    if rol == "primero":
        def _plantado():
            (sync / "plantado").touch()
            esperar(sync / "escaneado", sync / "bloqueado")
        ganchos["tras_plantar"] = _plantado
    elif rol == "segundo":
        esperar(sync / "plantado")
        ganchos["tras_control"] = lambda: (sync / "escaneado").touch()
        al_esperar = lambda: (sync / "bloqueado").touch()  # noqa: E731
    if not con_candado:
        return plantar_y_verificar(**ganchos)
    with candado_arbol(ruta, al_esperar=al_esperar):
        return plantar_y_verificar(**ganchos)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sin-candado", action="store_true")
    ap.add_argument("--candado", type=Path, default=None)
    ap.add_argument("--rol", choices=("primero", "segundo"), default=None)
    ap.add_argument("--sync", type=Path, default=None, help="carpeta de las señales de la carrera")
    a = ap.parse_args()
    if bool(a.rol) != bool(a.sync):
        ap.error("--rol y --sync van juntos")
    return 0 if probar(not a.sin_candado, a.candado, a.rol, a.sync) else 1


if __name__ == "__main__":
    sys.exit(main())
