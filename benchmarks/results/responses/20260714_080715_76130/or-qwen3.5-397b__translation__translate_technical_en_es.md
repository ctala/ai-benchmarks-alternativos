# Qwen 3.5 397B — translation/translate_technical_en_es

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 7.1 | quality: 8.0
- latency_total: 47.546s | tokens_per_second: 58.9
- input_tokens: 160 | output_tokens: 2800
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y añadiendo información útil sobre el manejo de webhooks, aunque no se completa la oración original.

## Respuesta completa

Para autenticarse con la API, incluya su token Bearer en el header Authorization. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si excede el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puede reanudar. Los endpoints de Webhook deben responder dentro de 30 segundos o la delivery se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.