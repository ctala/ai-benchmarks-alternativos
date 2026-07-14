# Grok 4.3 — content_verificable/audiencia_que_ya_sabe

- model_id: `x-ai/grok-4.3`
- success: True  | final: 8.82 | quality: 10.0
- latency_total: 8.993s | tokens_per_second: 72.2
- input_tokens: 285 | output_tokens: 649
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando soluciones prácticas y detalladas para detectar y manejar workflows que devuelven 'success' sin realizar acciones.

## Respuesta completa

Un workflow que termina en verde no siempre significa que haya hecho algo. En n8n es bastante común que una ejecución devuelva “success” aunque el flujo haya procesado cero ítems. Esto suele pasar cuando los datos de entrada no cumplen las condiciones esperadas, cuando un nodo intermedio filtra todo o cuando una API responde 200 con un array vacío.

El problema es que n8n marca la ejecución como exitosa siempre que no se lance un error no controlado. Por eso puedes tener workflows que “funcionan” durante semanas sin mover ni un solo registro.

Para detectarlo de forma fiable, lo más efectivo es medir explícitamente el volumen de datos en puntos clave. Puedes usar un nodo **Function** o **Code** justo antes de la última acción que cuente los ítems y, si el resultado es cero, lance un error controlado o envíe una notificación. Otra opción es añadir un nodo **If** que compare `$items().length` contra cero y derive a una rama de “sin datos”.

También ayuda revisar periódicamente el panel de ejecuciones y filtrar por duración muy baja combinada con cero ítems procesados. Si detectas este patrón de forma recurrente, lo más robusto suele ser añadir una comprobación explícita de “hay datos” antes de ejecutar cualquier acción con efectos secundarios.

Sin esa validación, el verde del workflow deja de ser una señal útil.