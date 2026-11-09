## Why

v5.0.0 salió el 8-nov-2026 con lo medido en la ventana: proveedor fijo, thinking por peldaño y el trabajo agéntico contado en tareas de Harbor. Lo que el corte v5 planificó y no construyó, más lo que se anotó para después, no se pierde: vive en este change, cada tarea con el motivo por el que salió de v5.0.0. El porqué de cada decisión está en `DECISIONES.md` (fila del 8-nov-2026, «v5.0.0 sale con lo medido…»); este change apunta, no repite.

## What Changes

- **Ocasiones en vez de pilares** (de `corte-v5` 3.1, 3.3-3.6): registro, selector en la calculadora, generadores y blog, guardrails de líder, fichas huérfanas, línea «medido en» y CTA único.
- **Recalibración del z-score** (de `corte-v5` 3.2): se simula contra el ranking v5 y, con su OK aparte (R8), se mueve la referencia congelada.
- **Terminal-Bench en el Spark** (de `corte-v5` 4.1-4.3), con la ventana que autorice Cristian.
- **Registro y hallazgos de la ventana de v5** (de `corte-v5` 6.6-6.9): la cifra, la verificación sobre los 64 y los dos posts.
- **Lo anotado para 5.1:** `prompt_injection_es` al examen, grupo de cabeza por bootstrap pareado, fichas con «N de 4» (puede salir en v5.0.1), `dateModified` solo con cambio de contenido, rediseño de la precisión y reescritura de AGENTS.md.

## Capabilities

### New Capabilities
- `recomendacion-por-ocasiones`: la delta que `corte-v5` escribió y no implementó; vuelve acá sin cambios.

### Modified Capabilities
- Ninguna.

## Impact

- Medición: `prompt_injection_es` y la precisión rediseñada entran en ventana declarada, con el OK de Cristian y la cifra delante.
- Presentación: ocasiones, recalibración, bootstrap y fichas se simulan contra los runs en disco antes de aplicar.
- Afuera: blog, cheatsheet y datasheet solo con el OK textual de Cristian.
