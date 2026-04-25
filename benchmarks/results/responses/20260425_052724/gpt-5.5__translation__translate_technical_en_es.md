# GPT-5.5 — translation/translate_technical_en_es

- model_id: `gpt-5.5`
- success: True  | final: 7.25 | quality: 7.72
- latency_total: 1.619s | tokens_per_second: 62.4
- input_tokens: 149 | output_tokens: 101
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si superas el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puedes reanudar. Los webhook endpoints deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.