# Qwen 3.7 Max — translation/translate_technical_en_es

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 6.57 | quality: 7.72
- latency_total: 15.221s | tokens_per_second: 71.5
- input_tokens: 160 | output_tokens: 1089
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticarte con la API, incluye tu token Bearer en el header Authorization. Los rate limits están establecidos en 100 solicitudes por minuto para el plan gratuito. Si superas el rate limit, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder en un máximo de 30 segundos; de lo contrario, la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.