# Claude Haiku 4.5 (suscripción) — translation/translate_technical_en_es

- model_id: `claude-haiku-4-5`
- success: True  | final: 7.43 | quality: 8.0
- latency_total: 3.865s | tokens_per_second: 147.2
- input_tokens: 10 | output_tokens: 569
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando detalles adicionales útiles sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header de Authorization. Los rate limits se establecen en 100 solicitudes por minuto para el tier gratuito. Si excedes el rate limit, la API devuelve un código de estado 429 con un header Retry-After indicando cuándo puedes reanudar. Los endpoints de Webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.