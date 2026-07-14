# GPT-OSS 120B — translation/translate_technical_en_es

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.44 | quality: 8.2
- latency_total: 1.181s | tokens_per_second: 314.0
- input_tokens: 214 | output_tokens: 371
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante, y clara, con una buena profundidad al incluir detalles sobre el manejo de webhooks, aunque el texto original se corta antes de completar la oración.

## Respuesta completa

Para autenticarse con la API, incluya su **Bearer token** en el encabezado **Authorization**. Los límites de velocidad están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si supera el límite de velocidad, la API devuelve un código de estado **429** con un encabezado **Retry-After** que indica cuándo puede reanudar. Los **endpoint** de webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con **exponential backoff**.