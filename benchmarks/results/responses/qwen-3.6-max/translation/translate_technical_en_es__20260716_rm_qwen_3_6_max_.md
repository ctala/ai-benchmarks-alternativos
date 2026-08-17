# Qwen 3.6 Max — translation/translate_technical_en_es

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 6.77 | quality: 8.0
- latency_total: 57.857s | tokens_per_second: 46.2
- input_tokens: 160 | output_tokens: 2672
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y añadiendo detalles útiles sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están fijados en 100 requests por minuto para el free tier. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puedes reanudar. Los Webhook endpoints deben responder en un plazo de 30 segundos o la delivery se marcará como failed y se reintentará hasta 3 veces con exponential backoff.