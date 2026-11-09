## 1. Núcleo

- [x] 1.1 `benchmarks/indice.py`: peso, nota de Harbor, margen (método B) y combinación. Verificar: `test_unitarios`.
- [x] 1.2 Export: `score_calidad` nuevo, `calidad_ci95`, `nota_harbor`, sin dato agéntico fuera del ranking, Pareto después de la nota, `grupo_cabeza` con margen y más barato. Verificar: el control reproduce la simulación (18 de 68).
- [x] 1.3 `bands` global sobre la nota nueva; `score_agentico` usa la misma nota de Harbor. Verificar: `test_unitarios`.
- [x] 1.4 Tier de precio y ruta aparte. Verificar: ningún tier publicado es una ruta.

## 2. Superficies

- [x] 2.1 Calculadora: vista por defecto por la nota, «≈», línea del grupo, más barato, «Examen» en el compuesto y en pilares, limitación de «a tu medida», «Dataset v6.0.0 · examen v5». Verificar: `qa_calculadora`.
- [x] 2.2 Páginas de orden global, README, MODELOS.md, fichas y landings por la nota nueva. Verificar: `auditar_paginas`, `check_consistency`.
- [x] 2.3 Guardrails: peso único, grupo desde el export, sin dato agéntico fuera de los órdenes; cada uno con su sabotaje en `test_guardrails`.

## 3. Cierre

- [x] 3.1 DECISIONES (reemplaza la fila del 6-nov), CHANGELOG v6.0.0, 7 superficies de versión.
- [x] 3.2 Blog: `--check` y la lista de cifras que cambian; `--write` solo con OK (parada c).
- [x] 3.3 Push, release y deploy, cada uno con OK y verificación en vivo (parada d). OK de Cristian el 9-nov; la verificación en vivo se hace sobre lo empujado y, si algo falla, entra como fix.
