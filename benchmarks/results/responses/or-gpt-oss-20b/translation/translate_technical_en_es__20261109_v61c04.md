# GPT-OSS 20B — translation/translate_technical_en_es

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 8.15 | quality: 8.0
- latency_total: 4.621s | tokens_per_second: 118.6
- input_tokens: 210 | output_tokens: 548
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre el manejo de webhooks, aunque no se menciona en el texto original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el encabezado Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si excede el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After indicando cuándo puede reanudar. Los Webhook endpoints deben responder dentro de 30 segundos o la entrega será marcada como fallida y se reintentará hasta 3 veces con exponential backoff.