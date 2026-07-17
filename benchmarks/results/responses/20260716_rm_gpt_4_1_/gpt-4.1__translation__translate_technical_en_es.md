# GPT-4.1 — translation/translate_technical_en_es

- model_id: `gpt-4.1`
- success: True  | final: 7.83 | quality: 8.0
- latency_total: 1.604s | tokens_per_second: 64.8
- input_tokens: 150 | output_tokens: 104
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre el manejo de endpoints de webhook, aunque no se completó la oración original.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el encabezado Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si excedes el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder en un máximo de 30 segundos o la entrega será marcada como fallida y se reintentará hasta 3 veces con backoff exponencial.