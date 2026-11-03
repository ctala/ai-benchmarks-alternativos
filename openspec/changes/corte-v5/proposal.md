## Why

El benchmark mide 115 modelos con 143 tests propios y un juez LLM que decide el 31 % del índice. Cristian abrió la puerta a cambiar el cómo (*«no me importa dejar de hacer suites si estandarizamos»*) con una condición: el qué, un emprendedor hispanohablante decidiendo qué modelo pagar, no se toca. En el camino se descartó replicar lo que otros ya miden (*«NocoDB como prueba no sé si aporta mucho… No estamos aportando algo realmente valioso»*) y se fijó la dirección: **enriquecer con lo propio los benchmarks públicos verificados por la comunidad**, no competir con ellos.

Es un cambio de qué significa el número: **v5.0.0, mayor**. Y un mayor dura varias sesiones. `abrir-sesion` planifica una; lo que faltaba era un plan que sobreviva entre sesiones y un guardrail que no lo deje en el aire. El porqué de cada decisión sigue viviendo en `DECISIONES.md` (filas del 3-nov-2026): este change apunta, no repite.

## What Changes

- **Ocasiones en vez de pilares.** Seis ocasiones del emprendedor (Escribir, Relación comercial, Automatizar, Decidir con documentos, Programar, Local) con volúmenes por defecto que la calculadora deja cambiar. Educación queda dentro de Escribir. `code_generation` se jubila; la conversación en español con el agente se mantiene en las tareas Harbor propias. Detalle: `OCASIONES.md`.
- **Fuentes externas como filtro duro.** Terminal-Bench (Programar) y Toolathlon-Verified (Automatizar) entran por ingesta con script, licencia y fecha. SWE-bench Pro público y Arena se muestran como banda. Artificial Analysis se enlaza, no se ingesta. Nunca se promedian cifras de harnesses distintos. Detalle y criterio de entrada: `FUENTES-EXTERNAS.md`.
- **Conjunto base.** Los modelos que esas fuentes ya midieron, cruzados con lo que se puede llamar por OpenRouter. El resto de los 115 sale con la capa propia y la marca «sin dato comunitario».
- **Modelos sin dato comunitario que le importan a un founder** se miden con el harness oficial de la fuente, se publican como corrida independiente y se referencian desde Hugging Face. Primer caso: Qwen 3.8 Flash contra Ornith 1.5 en Terminal-Bench. Antes, `check_caminos` recibe un camino declarado (`externos/`), no una excepción.
- **Orden desde el comienzo.** Rama `corte/v5`; OpenSpec dentro del benchmark; `check_specs.py` exige un solo change activo, 14 días como máximo sin tocarlo, archivo sin tareas abiertas y ninguno activo en `main`. Tarea cero: auditoría de confianza de los 20 guardrails, porque uno (`check_release_mensual`) estuvo meses en verde sin probar nada. Ningún guardrail se debilita para que el corte pase.

**BREAKING:** sí. Una cifra de v4.x deja de ser comparable con una de v5. El scoring_reference se recalibra en el release y todo lo publicado afuera (blog, cheatsheet, datasheet) se regenera.

## Capabilities

### New Capabilities
- `recomendacion-por-ocasiones`: cómo se organiza, se enriquece con fuentes comunitarias y se publica la recomendación por ocasión del emprendedor, incluido qué se mide con harness oficial cuando no hay dato público.
- `orden-del-corte`: cómo se planifica, se vigila y se cierra un corte mayor del benchmark sin debilitar guardrails ni dejar el plan en el aire.

### Modified Capabilities
- Ninguna spec previa en `openspec/specs/`: el benchmark adopta OpenSpec con este change.

## Impact

- Código: `benchmarks/check_specs.py` (nuevo), `fuentes_externas.py` (nuevo), `export_for_pages.py`, `scoring.py`, `suites.py`, `check_caminos.py`, `check_consistency.py`, `docs/app.js`, generadores de páginas y de tablas del blog.
- Datos: `docs/data/models.json` cambia de esquema (ocasiones, bandas externas, `sin_dato_comunitario`).
- Docs: `DECISIONES.md`, `OCASIONES.md`, `FUENTES-EXTERNAS.md`, `CLAUDE.md`, skill `abrir-sesion`, `CHANGELOG.md`.
- Afuera: posts pilar del blog (se regeneran con `generate_blog_tablas.py`), cheatsheet y datasheet del release, referencia en Hugging Face. Nada se publica sin el ok textual de Cristian.
- Costo: la ingesta es gratis. La corrida Qwen 3.8 Flash contra Ornith 1.5 corre en el Spark cuando Cristian lo autorice (el modelo principal está abajo y no se sube). Se estima con `check_presupuesto.py --necesito` antes de cualquier gasto en OpenRouter.
