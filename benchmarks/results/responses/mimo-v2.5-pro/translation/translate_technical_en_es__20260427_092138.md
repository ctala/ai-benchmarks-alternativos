# MiMo V2.5-Pro (Xiaomi) — translation/translate_technical_en_es

- model_id: `mimo-v2.5-pro`
- success: True  | final: 7.45 | quality: 8.0
- latency_total: 3.789s | tokens_per_second: 35.4
- input_tokens: 403 | output_tokens: 134
- judge_score: 4.0 | justificación: 

## Respuesta completa

"Para autenticarse con la API, incluye tu Bearer token en el header Authorization. Los rate limits están establecidos en 100 requests por minuto para el tier gratuito. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After indicando cuándo puedes reanudar. Los endpoints de webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff."