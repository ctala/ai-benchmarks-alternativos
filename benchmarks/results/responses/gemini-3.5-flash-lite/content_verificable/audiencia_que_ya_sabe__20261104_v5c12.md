# Gemini 3.5 Flash Lite — content_verificable/audiencia_que_ya_sabe

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 9.24 | quality: 10.0
- latency_total: 2.841s | tokens_per_second: 145.7
- input_tokens: 93 | output_tokens: 414

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

¿Te ha pasado? Miras el historial de ejecuciones en n8n, todo verde, un flamante *success* de punta a punta... pero vas a la herramienta de destino y el dato no está. 

El workflow mintió. O, mejor dicho, hizo exactamente lo que le pediste, no lo que necesitabas. 

En n8n, el nodo *Respond to Webhook* o el final natural de una rama devuelven un 200 OK tan pronto como el proceso técnico termina sin errores fatales de sintaxis o conexión. A la plataforma le da igual si tu API externa respondió con un `204 No Content` porque el ID no existía, o si el filtro inicial descartó el 100% de los elementos. Para el motor, la ejecución fue exitosa. Para tu negocio, el workflow no hizo nada.

El verdadero peligro de los falsos positivos es que destruyen la trazabilidad silenciosamente. No hay alertas porque técnicamente no hubo fallo.

Para detectarlo a tiempo, aplica estas tres prácticas en tus flujos diarios:

1. **Valida la respuesta real, no el código HTTP:** No te fíes de un status 2xx. Añade un nodo *If* posterior que lea la propiedad de éxito del payload de respuesta (ej. `success: true` o un array con longitud mayor a 0).
2. **Usa `Error Trigger` con criterio de negocio:** Configura alertas no solo cuando n8n rompa, sino cuando el output crítico esté vacío. Si esperabas 5 registros y procesaste 0, fuérzalo como excepción.
3. **Métricas de salida:** Diseña tus flujos para que devuelvan contadores. Saber que el workflow corrió es inútil; saber que procesó 42 elementos es lo que te da tranquilidad.

Deja de confiar en el verde automático. Empieza a auditar lo que tus nodos realmente logran.