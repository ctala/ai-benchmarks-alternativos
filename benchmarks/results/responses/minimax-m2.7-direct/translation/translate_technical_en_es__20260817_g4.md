# MiniMax M2.7 (directo) — translation/translate_technical_en_es

- model_id: `MiniMax-M2.7`
- success: True  | final: 7.68 | quality: 8.0
- latency_total: 7.038s | tokens_per_second: 53.6
- input_tokens: 182 | output_tokens: 377
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con información útil y adicional sobre el manejo de endpoints de webhook.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu token Bearer en el header de Authorization. Los rate limits están establecidos en 100 solicitudes por minuto para el plan gratuito. Si excedes el rate limit, la API devuelve un código de estado 429 con un header de Retry-After indicando cuándo puedes continuar. Los endpoints de webhook deben responder en 30 segundos o la entrega será marcada como fallida y se reintentará hasta 3 veces con exponential backoff.