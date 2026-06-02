# Gemini 3.5 Flash — translation/translate_technical_en_es

- model_id: `google/gemini-3.5-flash`
- success: True  | final: 6.88 | quality: 8.0
- latency_total: 8.472s | tokens_per_second: 167.1
- input_tokens: 150 | output_tokens: 1416
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre el manejo de webhooks, aunque no se solicita explícitamente.

## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el header Authorization. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si excede el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puede reanudar. Los webhook endpoints deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.