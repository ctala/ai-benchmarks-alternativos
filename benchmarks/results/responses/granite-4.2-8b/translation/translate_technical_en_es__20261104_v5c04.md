# Granite 4.2 8B — translation/translate_technical_en_es

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 8.3 | quality: 8.0
- latency_total: 1.135s | tokens_per_second: 106.6
- input_tokens: 168 | output_tokens: 121
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una claridad excepcional, aunque la profundidad es solo aceptable y no se proporciona información adicional sobre el tiempo de respuesta de los endpoints de webhook.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu token Bearer en la cabecera Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para la versión gratuita. Si excedes el límite de tasa, la API devuelve un código de estado 429 con una cabecera Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder dentro de 30 segundos; de lo contrario, la entrega se marcará como fallida y se reintentará hasta tres veces con retroceso exponencial.