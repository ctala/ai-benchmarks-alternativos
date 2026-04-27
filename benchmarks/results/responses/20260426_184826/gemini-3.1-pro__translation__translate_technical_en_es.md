# Gemini 3.1 Pro — translation/translate_technical_en_es

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 6.5 | quality: 7.72
- latency_total: 16.644s | tokens_per_second: 113.7
- input_tokens: 151 | output_tokens: 1892
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están establecidos en 100 peticiones por minuto para el plan gratuito. Si excedes el rate limit, la API devuelve un código de estado 429 con un header Retry-After indicando cuándo puedes reanudar. Los endpoints del webhook deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.