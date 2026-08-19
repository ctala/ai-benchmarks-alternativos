# Qwen 2.5 72B — translation/translate_technical_en_es

- model_id: `qwen/qwen-2.5-72b-instruct`
- success: True  | final: 7.85 | quality: 8.0
- latency_total: 3.289s | tokens_per_second: 37.1
- input_tokens: 160 | output_tokens: 122
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los terminos tecnicos en ingles y traduciendo correctamente el resto. Añade información útil sobre el tiempo de respuesta para los endpoints de webhook, aunque esta información no estaba en el texto original. La claridad y la utilidad práctica son altas, siendo útil para un emprendedor.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

"Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los límites de tasas están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si superas el límite de tasa, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con un respaldo exponencial."