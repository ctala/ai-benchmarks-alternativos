# Qwen 3.5 397B — translation/translate_technical_en_es

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 6.99 | quality: 8.0
- latency_total: 70.51s | tokens_per_second: 68.6
- input_tokens: 160 | output_tokens: 4834
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el Authorization header. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si excede el rate limit, la API devuelve un status code 429 con un Retry-After header indicando cuándo puede reanudar. Los Webhook endpoints deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.