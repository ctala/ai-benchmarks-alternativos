# Nemotron Nano 9B v2 — translation/translate_technical_en_es

- model_id: `nvidia/nemotron-nano-9b-v2:free`
- success: True  | final: 7.33 | quality: 8.0
- latency_total: 70.558s | tokens_per_second: 11.6
- input_tokens: 162 | output_tokens: 815
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y añadiendo información útil sobre el manejo de webhooks, aunque no se especifica en el texto original.

## Respuesta completa

Para autenticar con la API, incluya su token Bearer en el encabezado de autorización. Los límites de tasa están establecidos en 100 solicitudes por minuto para la versión gratuita. Si supera el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After indicando cuándo puede reanudar. Los puntos finales de webhook deben responder dentro de 30 segundos, de lo contrario, la entrega se marcará como fallida y se reintentará hasta 3 veces con retroceso exponencial.
