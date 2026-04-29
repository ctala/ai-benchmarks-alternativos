# GLM 5 (NIM) — translation/translate_technical_en_es

- model_id: `z-ai/glm5`
- success: True  | final: 6.95 | quality: 7.72
- latency_total: 23.43s | tokens_per_second: 4.6
- input_tokens: 151 | output_tokens: 108
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los límites de tasa están configurados en 100 solicitudes por minuto para el free tier. Si excedes el límite de tasa, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder en 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.