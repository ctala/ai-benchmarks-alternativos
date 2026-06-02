# MiniMax M3 (directo / sub) — translation/translate_technical_en_es

- model_id: `MiniMax-M3`
- success: True  | final: 7.82 | quality: 9.4
- latency_total: 23.633s | tokens_per_second: 40.7
- input_tokens: 317 | output_tokens: 961
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, manteniendo los términos técnicos en inglés según lo solicitado, y proporciona una traducción adecuada para un contexto técnico.

## Respuesta completa

<think>
The user wants me to translate a technical documentation from English to Spanish. They want me to keep technical terms in English when they are standard (API, endpoint, token, etc.) and not invent forced translations.

Let me translate this carefully:

"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Spanish translation:
"Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están fijados en 100 requests por minuto para el plan free. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After indicando cuándo puedes reanudar. Los webhook endpoints deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff."

Let me review:
- "Bearer token" - keep in English, it's standard
- "Authorization header" - could be translated but "header" in technical context is often kept, though "header" translates to "encabezado" in Spanish. However, in API documentation, "header" is commonly kept in English. Let me think... Actually, in Spanish tech docs, "header" is often kept as is or translated to "encabezado". I'll keep "header" as it's standard.
- "Rate limits" - keep in English, it's standard terminology
- "free tier" - "plan free" or "plan gratuito"? "free tier" is often kept as is, or translated to "nivel gratuito" or "plan gratuito". I think "plan gratuito" or keeping "free tier" is fine. Let me go with "plan gratuito" to make it more natural in Spanish, or keep "free tier". The user said to keep technical terms in English when standard. "Free tier" is commonly used as is in Spanish tech docs. I'll keep it.
- "requests" - could translate to "solicitudes" but "requests" is very common in Spanish tech context
- "status code" - keep in English or translate to "código de estado"? "status code" is often kept. I'll keep it.
- "Retry-After" - this is a specific HTTP header name, keep in English
- "webhook endpoints" - keep "webhook" and "endpoints" in English
- "exponential backoff" - keep in English, it's a standard technical term

Let me refine:

"Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están fijados en 100 requests por minuto para el free tier. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After indicando cuándo puedes reanudar. Los webhook endpoints deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff."

This looks good. Let me check once more for natural Spanish flow:
- "Para autenticarte con la API" - good
- "incluye tu Bearer token" - good
- "en el header Authorization" - good, keeping technical terms
- "Los rate limits están fijados en 100 requests por minuto" - good
- "para el free tier" - could be "para el plan gratuito" but keeping "free tier" is also acceptable
- "Si excedes el rate limit" - good
- "la API devuelve un status code 429" - good
- "con un header Retry-After" - good
- "indicando cuándo puedes reanudar" - good
- "Los webhook endpoints deben responder dentro de 30 segundos" - good
- "o la entrega se marcará como fallida" - good
- "y se reintentará hasta 3 veces con exponential backoff" - good

I think this is a solid translation.
</think>
Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los rate limits están fijados en 100 requests por minuto para el free tier. Si excedes el rate limit, la API devuelve un status code 429 con un header Retry-After indicando cuándo puedes reanudar. Los webhook endpoints deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff.