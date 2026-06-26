# Kimi K2.7 Code — translation/translate_technical_en_es

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 6.98 | quality: 7.72
- latency_total: 8.291s | tokens_per_second: 38.7
- input_tokens: 157 | output_tokens: 321
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticarte con la API, incluye tu token Bearer en el header `Authorization`. Los rate limits están configurados en 100 requests por minuto para el free tier. Si excedes el rate limit, la API devuelve un status code `429` con un header `Retry-After` que indica cuándo puedes reanudar. Los webhook endpoints deben responder en menos de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.