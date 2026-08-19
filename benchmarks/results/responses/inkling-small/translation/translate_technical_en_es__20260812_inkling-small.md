# Inkling Small — translation/translate_technical_en_es

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 6.5 | quality: 6.6
- latency_total: 13.869s | tokens_per_second: 123.8
- input_tokens: 158 | output_tokens: 1717
- judge_score: 3.0 | justificación: La respuesta es generalmente precisa y relevante, pero añade información no solicitada sobre el tiempo de respuesta de los webhook endpoints, lo que reduce la precisión y relevancia.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el Authorization header. Los rate limits están configurados en 100 requests por minuto para el free tier. Si excedes el rate limit, la API devuelve un status code 429 con un Retry-After header que indica cuándo puedes reanudar. Los webhook endpoints deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.