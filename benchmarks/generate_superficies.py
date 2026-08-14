#!/usr/bin/env python3
"""Genera `SUPERFICIES.md`: qué tiene que coincidir con qué, y quién lo verifica.

POR QUÉ EXISTE (14-ago-2026)
----------------------------
Cristian, después de que aparecieran TRES superficies de versión desalineadas en una
sola sesión: *"documenta las superficies que tienen que estar sincronizadas, o siempre
nos pasará lo mismo."*

Tenía razón en el diagnóstico, y el diagnóstico incluye a la solución obvia: **un
documento escrito a mano con la lista se desincroniza igual que todo lo demás.** Sería
el mismo bug un nivel más arriba — de hecho ES el bug que acabábamos de encontrar, donde
la docstring de `check_version` decía "seis superficies" y el código leía cuatro.

Por eso este doc NO se escribe: se genera. La tabla de versión sale del registro
`check_version.SUPERFICIES`, que es lo que el guardrail realmente ejecuta. Si alguien
agrega una superficie al chequeo, aparece acá sola; si la agrega acá, no aparece —
porque acá no se agrega nada.

Las otras clases de sincronía (conteos, scores, campos de la calculadora, cifras del
blog) viven en sus propios guardrails. De ésas se declara el MAPA —qué sincroniza con
qué y quién lo hace cumplir— y se verifica que **el script que lo hace cumplir exista**:
un guardrail renombrado o borrado deja de ser una fila muerta en una tabla y pasa a ser
un fallo ruidoso.

Uso:
    python benchmarks/generate_superficies.py          # escribe SUPERFICIES.md
    python benchmarks/generate_superficies.py --check  # exit 1 si está desactualizado
"""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from benchmarks.check_version import SUPERFICIES  # noqa: E402

SALIDA = ROOT / "SUPERFICIES.md"

# Las otras clases de sincronía. `guardrail` se verifica que exista en disco.
CLASES = [
    {
        "clase": "Conteos",
        "que_sincroniza": "modelos catalogados · testeados · rankeados · tests · suites, "
                          "citados en README, ROADMAP, MODELOS.md y las landings",
        "fuente": "`docs/data/models.json`",
        "guardrail": "benchmarks/sync_doc_counts.py",
        "como": "reescribe los bloques `<!-- AUTO:campo -->…<!-- /AUTO -->`. "
                "**Un conteo fuera de un bloque AUTO no se sincroniza**: si lo escribís a "
                "mano, caduca solo.",
    },
    {
        "clase": "Scores citados en prosa",
        "que_sincroniza": "toda cifra de score que aparezca en un doc VIVO "
                          "(README, MODELOS, CLAUDE, AGENTS, RECOMENDACIONES, COMPARATIVA)",
        "fuente": "`docs/data/models.json`",
        "guardrail": "benchmarks/check_consistency.py",
        "como": "compara lo citado contra el dato. Ignora a propósito los snapshots con "
                "fecha (CHANGELOG, DATASHEET_*, INSIGHTS): ésos DEBEN conservar el valor "
                "del momento — reescribir la historia sería el bug, no el fix.",
    },
    {
        "clase": "Campos que la calculadora lee",
        "que_sincroniza": "cada campo que `docs/app.js` consume, y cada umbral de filtro",
        "fuente": "`docs/data/models.json`",
        "guardrail": "benchmarks/check_calculator.py",
        "como": "caza un campo que el JS lee y el export dejó de emitir, y un umbral fuera "
                "del rango real de los datos (un filtro que no filtra a nadie es decorativo).",
    },
    {
        "clase": "Cifras del pilar del blog",
        "que_sincroniza": "el post cornerstone en el repo hermano `cristiantala-blog`",
        "fuente": "`docs/data/models.json`",
        "guardrail": "benchmarks/check_blog_consistency.py",
        "como": "un rescoring caduca TODAS las cifras del post — prosa, tablas y FAQ — y "
                "puede dejar una recomendación de seguridad peligrosa.",
    },
    {
        "clase": "Ciclo de vida de la documentación",
        "que_sincroniza": "la marca `<!-- doc: vigente | verificado: FECHA -->` de cada doc",
        "fuente": "la fecha de verificación humana",
        "guardrail": "benchmarks/check_docs.py",
        "como": "avisa cuando un doc VIGENTE lleva >90 días sin que nadie lo mire. "
                "Verifica que ALGUIEN LO MIRÓ, no que el contenido sea correcto — es "
                "honesto sobre ese techo.",
    },
    {
        "clase": "Caminos de medición",
        "que_sincroniza": "que todo lo que llame a una API de modelos esté sancionado",
        "fuente": "la lista `SANCIONADOS`",
        "guardrail": "benchmarks/check_caminos.py",
        "como": "un instrumento que se puede esquivar escribiendo un script nuevo, se "
                "esquiva. Costó cinco pozos ya tapados, re-pisados en una tarde.",
    },
]

CABECERA = """<!-- doc: generado -->
# Superficies sincronizadas — qué tiene que coincidir con qué

> **AUTO-GENERADO** por `benchmarks/generate_superficies.py`. **No editar a mano.**
> La tabla de versión sale del registro que el guardrail realmente ejecuta
> (`check_version.SUPERFICIES`), no de una copia — por eso no puede desincronizarse.

Este repo publica el mismo hecho en varios lugares a la vez. Cada lugar es una
**superficie**, y una superficie que se queda atrás no rompe nada: el sitio carga, el
pipeline pasa, los auditores dan verde. Simplemente **el repo dice dos cosas distintas
de sí mismo** y quien lea la equivocada se lleva la vieja.

Por eso cada clase de sincronía tiene un instrumento que la hace cumplir. La regla del
repo —*una regla sin instrumento que la haga cumplir es una regla que ya se rompió*—
aplica especialmente acá, porque es donde más barato es olvidarse.

---

## Cómo agregar una superficie nueva

Si vas a publicar un dato que ya existe en otro lado, no lo escribas y sigas: **es una
superficie, y necesita entrar al registro en el MISMO commit.**

1. **¿Es versión?** Agregá una fila a `SUPERFICIES` en `benchmarks/check_version.py`
   (archivo + `patron` o `json_key` + por qué importa). Este doc se regenera solo.
2. **¿Es otra cosa?** Agregala a `CLASES` en `benchmarks/generate_superficies.py` y
   nombrá el guardrail que la hace cumplir. Si todavía no existe, **ese guardrail es
   parte del trabajo**, no un pendiente.
3. Corré `python benchmarks/generate_superficies.py` y commiteá el doc.

**Lo que NO sirve:** documentar la superficie en prosa y confiar en acordarse. Es
exactamente lo que falló — la docstring de `check_version` nombraba seis superficies
mientras el código leía cuatro, y las dos que faltaban estaban desalineadas.

---
"""


def _tabla_version() -> str:
    filas = ["## Versión — las {n} superficies que declaran qué versión es ésta".format(
        n=len(SUPERFICIES)), ""]
    filas.append("Todas tienen que decir lo mismo. Lo verifica **`benchmarks/check_version.py`**, "
                 "que corre en `regenerate_all.py` y en el Action.")
    filas.append("")
    filas.append("| Superficie | Qué declara | Por qué importa |")
    filas.append("|---|---|---|")
    for s in SUPERFICIES:
        etiqueta = s.get("etiqueta") or s["archivo"]
        filas.append(f"| `{etiqueta}` | {s['que_es']} | {s['por_que']} |")
    filas += [
        "",
        "Y dos condiciones más, que no son archivos:",
        "",
        "| Requisito | Por qué |",
        "|---|---|",
        "| **git tag** para la versión declarada | Sin tag no hay punto de retorno: no se "
        "puede reconstruir qué se publicó ni comparar contra el release anterior |",
        "| **entrada en el CHANGELOG** | Publicar sin entrada es publicar sin traza |",
    ]
    return "\n".join(filas)


def _tabla_clases() -> tuple[str, list[str]]:
    faltan = []
    filas = ["## Las otras clases de sincronía", "",
             "| Clase | Qué sincroniza | Fuente única | Guardrail |",
             "|---|---|---|---|"]
    for c in CLASES:
        g = c["guardrail"]
        if not (ROOT / g).exists():
            faltan.append(g)
        filas.append(f"| **{c['clase']}** | {c['que_sincroniza']} | {c['fuente']} | `{g}` |")
    filas.append("")
    filas.append("### Detalle de cada una")
    filas.append("")
    for c in CLASES:
        filas.append(f"**{c['clase']}** — {c['como']}")
        filas.append("")
    return "\n".join(filas), faltan


def construir() -> tuple[str, list[str]]:
    clases_md, faltan = _tabla_clases()
    cuerpo = "\n\n".join([CABECERA.rstrip(), _tabla_version(), "---", clases_md.rstrip()])
    return cuerpo + "\n", faltan


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="no escribe; falla si el doc en disco está desactualizado")
    a = ap.parse_args()

    contenido, faltan = construir()

    if faltan:
        print("  ❌ SUPERFICIES.md nombra guardrails que NO EXISTEN en disco:")
        for g in faltan:
            print(f"     · {g}")
        print("     Un guardrail renombrado o borrado deja la superficie sin quien la haga")
        print("     cumplir. Arreglá la ruta en CLASES, o volvé a crear el chequeo.")
        return 1

    if a.check:
        actual = SALIDA.read_text(encoding="utf-8") if SALIDA.exists() else ""
        if actual != contenido:
            print("  ❌ SUPERFICIES.md está desactualizado respecto del registro.")
            print("     Corré: python benchmarks/generate_superficies.py")
            return 1
        print(f"  ✅ SUPERFICIES.md al día ({len(SUPERFICIES)} superficies de versión, "
              f"{len(CLASES)} clases de sincronía).")
        return 0

    SALIDA.write_text(contenido, encoding="utf-8")
    print(f"  ✅ SUPERFICIES.md — {len(SUPERFICIES)} superficies de versión, "
          f"{len(CLASES)} clases de sincronía, todos los guardrails existen.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
