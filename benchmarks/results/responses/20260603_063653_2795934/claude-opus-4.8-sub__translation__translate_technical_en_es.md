# Claude Opus 4.8 (suscripción) — translation/translate_technical_en_es

- model_id: `claude-opus-4-8`
- success: True  | final: 6.71 | quality: 8.0
- latency_total: 3.839s | tokens_per_second: 42.7
- input_tokens: 2026 | output_tokens: 164
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando detalles adicionales útiles sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están configurados en 100 requests por minuto para el tier gratuito. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puedes reanudar. Los webhook endpoints deben responder en menos de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.