# Llama 3.1 8B Instant — translation/translate_technical_en_es

- model_id: `meta-llama/llama-3.1-8b-instruct`
- success: True  | final: 8.3 | quality: 8.0
- latency_total: 1.006s | tokens_per_second: 120.2
- input_tokens: 158 | output_tokens: 121
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información útil sobre el manejo de límites de tasa y webhooks, aunque añade detalles no presentes en el texto original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

"Para autenticarte con la API, incluye tu token Bearer en el encabezado de Autorización. Los límites de velocidad se establecen en 100 solicitudes por minuto para la versión gratuita. Si superas el límite de velocidad, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puedes reanudar. Los puntos de conexión de webhook deben responder dentro de 30 segundos o se marcará como fallido y se reintentará hasta 3 veces con un backoff exponencial."