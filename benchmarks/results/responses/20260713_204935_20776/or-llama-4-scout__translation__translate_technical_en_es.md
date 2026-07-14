# Llama 4 Scout 17B — translation/translate_technical_en_es

- model_id: `meta-llama/llama-4-scout`
- success: True  | final: 6.87 | quality: 6.6
- latency_total: 3.134s | tokens_per_second: 34.1
- input_tokens: 151 | output_tokens: 107
- judge_score: 3.0 | justificación: La respuesta es generalmente precisa y relevante, pero añade información no presente en el texto original, afectando la precisión y profundidad.

## Respuesta completa

"Para autenticarte con la API, incluye tu token Bearer en el encabezado de Autorización. Los límites de velocidad se establecen en 100 solicitudes por minuto para el nivel gratuito. Si superas el límite de velocidad, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puedes reanudar. Los puntos finales de webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con retroceso exponencial."