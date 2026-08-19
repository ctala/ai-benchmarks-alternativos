# KAT Coder Pro v2.5 — translation/translate_technical_en_es

- model_id: `kwaipilot/kat-coder-pro-v2.5`
- success: True  | final: 8.16 | quality: 8.84
- latency_total: 5.937s | tokens_per_second: 104.1
- input_tokens: 160 | output_tokens: 618
- judge_score: 4.6 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa



Para autenticarse con la API, incluya su Bearer token en el header Authorization. Los rate limits están configurados en 100 solicitudes por minuto para el free tier. Si excede el rate limit, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puede reanudar. Los endpoints de Webhook deben responder dentro de los 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.