# Gemini 2.5 Flash Lite — translation/translate_technical_en_es

- model_id: `google/gemini-2.5-flash-lite`
- success: True  | final: 7.85 | quality: 8.0
- latency_total: 2.472s | tokens_per_second: 43.7
- input_tokens: 150 | output_tokens: 108
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el header de Authorization. Los límites de tasa se establecen en 100 requests por minuto para el free tier. Si excede el límite de tasa, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puede reanudar. Los Webhook endpoints deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.