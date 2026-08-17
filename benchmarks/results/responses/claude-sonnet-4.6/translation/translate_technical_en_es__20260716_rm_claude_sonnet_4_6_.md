# Claude Sonnet 4.6 (ultimo Anthropic) — translation/translate_technical_en_es

- model_id: `anthropic/claude-sonnet-4-6`
- success: True  | final: 7.38 | quality: 8.0
- latency_total: 2.54s | tokens_per_second: 48.4
- input_tokens: 166 | output_tokens: 123
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con terminos tecnicos mantenidos apropiadamente, y proporciona detalles adicionales útiles sobre el manejo de webhooks, aunque no se completó la sección original.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header de Authorization. Los rate limits están configurados en 100 requests por minuto para el tier gratuito. Si superas el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puedes continuar. Los endpoints de Webhook deben responder en menos de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.