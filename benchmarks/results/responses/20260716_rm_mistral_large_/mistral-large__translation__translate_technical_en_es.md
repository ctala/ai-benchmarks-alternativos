# Mistral Large — translation/translate_technical_en_es

- model_id: `mistralai/mistral-large`
- success: True  | final: 7.69 | quality: 8.0
- latency_total: 2.457s | tokens_per_second: 50.9
- input_tokens: 153 | output_tokens: 125
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una claridad excepcional, aunque carece de profundidad en algunos aspectos técnicos.

## Respuesta completa

"Para autenticarte con la API, incluye tu token Bearer en el encabezado Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para el plan gratuito. Si excedes el límite de tasa, la API devuelve un código de estado 429 junto con un encabezado Retry-After que indica cuándo puedes reanudar las solicitudes. Los endpoints de webhook deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con *exponential backoff*."