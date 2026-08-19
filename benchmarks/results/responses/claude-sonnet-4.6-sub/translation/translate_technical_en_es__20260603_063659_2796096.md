# Claude Sonnet 4.6 (suscripción) — translation/translate_technical_en_es

- model_id: `claude-sonnet-4-6`
- success: True  | final: 7.25 | quality: 8.0
- latency_total: 3.78s | tokens_per_second: 31.2
- input_tokens: 3 | output_tokens: 118
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están configurados en 100 requests por minuto para el tier gratuito. Si excedes el rate limit, la API retorna un status code 429 con un header Retry-After que indica cuándo puedes retomar. Los endpoints webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.