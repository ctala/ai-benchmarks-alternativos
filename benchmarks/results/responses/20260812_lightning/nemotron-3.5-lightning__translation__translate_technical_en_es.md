# Nemotron 3.5 Lightning — translation/translate_technical_en_es

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 7.97 | quality: 8.0
- latency_total: 3.187s | tokens_per_second: 652.9
- input_tokens: 166 | output_tokens: 2081
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante, y clara, proporcionando detalles útiles sobre la autenticación y manejo de límites de tasa, con una buena profundidad en la explicación de los códigos de estado y el manejo de webhooks.

## Respuesta completa

Para autenticar con la API, incluye tu Bearer token en el encabezado Authorization. Los Rate limits están establecidos en 100 solicitudes por minuto para el free tier. Si excedes el rate limit, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo reanudar. Los Webhook endpoints deben responder dentro de 30 segundos o el envío se marcará como fallido y se reintentará hasta 3 veces con exponential backoff.