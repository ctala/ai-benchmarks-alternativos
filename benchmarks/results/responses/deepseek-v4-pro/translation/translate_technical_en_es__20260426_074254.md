# DeepSeek V4 Pro — translation/translate_technical_en_es

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 6.7 | quality: 7.44
- latency_total: 45.752s | tokens_per_second: 27.1
- input_tokens: 153 | output_tokens: 1238
- judge_score: 3.6 | justificación: 

## Respuesta completa

Para autenticarse con la API, incluya su token Bearer en el encabezado Authorization. Los límites de frecuencia están establecidos en 100 solicitudes por minuto para el nivel gratuito. Si excede el límite de frecuencia, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puede reanudar. Los endpoints de webhook deben responder en un plazo de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con retroceso exponencial.