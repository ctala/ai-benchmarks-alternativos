# Claude Opus 5 (suscripción) — translation/translate_technical_en_es

- model_id: `claude-opus-5`
- success: True  | final: 6.7 | quality: 8.0
- latency_total: 14.419s | tokens_per_second: 14.4
- input_tokens: 2 | output_tokens: 207
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con información útil y adicional sobre el manejo de webhooks, aunque no se menciona en el texto original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header `Authorization`. Los rate limits están fijados en 100 requests por minuto para el tier gratuito. Si excedes el rate limit, la API devuelve un status code 429 con un header `Retry-After` que indica cuándo puedes reanudar. Los endpoints de webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.