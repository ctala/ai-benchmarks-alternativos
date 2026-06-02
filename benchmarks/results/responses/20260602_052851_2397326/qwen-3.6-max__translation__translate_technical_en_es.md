# Qwen 3.6 Max — translation/translate_technical_en_es

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 6.44 | quality: 8.0
- latency_total: 62.136s | tokens_per_second: 42.9
- input_tokens: 160 | output_tokens: 2665
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre el manejo de webhooks, aunque no se solicitaron detalles adicionales.

## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el Authorization header. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si supera el rate limit, la API devuelve un 429 status code con un Retry-After header que indica cuándo puede reanudar. Los Webhook endpoints deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.