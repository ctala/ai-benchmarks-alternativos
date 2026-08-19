# DeepSeek V4 Flash (OpenRouter) — translation/translate_technical_en_es

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 7.95 | quality: 8.0
- latency_total: 7.076s | tokens_per_second: 110.7
- input_tokens: 153 | output_tokens: 783
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una claridad excepcional, aunque la profundidad es solo aceptable debido a la adición de detalles no solicitados sobre el manejo de webhooks.

## Respuesta completa

Para autenticarte con la API, incluye tu token Bearer en el header Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si excedes el límite de tasa, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder dentro de 30 segundos, de lo contrario la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.