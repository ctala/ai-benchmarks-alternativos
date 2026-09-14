# Muse Spark 1.3 — translation/translate_technical_en_es

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 7.27 | quality: 7.72
- latency_total: 5.055s | tokens_per_second: 149.4
- input_tokens: 148 | output_tokens: 755
- judge_score: 3.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el Authorization header. Los rate limits están fijados en 100 requests por minuto para el free tier. Si excede el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puede reanudar. Los Webhook endpoints deben responder dentro de 30 segundos o la entrega se marcará como failed y se reintentará hasta 3 veces con exponential backoff.