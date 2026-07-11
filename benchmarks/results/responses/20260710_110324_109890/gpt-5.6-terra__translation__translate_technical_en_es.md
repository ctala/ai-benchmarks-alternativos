# GPT-5.6 Terra — translation/translate_technical_en_es

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 6.74 | quality: 6.6
- latency_total: 1.937s | tokens_per_second: 54.7
- input_tokens: 149 | output_tokens: 106
- judge_score: 3.0 | justificación: La respuesta es generalmente precisa y relevante, pero añade información no presente en el texto original, afectando la precisión y profundidad.

## Respuesta completa

"Para autenticarte con la API, incluye tu token Bearer en el header Authorization. Los rate limits están configurados en 100 solicitudes por minuto para el plan gratuito. Si superas el rate limit, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff."