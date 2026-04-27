# Llama 3.1 8B Instant (Groq) — translation/translate_technical_en_es

- model_id: `llama-3.1-8b-instant`
- success: True  | final: 7.65 | quality: 7.44
- latency_total: 0.52s | tokens_per_second: 232.8
- input_tokens: 182 | output_tokens: 121
- judge_score: 3.6 | justificación: 

## Respuesta completa

"Para autenticarse con la API, incluye tu token Bearer en el encabezado de Authorization. Los límites de velocidad están establecidos en 100 solicitudes por minuto para la tarifa gratuita. Si superas el límite de velocidad, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder dentro de 30 segundos o la entrega será marcada como fallida y se intentará hasta 3 veces con un retraso exponencial."