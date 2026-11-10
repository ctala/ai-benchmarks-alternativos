# Gemini 3.1 Flash Lite (GA) — translation/translate_technical_en_es

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 8.15 | quality: 8.0
- latency_total: 1.248s | tokens_per_second: 84.9
- input_tokens: 150 | output_tokens: 106
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre el manejo de webhooks, aunque no se solicita explícitamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el header Authorization. Los rate limits están establecidos en 100 requests por minuto para el nivel gratuito. Si excede el rate limit, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puede reanudar. Los Webhook endpoints deben responder en un plazo de 30 segundos o el envío se marcará como fallido y se reintentará hasta 3 veces con exponential backoff.