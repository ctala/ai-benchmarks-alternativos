# Qwen 3.8 27B — translation/translate_technical_en_es

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 6.84 | quality: 8.0
- latency_total: 118.485s | tokens_per_second: 31.9
- input_tokens: 202 | output_tokens: 3781
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando detalles adicionales sobre el manejo de webhooks, lo que añade profundidad y utilidad práctica.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa



Para autenticarte con la API, incluye tu Bearer token en el Authorization header. Los rate limits están configurados en 100 peticiones por minuto para el free tier. Si excedes el rate limit, la API devuelve un código de estado 429 con un Retry-After header que indica cuándo puedes reanudar. Los endpoints de webhook deben responder en 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.