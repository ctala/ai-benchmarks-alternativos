# MiniMax M2.5 — translation/translate_technical_en_es

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 7.75 | quality: 8.0
- latency_total: 6.528s | tokens_per_second: 55.9
- input_tokens: 182 | output_tokens: 365
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando detalles adicionales útiles sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header de Authorization. Los rate limits están configurados en 100 solicitudes por minuto para el tier gratuito. Si excedes el rate limit, la API devuelve un código de estado 429 con un header Retry-After indicando cuándo puedes continuar. Los endpoints de webhook deben responder dentro de 30 segundos o la entrega será marcada como fallida y se reintentará hasta 3 veces con exponential backoff.