# Qwen 3.5 35B — translation/translate_technical_en_es

- model_id: `qwen/qwen3.5-35b-a3b`
- success: True  | final: 8.15 | quality: 8.0
- latency_total: 1.636s | tokens_per_second: 67.2
- input_tokens: 162 | output_tokens: 110
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando detalles adicionales útiles sobre el manejo de webhooks, aunque no se requiere en la instrucción original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si excedes el límite de tasa, la API devuelve un código de estado 429 con un header Retry-After indicando cuándo puedes reanudar. Los endpoints de Webhook deben responder dentro de los 30 segundos, de lo contrario la entrega se marcará como fallida y se reintentará hasta 3 veces con backoff exponencial.