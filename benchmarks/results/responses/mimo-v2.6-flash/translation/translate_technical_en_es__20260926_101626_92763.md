# MiMo V2.6 Flash — translation/translate_technical_en_es

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 7.07 | quality: 6.88
- latency_total: 3.856s | tokens_per_second: 34.0
- input_tokens: 159 | output_tokens: 131
- judge_score: 3.2 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. El rate limit se establece en 100 requests por minuto en el tier gratuito. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puedes reanudar. Los webhook endpoints deben responder en un plazo de 30 segundos o el delivery se marcará como fallido y se reintentará hasta 3 veces con exponential backoff.