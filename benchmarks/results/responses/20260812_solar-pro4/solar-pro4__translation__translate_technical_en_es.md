# Solar Pro 4 — translation/translate_technical_en_es

- model_id: `upstage/solar-pro4`
- success: True  | final: 7.85 | quality: 8.0
- latency_total: 3.962s | tokens_per_second: 33.3
- input_tokens: 203 | output_tokens: 132
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con información útil y adicional sobre el manejo de webhooks, aunque no se menciona en el texto original.

## Respuesta completa



Para autenticarse con la API, incluya su Bearer token en el encabezado Authorization. Los límites de tasa están configurados en 100 solicitudes por minuto para el plan gratuito. Si excede el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puede reanudar. Los endpoints de webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con backoff exponencial.