# MiMo-V2.5 Pro — translation/translate_technical_en_es

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 7.48 | quality: 8.0
- latency_total: 6.154s | tokens_per_second: 55.6
- input_tokens: 403 | output_tokens: 342
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una claridad excepcional, aunque la profundidad es solo aceptable debido a la falta de información adicional sobre el manejo de webhooks.

## Respuesta completa

Para autenticarse con la API, incluye tu token Bearer en el header Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si excedes el límite de tasa, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con retroceso exponencial.