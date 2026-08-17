# Qwen 3-Next 80B Instruct — translation/translate_technical_en_es

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 8.15 | quality: 8.0
- latency_total: 1.559s | tokens_per_second: 82.7
- input_tokens: 160 | output_tokens: 129
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una claridad excepcional, aunque la profundidad es solo aceptable debido a la falta de detalles adicionales sobre el manejo de errores o configuraciones avanzadas.

## Respuesta completa

Para autenticarte con la API, incluye tu token Bearer en el encabezado Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para el plan gratuito. Si superas el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puedes reanudar. Los endpoints de Webhook deben responder dentro de 30 segundos, de lo contrario la entrega se marcará como fallida y se reintentará hasta 3 veces con backoff exponencial.