# Tencent Hy4 preview — translation/translate_technical_en_es

- model_id: `tencent/hy4-preview`
- success: True  | final: 7.17 | quality: 8.0
- latency_total: 25.248s | tokens_per_second: 74.4
- input_tokens: 174 | output_tokens: 1879
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una buena profundidad y claridad, proporcionando información útil para un emprendedor.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el Authorization header. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si excede el rate limit, la API devuelve un status code 429 con un Retry-After header que indica cuándo puede reanudar. Los endpoints de Webhook deben responder en 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.