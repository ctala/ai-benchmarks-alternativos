# Claude Fable 5 (suscripción) — translation/translate_technical_en_es

- model_id: `claude-fable-5`
- success: True  | final: 6.84 | quality: 8.0
- latency_total: 4.485s | tokens_per_second: 37.7
- input_tokens: 2 | output_tokens: 169

## Respuesta completa

"Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están configurados en 100 requests por minuto para el tier gratuito. Si excedes el rate limit, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhooks deben responder en menos de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff."