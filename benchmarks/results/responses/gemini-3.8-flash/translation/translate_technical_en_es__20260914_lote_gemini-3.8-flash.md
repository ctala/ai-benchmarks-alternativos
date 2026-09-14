# Gemini 3.8 Flash — translation/translate_technical_en_es

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 6.41 | quality: 6.6
- latency_total: 8.366s | tokens_per_second: 152.3
- input_tokens: 150 | output_tokens: 1274
- judge_score: 3.0 | justificación: La respuesta es generalmente precisa y relevante, pero añade información no solicitada sobre el tiempo de respuesta de los endpoints de webhook y los reintentos, lo que no está en el texto original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si superas el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.