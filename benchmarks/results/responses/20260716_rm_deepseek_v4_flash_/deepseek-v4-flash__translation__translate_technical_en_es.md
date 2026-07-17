# DeepSeek V4 Flash (OpenRouter) — translation/translate_technical_en_es

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 7.33 | quality: 8.0
- latency_total: 11.188s | tokens_per_second: 10.4
- input_tokens: 153 | output_tokens: 116
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando detalles adicionales útiles sobre el manejo de webhooks, aunque no se solicitaron explícitamente.

## Respuesta completa

"Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están establecidos en 100 requests por minuto para el plan gratuito. Si excedes el rate limit, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder dentro de los 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff."