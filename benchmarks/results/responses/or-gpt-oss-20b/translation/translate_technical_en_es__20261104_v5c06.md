# GPT-OSS 20B — translation/translate_technical_en_es

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.85 | quality: 8.0
- latency_total: 8.7s | tokens_per_second: 56.7
- input_tokens: 197 | output_tokens: 493
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre el manejo de webhooks, aunque no se completó la oración original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticar con la API, incluye tu Bearer token en el Authorization header. Los rate limits se establecen en 100 requests per minute para el free tier. Si superas el rate limit, la API devuelve un 429 status code con un Retry-After header indicando cuándo puedes reanudar. Los webhook endpoints deben responder dentro de 30 seconds o la entrega se marcará como failed y se reintentará hasta 3 veces con exponential backoff.