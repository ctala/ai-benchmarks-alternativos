# Grok 4.1 Fast — translation/translate_technical_en_es

- model_id: `x-ai/grok-4.1-fast`
- success: True  | final: 7.55 | quality: 8.0
- latency_total: 5.766s | tokens_per_second: 156.4
- input_tokens: 297 | output_tokens: 902
- judge_score: 4.0 | justificación: 

## Respuesta completa

Para autenticarte con la API, incluye tu token Bearer en la cabecera Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si excedes el límite de tasa, la API devuelve un código de estado 429 con una cabecera Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con backoff exponencial.