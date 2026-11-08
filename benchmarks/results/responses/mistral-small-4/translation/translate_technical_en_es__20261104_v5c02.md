# Mistral Small 4 — translation/translate_technical_en_es

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 8.45 | quality: 8.0
- latency_total: 0.974s | tokens_per_second: 125.3
- input_tokens: 165 | output_tokens: 122
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y añadiendo información útil sobre el manejo de webhooks, aunque no se completó la oración original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el header Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si excede el límite de tasa, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puede reanudar. Los *webhook endpoints* deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se volverá a intentar hasta 3 veces con un *exponential backoff*.