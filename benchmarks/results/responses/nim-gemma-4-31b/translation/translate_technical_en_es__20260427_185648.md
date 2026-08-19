# Gemma 4 31B (NIM) — translation/translate_technical_en_es

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 6.95 | quality: 7.72
- latency_total: 274.839s | tokens_per_second: 0.4
- input_tokens: 159 | output_tokens: 111
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el header de Authorization. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si excede el rate limit, la API devolverá un código de estado 429 con un header Retry-After que indica cuándo puede reanudar las solicitudes. Los endpoints de Webhook deben responder en menos de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.