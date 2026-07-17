# MiniMax M2.7 — translation/translate_technical_en_es

- model_id: `minimax/minimax-m2.7`
- success: True  | final: 7.4 | quality: 8.0
- latency_total: 14.736s | tokens_per_second: 78.2
- input_tokens: 182 | output_tokens: 1152
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando información adicional útil sobre el manejo de webhooks, aunque no se requiere en la instrucción original.

## Respuesta completa

Para autenticarte con la API, incluye tu token Bearer en el header Authorization. Los rate limits están establecidos en 100 solicitudes por minuto para el tier gratuito. Si excedes el rate limit, la API devuelve un código de estado 429 con un header Retry‑After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder en un plazo de 30 segundos; de lo contrario, la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.