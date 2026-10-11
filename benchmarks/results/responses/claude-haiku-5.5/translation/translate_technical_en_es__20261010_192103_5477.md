# Claude Haiku 5.5 — translation/translate_technical_en_es

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.3 | quality: 8.0
- latency_total: 1.632s | tokens_per_second: 122.6
- input_tokens: 241 | output_tokens: 200
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con una buena profundidad y utilidad práctica, aunque añade información no presente en el texto original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu token Bearer en el encabezado Authorization. Los límites de uso (rate limits) están establecidos en 100 solicitudes por minuto para el plan gratuito. Si superas el límite de uso, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puedes reanudar las solicitudes. Los endpoints de webhook deben responder en un plazo de 30 segundos; de lo contrario, la entrega se marcará como fallida y se reintentará hasta 3 veces con backoff exponencial.