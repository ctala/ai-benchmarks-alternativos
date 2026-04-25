# Kimi K2.6 — translation/translate_technical_en_es

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 6.3 | quality: 7.72
- latency_total: 71.843s | tokens_per_second: 43.3
- input_tokens: 157 | output_tokens: 3114
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están establecidos en 100 solicitudes por minuto para el free tier. Si excedes el rate limit, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder dentro de 30 segundos o la entrega será marcada como fallida y se reintentará hasta 3 veces con exponential backoff.