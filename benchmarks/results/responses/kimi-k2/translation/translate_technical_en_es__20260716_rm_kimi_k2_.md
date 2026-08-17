# Kimi K2 — translation/translate_technical_en_es

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 7.85 | quality: 8.0
- latency_total: 3.428s | tokens_per_second: 33.0
- input_tokens: 159 | output_tokens: 113
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticar con la API, incluye tu Bearer token en el header Authorization. Los rate limits están configurados en 100 requests por minuto para el tier gratuito. Si excedes el rate limit, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los webhook endpoints deben responder en 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.