# Claude Opus 4.6 — translation/translate_technical_en_es

- model_id: `anthropic/claude-opus-4-6`
- success: True  | final: 7.25 | quality: 7.44
- latency_total: 3.423s | tokens_per_second: 37.1
- input_tokens: 166 | output_tokens: 127
- judge_score: 3.6 | justificación: 

## Respuesta completa

Para autenticarse con la API, incluye tu Bearer token en el header Authorization. Los rate limits están configurados en 100 requests por minuto para el tier gratuito. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puedes reanudar las solicitudes. Los endpoints de webhook deben responder en un máximo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.