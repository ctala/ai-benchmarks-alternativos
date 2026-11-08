# Qwen 3-Next 80B Instruct — translation/translate_technical_en_es

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 8.45 | quality: 8.0
- latency_total: 0.893s | tokens_per_second: 143.3
- input_tokens: 160 | output_tokens: 128
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con buena claridad y utilidad práctica, aunque la profundidad es solo aceptable.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu token Bearer en el encabezado Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para el plan gratuito. Si superas el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder dentro de 30 segundos, de lo contrario la entrega se marcará como fallida y se reintentará hasta 3 veces con backoff exponencial.