#!/usr/bin/env python3
"""Genera `MAPA.md`: dónde vive cada artefacto publicado, quién lo escribe y quién lo vigila.

POR QUÉ EXISTE (3-sep-2026)
---------------------------
Cristian, después de verme buscar las fichas de modelo en tres lugares equivocados
—`docs/modelos/*.html`, `docs/ficha-*`, `results/per-model/`— antes de dar con
`docs/modelo/<key>/index.html`: *"tenemos que tener ese mapa listo y no construirlo
cada vez"*.

Lo caro no fueron los tres intentos: fue que en el intento fallido **concluí que
faltaban 95 fichas**, cuando estaban todas. Buscar en el lugar equivocado y creerle al
resultado es el error más repetido de este repo, y acá lo cometí sobre la estructura
del propio repo.

Y el dato ya existía en el código: `check_fichas_alcanzables.py` sabe exactamente dónde
viven. Lo que faltaba no era la información — era que estuviera **en un lugar legible
sin leer el código**.

POR QUÉ SE GENERA Y NO SE ESCRIBE
---------------------------------
Mismo argumento que `SUPERFICIES.md`: un mapa a mano se desincroniza igual que todo lo
demás, y un mapa que miente es peor que ninguno, porque se le cree. Acá cada fila se
**verifica contra el disco** al generarse: si una ruta no existe, si el generador que la
declara desapareció o si el guardrail fue renombrado, esto falla ruidoso en vez de
publicar una fila muerta.

Uso:
    python benchmarks/generate_mapa.py           # escribe MAPA.md
    python benchmarks/generate_mapa.py --check   # exit 1 si está desactualizado o miente
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SALIDA = ROOT / "MAPA.md"

# ── EL REGISTRO ───────────────────────────────────────────────────────────────
# `ruta` es relativa a la raíz del repo. Si es un directorio, se cuenta lo que hay
# dentro con `patron`. `genera` y `vigila` son archivos que TIENEN que existir.
ARTEFACTOS = [
    # ── el dato ──
    {"que": "El dataset que sirve el sitio y consume todo lo demás",
     "ruta": "docs/data/models.json", "genera": "benchmarks/export_for_pages.py",
     "vigila": "benchmarks/check_consistency.py", "grupo": "Dato"},
    {"que": "La referencia congelada del score (mean/std por dimensión)",
     "ruta": "scoring_reference.json", "genera": "benchmarks/export_for_pages.py --recalibrate",
     "vigila": "benchmarks/check_version.py", "grupo": "Dato"},
    {"que": "Resultados crudos de cada lote, uno por corrida",
     "ruta": "benchmarks/results", "patron": "*.json", "genera": "benchmarks/runner.py",
     "vigila": "benchmarks/validate.py", "grupo": "Dato"},
    {"que": "La ENTRADA y la salida de cada run, auditable desde GitHub",
     "ruta": "benchmarks/results/responses", "patron": "*/*/*.md",
     "genera": "benchmarks/runner.py", "vigila": "benchmarks/check_truncamiento.py",
     "grupo": "Dato"},
    {"que": "Tareas agénticas ejecutadas (Harbor), por tarea y modelo",
     "ruta": "tareas-agente/resultados.json", "genera": "benchmarks/export_harbor.py",
     "vigila": "benchmarks/check_agentico_publicado.py", "grupo": "Dato"},

    # ── lo que ve un lector ──
    {"que": "FICHA POR MODELO — una por cada rankeado",
     "ruta": "docs/modelo", "patron": "*/index.html",
     "genera": "benchmarks/generate_model_cards.py",
     "vigila": "benchmarks/check_fichas_alcanzables.py", "grupo": "Páginas"},
    {"que": "La calculadora (home) y su lógica",
     "ruta": "docs/index.html", "genera": "benchmarks/generate_home_explore.py",
     "vigila": "benchmarks/qa_calculadora.mjs", "grupo": "Páginas"},
    {"que": "Rankings por dimensión y comparaciones (pSEO)",
     "ruta": "docs", "patron": "*/index.html",
     "genera": "benchmarks/generate_rankings.py · benchmarks/generate_comparison.py",
     "vigila": "benchmarks/auditar_paginas.py", "grupo": "Páginas"},
    {"que": "Sitemap y llms.txt",
     "ruta": "docs/sitemap.xml", "genera": "benchmarks/generate_sitemap.py",
     "vigila": "benchmarks/check_docs.py", "grupo": "Páginas"},

    # ── docs del repo ──
    {"que": "Ranking del README (bloque AUTO-RANKING)",
     "ruta": "README.md", "genera": "benchmarks/generate_readme_ranking.py",
     "vigila": "benchmarks/check_consistency.py", "grupo": "Docs"},
    {"que": "Catálogo de modelos con su estado",
     "ruta": "MODELOS.md", "genera": "benchmarks/generate_modelos_md_table.py",
     "vigila": "benchmarks/check_consistency.py", "grupo": "Docs"},
    {"que": "Recomendaciones por caso de uso",
     "ruta": "RECOMENDACIONES.md", "genera": "benchmarks/generate_recomendaciones.py",
     "vigila": "benchmarks/check_consistency.py", "grupo": "Docs"},
    {"que": "MD navegable por modelo, con enlace a sus respuestas",
     "ruta": "benchmarks/results/per-model", "patron": "*.md",
     "genera": "benchmarks/generate_per_model_md.py",
     "vigila": "benchmarks/check_docs.py", "grupo": "Docs"},
    {"que": "Qué dato tiene que coincidir con qué, y quién lo hace cumplir",
     "ruta": "SUPERFICIES.md", "genera": "benchmarks/generate_superficies.py",
     "vigila": "benchmarks/check_version.py", "grupo": "Docs"},
    # `es_salida`: se exime de la comprobación de existencia porque se verifica ANTES
    # de escribirse. Sin esto, la primera generación falla por no encontrarse a sí misma.
    {"que": "ESTE MAPA", "es_salida": True,
     "ruta": "MAPA.md", "genera": "benchmarks/generate_mapa.py",
     "vigila": "benchmarks/generate_mapa.py --check", "grupo": "Docs"},

    # ── release mensual ──
    {"que": "Cheatsheet PDF del mes (necesita DYLD_FALLBACK_LIBRARY_PATH)",
     "ruta": "cheatsheet", "patron": "*.pdf",
     "genera": "cheatsheet/generate_cheatsheet.py",
     "vigila": "benchmarks/check_release_mensual.py", "grupo": "Release"},
]


def _resolver(a: dict) -> tuple[bool, str]:
    """Verifica la fila contra el disco. Devuelve (ok, detalle)."""
    p = ROOT / a["ruta"]
    if a.get("es_salida"):
        # Detalle FIJO: si dependiera de si el archivo ya existe, la primera corrida y
        # la segunda producirían textos distintos y `--check` fallaría para siempre
        # después de generar. Un chequeo que nace en rojo se aprende a ignorar.
        return True, "se genera acá"
    if a.get("patron"):
        if not p.is_dir():
            return False, f"no existe el directorio {a['ruta']}"
        n = len(list(p.glob(a["patron"])))
        return (n > 0), (f"{n} archivos" if n else f"vacío ({a['patron']})")
    if not p.exists():
        return False, "no existe"
    return True, "1 archivo"


def _existe_script(ref: str) -> bool:
    """El primer token de `genera`/`vigila` tiene que ser un archivo real."""
    for parte in ref.split("·"):
        arch = parte.strip().split()[0]
        if not (ROOT / arch).exists():
            return False
    return True


def construir() -> tuple[str, list[str]]:
    problemas: list[str] = []
    filas_por_grupo: dict[str, list[str]] = {}
    for a in ARTEFACTOS:
        ok, detalle = _resolver(a)
        if not ok:
            problemas.append(f"{a['ruta']}: {detalle}")
        for campo in ("genera", "vigila"):
            if not _existe_script(a[campo]):
                problemas.append(f"{a['ruta']}: `{a[campo]}` ({campo}) no existe")
        ruta = f"`{a['ruta']}/{a['patron']}`" if a.get("patron") else f"`{a['ruta']}`"
        filas_por_grupo.setdefault(a["grupo"], []).append(
            f"| {a['que']} | {ruta} | {detalle} | `{a['genera']}` | `{a['vigila']}` |"
        )

    out = ["<!-- doc: generado -->",
           "<!-- GENERADO por benchmarks/generate_mapa.py — NO editar a mano -->",
           "# Mapa de artefactos — dónde vive cada cosa\n",
           "> **Este doc se GENERA y cada fila se verifica contra el disco.** Si una ruta",
           "> no existe o el script que la declara desapareció, `generate_mapa.py --check`",
           "> falla. Un mapa que miente es peor que ninguno, porque se le cree.",
           ">",
           "> **Existe porque** el 3-sep-2026 busqué las fichas de modelo en tres lugares",
           "> equivocados y, en el intento fallido, **concluí que faltaban 95 fichas cuando",
           "> estaban las 100**. El dato ya vivía en el código (`check_fichas_alcanzables.py`",
           "> sabe la ruta); lo que faltaba era poder leerlo sin leer el código.\n",
           "**Regla de uso:** antes de buscar dónde está algo, mirá acá. Antes de crear un",
           "artefacto nuevo, agregá su fila **en el mismo commit** — si no, no existe para",
           "el próximo que lo busque.\n"]
    for g in ("Dato", "Páginas", "Docs", "Release"):
        if g not in filas_por_grupo:
            continue
        out += [f"\n## {g}\n",
                "| Qué es | Dónde vive | Hoy | Quién lo escribe | Quién lo vigila |",
                "|---|---|---|---|---|"]
        out += filas_por_grupo[g]
    out += ["\n---\n",
            "*Generado por `benchmarks/generate_mapa.py`. El pipeline maestro",
            "(`regenerate_all.py`) lo regenera y `--check` falla si quedó desactualizado.*"]
    return "\n".join(out) + "\n", problemas


def main() -> int:
    texto, problemas = construir()
    if problemas:
        print("  ❌ el mapa no cuadra con el disco:\n")
        for p in problemas:
            print(f"     · {p}")
        print("\n  Una fila que apunta a algo que no existe es exactamente lo que este")
        print("  doc existe para evitar. Corregí el registro en generate_mapa.py.")
        return 1
    if "--check" in sys.argv:
        actual = SALIDA.read_text() if SALIDA.exists() else ""
        if actual != texto:
            print("  ❌ MAPA.md está desactualizado. Correr: python benchmarks/generate_mapa.py")
            return 1
        print(f"  ✅ MAPA.md al día · {len(ARTEFACTOS)} artefactos, todos verificados en disco")
        return 0
    SALIDA.write_text(texto)
    print(f"  ✅ MAPA.md · {len(ARTEFACTOS)} artefactos, todos verificados contra el disco")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
