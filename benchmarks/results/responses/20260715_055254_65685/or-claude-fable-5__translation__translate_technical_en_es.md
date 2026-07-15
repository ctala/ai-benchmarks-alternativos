# Claude Fable 5 — translation/translate_technical_en_es

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 6.47 | quality: 8.0
- latency_total: 37.799s | tokens_per_second: 4.8
- input_tokens: 239 | output_tokens: 183
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando detalles adicionales útiles sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están configurados en 100 requests por minuto para el plan gratuito. Si excedes el rate limit, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhooks deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.