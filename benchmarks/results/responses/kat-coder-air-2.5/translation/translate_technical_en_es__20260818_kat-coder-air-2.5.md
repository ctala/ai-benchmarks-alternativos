# KAT Coder Air v2.5 — translation/translate_technical_en_es

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 8.3 | quality: 8.0
- latency_total: 1.481s | tokens_per_second: 104.0
- input_tokens: 160 | output_tokens: 154
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con detalles adicionales útiles sobre el manejo de webhooks, y está claramente escrita y organizada.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa



Para autenticarte con la API, incluye tu token Bearer en el encabezado Authorization. Los límites de velocidad están configurados en 100 solicitudes por minuto para el plan gratuito. Si excedes el límite de velocidad, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puedes reanudar. Los endpoints de Webhook deben responder dentro de los 30 segundos, de lo contrario la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.