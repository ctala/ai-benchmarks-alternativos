# DeepSeek V4 Flash (NIM) — translation/translate_technical_en_es

- model_id: `deepseek-ai/deepseek-v4-flash`
- success: True  | final: 7.45 | quality: 8.0
- latency_total: 3.185s | tokens_per_second: 39.9
- input_tokens: 153 | output_tokens: 127
- judge_score: 4.0 | justificación: 

## Respuesta completa

"Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los límites de tasa (rate limits) están configurados en 100 solicitudes por minuto para el plan gratuito. Si excedes el rate limit, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder dentro de los 30 segundos, de lo contrario la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff."