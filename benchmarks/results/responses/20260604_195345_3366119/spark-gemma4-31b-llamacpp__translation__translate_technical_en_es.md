# Gemma 4 31B (Spark llama-server Q4_K_M) — translation/translate_technical_en_es

- model_id: `gemma-4-31B-it-Q4_K_M.gguf`
- success: True  | final: 6.93 | quality: 7.72
- latency_total: 11.866s | tokens_per_second: 9.2
- input_tokens: 163 | output_tokens: 109
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el header de Authorization. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si excede el rate limit, la API devolverá un status code 429 con un header Retry-After que indica cuándo puede reintentar. Los endpoints de Webhook deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.