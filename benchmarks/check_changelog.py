#!/usr/bin/env python3
"""¿Cada cambio dejó su rastro, y el bump alcanza para lo que se tocó?

POR QUÉ EXISTE (17-ago-2026)
----------------------------
Cristian: *"define una estructura de changelog y versionado para que cada commit y push
lleve el suyo y estandariza"*.

Lo pidió después de una sesión con **once commits en los que el CHANGELOG se escribió al
final, de memoria**. Salió bien porque la sesión no se cortó. Ese mismo día un
`git reset --hard` se llevó diez ediciones sin commitear, así que el riesgo de perder el
relato no era teórico — y el relato es la parte que nadie puede reconstruir después: el
QUÉ se ve en el diff, el PORQUÉ no.

`check_version.py` ya verificaba que las 7 superficies declaren lo mismo. Lo que nadie
miraba es lo de antes: **si lo que se hizo llegó a estar escrito**, y si el número que se
bumpeó alcanza para lo que se tocó.

QUÉ VERIFICA
------------
  C1  Si hay commits desde el último tag que tocaron código o datos, la sección
      `## [No publicado]` del CHANGELOG no puede estar vacía.
  C2  El bump declarado alcanza para lo que se tocó, según el mapa de VERSIONADO.md §2.
      Tocar `scoring_reference.json` y publicar un PATCH es exactamente cómo se reescribe
      en silencio el significado de una cifra ya citada.

LO QUE NO PUEDE VERIFICAR, Y CONVIENE SABERLO
---------------------------------------------
Que la entrada sea **buena**. Puede decir «varios arreglos» y pasa. Contra eso no hay
instrumento: hay estándar (VERSIONADO.md §4) y hay revisar. Lo que sí garantiza es que
nadie publique una versión sin que exista el rastro — que es donde estaba el agujero.

Uso:
    python benchmarks/check_changelog.py            # C1
    python benchmarks/check_changelog.py --nivel    # C1 + C2
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHANGELOG = ROOT / "CHANGELOG.md"

# VERSIONADO.md §2 — qué tocaste, qué nivel te toca como mínimo. El orden importa:
# gana la primera regla que matchea, y están de más fuerte a más débil.
NIVEL_POR_PATH = [
    ("major", ("scoring_reference.json",)),
    ("minor", ("benchmarks/tests/", "benchmarks/suites.py", "providers/adapters.py",
               "benchmarks/scoring.py", "benchmarks/export_for_pages.py",
               "benchmarks/elegibilidad.py")),
]
ORDEN = {"patch": 0, "minor": 1, "major": 2}
# Lo que no exige entrada de CHANGELOG.
#
# Dos clases distintas, y conviene no mezclarlas:
#   · ruido de entorno (.DS_Store, .coverage): nunca fue un cambio.
#   · ARTEFACTOS AUTO-GENERADOS: son *consecuencia* de un cambio, no el cambio. Pedir una
#     entrada por regenerar `models.json` obligaría a escribir una línea cada vez que el
#     bot del CI hace su trabajo — y una regla que se dispara sola es una que se aprende a
#     ignorar. Lo que sí exige entrada es lo que los produce.
#
# `benchmarks/results/` NO está acá a propósito: medir modelos nuevos es un cambio real
# (PATCH) y merece su línea. Es data, no un derivado.
IRRELEVANTES = (
    ".gitignore", ".DS_Store", ".coverage", "scratchpad/",
    "docs/data/models.json", "docs/sitemap.xml", "docs/llms.txt", "docs/modelo/",
    "docs/og-benchmark.png", "MODELOS.md", "TESTS.md", "PROMPTS.md",
    "benchmarks/results/per-model/", "SUPERFICIES.md",
)


def _sh(*args) -> str:
    return subprocess.run(args, capture_output=True, text=True, cwd=ROOT).stdout.strip()


def ultimo_tag() -> str | None:
    t = _sh("git", "describe", "--tags", "--abbrev=0")
    return t or None


def cambios_desde(tag: str) -> list[str]:
    """Lo commiteado desde el tag MÁS lo que está sin commitear.

    Las dos mitades hacen falta y por razones distintas. En el pre-push solo importa lo
    primero (ya está todo commiteado). Pero `qa.py` se corre mientras se trabaja, y ahí
    lo que interesa es justamente lo que todavía no se guardó — que es lo que se pierde
    si la sesión se corta o alguien resetea, como pasó el 17-ago-2026.
    """
    paths = set()
    if tag:
        paths.update(_sh("git", "diff", "--name-only", f"{tag}..HEAD").splitlines())
    # `--porcelain` trae modificados, staged y sin trackear, con el estado en 2 columnas.
    for linea in _sh("git", "status", "--porcelain").splitlines():
        if len(linea) > 3:
            paths.add(linea[3:].strip().strip('"'))
    return sorted(p for p in paths if p and not p.startswith(IRRELEVANTES))


def nivel_minimo(paths: list[str]) -> str:
    peor = "patch"
    for nivel, prefijos in NIVEL_POR_PATH:
        if any(p.startswith(prefijos) for p in paths):
            if ORDEN[nivel] > ORDEN[peor]:
                peor = nivel
    return peor


def seccion_no_publicado(texto: str) -> str | None:
    """El cuerpo de `## [No publicado]`, o None si la sección no existe."""
    m = re.search(r"^##\s*\[No publicado\]\s*$(.*?)(?=^##\s*\[)", texto, re.S | re.M)
    return m.group(1).strip() if m else None


def salto_de_version(tag: str) -> str | None:
    """De v4.5.0 a v4.6.0 → 'minor'. None si no hay bump o no se puede leer."""
    ult = re.search(r"^##\s*\[(v[\d.]+)\]", CHANGELOG.read_text(), re.M)
    if not ult or not tag:
        return None
    def nums(v):
        return [int(x) for x in v.lstrip("v").split(".")]
    try:
        a, b = nums(tag), nums(ult.group(1))
    except ValueError:
        return None
    if b[0] > a[0]:
        return "major"
    if len(b) > 1 and len(a) > 1 and b[1] > a[1]:
        return "minor"
    return "patch"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--nivel", action="store_true",
                    help="además, verificar que el bump alcance para lo que se tocó")
    a = ap.parse_args()

    texto = CHANGELOG.read_text()
    tag = ultimo_tag()
    paths = cambios_desde(tag)
    cuerpo = seccion_no_publicado(texto)
    problemas = []

    print(f"CHANGELOG — último tag: {tag or '(ninguno)'} · "
          f"{len(paths)} archivo(s) tocados desde entonces\n")

    # C1 · lo que se hizo tiene que estar escrito
    if paths and not cuerpo:
        if cuerpo is None:
            problemas.append(
                "no existe la sección `## [No publicado]` en el CHANGELOG. "
                "Es donde cada commit deja su línea (VERSIONADO.md §3).")
        else:
            ejemplos = ", ".join(paths[:4]) + ("…" if len(paths) > 4 else "")
            problemas.append(
                f"hay {len(paths)} archivo(s) cambiados desde {tag} y `## [No publicado]` "
                f"está vacía ({ejemplos}). El QUÉ se ve en el diff; el PORQUÉ, si no se "
                f"escribe ahora, no lo reconstruye nadie.")
    elif not paths:
        print("  ✅ sin cambios desde el último tag: nada que anotar.")
    else:
        n = len([l for l in cuerpo.splitlines() if l.strip().startswith(("-", "*"))])
        print(f"  ✅ `## [No publicado]` tiene {n or 'algunas'} entrada(s) para "
              f"{len(paths)} archivo(s) tocados.")

    # C2 · el bump alcanza para lo que se tocó
    if a.nivel and paths:
        exige = nivel_minimo(paths)
        hizo = salto_de_version(tag)
        print(f"\n  nivel exigido por lo tocado: {exige.upper()}"
              f" · salto declarado: {(hizo or '—').upper()}")
        if hizo and ORDEN[hizo] < ORDEN[exige]:
            culpables = [p for _, pref in NIVEL_POR_PATH for p in paths
                         if p.startswith(pref)][:3]
            problemas.append(
                f"se declaró un {hizo.upper()} y lo tocado exige al menos {exige.upper()} "
                f"({', '.join(culpables)}). Publicar un cambio de medición como si fuera "
                f"un arreglo es cómo se reescribe en silencio lo que significa una cifra "
                f"que alguien ya citó.")

    if problemas:
        print()
        for p in problemas:
            print(f"  ❌ {p}")
        print("\n  Ver VERSIONADO.md — el estándar y por qué existe.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
