# Gemini 3.1 Pro — translation/translate_technical_en_es

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 7.0 | quality: 8.0
- latency_total: 19.116s | tokens_per_second: 102.8
- input_tokens: 150 | output_tokens: 1965
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando detalles adicionales útiles sobre el manejo de webhooks, aunque no se solicitaron explícitamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están establecidos en 100 peticiones por minuto para el nivel gratuito. Si excedes el rate limit, la API devuelve un código de estado 429 con un header Retry-After indicando cuándo puedes reanudar. Los endpoints del webhook deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.