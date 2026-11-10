# LFM-3 1.7B — translation/translate_technical_en_es

- model_id: `liquid/lfm-3-1.7b`
- success: True  | final: 7.86 | quality: 8.0
- latency_total: 7.403s | tokens_per_second: 282.9
- input_tokens: 158 | output_tokens: 2094
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre el manejo de webhooks, aunque esta parte no estaba en el texto original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu token Bearer en el encabezado Authorization. Los límites de tasa están configurados en 100 solicitudes por minuto para el plan gratuito. Si superas el límite de tasa, la API devuelve un código de estado 429 junto con un encabezado Retry-After que indica cuándo puedes reanudar. Los endpoints webhook deben responder dentro de 30 segundos o la entrega será marcada como failada y se intentará de nuevo hasta 3 veces con backoff exponencial.