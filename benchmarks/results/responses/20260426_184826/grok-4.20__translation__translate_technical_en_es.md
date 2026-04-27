# Grok 4.20 — translation/translate_technical_en_es

- model_id: `x-ai/grok-4.20`
- success: True  | final: 6.83 | quality: 7.08
- latency_total: 2.295s | tokens_per_second: 47.1
- input_tokens: 263 | output_tokens: 108
- judge_score: 3.2 | justificación: 

## Respuesta completa

**Traducción:**

Para autenticarse con la API, incluya su Bearer token en el header Authorization. Los rate limits están establecidos en 100 requests por minuto para el plan gratuito. Si excede el rate limit, la API devuelve un código de estado 429 junto con un header Retry-After que indica cuándo puede reanudar. Los webhook endpoints deben responder en un máximo de 30 segundos, de lo contrario la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.