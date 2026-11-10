# GPT-OSS 120B — translation/translate_technical_en_es

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.29 | quality: 8.2
- latency_total: 2.793s | tokens_per_second: 138.5
- input_tokens: 210 | output_tokens: 387
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre el manejo de webhooks, aunque no se requiere en la instrucción original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarse con la API, incluya su **Bearer token** en el **Authorization header**. Los **rate limits** están fijados en 100 solicitudes por minuto para el **free tier**. Si supera el límite, la API devuelve un **status code** 429 con un **Retry-After header** que indica cuándo puede reanudar. Los **webhook endpoints** deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con **exponential backoff**.