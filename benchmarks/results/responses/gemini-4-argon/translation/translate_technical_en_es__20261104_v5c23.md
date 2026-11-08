# Gemini 4 Argon — translation/translate_technical_en_es

- model_id: `google/gemini-4-argon`
- success: True  | final: 7.32 | quality: 8.0
- latency_total: 4.984s | tokens_per_second: 22.7
- input_tokens: 178 | output_tokens: 113
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando detalles útiles sobre el manejo de límites de tasa y webhooks, aunque carece de profundidad en algunos aspectos.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header `Authorization`. Los rate limits están establecidos en 100 requests por minuto para el plan gratuito (free tier). Si excedes el rate limit, la API devuelve un código de estado 429 con un header `Retry-After` que indica cuándo puedes reanudar. Los endpoints de los webhooks deben responder en un máximo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces usando exponential backoff.