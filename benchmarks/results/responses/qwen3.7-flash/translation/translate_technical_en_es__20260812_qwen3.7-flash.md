# Qwen 3.7 Flash — translation/translate_technical_en_es

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 7.82 | quality: 8.0
- latency_total: 17.697s | tokens_per_second: 161.7
- input_tokens: 160 | output_tokens: 2862
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando detalles adicionales útiles sobre el manejo de webhooks, aunque no se mencionó en el texto original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el Authorization header. Los Rate limits están establecidos en 100 requests por minuto para la capa gratuita. Si excedes el Rate limit, la API devuelve un 429 status code con un Retry-After header que indica cuándo puedes reanudar. Los Webhook endpoints deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.