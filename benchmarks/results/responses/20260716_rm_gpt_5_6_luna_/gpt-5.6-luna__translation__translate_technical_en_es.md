# GPT-5.6 Luna — translation/translate_technical_en_es

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 7.86 | quality: 8.0
- latency_total: 1.452s | tokens_per_second: 89.6
- input_tokens: 149 | output_tokens: 130
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando detalles útiles sobre el manejo de límites de tasa y webhooks, aunque la profundidad podría mejorarse con más contexto o ejemplos.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header `Authorization`. Los límites de solicitudes están establecidos en 100 requests por minuto para el free tier. Si superas el rate limit, la API devuelve un status code 429 con un header `Retry-After` que indica cuándo puedes reanudar las solicitudes. Los endpoints de webhook deben responder en un plazo de 30 segundos; de lo contrario, la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.