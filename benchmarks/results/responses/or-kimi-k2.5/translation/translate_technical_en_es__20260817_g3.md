# Kimi K2.5 — translation/translate_technical_en_es

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 6.98 | quality: 8.0
- latency_total: 41.764s | tokens_per_second: 49.0
- input_tokens: 157 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, manteniendo los términos técnicos en inglés como se solicitó, aunque carece de profundidad adicional más allá de la traducción.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están configurados en 100 solicitudes por minuto para el free tier. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de Webhook deben