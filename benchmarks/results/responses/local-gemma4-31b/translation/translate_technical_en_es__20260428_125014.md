# Gemma 4 31B (DGX Spark Q4_K_M) — translation/translate_technical_en_es

- model_id: `gemma4:31b`
- success: True  | final: 6.4 | quality: 7.72
- latency_total: 187.838s | tokens_per_second: 9.3
- input_tokens: 166 | output_tokens: 1753
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el header de Authorization. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si excede el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puede reanudar. Los endpoints de Webhook deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.