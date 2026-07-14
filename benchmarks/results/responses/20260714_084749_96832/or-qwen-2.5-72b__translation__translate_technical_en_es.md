# Qwen 2.5 72B — translation/translate_technical_en_es

- model_id: `qwen/qwen-2.5-72b-instruct`
- success: True  | final: 7.85 | quality: 8.0
- latency_total: 3.941s | tokens_per_second: 31.7
- input_tokens: 160 | output_tokens: 125
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con buena claridad y utilidad práctica, aunque la profundidad es solo aceptable.

## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el encabezado Authorization. Los límites de velocidad están establecidos en 100 solicitudes por minuto para el plan gratuito. Si supera el límite de velocidad, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puede reanudar las solicitudes. Los webhook endpoints deben responder dentro de los 30 segundos o la entrega será marcada como fallida y se reintentará hasta 3 veces con un respaldo exponencial.