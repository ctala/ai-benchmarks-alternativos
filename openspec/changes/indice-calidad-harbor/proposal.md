## Why

El examen separa poco a los rankeados (desviación 0,27 entre 70) y Harbor separa mucho (1,87): las 4 tareas reales de agente son la señal que el índice no ve. Hoy la nota visible es solo examen y las páginas ordenan por otras cosas (compuesto, precio dentro del grupo), y eso confunde. Decisión de Cristian del 9-nov-2026; reemplaza la fila del 6-nov «dentro del grupo, elige por precio». Detalle y simulación en DECISIONES.md.

## What Changes

- **Calidad = 75 % examen + 25 % Harbor.** Nota de Harbor 0-10 = 0,6 × media + 0,4 × piso de las 4 tareas (la fórmula de `score_agentico` sin tool calling). Peso en una constante (`indice.PESO_HARBOR_EN_CALIDAD`); el export publica la nota y nadie la recalcula.
- **Margen con el ruido de Harbor** (método B): bootstrap de los 3 intentos por tarea, con la varianza de cada tarea encogida hacia la varianza agrupada de esa tarea (k0 = 1 frente a k = 3); se combina con el del examen como independientes.
- **Sin dato agéntico = fuera del ranking** (GPT-OSS 20B y 120B), con ficha y motivo visible.
- **Orden por la nota nueva** en la calculadora (vista por defecto) y en todas las páginas de orden global; grupo de cabeza con «≈», una línea con N y margen, y el más barato etiquetado, todo desde el export. Fuera del grupo, puesto con número. El «no concluyente» se escribe «El benchmark no separa a estos N: …; dentro del grupo, el más barato es X».
- **Compuesto y pilares siguen sobre el examen**, rotulados «Examen», sin recalibrar. El compuesto solo manda en «a tu medida» con pesos movidos; ahí no ve lo agéntico (limitación escrita).
- **Tier = precio; la ruta va aparte** (`cloud_nim` deja de mostrarse como tier).
- Versión **v6.0.0** (MAJOR: cambia qué significa la nota). Superficies: «Dataset v6.0.0 · examen v5».

## Capabilities

### New Capabilities
- `indice-calidad`: cómo se compone, se publica y se ordena la nota de calidad.

### Modified Capabilities

## Impact

`benchmarks/indice.py` (nuevo), `export_for_pages.py`, `bands.py`, `elegibilidad.py`, generadores de páginas y README, `docs/app.js`, guardrails nuevos con su sabotaje, blog (pilar y guía, con parada). `scoring_reference.json`: solo la etiqueta.
