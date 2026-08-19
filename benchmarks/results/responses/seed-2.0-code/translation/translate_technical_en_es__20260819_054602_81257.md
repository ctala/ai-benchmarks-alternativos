# Seed 2.0 Code — translation/translate_technical_en_es

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 7.08 | quality: 8.0
- latency_total: 43.966s | tokens_per_second: 57.6
- input_tokens: 187 | output_tokens: 2534
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con buena claridad y utilidad práctica, aunque la profundidad es moderada debido a la adición de detalles no presentes en el texto original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el encabezado Authorization. Los rate limits se establecen en 100 solicitudes por minuto para el free tier. Si superas el rate limit, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puedes reanudar las solicitudes. Los endpoints de webhook deben responder en menos de 30 segundos; de lo contrario, la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.