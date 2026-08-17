# Kimi K2.6 — translation/translate_technical_en_es

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 6.9 | quality: 7.72
- latency_total: 23.589s | tokens_per_second: 47.9
- input_tokens: 157 | output_tokens: 1130
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si excedes el rate limit, la API retorna un status code 429 con un header Retry-After que indica cuándo puedes reanudar. Los webhook endpoints deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.