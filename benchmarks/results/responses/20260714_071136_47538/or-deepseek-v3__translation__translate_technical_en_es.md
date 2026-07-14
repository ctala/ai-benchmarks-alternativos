# DeepSeek V3 — translation/translate_technical_en_es

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 7.55 | quality: 8.0
- latency_total: 6.362s | tokens_per_second: 18.9
- input_tokens: 162 | output_tokens: 120
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una claridad excepcional y utilidad práctica, aunque la profundidad es solo aceptable.

## Respuesta completa

Para autenticarse con la API, incluya su token Bearer en el encabezado Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si excede el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puede reanudar. Los endpoints de webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con retroceso exponencial.