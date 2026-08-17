# MiMo-V2-Pro — translation/translate_technical_en_es

- model_id: `xiaomi/mimo-v2-pro`
- success: True  | final: 7.05 | quality: 8.0
- latency_total: 7.706s | tokens_per_second: 39.2
- input_tokens: 401 | output_tokens: 302
- judge_score: 4.0 | justificación: 

## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el encabezado Authorization. Los límites de tasa (rate limits) están establecidos en 100 solicitudes por minuto para la capa gratuita. Si excede el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puede reanudar. Los endpoints de webhook deben responder dentro de 30 segundos; de lo contrario, la entrega se marcará como fallida y se reintentará hasta 3 veces con retroceso exponencial (exponential backoff).