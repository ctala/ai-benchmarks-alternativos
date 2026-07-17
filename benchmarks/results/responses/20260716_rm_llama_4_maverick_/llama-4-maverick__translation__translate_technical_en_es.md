# Llama 4 Maverick — translation/translate_technical_en_es

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 7.85 | quality: 8.0
- latency_total: 3.3s | tokens_per_second: 31.8
- input_tokens: 151 | output_tokens: 105
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con buena claridad y utilidad práctica, aunque la profundidad es solo aceptable debido a la adición de detalles no solicitados sobre el tiempo de respuesta de los webhooks.

## Respuesta completa

"Para autenticar con la API, incluya su token Bearer en el encabezado Authorization. Los límites de velocidad están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si supera el límite de velocidad, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puede reanudar. Los endpoint de webhook deben responder dentro de los 30 segundos o la entrega se marcará como fallida y se volverá a intentar hasta 3 veces con retroceso exponencial."