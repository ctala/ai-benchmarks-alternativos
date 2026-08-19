# MiMo-V2.5 (omnimodal) — translation/translate_technical_en_es

- model_id: `xiaomi/mimo-v2.5`
- success: True  | final: 7.15 | quality: 7.72
- latency_total: 4.968s | tokens_per_second: 72.3
- input_tokens: 399 | output_tokens: 359
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el Authorization header. Los límites de tasa se establecen en 100 solicitudes por minuto para el nivel gratuito. Si excedes el límite de tasa, la API devuelve un 429 status code con un Retry-After header que indica cuándo puedes reanudar. Los Webhook endpoints deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con backoff exponencial.