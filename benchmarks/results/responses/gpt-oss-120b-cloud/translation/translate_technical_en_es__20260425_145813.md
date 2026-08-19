# GPT-OSS 120B (Ollama Cloud) — translation/translate_technical_en_es

- model_id: `gpt-oss:120b-cloud`
- success: True  | final: 7.7 | quality: 8.0
- latency_total: 4.807s | tokens_per_second: 91.5
- input_tokens: 210 | output_tokens: 440
- judge_score: 4.0 | justificación: 

## Respuesta completa

Para autenticarse con la API, incluya su token Bearer en el encabezado Authorization. Los límites de velocidad están establecidos en 100 requests por minuto para el nivel gratuito. Si supera el límite de velocidad, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puede reanudar. Los endpoints de Webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.