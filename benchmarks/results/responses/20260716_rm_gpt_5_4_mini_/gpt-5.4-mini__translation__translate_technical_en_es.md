# GPT-5.4 Mini — translation/translate_technical_en_es

- model_id: `gpt-5.4-mini`
- success: True  | final: 8.14 | quality: 8.0
- latency_total: 1.321s | tokens_per_second: 75.7
- input_tokens: 149 | output_tokens: 100
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con buena claridad y utilidad práctica, aunque la profundidad es solo aceptable debido a la falta de detalles adicionales sobre el manejo de webhooks.

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están establecidos en 100 requests por minuto para el plan free tier. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puedes reanudar. Los webhook endpoints deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.