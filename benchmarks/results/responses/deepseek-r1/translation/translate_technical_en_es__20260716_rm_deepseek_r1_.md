# DeepSeek R1 (reasoning) — translation/translate_technical_en_es

- model_id: `deepseek/deepseek-r1`
- success: True  | final: 6.92 | quality: 8.0
- latency_total: 46.569s | tokens_per_second: 13.6
- input_tokens: 152 | output_tokens: 633
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando detalles adicionales útiles sobre el manejo de webhooks, aunque no se completó la oración original.

## Respuesta completa

Para autenticarse con la API, incluya su token Bearer en el encabezado Authorization. Los límites de frecuencia están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si excede el límite de frecuencia, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puede reanudar. Los endpoints de webhook deben responder en 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.