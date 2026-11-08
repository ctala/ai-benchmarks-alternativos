# Qwen 3.8 27B — translation/translate_technical_en_es

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 7.76 | quality: 8.0
- latency_total: 3.138s | tokens_per_second: 39.2
- input_tokens: 162 | output_tokens: 123
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre los endpoints de webhook, aunque esta información no estaba en el texto original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu token Bearer en la cabecera Authorization. Los límites de tasa (rate limits) se establecen en 100 solicitudes por minuto para el plan gratuito. Si superas el límite de tasa, la API devuelve un código de estado 429 junto con una cabecera Retry-After que indica cuándo puedes reanudar las solicitudes. Los endpoints de webhook deben responder en un plazo de 30 segundos; de lo contrario, la entrega se marcará como fallida y se reintentará hasta 3 veces con backoff exponencial.