# Step 3.5 Flash (NIM) — translation/translate_technical_en_es

- model_id: `stepfun-ai/step-3.5-flash`
- success: True  | final: 6.9 | quality: 8.0
- latency_total: 23.103s | tokens_per_second: 21.3
- input_tokens: 161 | output_tokens: 493
- judge_score: 4.0 | justificación: 

## Respuesta completa

Para autenticarte con la API, incluye tu Bearer token en el header de Authorization. Los límites de tasa (rate limits) están establecidos en 100 solicitudes por minuto para el nivel gratuito (free tier). Si excedes el límite de tasa, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder en menos de 30 segundos, de lo contrario la entrega se marcará como fallida y se reintentará hasta 3 veces con un reintento exponencial (exponential backoff).