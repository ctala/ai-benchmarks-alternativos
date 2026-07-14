# GLM 5.2 — translation/translate_technical_en_es

- model_id: `z-ai/glm-5.2`
- success: True  | final: 6.26 | quality: 6.6
- latency_total: 14.025s | tokens_per_second: 76.6
- input_tokens: 157 | output_tokens: 1074
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante, pero añade información no solicitada sobre el tiempo de respuesta de los endpoints de Webhook, lo que afecta la precisión y profundidad.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en la cabecera Authorization. Los rate limits están establecidos en 100 peticiones por minuto para el plan gratuito. Si excedes el rate limit, la API devuelve un código de estado 429 con una cabecera Retry-After que indica cuándo puedes continuar. Los endpoints de Webhook deben responder en un máximo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con un backoff exponencial.