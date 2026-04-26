# MiMo-V2.5 Pro — translation/translate_technical_en_es

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 7.05 | quality: 7.72
- latency_total: 7.607s | tokens_per_second: 58.1
- input_tokens: 403 | output_tokens: 442
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header de Authorization. Los rate limits están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si excedes el rate limit, la API devuelve un código de estado 429 con un header Retry-After indicando cuándo puedes reanudar. Los webhook endpoints deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.