# DeepSeek V4 Pro — content_verificable/audiencia_que_ya_sabe

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 8.21 | quality: 10.0
- latency_total: 98.489s | tokens_per_second: 93.5
- input_tokens: 100 | output_tokens: 9207

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Revisas el historial: todo verde, «Success». Pero la salida muestra cero ítems. Tu workflow corrió sin errores y no hizo nada. Silencio absoluto.

Pasa a menudo: un webhook con payload inesperado, un Item Lists que filtra todo, una API que devuelve array vacío, una rama Switch sin acciones. n8n marca Success porque no hubo excepción, no porque la lógica se cumpliera.

¿Cómo detectarlo? Deja de fiarte del verde. Después de cualquier filtro o paso dependiente de datos, mete un IF que evalúe {{ $items().length }}. Si es cero, redirige a Stop and Error o lanza alerta a Slack/email. Así el silencio se convierte en ruido. Y no cuentes con el Error Trigger: sin excepción, jamás se activará.

En webhooks, el Respond to Webhook siempre debería incluir un campo con el conteo, tipo { "procesados": {{ $items().length }} }. Si manejas múltiples ramas, añade una rama final que fuerce error cuando ningún camino tuvo ítems.

En producción, instrumenta nodos clave con un Function que registre la cantidad de ítems de entrada. Poco esfuerzo, gran beneficio cuando una API cambia en silencio.

Recuerda: Success en n8n es solo ausencia de excepciones, no validación de negocio. Cerrar esa brecha con un simple IF te da observabilidad real sin depender de logs manuales.