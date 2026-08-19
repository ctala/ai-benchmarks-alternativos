# Claude Haiku 4.5 — translation/translate_technical_en_es

- model_id: `anthropic/claude-haiku-4.5`
- success: True  | final: 7.89 | quality: 8.0
- latency_total: 1.897s | tokens_per_second: 68.0
- input_tokens: 166 | output_tokens: 129
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticarse con la API, incluye tu Bearer token en el header de Authorization. Los límites de velocidad están configurados en 100 solicitudes por minuto para el tier gratuito. Si excedes el límite de velocidad, la API devuelve un código de estado 429 con un header Retry-After indicando cuándo puedes reanudar. Los endpoints de webhook deben responder en 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.