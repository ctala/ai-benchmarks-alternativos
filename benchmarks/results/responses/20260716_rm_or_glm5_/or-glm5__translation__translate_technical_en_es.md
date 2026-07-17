# GLM 5 — translation/translate_technical_en_es

- model_id: `z-ai/glm-5`
- success: True  | final: 7.24 | quality: 8.0
- latency_total: 18.877s | tokens_per_second: 91.3
- input_tokens: 157 | output_tokens: 1724
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando detalles adicionales útiles sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están establecidos en 100 peticiones por minuto para el plan gratuito. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After indicando cuándo puedes reanudar. Los endpoints de webhook deben responder dentro de los 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.