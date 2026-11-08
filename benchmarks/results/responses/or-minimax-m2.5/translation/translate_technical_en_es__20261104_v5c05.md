# MiniMax M2.5 — translation/translate_technical_en_es

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 7.68 | quality: 8.0
- latency_total: 5.457s | tokens_per_second: 79.2
- input_tokens: 179 | output_tokens: 432
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una claridad excepcional, aunque la profundidad es solo aceptable y no se expande mucho más allá de la información básica.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarse con la API, incluya su token Bearer en el encabezado de Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si excede el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After indicando cuándo puede reanudar. Los endpoints de webhook deben responder en 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con retroceso exponencial.