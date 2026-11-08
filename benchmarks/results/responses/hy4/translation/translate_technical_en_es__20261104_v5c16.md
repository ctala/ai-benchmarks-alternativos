# Tencent Hy4 — translation/translate_technical_en_es

- model_id: `tencent/hy4`
- success: True  | final: 7.84 | quality: 8.0
- latency_total: 2.454s | tokens_per_second: 48.1
- input_tokens: 177 | output_tokens: 118
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una buena profundidad al añadir detalles sobre el manejo de webhooks, y está claramente escrita y organizada, siendo útil para un emprendedor.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header `Authorization`. Los rate limits están configurados en 100 requests por minuto para el free tier. Si excedes el rate limit, la API devuelve un status code `429` con un header `Retry-After` que indica cuándo puedes reanudar. Los endpoints de webhook deben responder dentro de los 30 segundos; de lo contrario, el delivery se marcará como failed y se reintentará hasta 3 veces con exponential backoff.