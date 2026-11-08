# Gemma 4 26B MoE (3.8B activos) — translation/translate_technical_en_es

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 8.15 | quality: 8.0
- latency_total: 1.767s | tokens_per_second: 58.3
- input_tokens: 163 | output_tokens: 103
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando detalles adicionales útiles sobre el manejo de webhooks, aunque no se completó la oración original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el header Authorization. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si excede el rate limit, la API devuelve un status code 429 con un header Retry-After indicando cuándo puede reanudar. Los webhook endpoints deben responder dentro de los 30 segundos o la entrega será marcada como fallida y se reintentará hasta 3 veces con exponential backoff.