# Ling 3.0 Flash VL — translation/translate_technical_en_es

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 7.22 | quality: 6.88
- latency_total: 4.961s | tokens_per_second: 93.9
- input_tokens: 177 | output_tokens: 466
- judge_score: 3.2 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarse con la API, incluye tu Bearer token en el Authorization header. Los Rate limits están configurados en 100 solicitudes por minuto para el free tier. Si excedes el rate limit, la API retorna un 429 status code con un Retry-After header que indica cuándo puedes reanudar. Los Webhook endpoints deben responder en menos de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.