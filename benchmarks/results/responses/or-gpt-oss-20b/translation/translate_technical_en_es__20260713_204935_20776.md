# GPT-OSS 20B — translation/translate_technical_en_es

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 8.0 | quality: 8.0
- latency_total: 5.066s | tokens_per_second: 129.1
- input_tokens: 197 | output_tokens: 654
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con información adicional útil sobre el manejo de webhooks, aunque no se menciona en el texto original.

## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el encabezado Authorization. Los límites de tasa están establecidos en 100 peticiones por minuto para la capa gratuita. Si excede el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puede reanudar. Los webhook endpoints deben responder dentro de 30 segundos o la entrega se marcará como fallida y se volverá a intentar hasta 3 veces con exponential backoff.