# Mercury 2.5 — translation/translate_technical_en_es

- model_id: `inception/mercury-2.5`
- success: True  | final: 7.95 | quality: 7.72
- latency_total: 2.524s | tokens_per_second: 559.9
- input_tokens: 142 | output_tokens: 1413
- judge_score: 3.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa



Para autenticarse con la API, incluye tu Bearer token en el encabezado Authorization. Los rate limits se establecen en 100 requests por minuto para el free tier. Si superas el rate limit, la API devuelve un código de estado 429 con un encabezado Retry-After indicando cuándo puedes reanudar. Los endpoints Webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.