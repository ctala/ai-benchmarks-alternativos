# Gemini 2.5 Flash — translation/translate_technical_en_es

- model_id: `google/gemini-2.5-flash`
- success: True  | final: 7.55 | quality: 7.72
- latency_total: 1.406s | tokens_per_second: 74.7
- input_tokens: 151 | output_tokens: 105
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el Authorization header. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si excede el rate limit, la API devuelve un status code 429 con un Retry-After header indicando cuándo puede reanudar. Los webhook endpoints deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.