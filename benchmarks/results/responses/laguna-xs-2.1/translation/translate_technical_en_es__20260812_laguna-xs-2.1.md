# Poolside Laguna XS 2.1 — translation/translate_technical_en_es

- model_id: `poolside/laguna-xs-2.1`
- success: True  | final: 7.95 | quality: 7.72
- latency_total: 4.288s | tokens_per_second: 185.4
- input_tokens: 172 | output_tokens: 795
- judge_score: 3.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarse en la API, incluya su token Bearer en la cabecera Authorization. Los límites de solicitudes están establecidos en 100 peticiones por minuto en el plan gratuito. Si excedes el límite de solicitudes, la API devuelve un código de estado 429 con una cabecera Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder en menos de 30 segundos, de lo contrario se marcará el envío como fallido y se reintentará hasta 3 veces con exponential backoff.