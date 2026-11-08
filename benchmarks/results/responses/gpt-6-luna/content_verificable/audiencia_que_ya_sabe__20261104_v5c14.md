# GPT-6 Luna — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-6-luna`
- success: True  | final: 9.17 | quality: 10.0
- latency_total: 7.335s | tokens_per_second: 87.0
- input_tokens: 101 | output_tokens: 638

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

## «Success» no significa «hecho»

Un workflow puede terminar en verde y no haber producido ningún cambio. En n8n, *success* suele significar que la ejecución terminó sin un error no controlado; no que se cumpliera el objetivo de negocio.

Pasa, por ejemplo, cuando un `IF` manda los datos por una rama que acaba ahí, un filtro deja cero ítems, un nodo configurado para continuar tras un error permite seguir, o una API responde `200` pero informa que no modificó nada. También puede ocurrir que el flujo descarte un registro por idempotencia —correctamente—, aunque desde fuera parezca que no hizo nada.

La solución es comprobar efectos, no solo estados de ejecución:

- **Define una postcondición**: ¿qué debe existir o cambiar si el flujo funcionó? Comprueba la respuesta de la API, el registro creado o el estado actualizado.
- **Mide el resultado**: registra cuántos ítems entraron, cuántos se filtraron y cuántas acciones se completaron. Un cero inesperado debe ser visible.
- **Falla ante resultados vacíos cuando corresponda**: tras el paso crítico, valida que haya un resultado útil. Si no lo hay, lanza un error o enruta la ejecución a una alerta.
- **Distingue «sin cambios» de «fallo»**: si una ejecución idempotente no debía actuar, registra ese resultado como tal; no lo confundas con una ejecución que procesó trabajo.
- **Alerta por invariantes**, no solo por ejecuciones fallidas: por ejemplo, ejecuciones completadas con cero elementos procesados durante una ventana en la que se esperaban eventos.

La pregunta clave para revisar un workflow no es «¿acabó?», sino «¿qué evidencia verificable demuestra que hizo lo que debía?».