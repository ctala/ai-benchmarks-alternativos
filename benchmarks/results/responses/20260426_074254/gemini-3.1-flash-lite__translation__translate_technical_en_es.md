# Gemini 3.1 Flash Lite — translation/translate_technical_en_es

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 7.75 | quality: 7.72
- latency_total: 0.998s | tokens_per_second: 107.2
- input_tokens: 151 | output_tokens: 107
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el header Authorization. Los rate limits están establecidos en 100 solicitudes por minuto para el plan gratuito. Si excede el rate limit, la API devolverá un código de estado 429 con un header Retry-After que indica cuándo puede reanudar. Los Webhook endpoints deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.