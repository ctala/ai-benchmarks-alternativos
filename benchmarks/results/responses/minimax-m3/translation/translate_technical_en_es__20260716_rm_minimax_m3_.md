# MiniMax M3 — translation/translate_technical_en_es

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.91 | quality: 8.0
- latency_total: 4.893s | tokens_per_second: 106.9
- input_tokens: 317 | output_tokens: 523
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, proporcionando detalles útiles sobre el manejo de límites de tasa y webhooks, aunque no se completó la traducción.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header `Authorization`. Los rate limits están fijados en 100 requests por minuto para el plan gratuito. Si excedes el rate limit, la API devuelve un status code 429 con un header `Retry-After` indicando cuándo puedes continuar. Los webhook endpoints deben responder en menos de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.