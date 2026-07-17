# Mistral Large 3 675B — translation/translate_technical_en_es

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 7.82 | quality: 8.0
- latency_total: 2.485s | tokens_per_second: 48.3
- input_tokens: 153 | output_tokens: 120
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con buena claridad y utilidad práctica, aunque la profundidad es solo aceptable debido a la adición de detalles no presentes en el texto original.

## Respuesta completa

"Para autenticarte con la API, incluye tu token Bearer en el encabezado Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para el plan gratuito. Si excedes el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con un backoff exponencial."