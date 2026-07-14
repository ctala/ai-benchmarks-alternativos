# Nemotron 3 Nano Omni 30B-A3B Reasoning — translation/translate_technical_en_es

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- success: True  | final: 8.15 | quality: 8.0
- latency_total: 4.211s | tokens_per_second: 166.7
- input_tokens: 166 | output_tokens: 702
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticarse con la API, incluye tu Bearer token en el encabezado Authorization. Los límites de tasa están fijados en 100 solicitudes por minuto para la capa gratuita. Si superas el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puedes reanudar. Los endpoints Webhook deben responder dentro de los 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.