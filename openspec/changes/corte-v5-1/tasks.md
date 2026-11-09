## 1. Ocasiones (de corte-v5 3.1, 3.3-3.6)

Motivo de salida de v5.0.0: no se construyeron en la ventana; v5.0.0 sale con los pilares y la columna agéntica medidos.

- [ ] 1.1 Registro de las 6 ocasiones en `suites.py` con volúmenes por defecto de `OCASIONES.md` (era 3.1). Verificar: `check_suites.py` falla si una suite del índice no pertenece a ninguna ocasión.
- [ ] 1.2 Programar: jubilar `code_generation` del índice; las tareas Harbor propias sostienen la ocasión con Terminal-Bench como banda (era 3.3). Verificar: `suites.del_indice()` lo refleja y ningún doc vivo cita `code_generation` como vigente.
- [ ] 1.3 Calculadora: selector de ocasión, volúmenes editables, precio mensual al volumen declarado (era 3.4). Verificar: `qa_calculadora.mjs` con un caso por ocasión.
- [ ] 1.4 Páginas y blog leen ocasiones; `check_consistency` y `check_blog_consistency` se adaptan con su prueba (era 3.5). Verificar: QA verde sin bajar ningún bloqueante.
  - [ ] 1.4.a `auditar_paginas` verifica cada «X lidera el pilar Y» contra `models.json` (era 3.5.a). Verificar: prueba con un líder falso en rojo y control verde.
  - [ ] 1.4.b Fichas huérfanas detectadas por `validate.py` (era 3.5.b). Verificar: prueba que publica una huérfana y exige rojo.
  - [ ] 1.4.c Línea «medido en: proveedor, cuantización, thinking» en ficha, comparación y calculadora (era 3.5.c). Verificar: guardrail con su prueba.
  - [ ] 1.4.d CTA único al go-link `go.aprenderepite.com/benchmark`, sin «gratis» ni `skool.com`, firma Tala (era 3.5.d). Verificar: sabotaje que duplica el bloque, mete «gratis» y enlaza a `skool.com`.
- [ ] 1.5 Reporte por modelo de tokens de razonamiento, tiempo y respuestas vacías por pensar de más (era 3.6). Verificar: una cifra recalculada a mano desde sus runs coincide.

## 2. Recalibración del z-score (de corte-v5 3.2 y ROADMAP v5.1)

Motivo de salida: `--recalibrate` mueve la media/std congeladas; necesita su OK aparte (R8).

- [ ] 2.1 Simular la referencia v5 contra el ranking v5 (con la v4, 1 punto de calidad vale 5,73 de score). Verificar: simulación con control verde sobre lo publicado en v5.0.0.
- [ ] 2.2 Con el OK de Cristian, `export_for_pages.py --recalibrate --scoring-version v5.1` y `ocasiones` por modelo. Verificar: fila en DECISIONES y bump según VERSIONADO.
- [ ] 2.3 Harbor entra al compuesto («ajustado a mis pesos») como componente propio, con su media/std en la referencia recalibrada. Motivo: desde v6.0.0 la nota de calidad incluye Harbor (25 %), pero el compuesto sigue sobre el examen y no ve el trabajo agéntico; la calculadora lo declara como limitación conocida (DECISIONES, 9-nov-2026). Verificar: simulación con control verde, OK aparte para recalibrar (R8) y la limitación se retira de la calculadora con su guardrail.

## 3. Terminal-Bench en el Spark (de corte-v5 4.1-4.3)

Motivo de salida: necesita la ventana del Spark que autoriza Cristian.

- [ ] 3.1 Camino `externos/` declarado en `check_caminos.py` y fila en DECISIONES (era 4.1). Verificar: prueba de sabotaje.
- [ ] 3.2 Qwen 3.8 Flash contra Ornith 1.5 en el harness oficial, mínimo 5 intentos por tarea (era 4.2). Verificar: OK de Cristian para la ventana.
- [ ] 3.3 Publicación como corrida independiente y referencia desde Hugging Face (era 4.3). Verificar: OK textual antes de publicar.

## 4. Registro y hallazgos de la ventana de v5 (de corte-v5 6.6-6.9)

Motivo de salida: la ventana se midió (lotes v5c01-v5c30), pero su registro formal y los dos hallazgos no se publicaron.

- [ ] 4.1 Registrar la cifra gastada en la ventana contra la dimensionada ($47-53) (era 6.6). Verificar: `check_presupuesto` y el gasto real.
- [ ] 4.2 Verificación formal sobre los 64: `check_effort`, `check_truncamiento` y `check_mezcla` (era 6.7). Verificar: los tres en verde, citados.
- [ ] 4.3 Hallazgo 1: delta de calidad apagado − default por suite de peldaño 1 y 2, sobre tests comunes (era 6.8). Verificar: cifra recalculada a mano; post por el flujo del blog con OK.
- [ ] 4.4 Hallazgo 2: delta de calidad por proveedor en los abiertos, sobre tests comunes, con el caso GPT-OSS en DeepInfra (era 6.9). Verificar: igual que 4.3.

## 5. Lo anotado para 5.1

- [ ] 5.1 `prompt_injection_es` entra al examen (hoy 16 rankeados sin dato de seguridad; la mediana sale de 55). Es medición: ventana declarada. Verificar: `suites.del_examen()` lo incluye y la ficha muestra el dato.
- [ ] 5.2 Grupo de cabeza por bootstrap pareado sobre los tests comunes (opción B, DECISIONES 6-nov-2026). Verificar: simulación contra `bands.py` y rango de puestos publicable.
- [ ] 5.3 Las fichas `/modelo/<key>/` muestran «N de 4» con A3 cubriéndolas; puede salir en v5.0.1. Verificar: sabotaje de A3 en una ficha.
- [ ] 5.4 `dateModified` solo con cambio de contenido en `generate_comparison.py` y `generate_rankings.py`. Verificar: guardrail con sabotaje.
- [ ] 5.5 Rediseño de la precisión con cadenas difíciles que no parezcan secretos (suite nueva, aditiva; DECISIONES 7-nov-2026). Verificar: muestra antes del examen (Regla 0.7 del RUNBOOK).
- [ ] 5.6 Reescribir AGENTS.md para v5 (hoy snapshot v4: recomienda modelos retirados) y devolverlo a «vigente». Verificar: `check_docs` y `check_consistency` verdes.
- [x] 5.7 «≈» en la calculadora para el grupo de cabeza. — **descartada en este change: pasa a `indice-calidad-harbor` (DECISIONES, 9-nov-2026)**: Cristian decidió que el «≈» llega a la calculadora con el índice v6.0.0, sin esperar a que el grupo baje de 20 %; con la nota nueva el grupo es 18 de 68 (26 %) y `MAX_BAND_SHARE` se queda en 20 %. La condición original (después de 5.2, grupo ≤ 20 %) queda reemplazada; 5.2 sigue abierta para achicar el grupo.
