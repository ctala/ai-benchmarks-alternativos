# Ministral 14B (NIM) — translation/translate_technical_en_es

- model_id: `mistralai/ministral-14b-instruct-2512`
- success: True  | final: 7.32 | quality: 8.2
- latency_total: 8.036s | tokens_per_second: 15.9
- input_tokens: 153 | output_tokens: 128
- judge_score: 4.0 | justificación: 

## Respuesta completa

Para autenticar con el **API**, incluye tu **Bearer token** en el encabezado **Authorization**. Los límites de tasa están establecidos en 100 solicitudes por minuto para el plan gratuito. Si superas el límite, el **API** devuelve un código de estado **429** con un encabezado **Retry-After** que indica cuándo puedes reintentar.

Los **webhook endpoints** deben responder en un plazo máximo de 30 segundos, o la entrega se marcará como fallida y se reintentará hasta 3 veces con *backoff* exponencial.