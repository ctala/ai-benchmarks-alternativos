# Llama 4 Maverick — translation/translate_technical_en_es

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 8.15 | quality: 8.0
- latency_total: 1.684s | tokens_per_second: 62.3
- input_tokens: 151 | output_tokens: 105
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con terminos tecnicos mantenidos en ingles y una traduccion clara y organizada. Aunque añade información sobre el tiempo de respuesta de los webhook, no es parte del texto original, lo que reduce ligeramente la profundidad.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

"Para autenticar con la API, incluya su token Bearer en el encabezado Authorization. Los límites de velocidad están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si supera el límite de velocidad, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puede reanudar. Los endpoint de Webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se volverá a intentar hasta 3 veces con retroceso exponencial."