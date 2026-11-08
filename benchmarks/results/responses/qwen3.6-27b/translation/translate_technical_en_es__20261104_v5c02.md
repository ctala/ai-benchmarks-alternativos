# Qwen 3.6 27B base (OpenRouter FP8) — translation/translate_technical_en_es

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 7.94 | quality: 8.0
- latency_total: 2.318s | tokens_per_second: 52.2
- input_tokens: 162 | output_tokens: 121
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una buena profundidad al añadir detalles sobre el manejo de webhooks, y está claramente escrita y organizada, siendo útil para un emprendedor.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu token Bearer en el encabezado Authorization. Los límites de tasa (rate limits) se establecen en 100 solicitudes por minuto para el nivel gratuito. Si superas el límite de tasa, la API devuelve un código de estado 429 junto con un encabezado Retry-After que indica cuándo puedes reanudar las solicitudes. Los endpoints de webhook deben responder dentro de los 30 segundos; de lo contrario, la entrega se marcará como fallida y se reintentará hasta 3 veces con backoff exponencial.