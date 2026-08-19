# GPT-5.6 Terra — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 7.199s | tokens_per_second: 67.9
- input_tokens: 101 | output_tokens: 489
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para expertos en n8n, proporcionando soluciones prácticas y detalladas para detectar workflows que devuelven 'success' sin efecto.

## Respuesta completa

Un workflow puede terminar en verde y, aun así, no haber producido ningún efecto. En n8n, *success* significa esencialmente que ningún nodo lanzó un error no gestionado. No significa que se creó el registro, se envió el mensaje, se actualizó la factura o se procesaron los datos esperados.

Los casos más comunes:

- Un `IF` o `Switch` derivó todos los items a una rama sin acciones.
- Un filtro, búsqueda o paginación devolvió cero resultados.
- Un nodo HTTP recibió `200 OK`, pero el cuerpo contiene un error funcional: `{"success": false}`, una lista vacía o un estado `pending`.
- Un upsert no modificó nada porque el dato ya existía.
- Una expresión produjo `null`, una fecha fuera de rango o un identificador incorrecto, pero la API aceptó la petición.
- Un nodo configurado para continuar ante error ocultó un fallo que debía ser relevante.

La solución no es mirar más ejecuciones verdes. Es definir explícitamente qué significa “hecho”.

Añade controles de postcondición: ¿el número de items procesados es mayor que cero? ¿La API devolvió el ID del recurso creado? ¿El contador de registros actualizados coincide con el esperado? ¿El estado final pasó realmente a `completed`?

Convierte esas condiciones en fallos deliberados. Si esperabas al menos un resultado y recibes cero, lanza un error. Si una API responde 200 pero su payload indica rechazo, trátalo como fallo. Si una operación es idempotente, registra si creó, actualizó o ignoró el recurso.

También ayuda guardar métricas por ejecución: items de entrada, items tras cada filtro, acciones intentadas y acciones confirmadas. Un workflow fiable no solo termina sin errores: deja evidencia verificable de su resultado.