# Claude Sonnet 5 — translation/translate_technical_en_es

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 6.42 | quality: 6.6
- latency_total: 3.687s | tokens_per_second: 45.3
- input_tokens: 239 | output_tokens: 167
- judge_score: 3.0 | justificación: La respuesta es generalmente precisa y relevante, pero añade información no presente en el texto original, como el tiempo de respuesta para los endpoints de webhook, lo que afecta la precisión.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header de Authorization. Los rate limits están configurados en 100 requests por minuto para el tier gratuito. Si excedes el rate limit, la API retorna un status code 429 con un header de Retry-After indicando cuándo puedes reanudar. Los webhook endpoints deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.