# Grok 4.5 — translation/translate_technical_en_es

- model_id: `x-ai/grok-4.5`
- success: True  | final: 7.19 | quality: 8.0
- latency_total: 10.487s | tokens_per_second: 135.4
- input_tokens: 346 | output_tokens: 1420
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información útil sobre la respuesta de los endpoints de webhook, aunque no se completó la oración original.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el Authorization header. Los rate limits se establecen en 100 requests por minuto para el free tier. Si excedes el rate limit, la API devuelve un 429 status code con un Retry-After header indicando cuándo puedes reanudar. Los webhook endpoints deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.