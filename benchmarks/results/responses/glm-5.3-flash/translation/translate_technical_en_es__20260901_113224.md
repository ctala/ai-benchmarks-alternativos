# GLM 5.3 Flash — translation/translate_technical_en_es

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 6.55 | quality: 6.6
- latency_total: 28.917s | tokens_per_second: 48.1
- input_tokens: 157 | output_tokens: 1391
- judge_score: 3.0 | justificación: La respuesta es generalmente precisa y relevante, pero introduce detalles no presentes en el texto original, como el tiempo de respuesta para los endpoints de webhook y el número de reintentos, lo que afecta la precisión y profundidad.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits se establecen en 100 requests por minuto para el free tier. Si excedes el rate limit, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.