# MiMo V2.5 (Xiaomi) — translation/translate_technical_en_es

- model_id: `mimo-v2.5`
- success: True  | final: 7.45 | quality: 8.0
- latency_total: 5.031s | tokens_per_second: 69.4
- input_tokens: 399 | output_tokens: 349
- judge_score: 4.0 | justificación: 

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los límites de tasa se establecen en 100 solicitudes por minuto para el nivel gratuito. Si excedes el límite de tasa, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.