# Grok 4.3 — translation/translate_technical_en_es

- model_id: `x-ai/grok-4.3`
- success: True  | final: 7.51 | quality: 8.0
- latency_total: 7.406s | tokens_per_second: 121.4
- input_tokens: 271 | output_tokens: 899

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el Authorization header. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si excedes el rate limit, la API devuelve un status code 429 con un Retry-After header indicando cuándo puedes reanudar. Los webhook endpoints deben responder dentro de 30 segundos o la entrega será marcada como fallida y se reintentará hasta 3 veces con exponential backoff.