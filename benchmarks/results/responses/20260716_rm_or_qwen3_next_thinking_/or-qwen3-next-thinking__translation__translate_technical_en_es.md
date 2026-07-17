# Qwen 3-Next 80B Thinking — translation/translate_technical_en_es

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 7.38 | quality: 8.0
- latency_total: 26.688s | tokens_per_second: 166.1
- input_tokens: 160 | output_tokens: 4433
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una buena profundidad al añadir detalles sobre el manejo de webhooks, y está claramente escrita y organizada, siendo útil para un emprendedor.

## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el Authorization header. Los límites de tasa están establecidos en 100 solicitudes por minuto para el plan gratuito. Si excede el límite de tasa, la API devuelve un código de estado 429 con un header Retry-After indicando cuándo puede reanudar. Los endpoints de webhook deben responder en 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con backoff exponencial.