# DeepSeek V4 Pro — translation/translate_technical_en_es

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 7.7 | quality: 8.0
- latency_total: 4.894s | tokens_per_second: 23.1
- input_tokens: 153 | output_tokens: 113
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre los endpoints de webhook, aunque no se solicitaron detalles adicionales.

## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el header Authorization. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si excede el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puede reanudar. Los endpoints de webhook deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.