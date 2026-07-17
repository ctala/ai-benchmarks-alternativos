# GPT-4.1 Mini — translation/translate_technical_en_es

- model_id: `gpt-4.1-mini`
- success: True  | final: 7.84 | quality: 8.0
- latency_total: 2.607s | tokens_per_second: 39.5
- input_tokens: 150 | output_tokens: 103
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre el manejo de webhooks, aunque no se especifica en el texto original.

## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el header Authorization. Los límites de tasa están establecidos en 100 requests por minuto para el plan gratuito. Si excede el límite de tasa, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puede reanudar. Los endpoints de webhook deben responder en un máximo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con backoff exponencial.