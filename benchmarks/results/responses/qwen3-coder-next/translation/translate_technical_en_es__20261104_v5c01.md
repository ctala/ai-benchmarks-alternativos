# Qwen3-Coder-Next (OpenRouter FP8) — translation/translate_technical_en_es

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 7.85 | quality: 8.0
- latency_total: 2.906s | tokens_per_second: 43.4
- input_tokens: 160 | output_tokens: 126
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una claridad excepcional, aunque la profundidad es solo aceptable debido a la falta de detalles adicionales sobre el manejo de errores o configuraciones.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarse con la API, incluya su token Bearer en el encabezado Authorization. Los límites de velocidad están establecidos en 100 solicitudes por minuto para la capa gratuita. Si supera el límite de velocidad, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puede reanudar. Los endpoints de Webhook deben responder dentro de los 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con retroceso exponencial.