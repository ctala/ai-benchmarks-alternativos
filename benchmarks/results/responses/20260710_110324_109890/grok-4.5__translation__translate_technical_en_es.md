# Grok 4.5 — translation/translate_technical_en_es

- model_id: `x-ai/grok-4.5`
- success: True  | final: 7.21 | quality: 8.0
- latency_total: 10.343s | tokens_per_second: 122.4
- input_tokens: 346 | output_tokens: 1266
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una buena profundidad al añadir detalles sobre el manejo de webhooks, y está claramente escrita y organizada, siendo útil para un emprendedor.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el Authorization header. Los rate limits están configurados en 100 requests por minuto para el free tier. Si excedes el rate limit, la API devuelve un 429 status code con un Retry-After header que indica cuándo puedes reanudar. Los webhook endpoints deben responder dentro de 30 segundos o la delivery se marcará como failed y se reintentará hasta 3 veces con exponential backoff.