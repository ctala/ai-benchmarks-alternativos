# Nemotron 3 Nano Omni 30B-A3B Reasoning — translation/translate_technical_en_es

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- success: True  | final: 7.8 | quality: 8.0
- latency_total: 6.005s | tokens_per_second: 237.5
- input_tokens: 166 | output_tokens: 1426
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando detalles útiles sobre el manejo de límites de tasa y webhooks, aunque la profundidad podría mejorarse con más contexto o ejemplos.

## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el Authorization header. Los límites de tasa están establecidos en 100 solicitudes por minuto para el plan gratuito. Si supera el rate limit, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puede reanudar. Los webhook endpoints deben responder dentro de 30 seconds o la entrega se marcará como failed y se reintentará hasta 3 veces con exponential backoff.