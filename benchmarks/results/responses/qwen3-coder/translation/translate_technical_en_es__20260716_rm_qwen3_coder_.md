# Qwen3 Coder — translation/translate_technical_en_es

- model_id: `qwen/qwen3-coder`
- success: True  | final: 8.0 | quality: 8.0
- latency_total: 2.423s | tokens_per_second: 51.2
- input_tokens: 160 | output_tokens: 124
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con terminos tecnicos mantenidos en ingles y adiciones claras sobre el tiempo de respuesta de los webhook, aunque no se menciona en el texto original.

## Respuesta completa

"Para autenticarte con la API, incluye tu Bearer token en el encabezado Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si excedes el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After indicando cuándo puedes reanudar. Los endpoint de webhook deben responder dentro de 30 segundos o la entrega será marcada como fallida y se reintentará hasta 3 veces con retroceso exponencial."