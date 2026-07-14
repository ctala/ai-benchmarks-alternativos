# GLM 5 — translation/translate_technical_en_es

- model_id: `z-ai/glm-5`
- success: True  | final: 7.2 | quality: 8.0
- latency_total: 27.462s | tokens_per_second: 76.9
- input_tokens: 150 | output_tokens: 2113
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con terminos tecnicos mantenidos en ingles. Aunque agrega detalles sobre el tiempo de respuesta de los webhook endpoints, no se especifica en el texto original, lo que reduce ligeramente la profundidad.

## Respuesta completa

Para autenticarse con la API, incluye tu Bearer token en el header Authorization. Los rate limits están establecidos en 100 solicitudes por minuto para el plan gratuito. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After indicando cuándo puedes reanudar. Los webhook endpoints deben responder dentro de 30 segundos o la entrega será marcada como fallida y se reintentará hasta 3 veces con exponential backoff.