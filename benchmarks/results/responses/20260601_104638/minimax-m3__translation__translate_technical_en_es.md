# MiniMax M3 — translation/translate_technical_en_es

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.25 | quality: 8.0
- latency_total: 13.222s | tokens_per_second: 41.3
- input_tokens: 317 | output_tokens: 546
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando detalles adicionales útiles sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están configurados en 100 requests por minuto para el free tier. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After indicando cuándo puedes reanudar. Los endpoints de webhook deben responder dentro de 30 segundos o la entrega será marcada como fallida y se reintentará hasta 3 veces con exponential backoff.