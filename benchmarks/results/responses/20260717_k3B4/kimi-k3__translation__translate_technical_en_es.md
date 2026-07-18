# Kimi K3 — translation/translate_technical_en_es

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 6.71 | quality: 8.0
- latency_total: 42.301s | tokens_per_second: 35.8
- input_tokens: 235 | output_tokens: 1516
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con terminos tecnicos mantenidos en ingles y adiciones útiles sobre el manejo de webhooks, aunque la profundidad es moderada.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puedes reanudar las requests. Los endpoints de webhook deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.