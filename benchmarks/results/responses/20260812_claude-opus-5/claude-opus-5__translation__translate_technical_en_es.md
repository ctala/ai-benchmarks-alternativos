# Claude Opus 5 — translation/translate_technical_en_es

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.17 | quality: 8.0
- latency_total: 4.911s | tokens_per_second: 48.3
- input_tokens: 239 | output_tokens: 237
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los terminos tecnicos en ingles y traduciendo el resto correctamente. Aunque añade información sobre el tiempo de respuesta de los webhook endpoints, esta no estaba en el texto original, lo que reduce la puntuación de profundidad. Sin embargo, la claridad y utilidad práctica son altas, siendo útil para un emprendedor.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están establecidos en 100 requests por minuto para el tier gratuito. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puedes reanudar las peticiones. Los endpoints de webhook deben responder en un plazo de 30 segundos; de lo contrario, la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.