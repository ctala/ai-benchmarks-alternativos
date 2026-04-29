# Qwen 3-Next 80B Thinking (NIM) — translation/translate_technical_en_es

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 6.31 | quality: 6.6
- latency_total: 22.626s | tokens_per_second: 90.5
- input_tokens: 163 | output_tokens: 2048
- judge_score: 3.0 | justificación: 

## Respuesta completa

Okay, I need to translate this technical documentation from English to Spanish. Let me read through it carefully.

Original: "To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

First, I should keep technical terms like API, endpoint, token, etc., in English as specified. So terms like Bearer token, Authorization header, 429 status code, Retry-After header, Webhook endpoints, exponential backoff should stay in English.

Let me go sentence by sentence.

"To authenticate with the API, include your Bearer token in the Authorization header."

In Spanish: "Para autenticarte con la API, incluye tu token Bearer en el encabezado Authorization."

Wait, "Bearer token" is usually written as "Bearer token" in Spanish too, but sometimes it's "token Bearer". But standard practice is to keep "Bearer token" as is. However, in Spanish, sometimes it's written as "token Bearer" but the term is usually kept in English. The correct way is "Bearer token" as a term. So "incluye tu Bearer token en el encabezado Authorization" – but "Authorization" header should stay as "Authorization header" but maybe in Spanish it's "encabezado Authorization" or "cabecera Authorization". In Spanish tech docs, they often use "encabezado" for header, but sometimes "cabecera". However, "header" is commonly used as is, but maybe "encabezado" is more common. Let me check. For example, in Spanish documentation, "Authorization header" is often translated as "encabezado Authorization" or "cabecera Authorization". But sometimes they just say "header Authorization" but that's not right. Wait, in Spanish, "header" is usually translated as "encabezado" or "cabecera". However, in technical contexts, sometimes they keep "header" but in Spanish, it's better to use "encabezado". But sometimes the term "header" is kept. However, the instruction says to keep technical terms in English when standard. So "Authorization header" is a standard term, so "Authorization header" stays, but in Spanish, it's common to say "encabezado Authorization" or "cabecera Authorization". For example, "Authorization header" in Spanish docs is often "cabecera Authorization" or "encabezado Authorization". But maybe in Spanish, they use "encabezado" more. Let me think. For instance, in many Spanish technical documents, "header" is translated as "encabezado". So "Authorization header" becomes "encabezado Authorization". But the word "Authorization" itself is kept in English. So "incluye tu token Bearer en el encabezado Authorization".

Next sentence: "Rate limits are set at 100 requests per minute for the free tier."

In Spanish: "Los límites de tasa están establecidos en 100 solicitudes por minuto para el plan gratuito." But "rate limits" is commonly translated as "límites de tasa" but sometimes "límites de velocidad" or "límites de solicitudes". However, "rate limits" in tech context is often kept as "límites de tasa" or sometimes "rate limits" in Spanish, but the standard translation is "límites de tasa". Alternatively, "límites de solicitudes por minuto". But the original says "Rate limits are set at 100 requests per minute for the free tier." So "Los límites de tasa son de 100 solicitudes por minuto para la versión gratuita." But "free tier" is usually "plan gratuito" or "nivel gratuito". So "para el plan gratuito" or "para la tier gratuita". But "tier" is often kept as "tier" in Spanish tech docs. So maybe "para la tier gratuita". However, sometimes "tier" is translated as "nivel". So "para el nivel gratuito". But "free tier" is commonly translated as "plan gratuito" in many contexts. For example, "free tier" in pricing is "plan gratuito". So "Los límites de tasa están establecidos en 100 solicitudes por minuto para el plan gratuito."

But "rate limits" is sometimes translated as "límites de tasa" or "límites de velocidad". However, in API contexts, "rate limits" is usually translated as "límites de tasa". Alternatively, "límites de solicitudes". But the standard term is "rate limits" and in Spanish, it's often "límites de tasa". So "Los límites de tasa son de 100 solicitudes por minuto para el plan gratuito."

Next part: "If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume."

In Spanish: "Si excedes el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puedes reanudar."

"excedes" is correct for "you exceed" (tú excedes), but maybe "si excedes" or "si superas". "Superas" might be more common. But "exceder" is also correct. However, in Spanish, "superar" is often used for "exceed". So "Si superas el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puedes reanudar."

"Retry-After header" should stay as is, but in Spanish, sometimes "cabecera Retry-After" or "encabezado Retry-After". As before, "encabezado" is better.

"Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

"Webhook endpoints" – "endpoints" stays, but in Spanish, sometimes "puntos finales" but usually "endpoints" is kept. So "Los endpoints de Webhook deben responder en 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con backoff exponencial."

But "Webhook" is usually kept as is. So "Los endpoints de Webhook deben responder en 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con backoff exponencial."

Wait, "Webhook endpoints" could be "endpoints de Webhook" or "puntos finales de Webhook", but "endpoint" is commonly kept as "endpoint" in Spanish tech docs. So "Los endpoints de Webhook deben responder en 30 segundos..." Yes.

"must respond within 30 seconds" → "deben responder en 30 segundos"

"or the delivery will be marked as failed" → "o la entrega se marcará como fallida"

"and retried up to 3 times with exponential backoff." → "y se reintentará hasta 3 veces con backoff exponencial."

But "retried" in Spanish is "reintentado", so "se reintentará hasta 3 veces con backoff exponencial."

Yes.

Putting it all together:

Para autenticarte con la API, incluye tu Bearer token en el encabezado Authorization. Los límites de tasa están establecidos en 100 solicitudes por minuto para el plan gratuito. Si superas el límite de tasa, la API devuelve un código de estado 429 con un encabezado Retry-After que indica cuándo puedes reanudar. Los endpoints de Webhook deben responder en 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con backoff exponencial.

Wait, but "Bearer token" – in Spanish sometimes it's written as "token Bearer" but the standard is to keep it as "Bearer token". So "incluye tu Bearer token en el encabezado Authorization" is correct.

Also, "código de estado 429" – yes, that's standard.

"Retry-After header" as "encabezado Retry-After" is correct.

"backoff exponencial" – yes, exponential backoff is usually translated as "backoff exponencial" in Spanish.

"plan gratuito" for "free tier" – yes.

Alternatively, "tier" might be kept as "tier", so "para la tier gratuita", but "plan gratuito" is more common. For example, in many Spanish documentation, "free tier" is translated as "plan gratuito". So that's correct.

Another check: "Webhook endpoints" – in Spanish, "endpoints de Webhook" is correct. Sometimes "puntos finales" but "endpoint" is widely used as is.

So the translation seems correct. Let me check again.

Original: "To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried