# Gemini 3.5 Flash — translation/translate_technical_en_es

- model_id: `google/gemini-3.5-flash`
- success: True  | final: 7.52 | quality: 8.0
- latency_total: 2.337s | tokens_per_second: 45.3
- input_tokens: 150 | output_tokens: 106
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con terminos tecnicos mantenidos en ingles y adiciones útiles sobre el manejo de webhooks, aunque la profundidad es moderada.

## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el header de Authorization. Los rate limits están establecidos en 100 requests por minuto para el tier gratuito. Si supera el rate limit, la API devuelve un status code 429 con un header Retry-After que indica cuándo puede reanudar. Los endpoints de los webhooks deben responder dentro de los 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.