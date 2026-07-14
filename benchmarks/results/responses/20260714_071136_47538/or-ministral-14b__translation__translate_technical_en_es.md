# Ministral 14B — translation/translate_technical_en_es

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 9.12 | quality: 9.6
- latency_total: 2.452s | tokens_per_second: 52.6
- input_tokens: 153 | output_tokens: 129
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al incluir detalles sobre el manejo de webhooks.

## Respuesta completa

Para autenticarte con la **API**, incluye tu **Bearer token** en el encabezado **Authorization**. Los límites de tasa están establecidos en 100 solicitudes por minuto para el plan gratuito. Si superas el límite de tasa, la **API** devuelve un código de estado **429** con un encabezado **Retry-After** indicando cuándo puedes reanudar.

Los **endpoints** de webhook deben responder en menos de 30 segundos, o la entrega se marcará como fallida y se intentará hasta 3 veces con *backoff* exponencial.