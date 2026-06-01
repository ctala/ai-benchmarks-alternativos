# DeepSeek V4 Flash (OpenRouter) — translation/translate_technical_en_es

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 7.56 | quality: 8.0
- latency_total: 27.492s | tokens_per_second: 38.9
- input_tokens: 153 | output_tokens: 1069
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y añadiendo información útil sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticarse con la API, incluya su token Bearer en el encabezado Authorization. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si excede el rate limit, la API devuelve un código de estado 429 con un encabezado Retry-After indicando cuándo puede reanudar. Los webhook endpoints deben responder dentro de 30 segundos, de lo contrario, la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.