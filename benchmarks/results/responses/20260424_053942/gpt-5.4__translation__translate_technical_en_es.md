# GPT-5.4 — translation/translate_technical_en_es

- model_id: `gpt-5.4`
- success: True  | final: 7.55 | quality: 7.72
- latency_total: 1.973s | tokens_per_second: 52.2
- input_tokens: 149 | output_tokens: 103
- judge_score: 3.8 | justificación: 

## Respuesta completa

"Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están configurados en 100 requests por minuto para el plan gratuito. Si excedes el rate limit, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff."