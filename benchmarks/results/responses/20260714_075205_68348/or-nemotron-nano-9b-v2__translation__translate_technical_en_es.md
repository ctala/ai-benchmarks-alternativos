# Nemotron Nano 9B v2 — translation/translate_technical_en_es

- model_id: `nvidia/nemotron-nano-9b-v2:free`
- success: True  | final: 7.62 | quality: 8.0
- latency_total: 12.857s | tokens_per_second: 37.9
- input_tokens: 162 | output_tokens: 487
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, proporcionando detalles adicionales útiles sobre el manejo de webhooks, lo que la hace muy útil para un emprendedor.

## Respuesta completa



Para autenticarse con la API, incluya su token Bearer en el encabezado Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para la versión gratuita. Si excede el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puede reanudar. Los endpoints de webhook deben responder en 30 segundos o la entrega será marcada como fallida y se reintentarán hasta 3 veces con backoff exponencial.
