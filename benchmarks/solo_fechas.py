#!/usr/bin/env python3
"""¿Lo único que cambió es la fecha de la corrida? (corte-v5 2.7)

POR QUÉ EXISTE
--------------
El Action que regenera los artefactos corre todos los días por cron. Al 3-nov-2026, 12 de
los 13 commits del bot desde agosto solo cambiaban fechas: `generated_at` en `models.json`
y la «última regeneración» de los MD. Eso son ~365 commits de ruido al año, y además la
fecha que muestra la calculadora pasaba a ser la de la última corrida, no la del último
cambio de datos: decía «actualizado hoy» sobre datos de hace semanas.

Regla (DECISIONES, 4-nov-2026): si el diff de los artefactos, ignorando las líneas de fecha
de corrida, está vacío, no se commitea nada. La fecha publicada es la del último cambio
real de datos.

QUÉ CUENTA COMO «LÍNEA DE FECHA»
--------------------------------
Una línea cuenta como fecha de corrida solo si las dos condiciones se cumplen:
  1. lleva uno de los MARCADORES de fecha de corrida (`generated_at`, `dateModified`,
     `<lastmod>`, «actualizado», «Última actualización», «Última regeneración»), y
  2. quitando las fechas, la línea quitada y la agregada son idénticas.
Una fecha que es DATO (`retired_at`, una fecha de lanzamiento) no lleva marcador y cuenta
como cambio real: corregirla tiene que llegar al commit.

Un archivo binario o sin versionar cuenta siempre como cambio real.

Uso (desde la raíz del repo):
    python benchmarks/solo_fechas.py --cached              # lo que está en el índice (Action)
    python benchmarks/solo_fechas.py docs README.md        # el árbol, acotado a esas rutas
    python benchmarks/solo_fechas.py --restaurar docs …    # y si son solo fechas, las descarta

Sale con 0 si no hay nada real que commitear (sin diff, o solo fechas) y con 1 si hay un
cambio real. Con `--cached --restaurar` saca los archivos del índice y del árbol.
"""
import argparse
import re
import subprocess
import sys


MARCADORES = re.compile(
    r'"generated_at"|"dateModified"|<lastmod>|[Aa]ctualizado|[ÚU]ltima actualizaci[óo]n'
    r'|[ÚU]ltima regeneraci[óo]n'
)
FECHA = re.compile(
    r"\d{4}-\d{2}-\d{2}(?:[T ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:?\d{2})?)?"
    r"|\d{1,2} de [a-záéíóú]+ de \d{4}"
)


def _git(*args: str) -> str:
    # Sobre el repo del directorio actual, que se corre desde la raíz (el Action y el QA lo
    # hacen): así la prueba de sabotaje lo ejercita en un repo desechable sin tocar el real.
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def es_linea_de_fecha(quitada: str, agregada: str) -> bool:
    return (bool(MARCADORES.search(quitada)) and bool(MARCADORES.search(agregada))
            and FECHA.sub("<F>", quitada) == FECHA.sub("<F>", agregada))


def cambios_reales(diff: str) -> dict[str, list[str]]:
    """Por archivo, las líneas que NO son fecha de corrida. Un diff vacío da {}.

    Empareja dentro de cada hunk la i-ésima línea quitada con la i-ésima agregada: un cambio
    de fecha reescribe la línea en su lugar, así que un hunk de solo fechas tiene el mismo
    número de líneas de cada lado y se empareja exacto."""
    reales: dict[str, list[str]] = {}
    archivo = None
    menos: list[str] = []
    mas: list[str] = []

    def cerrar_hunk():
        if archivo is None:
            return
        malas = [f"-{q}" for q in menos[len(mas):]] + [f"+{a}" for a in mas[len(menos):]]
        for q, a in zip(menos, mas):
            if not es_linea_de_fecha(q, a):
                malas += [f"-{q}", f"+{a}"]
        if malas:
            reales.setdefault(archivo, []).extend(malas)
        menos.clear()
        mas.clear()

    for linea in diff.splitlines():
        if linea.startswith("diff --git "):
            cerrar_hunk()
            archivo = linea.split(" b/", 1)[-1]
        elif linea.startswith("Binary files ") or linea.startswith("GIT binary patch"):
            reales.setdefault(archivo, []).append("(binario)")
        elif linea.startswith("@@"):
            cerrar_hunk()
        elif linea.startswith(("---", "+++")):
            continue
        elif linea.startswith("-"):
            menos.append(linea[1:])
        elif linea.startswith("+"):
            mas.append(linea[1:])
    cerrar_hunk()
    return reales


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("rutas", nargs="*", help="Acotar a estas rutas (por defecto, todo)")
    ap.add_argument("--cached", action="store_true", help="Mirar el índice, no el árbol")
    ap.add_argument("--restaurar", action="store_true",
                    help="Si solo cambiaron fechas, descartar esos cambios")
    a = ap.parse_args()

    base = ["diff", "--no-color", "--no-ext-diff", "-U0"] + (["--cached"] if a.cached else [])
    diff = _git(*base, "--", *a.rutas)
    tocados = [l for l in _git(*base, "--name-only", "--", *a.rutas).splitlines() if l]
    reales = cambios_reales(diff)
    if not a.cached:
        for nuevo in _git("ls-files", "--others", "--exclude-standard", "--", *a.rutas).splitlines():
            reales.setdefault(nuevo, []).append("(sin versionar)")

    if reales:
        print(f"  Cambio real en {len(reales)} archivo(s):")
        for f, lineas in sorted(reales.items())[:20]:
            print(f"    {f}: {lineas[0][:110]}")
        return 1
    if not tocados:
        print("  Sin cambios.")
        return 0
    print(f"  Solo fechas de corrida en {len(tocados)} archivo(s): no hay nada que commitear.")
    if a.restaurar:
        _git("restore", *(["--staged", "--worktree"] if a.cached else []), "--", *tocados)
        print("  Descartados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
