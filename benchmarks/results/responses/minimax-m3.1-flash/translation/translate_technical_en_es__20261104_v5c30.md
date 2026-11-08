# MiniMax M3.1 Flash — translation/translate_technical_en_es

- model_id: `minimax/minimax-m3.1-flash`
- success: True  | final: 8.09 | quality: 8.0
- latency_total: 3.075s | tokens_per_second: 282.0
- input_tokens: 343 | output_tokens: 867
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una claridad excepcional, aunque la profundidad es solo aceptable al añadir detalles no solicitados sobre los endpoints de webhook.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el encabezado Authorization. El límite de solicitudes es de 100 solicitudes por minuto para el nivel gratuito. Si superas el límite, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puedes reanudar las solicitudes. Los endpoints de webhook deben responder en un plazo de 30 segundos; de lo contrario, la entrega se marcará como fallida y se reintentará hasta 3 veces con backoff exponencial.