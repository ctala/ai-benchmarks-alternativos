# DeepSeek V4 Flash 0731 — translation/translate_technical_en_es

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 7.75 | quality: 8.0
- latency_total: 16.29s | tokens_per_second: 78.5
- input_tokens: 153 | output_tokens: 1279
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con detalles adicionales útiles, aunque no todos son necesarios para la tarea original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu token Bearer en el header Authorization. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puedes reanudar. Los webhook endpoints deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.