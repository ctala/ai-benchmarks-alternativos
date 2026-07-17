# DeepSeek V3.2 — translation/translate_technical_en_es

- model_id: `deepseek/deepseek-chat`
- success: True  | final: 7.85 | quality: 8.0
- latency_total: 4.0s | tokens_per_second: 31.5
- input_tokens: 152 | output_tokens: 126
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con buena claridad y utilidad práctica, aunque la profundidad es solo aceptable debido a la adición de detalles no solicitados.

## Respuesta completa

"Para autenticarse con la API, incluye tu token Bearer en el encabezado Authorization. Los límites de tasa están configurados en 100 solicitudes por minuto para el plan gratuito. Si excedes el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puedes continuar. Los endpoints de webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con retroceso exponencial."