# MiMo-V2-Omni (multimodal) — translation/translate_technical_en_es

- model_id: `xiaomi/mimo-v2-omni`
- success: True  | final: 7.05 | quality: 7.72
- latency_total: 6.645s | tokens_per_second: 72.8
- input_tokens: 402 | output_tokens: 484
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los límites de tasa se establecen en 100 solicitudes por minuto para el nivel gratuito. Si excedes el límite de tasa, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los Webhook endpoints deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.