# Claude Fable 5 — translation/translate_technical_en_es

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 5.94 | quality: 6.6
- latency_total: 6.229s | tokens_per_second: 30.0
- input_tokens: 239 | output_tokens: 187
- judge_score: 3.0 | justificación: La respuesta es generalmente precisa y relevante, pero añade información no solicitada sobre el tiempo de respuesta de los webhooks y los reintentos, lo que no está en el texto original.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los límites de rate limit están establecidos en 100 requests por minuto para el tier gratuito. Si excedes el rate limit, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhooks deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.