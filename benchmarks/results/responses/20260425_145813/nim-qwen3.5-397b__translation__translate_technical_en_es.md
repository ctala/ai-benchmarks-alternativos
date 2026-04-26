# Qwen 3.5 397B (NIM) — translation/translate_technical_en_es

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 6.9 | quality: 7.44
- latency_total: 14.123s | tokens_per_second: 8.2
- input_tokens: 160 | output_tokens: 116
- judge_score: 3.6 | justificación: 

## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en la cabecera Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para el plan gratuito. Si supera el límite de tasa, la API devuelve un código de estado 429 con una cabecera Retry-After que indica cuándo puede reanudar. Los endpoints de Webhook deben responder en un plazo de 30 segundos; de lo contrario, la entrega se marcará como fallida y se reintentará hasta 3 veces con retroceso exponencial.