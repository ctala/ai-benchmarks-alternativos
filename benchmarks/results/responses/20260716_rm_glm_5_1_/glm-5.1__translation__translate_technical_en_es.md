# GLM-5.1 — translation/translate_technical_en_es

- model_id: `z-ai/glm-5.1`
- success: True  | final: 7.28 | quality: 8.0
- latency_total: 15.515s | tokens_per_second: 115.0
- input_tokens: 150 | output_tokens: 1785
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con terminos tecnicos mantenidos apropiadamente, y proporciona detalles adicionales útiles sobre el manejo de webhooks, aunque no profundiza en aspectos más complejos.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están configurados en 100 requests por minuto para el plan gratuito. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puedes reanudar. Los webhook endpoints deben responder en 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.