# Grok 4.3 — translation/translate_technical_en_es

- model_id: `x-ai/grok-4.3`
- success: True  | final: 7.5 | quality: 8.0
- latency_total: 7.296s | tokens_per_second: 127.7
- input_tokens: 332 | output_tokens: 932
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con una buena profundidad al añadir detalles sobre el manejo de webhooks, lo que la hace útil para un emprendedor.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits se establecen en 100 requests por minuto para el free tier. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After indicando cuándo puedes reanudar. Los endpoints de webhook deben responder dentro de 30 segundos o la delivery será marcada como fallida y reintentada hasta 3 veces con exponential backoff.