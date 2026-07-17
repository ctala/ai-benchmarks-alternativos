# Qwen 3.6 Plus — translation/translate_technical_en_es

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 7.22 | quality: 8.0
- latency_total: 63.983s | tokens_per_second: 54.1
- input_tokens: 160 | output_tokens: 3464
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el Authorization header. Los rate limits están establecidos en 100 solicitudes por minuto para el free tier. Si superas el rate limit, la API devuelve un status code 429 con un Retry-After header que indica cuándo puedes reanudar. Los Webhook endpoints deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.