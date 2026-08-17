# GPT-OSS 20B — translation/translate_technical_en_es

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 8.0 | quality: 8.0
- latency_total: 3.772s | tokens_per_second: 75.6
- input_tokens: 197 | output_tokens: 285
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el encabezado Authorization. Los límites de tasa están establecidos en 100 requests por minuto para el tier gratuito. Si superas el límite, la API devuelve un código de estado 429 con un header Retry-After indicando cuándo puedes reanudar. Los webhook endpoints deben responder dentro de 30 segundos o la entrega se marcará como failed y se reintentará hasta 3 veces con exponential backoff.