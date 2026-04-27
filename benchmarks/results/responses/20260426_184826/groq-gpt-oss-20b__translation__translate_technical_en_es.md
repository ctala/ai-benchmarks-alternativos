# GPT-OSS 20B (Groq) — translation/translate_technical_en_es

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.65 | quality: 7.72
- latency_total: 1.097s | tokens_per_second: 681.1
- input_tokens: 214 | output_tokens: 747
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para autenticar con la API, incluya su Bearer token en la Authorization header. Los Rate limits están establecidos en 100 requests per minute para el free tier. Si excede el Rate limit, la API devuelve un 429 status code con un Retry-After header que indica cuándo puede reanudar. Los Webhook endpoints deben responder dentro de 30 seconds o la entrega será marcada como failed y se reintentará hasta 3 times con exponential backoff.