#!/usr/bin/env python3
"""Un change de OpenSpec se COMPLETA y se ARCHIVA. Ninguno queda en el aire.

POR QUÉ EXISTE (3-nov-2026)
---------------------------
Cristian, al aceptar OpenSpec dentro del benchmark para el corte v5.0.0: *"lo que sí, un
guardrail para completar y archivar los specs para que no nos queden en el aire"*.

Tenía un antecedente a la vista: el único change de OpenSpec que se escribió sobre este
benchmark (`banco-desarrollo-modelos-abiertos`, en el repo padre) se archivó a los seis días
con **8 de 43 tareas** hechas. Nada avisó. Un plan que nadie cierra no ordena: deja la mitad
del trabajo sin dueño y la otra mitad sin registro de por qué se dejó.

Y la fila del 16-sep-2026 de `DECISIONES.md` tenía razón en lo suyo: una herramienta de
specs es una **segunda fuente de verdad** si se la deja. Acá se la acepta con una condición
verificable: el plan vive en `openspec/`, el porqué sigue viviendo en `DECISIONES.md`, y el
change tiene que decirlo.

QUÉ EXIGE
---------
  S1  En `main` no hay ningún change activo: lo que llega a `main` llega archivado. Se juzga
      en tres lugares: la rama actual, el árbol de cada commit que el pre-push manda a
      `main` (`--empuje`, 11-nov-2026) y el Action sobre `main` (`--rama main`).
  S2  Como mucho UN change activo a la vez, en cualquier rama (Regla 4 del repo padre).
  S3  Todo change activo tiene `proposal.md`, `design.md`, `tasks.md` con al menos una
      tarea, y `.openspec.yaml`.
  S4  Un change activo que nadie toca en 14 días está en el aire. Se mira el último commit
      que lo tocó; si no tiene commits, la fecha `created` de su `.openspec.yaml`.
  S5  Ningún change ARCHIVADO tiene tareas sin marcar. Una tarea que se decidió no hacer se
      marca hecha con «descartada: <motivo>»; lo que no está es que quede abierta.
  S6  El change nombra a `DECISIONES.md` en `proposal.md` o `design.md`: el porqué vive allá.

Si no existe `openspec/` el chequeo pasa: el guardrail vigila los changes que hay, no obliga
a tener uno.

Uso:
    python benchmarks/check_specs.py                     # exit 1 si algo queda en el aire
    python benchmarks/check_specs.py --raiz <dir> --rama main --hoy 2026-12-01   # para probarlo
"""

import argparse
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIAS_EN_EL_AIRE = 14
ARTEFACTOS = ("proposal.md", "design.md", "tasks.md", ".openspec.yaml")
TAREA = re.compile(r"^\s*- \[( |x|X)\]", re.M)
ABIERTA = re.compile(r"^\s*- \[ \]", re.M)


def rama_actual() -> str:
    r = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"],
                       capture_output=True, text=True, cwd=ROOT)
    return r.stdout.strip()


def ultimo_toque(change: Path, raiz: Path) -> date | None:
    """Fecha del último commit que tocó el change; si no hay, la fecha `created`."""
    try:
        r = subprocess.run(["git", "log", "-1", "--format=%cs", "--", str(change)],
                           capture_output=True, text=True, cwd=raiz.parent)
        if r.returncode == 0 and r.stdout.strip():
            return date.fromisoformat(r.stdout.strip())
    except (OSError, ValueError):
        pass
    yaml = change / ".openspec.yaml"
    if yaml.exists():
        m = re.search(r"^created:\s*(\d{4}-\d{2}-\d{2})", yaml.read_text(encoding="utf-8"), re.M)
        if m:
            return date.fromisoformat(m.group(1))
    return None


CERO = "0" * 40


def refs_a_main(texto: str) -> list[str]:
    """Los commits que un `git push` manda a `main`, leídos de lo que git le pasa al hook
    pre-push por stdin (`<ref local> <sha local> <ref remota> <sha remoto>` por línea). Un
    borrado (sha local en ceros) no manda nada."""
    shas = []
    for ln in texto.splitlines():
        partes = ln.split()
        if len(partes) == 4 and partes[2] == "refs/heads/main" and partes[1] != CERO:
            shas.append(partes[1])
    return shas


def activos_en_commit(sha: str, repo: Path) -> list[str] | None:
    """Los changes activos en el ÁRBOL de un commit (no en el working tree). None si el commit
    no tiene `openspec/changes/`."""
    r = subprocess.run(["git", "ls-tree", "-d", "--name-only", f"{sha}:openspec/changes"],
                       cwd=repo, capture_output=True, text=True)
    if r.returncode != 0:
        return None
    return sorted(n for n in r.stdout.split() if n != "archive")


def revisar_empuje(texto: str, repo: Path) -> list[str]:
    """S1 sobre lo que se empuja a main (11-nov-2026). Hasta acá S1 miraba el nombre de la rama
    local: el release v6.1.0 se empujó desde `ventana/v6-1` con `HEAD:main` y llevó a main un
    change activo (`corte-v5-1`, 1 de 34 tareas) sin que nada fallara."""
    fallas = []
    for sha in refs_a_main(texto):
        activos = activos_en_commit(sha, repo) or []
        if activos:
            fallas.append(f"S1 · el push lleva a `main` el commit {sha[:9]} con {len(activos)} "
                          f"change(s) activo(s) sin archivar: " + ", ".join(activos))
    return fallas


def revisar(raiz: Path, rama: str, hoy: date) -> list[str]:
    """Función pura sobre un directorio `openspec/`: devuelve los hallazgos."""
    changes = raiz / "changes"
    if not changes.is_dir():
        return []
    activos = sorted(p for p in changes.iterdir() if p.is_dir() and p.name != "archive")
    archivados = sorted(p for p in (changes / "archive").glob("*") if p.is_dir())
    fallas = []

    if rama == "main" and activos:
        fallas.append(f"S1 · en `main` hay {len(activos)} change(s) activo(s) sin archivar: "
                      + ", ".join(c.name for c in activos))
    if len(activos) > 1:
        fallas.append(f"S2 · {len(activos)} changes activos a la vez (máximo 1): "
                      + ", ".join(c.name for c in activos))
    for c in activos:
        faltan = [a for a in ARTEFACTOS if not (c / a).exists()]
        if faltan:
            fallas.append(f"S3 · {c.name} sin {', '.join(faltan)}")
        tasks = c / "tasks.md"
        if tasks.exists() and not TAREA.search(tasks.read_text(encoding="utf-8")):
            fallas.append(f"S3 · {c.name}/tasks.md no tiene ninguna tarea")
        toque = ultimo_toque(c, raiz)
        if toque is None:
            fallas.append(f"S4 · {c.name} no tiene commits ni fecha `created`: no se sabe "
                          f"desde cuándo está abierto")
        elif (hoy - toque).days > DIAS_EN_EL_AIRE:
            fallas.append(f"S4 · {c.name} lleva {(hoy - toque).days} días sin que nadie lo "
                          f"toque (tope {DIAS_EN_EL_AIRE}): se cierra, se archiva o se "
                          f"descarta, pero no se deja en el aire")
        texto = "".join((c / a).read_text(encoding="utf-8") for a in ("proposal.md", "design.md")
                        if (c / a).exists())
        if "DECISIONES.md" not in texto:
            fallas.append(f"S6 · {c.name} no nombra a DECISIONES.md: el porqué de cada "
                          f"decisión vive allá, el change solo apunta")
    for c in archivados:
        tasks = c / "tasks.md"
        if tasks.exists():
            abiertas = len(ABIERTA.findall(tasks.read_text(encoding="utf-8")))
            if abiertas:
                fallas.append(f"S5 · archivado {c.name} con {abiertas} tarea(s) sin marcar: "
                              f"se termina o se marca «descartada: <motivo>», no se archiva "
                              f"abierto")
    return fallas


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--raiz", type=Path, default=ROOT / "openspec",
                    help="otro directorio openspec/ (para probar el chequeo)")
    ap.add_argument("--rama", help="simular otra rama (para el sabotaje de test_guardrails)")
    ap.add_argument("--hoy", type=date.fromisoformat, default=date.today(),
                    help="simular otra fecha (para el sabotaje de test_guardrails)")
    ap.add_argument("--empuje", action="store_true",
                    help="modo hook pre-push: lee de stdin las refs empujadas y aplica S1 al "
                         "árbol de cada commit que va a main")
    ap.add_argument("--repo", type=Path, default=ROOT,
                    help="otro repositorio git (para el sabotaje de test_guardrails)")
    a = ap.parse_args()

    if a.empuje:
        fallas = revisar_empuje(sys.stdin.read(), a.repo)
        if fallas:
            print("\n  ❌ OpenSpec · el push no puede llegar a main así:\n")
            for f in fallas:
                print(f"  · {f}")
            print("\n  Lo que llega a main llega archivado: se completa, se archiva o se descarta.")
            return 1
        print("  ✅ OpenSpec · nada activo llega a main con este push.")
        return 0

    if not a.raiz.is_dir():
        print("  ✅ no hay openspec/: nada que vigilar.")
        return 0
    rama = a.rama or rama_actual()
    fallas = revisar(a.raiz, rama, a.hoy)
    changes = a.raiz / "changes"
    activos = [p.name for p in changes.iterdir() if p.is_dir() and p.name != "archive"] \
        if changes.is_dir() else []
    print(f"\nRevisando changes de OpenSpec en {a.raiz} (rama {rama}, hoy {a.hoy})…\n")
    if not fallas:
        print(f"  ✅ ningún change en el aire ({len(activos)} activo(s): "
              f"{', '.join(activos) or 'ninguno'}).")
        return 0
    print(f"  ❌ {len(fallas)} hallazgo(s):\n")
    for f in fallas:
        print(f"  · {f}")
    print("\n  Un plan que nadie cierra no ordena: se completa, se archiva o se descarta con motivo.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
