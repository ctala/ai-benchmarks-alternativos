# MiMo V2-Pro (Xiaomi direct) — translation/translate_technical_en_es

- model_id: `mimo-v2-pro`
- success: True  | final: 7.25 | quality: 7.72
- latency_total: 8.522s | tokens_per_second: 36.5
- input_tokens: 401 | output_tokens: 311
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticarse con la API, incluya su token Bearer en el header Authorization. Los rate limits están establecidos en 100 solicitudes por minuto para la capa gratuita. Si excede el rate limit, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puede reanudar. Los endpoints de webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.