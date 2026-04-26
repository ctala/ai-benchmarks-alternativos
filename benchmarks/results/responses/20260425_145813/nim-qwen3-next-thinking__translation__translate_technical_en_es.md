# Qwen 3-Next 80B Thinking (NIM) — translation/translate_technical_en_es

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 6.02 | quality: 5.48
- latency_total: 18.252s | tokens_per_second: 112.2
- input_tokens: 163 | output_tokens: 2048
- judge_score: 2.2 | justificación: 

## Respuesta completa

Okay, let's tackle this translation. The user wants the technical documentation translated from English to Spanish, keeping technical terms in English like API, endpoint, token, etc. No forced translations.

First, the original text: "To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Starting with the first sentence: "To authenticate with the API, include your Bearer token in the Authorization header." 

"Authenticate" is "autenticar" in Spanish, but the term "authenticate" is sometimes kept as is, but here it's probably better to translate. But "API" stays. "Bearer token" is a standard term, so it stays as "Bearer token" even in Spanish docs. "Authorization header" is "encabezado Authorization" or maybe "cabecera Authorization". In Spanish technical contexts, "header" is often translated as "encabezado" or "cabecera", but sometimes kept as "header". However, standard practice might be to use "cabecera" for header. Wait, but in Spanish tech documentation, sometimes "header" is left in English. Hmm. Let me check. For example, in many Spanish tech docs, they say "cabecera Authorization" or "encabezado Authorization". But "Authorization" itself is usually kept in English. So "incluya su token Bearer en la cabecera Authorization".

Next part: "Rate limits are set at 100 requests per minute for the free tier." 

"Rate limits" is "límites de tasa" but sometimes "límites de rate" but better to translate. "Rate limits" in Spanish is commonly "límites de tasa" or "límites de solicitud por minuto". Wait, but "rate limits" as a term is often translated as "límites de tasa" but sometimes kept as "rate limits" but the user said to keep technical terms in English when standard. Wait, "rate limits" is a standard term but in Spanish documentation, it's usually translated. Wait, but maybe "límites de rate" but no, more likely "límites de tasa" or "límites de solicitudes por minuto". Wait, the original says "Rate limits are set at 100 requests per minute for the free tier." So "Rate limits" here is the concept. In Spanish, it's common to say "límites de tasa" but sometimes "límites de solicitudes" but the standard translation for "rate limits" in tech is "límites de tasa". However, sometimes they just say "límites" and specify the rate. But the exact phrase: "Rate limits are set at 100 requests per minute for the free tier." So maybe "Los límites de tasa están establecidos en 100 solicitudes por minuto para el plan gratuito." But "rate limits" as a term is sometimes kept as "rate limits" in Spanish, but I think in most Spanish documentation, they translate it. For example, "límites de tasa" or "límites de velocidad". But "rate" here refers to request rate, so "límites de tasa" is correct. Alternatively, "límites de solicitudes por minuto" but the original says "Rate limits are set at 100 requests per minute", so the rate limit is 100 per minute. So "Los límites de tasa son de 100 solicitudes por minuto para el plan gratuito." Or "Los límites de tasa están establecidos en 100 solicitudes por minuto para el plan gratuito." That's okay.

Next: "If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume."

"exceed the rate limit" → "exceda el límite de tasa" or "exceda los límites de tasa". But "rate limit" here is singular? Maybe "límite de tasa" even though it's plural. Wait, "rate limits" plural, but when referring to the specific limit, it's "el límite de tasa". So "Si excede el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puede reanudar."

"Retry-After header" should stay as "Retry-After header" but in Spanish, sometimes "cabecera Retry-After" or "encabezado Retry-After". Since "header" is often translated as "cabecera" in Spanish. For example, "cabecera HTTP" is common. So "cabecera Retry-After".

"indicating when you can resume" → "que indica cuándo puede reanudar" or "que indica el momento en que puede reanudar". Maybe "que indica cuándo puede reanudar las solicitudes" but the original says "when you can resume", so "cuándo puede reanudar" is okay. But maybe "cuándo puede reanudar la solicitud" but the context is about resuming after rate limit, so "cuándo puede reanudar" is sufficient.

Next part: "Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

"Webhook endpoints" → "los endpoints de webhook" or "los extremos de webhook". But "endpoint" is usually kept in English, so "los endpoints de webhook". In Spanish, sometimes "puntos finales", but the standard is to keep "endpoint" as is. So "Los endpoints de webhook deben responder en 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con backoff exponencial."

"must respond within 30 seconds" → "deben responder en 30 segundos" or "deben responder dentro de 30 segundos". "Within" can be translated as "dentro de" but in technical contexts, sometimes "en" is used. For example, "responder en 30 segundos" is common.

"the delivery will be marked as failed" → "la entrega se marcará como fallida". "Marked as failed" → "marcada como fallida".

"retried up to 3 times" → "reintentada hasta 3 veces".

"with exponential backoff" → "con backoff exponencial". "Backoff" is usually kept in English in Spanish tech docs.

Let me check if all technical terms are correctly handled. API, Bearer token, Authorization header, 429 status code, Retry-After header, Webhook endpoints, exponential backoff. All these terms are kept in English as per the user's instruction. "Status code" might be "código de estado" in Spanish, which is the standard translation. So "código de estado 429" is correct. "Retry-After header" as "cabecera Retry-After" or "encabezado Retry-After". In Spanish, "cabecera" is more commonly used for HTTP headers. For example, "cabecera HTTP". So "cabecera Retry-After".

"exponential backoff" is "backoff exponencial" in Spanish.

Now, putting it all together.

Original:

"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Translation:

Para autenticarse con la API, incluya su token Bearer en la cabecera Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para el plan gratuito. Si excede el límite de tasa, la API devuelve un código de estado 429 con una cabecera Retry-After que indica cuándo puede reanudar. Los endpoints de webhook deben responder dentro de 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con backoff exponencial.

Wait, "solicitudes por minuto" is correct. "Plan gratuito" for "free tier". Sometimes "plan gratuito" or "nivel gratuito". But "free tier" is commonly translated as "plan gratuito" in Spanish tech docs. For example, "free tier" as "plan gratuito" or "nivel gratuito", but "plan" is more common.

"excede el límite de tasa" — but the original says "rate limit", so "límite de tasa" is correct. However, sometimes "límite de solicitudes" but the term "rate limit" is usually translated as "límite de tasa" or "límite de velocidad". But in this context, since it's about request rate, "límite de tasa" is appropriate. Alternatively, "límites de tasa" plural, but in the sentence "Si excede el límite de tasa" — singular.

Wait, "Rate limits are set at 100 requests