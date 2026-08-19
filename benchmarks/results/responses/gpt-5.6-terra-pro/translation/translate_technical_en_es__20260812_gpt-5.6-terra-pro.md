# GPT-5.6 Terra Pro — translation/translate_technical_en_es

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 6.37 | quality: 6.6
- latency_total: 5.151s | tokens_per_second: 116.3
- input_tokens: 2387 | output_tokens: 599
- judge_score: 3.0 | justificación: La traducción es correcta y relevante, pero añade información no presente en el texto original, afectando la precisión y profundidad.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

"Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están establecidos en 100 solicitudes por minuto para el plan gratuito. Si excedes el rate limit, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder en un plazo de 30 segundos; de lo contrario, la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff."