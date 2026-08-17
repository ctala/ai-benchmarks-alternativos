# Mistral Nemo — translation/translate_technical_en_es

- model_id: `mistralai/mistral-nemo`
- success: True  | final: 6.76 | quality: 6.88
- latency_total: 9.809s | tokens_per_second: 12.5
- input_tokens: 153 | output_tokens: 123
- judge_score: 3.2 | justificación: 

## Respuesta completa

"Para autenticar con la API, incluye tu token Bearer en el encabezado de Autorización. Los límites de tasa de solicitudes están configurados en 100 solicitudes por minuto para la capa gratuita. Si superas el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puedes reanudar. Los puntos finales de webhook deben responder dentro de los 30 segundos o la entrega se marcará como fallida y se intentará hasta 3 veces con retroceso exponencial."