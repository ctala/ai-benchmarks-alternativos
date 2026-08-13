# Decisiones — índice único

> **Qué es esto y qué NO es.** Es un **índice**, no un lugar nuevo donde escribir. Cada
> fila apunta a dónde vive el detalle. El repo tiene 34 documentos en la raíz y las
> decisiones estaban repartidas en 13 de ellos: el problema nunca fue falta de
> documentación, fue **no saber dónde buscarla**.
>
> **Regla de uso:** antes de proponer un cambio de diseño, buscá acá. Si la decisión ya
> está tomada, se respeta o se revierte explícitamente — no se reabre por olvido.
>
> **Regla de escritura:** una decisión entra acá cuando se toma, en el mismo commit. Una
> línea: qué se decidió, por qué en pocas palabras, y el enlace al detalle. Si no cabe en
> una línea, el detalle va al doc que corresponde y acá queda el puntero.

## Cómo leerlo

- **Vigente** = manda hoy. **Revertida** = se probó y se deshizo (se deja para no repetirla).
- El **por qué** es lo que más caduca de memoria y lo que más cuesta reconstruir. Si una
  fila no tiene por qué, está incompleta.

---

## Qué se publica y cómo se puntúa

| Fecha | Estado | Decisión | Por qué | Detalle |
|---|---|---|---|---|
| 13-ago-2026 | **Vigente** | El titular es el **índice de calidad**; precio y latencia van como columnas, nunca dentro | El compuesto castigaba caro y premiaba barato sin decirlo: Opus 4.6 era #5 en calidad y se publicaba #18 | [PLAN-V4.1 §3](PLAN-V4.1.md) |
| 13-ago-2026 | **Vigente** | Escala **absoluta**: `score_calidad` = `quality_avg` sin z-scorear | El z-score estiraba 1,39 puntos reales a 8 publicados. Y anclado, agregar un modelo no mueve a nadie: se acaban las recalibraciones | [PLAN-V4.1 §3](PLAN-V4.1.md) · [CHANGELOG v4.1.0](CHANGELOG.md) |
| 13-ago-2026 | **Revertida** | ~~Segunda tabla de "mejor valor" (el compuesto)~~ | Correlacionaba **r = 0,943** con el índice de calidad: dos tablas para decir lo mismo | [PLAN-V4.1 §3 corrección](PLAN-V4.1.md) |
| 13-ago-2026 | **Vigente** | Los segundos ejes son **frontera de Pareto** y **calidad por dólar** | Son las únicas métricas que no correlacionan con calidad (deja fuera 69 de 82; r = 0,052). Todo promedio ponderado terminó siendo una copia | [PLAN-V4.1 §3](PLAN-V4.1.md) |
| 13-ago-2026 | **Revertida** | ~~Columna "Rinde" (score² ÷ costo)~~ | **r = 0,999** con ordenar por precio. La calidad varía 1,19× y el costo 772×: "valor" *es* precio | [CHANGELOG v4.1.0](CHANGELOG.md) |
| 17-jul-2026 | Vigente | Referencia z-score **congelada por versión** para el compuesto | Antes, medir un modelo nuevo movía el score de todos | [README](README.md) |
| — | Vigente | **Nunca $0** como precio de un modelo del ranking | Un "gratis" gana el eje costo artificialmente y engaña la decisión que la calculadora existe para ayudar | [CLAUDE.md](CLAUDE.md) |

## Qué se mide y con qué

| Fecha | Estado | Decisión | Por qué | Detalle |
|---|---|---|---|---|
| 13-ago-2026 | **Vigente** | `niah_es` recortada a **128K+** | 8K y 64K daban 78% y 75% de notas perfectas: no distinguían y eran la mitad de la suite más cara | [niah_es.py](benchmarks/tests/niah_es.py) |
| 13-ago-2026 | **Vigente** | Dos suites duras nuevas, **validadas por discriminación** | Separan más que el examen completo (1,94 y 1,54 contra 1,28 entre el mejor y el peor modelo) | [CHANGELOG v4.1.0](CHANGELOG.md) |
| 12-ago-2026 | Vigente | **Nunca medir en un endpoint `:free`** | Fallan 69,2% contra 10,9% de los pagos — seis veces más. Rate limits y cuantización distinta no son el modelo | [CLAUDE.md](CLAUDE.md) |
| 12-ago-2026 | Vigente | **No reinventamos el motor de medición**; se adopta de LiveBench, BFCL, τ-bench, Artificial Analysis | Nuestro valor está en QUÉ medimos (español, casos de emprendedor), no en cómo | [CLAUDE.md](CLAUDE.md) · [PLAN-V4.1 §0](PLAN-V4.1.md) |
| — | Vigente | **No se editan prompts** de tests ya medidos | Invalida la comparación con runs previos. `prompt_sha` lo detecta | [CLAUDE.md](CLAUDE.md) |
| — | Vigente | Dos umbrales: **20 runs** para reportar, **50** para rankear | Con 3-12 runs un modelo lidera por azar | [export_for_pages.py](benchmarks/export_for_pages.py) |

## Proceso y control de cambios

| Fecha | Estado | Decisión | Por qué | Detalle |
|---|---|---|---|---|
| 13-ago-2026 | **Vigente** | **Presentación ≠ medición.** La presentación se simula antes y puede cambiar; la medición cambia **una vez por trimestre** | Lo que se rehizo tres veces en dos días costó $0 — el desgaste era rotación de decisiones, no dinero | [PLAN-ESTABILIDAD R1](PLAN-ESTABILIDAD.md) |
| 13-ago-2026 | **Vigente** | Las suites se **agregan, no se reemplazan** | Una suite nueva cuesta $29-43 y no invalida ningún run. Editar una existente invalida todo el histórico | [PLAN-ESTABILIDAD R2](PLAN-ESTABILIDAD.md) |
| 13-ago-2026 | **Vigente** | Calendario: día 1 = release con presentación **congelada**; ventana trimestral para medición | Que dejar de ser sorpresa | [PLAN-ESTABILIDAD §4](PLAN-ESTABILIDAD.md) |
| 12-ago-2026 | Vigente | **Una regla sin instrumento que la haga cumplir es una regla que ya se rompió** | Se pagó cinco veces en un día: reglas correctas, escritas, que fallaban en silencio | [CLAUDE.md](CLAUDE.md) |
| 13-ago-2026 | **Vigente** | Cada superficie nueva llega con su guardrail, en el mismo commit | Corolario de la anterior | [PLAN-ESTABILIDAD R3](PLAN-ESTABILIDAD.md) |

## Pendientes de decidir

| Tema | Qué falta saber | Dónde |
|---|---|---|
| Niveles de razonamiento | `effort=high` **no** es el techo de Anthropic. Estamos comparando modelos en configuraciones que no sabemos si son equivalentes | [CHANGELOG v4.1.0](CHANGELOG.md) |
| Benchmarks de terceros (SWE-Bench, GPQA) | Solo si la fuente es consultable y automatizable. Copiar de una landing devuelve el problema de cifras que caducan | [PLAN-V4.1 §3.ter](PLAN-V4.1.md) |
| Pilar del blog | Su sección de método explica el compuesto, que ya no se publica. Necesita reescritura, no find-replace | [CHANGELOG v4.1.0](CHANGELOG.md) |
| **9 docs citan modelos retirados** | Auditoría 13-ago: `COMPARATIVA`, `SUSCRIPCIONES`, `PROVEEDORES`, `CASOS_DE_USO`, `BENCHMARKS_EXTERNOS`, `THINKING_EXPLAINED` y otros recomiendan modelos que ya no existen — Devstral Small entre ellos. `check_consistency` lo avisa en cada corrida; limpiarlo es trabajo editorial pendiente | `check_consistency.py` |
| **8 docs sin tocar >45 días** | `PROVEEDORES` (113d), `DESCUBRIMIENTOS` (110d), `BENCHMARKS_EXTERNOS`/`NIAH_*`/`DATASHEET_04-05` (102d). Decidir cuáles son snapshots con fecha (se congelan) y cuáles son docs vivos podridos | — |

---

## Los instrumentos que hacen cumplir todo esto

Ninguna de las reglas de arriba se sostiene sola. Lo que las sostiene:

| Guardrail | Qué caza |
|---|---|
| `check_version.py` | Las 6 superficies que declaran versión, desalineadas · falta de tag · falta de CHANGELOG |
| `check_consistency.py` | Un doc vivo citando un score que ya no existe |
| `check_calculator.py` | Umbrales fuera de rango · filtros decorativos · campos que el JS lee y el export dejó de emitir |
| `check_blog_consistency.py` | Cifras caducas en el blog |
| `canario.py` | Invariantes rotos ANTES de lanzar un lote |
| `check_endpoints.py` | Modelos muertos en el ranking |
| `validate.py` · `audit_anomalies.py` · `audit_suites.py` | Integridad de los datos publicados |
| `calculate_costs.py --estimar` / `--gastado` | Estimar antes de gastar · saber cuánto se gastó de verdad |
