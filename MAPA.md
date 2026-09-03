<!-- doc: generado -->
<!-- GENERADO por benchmarks/generate_mapa.py — NO editar a mano -->
# Mapa de artefactos — dónde vive cada cosa

> **Este doc se GENERA y cada fila se verifica contra el disco.** Si una ruta
> no existe o el script que la declara desapareció, `generate_mapa.py --check`
> falla. Un mapa que miente es peor que ninguno, porque se le cree.
>
> **Existe porque** el 3-sep-2026 busqué las fichas de modelo en tres lugares
> equivocados y, en el intento fallido, **concluí que faltaban 95 fichas cuando
> estaban las 100**. El dato ya vivía en el código (`check_fichas_alcanzables.py`
> sabe la ruta); lo que faltaba era poder leerlo sin leer el código.

**Regla de uso:** antes de buscar dónde está algo, mirá acá. Antes de crear un
artefacto nuevo, agregá su fila **en el mismo commit** — si no, no existe para
el próximo que lo busque.


## Dato

| Qué es | Dónde vive | Hoy | Quién lo escribe | Quién lo vigila |
|---|---|---|---|---|
| El dataset que sirve el sitio y consume todo lo demás | `docs/data/models.json` | 1 archivo | `benchmarks/export_for_pages.py` | `benchmarks/check_consistency.py` |
| La referencia congelada del score (mean/std por dimensión) | `scoring_reference.json` | 1 archivo | `benchmarks/export_for_pages.py --recalibrate` | `benchmarks/check_version.py` |
| Resultados crudos de cada lote, uno por corrida | `benchmarks/results/*.json` | 647 archivos | `benchmarks/runner.py` | `benchmarks/validate.py` |
| La ENTRADA y la salida de cada run, auditable desde GitHub | `benchmarks/results/responses/*/*/*.md` | 36837 archivos | `benchmarks/runner.py` | `benchmarks/check_truncamiento.py` |
| Tareas agénticas ejecutadas (Harbor), por tarea y modelo | `tareas-agente/resultados.json` | 1 archivo | `benchmarks/export_harbor.py` | `benchmarks/check_agentico_publicado.py` |

## Páginas

| Qué es | Dónde vive | Hoy | Quién lo escribe | Quién lo vigila |
|---|---|---|---|---|
| FICHA POR MODELO — una por cada rankeado | `docs/modelo/*/index.html` | 101 archivos | `benchmarks/generate_model_cards.py` | `benchmarks/check_fichas_alcanzables.py` |
| La calculadora (home) y su lógica | `docs/index.html` | 1 archivo | `benchmarks/generate_home_explore.py` | `benchmarks/qa_calculadora.mjs` |
| Rankings por dimensión y comparaciones (pSEO) | `docs/*/index.html` | 71 archivos | `benchmarks/generate_rankings.py · benchmarks/generate_comparison.py` | `benchmarks/auditar_paginas.py` |
| Sitemap y llms.txt | `docs/sitemap.xml` | 1 archivo | `benchmarks/generate_sitemap.py` | `benchmarks/check_docs.py` |

## Docs

| Qué es | Dónde vive | Hoy | Quién lo escribe | Quién lo vigila |
|---|---|---|---|---|
| Ranking del README (bloque AUTO-RANKING) | `README.md` | 1 archivo | `benchmarks/generate_readme_ranking.py` | `benchmarks/check_consistency.py` |
| Catálogo de modelos con su estado | `MODELOS.md` | 1 archivo | `benchmarks/generate_modelos_md_table.py` | `benchmarks/check_consistency.py` |
| Recomendaciones por caso de uso | `RECOMENDACIONES.md` | 1 archivo | `benchmarks/generate_recomendaciones.py` | `benchmarks/check_consistency.py` |
| MD navegable por modelo, con enlace a sus respuestas | `benchmarks/results/per-model/*.md` | 171 archivos | `benchmarks/generate_per_model_md.py` | `benchmarks/check_docs.py` |
| Qué dato tiene que coincidir con qué, y quién lo hace cumplir | `SUPERFICIES.md` | 1 archivo | `benchmarks/generate_superficies.py` | `benchmarks/check_version.py` |
| ESTE MAPA | `MAPA.md` | se genera acá | `benchmarks/generate_mapa.py` | `benchmarks/generate_mapa.py --check` |

## Release

| Qué es | Dónde vive | Hoy | Quién lo escribe | Quién lo vigila |
|---|---|---|---|---|
| Cheatsheet PDF del mes (necesita DYLD_FALLBACK_LIBRARY_PATH) | `cheatsheet/*.pdf` | 6 archivos | `cheatsheet/generate_cheatsheet.py` | `benchmarks/check_release_mensual.py` |

---

*Generado por `benchmarks/generate_mapa.py`. El pipeline maestro
(`regenerate_all.py`) lo regenera y `--check` falla si quedó desactualizado.*
