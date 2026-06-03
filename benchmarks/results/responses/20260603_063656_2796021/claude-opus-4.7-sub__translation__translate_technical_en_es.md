# Claude Opus 4.7 (suscripción) — translation/translate_technical_en_es

- model_id: `claude-opus-4-7`
- success: True  | final: 7.03 | quality: 8.0
- latency_total: 3.67s | tokens_per_second: 45.2
- input_tokens: 6 | output_tokens: 166
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están configurados en 100 requests por minuto para el tier gratuito. Si excedes el rate limit, la API retorna un status code 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder en menos de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.