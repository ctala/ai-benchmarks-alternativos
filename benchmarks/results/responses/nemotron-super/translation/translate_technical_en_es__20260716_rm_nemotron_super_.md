# Nemotron 3 Super — translation/translate_technical_en_es

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 7.7 | quality: 8.0
- latency_total: 9.05s | tokens_per_second: 100.0
- input_tokens: 166 | output_tokens: 905
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando detalles adicionales útiles sobre el manejo de webhooks, aunque no profundiza significativamente más allá de la información básica.

## Respuesta completa



Para autenticarse con la API, incluya su Bearer token en el encabezado Authorization. Rate limits están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si supera el Rate limit, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puede reanudar. Los Webhook endpoints deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con retroceso exponencial.