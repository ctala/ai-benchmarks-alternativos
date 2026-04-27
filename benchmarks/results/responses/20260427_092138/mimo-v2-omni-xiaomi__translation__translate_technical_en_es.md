# MiMo V2-Omni (Xiaomi direct) — translation/translate_technical_en_es

- model_id: `mimo-v2-omni`
- success: True  | final: 7.45 | quality: 7.72
- latency_total: 4.939s | tokens_per_second: 86.9
- input_tokens: 402 | output_tokens: 429
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si excedes el límite de tasa, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con un backoff exponencial.