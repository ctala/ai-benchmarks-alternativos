# Nemotron 3 Nano 30B — translation/translate_technical_en_es

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 7.35 | quality: 7.72
- latency_total: 7.217s | tokens_per_second: 89.8
- input_tokens: 166 | output_tokens: 648
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticarse con la API, incluya su Bearer token en el Authorization header. Los rate limits están configurados en 100 requests por minuto para el free tier. Si supera el rate limit, la API devuelve un 429 status code con un header Retry-After que indica cuándo puede reanudar. Los Webhook endpoints deben responder dentro de 30 seconds o la entrega se marcará como failed y se reintentará hasta 3 times con exponential backoff.