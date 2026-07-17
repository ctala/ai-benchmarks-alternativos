# Claude Opus 4.7 — translation/translate_technical_en_es

- model_id: `anthropic/claude-opus-4-7`
- success: True  | final: 7.37 | quality: 8.0
- latency_total: 2.994s | tokens_per_second: 56.1
- input_tokens: 244 | output_tokens: 168
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo terminos tecnicos en ingles y proporcionando detalles adicionales útiles sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están establecidos en 100 requests por minuto para el tier gratuito. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder en menos de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.