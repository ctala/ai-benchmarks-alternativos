# Granite 4.2 8B — translation/translate_technical_en_es

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 7.47 | quality: 7.72
- latency_total: 29.309s | tokens_per_second: 109.9
- input_tokens: 168 | output_tokens: 3221
- judge_score: 3.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarse con la API, incluya su token Bearer en la cabecera Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si excede el límite de tasa, la API devuelve un código de estado 429 con la cabecera Retry-After que indica cuándo puede reanudar. Los endpoints de webhook deben responder dentro de 30 segundos; de lo contrario, la entrega se marcará como fallida y se reintentará hasta 3 veces con backoff exponencial.