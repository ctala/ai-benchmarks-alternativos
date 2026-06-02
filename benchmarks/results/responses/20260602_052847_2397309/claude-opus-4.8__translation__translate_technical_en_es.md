# Claude Opus 4.8 — translation/translate_technical_en_es

- model_id: `anthropic/claude-opus-4.8`
- success: True  | final: 7.11 | quality: 8.0
- latency_total: 3.172s | tokens_per_second: 53.0
- input_tokens: 239 | output_tokens: 168
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando detalles útiles sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están establecidos en 100 requests por minuto para el tier gratuito. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.