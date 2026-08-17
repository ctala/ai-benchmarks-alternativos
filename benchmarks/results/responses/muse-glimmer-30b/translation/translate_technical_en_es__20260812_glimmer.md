# Muse Glimmer 30B — translation/translate_technical_en_es

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 7.47 | quality: 8.0
- latency_total: 10.454s | tokens_per_second: 61.0
- input_tokens: 197 | output_tokens: 638
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante, y clara, proporcionando detalles útiles sobre la autenticación y manejo de límites de tasa, con una buena profundidad en la explicación de los webhooks.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el Authorization header. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si excedes el rate limit, la API devuelve un 429 status code con un Retry-After header indicando cuándo puedes reanudar. Los webhook endpoints deben responder dentro de 30 segundos o la entrega será marcada como failed y reintentada hasta 3 veces con exponential backoff.