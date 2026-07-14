# Qwen 3-Next 80B Thinking — translation/translate_technical_en_es

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 7.5 | quality: 8.0
- latency_total: 14.886s | tokens_per_second: 160.4
- input_tokens: 160 | output_tokens: 2387
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una claridad excepcional, aunque la profundidad es solo aceptable debido a la falta de información adicional sobre el manejo de webhooks.

## Respuesta completa

Para autenticarse con la API, incluya su token Bearer en la cabecera Authorization. Los límites de tasa están configurados en 100 solicitudes por minuto para el nivel gratuito. Si excede el límite de tasa, la API devuelve un código de estado 429 con una cabecera Retry-After que indica cuándo puede reanudar. Los endpoints de webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con retardo exponencial.