# Gemma 4 12B (Spark llama-server, reasoning) — translation/translate_technical_en_es

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 7.02 | quality: 7.72
- latency_total: 61.879s | tokens_per_second: 25.8
- input_tokens: 166 | output_tokens: 1597
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticarse con la API, incluye tu Bearer token en el header de Authorization. Los rate limits se establecen en 100 solicitudes por minuto para el free tier. Si excedes el rate limit, la API devuelve un código de estado 429 con un header Retry-After indicando cuándo puedes reanudar. Los endpoints de Webhook deben responder en menos de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.