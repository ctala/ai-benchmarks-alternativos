# Grok 4.6 — translation/translate_technical_en_es

- model_id: `x-ai/grok-4.6`
- success: True  | final: 6.05 | quality: 6.6
- latency_total: 19.278s | tokens_per_second: 77.2
- input_tokens: 346 | output_tokens: 1489
- judge_score: 3.0 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticar con la API, incluye tu Bearer token en el Authorization header. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si excedes el rate limit, la API devuelve un 429 status code con un Retry-After header indicando cuándo puedes reanudar. Los webhook endpoints deben responder en 30 segundos o la delivery se marcará como failed y se reintentará hasta 3 veces con exponential backoff.