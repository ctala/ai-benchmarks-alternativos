# Sakana Namazu — translation/translate_technical_en_es

- model_id: `sakana/sakana-namazu`
- success: True  | final: 7.28 | quality: 8.0
- latency_total: 8.413s | tokens_per_second: 243.4
- input_tokens: 233 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, manteniendo términos técnicos en inglés según lo solicitado, aunque carece de profundidad adicional.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

El usuario quiere que traduzca una documentación técnica del inglés al español, manteniendo los términos técnicos en inglés cuando sea estándar (API, endpoint, token, etc.), y que no invente traducciones forzadas. Debo devolver SOLO la traducción.

Analicemos el texto original:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Traducción término por término considerando los que deben mantenerse en inglés:
- "To authenticate with the API" -> "Para autenticarte con la API" (API se mantiene en inglés, es estándar)
- "include your Bearer token" -> "incluye tu Bearer token" (Bearer token es estándar, se mantiene)
- "in the Authorization header" -> "en el header Authorization" o "en el encabezado Authorization". "Header" es muy común en español técnico, pero "encabezado" también se usa. Sin embargo, en documentación técnica de APIs, "header" es muy estándar. Pero "Authorization header" podría ser "header Authorization" o "encabezado Authorization". Creo que "header Authorization" es más natural en docs técnicas en español, o "encabezado Authorization". Voy a usar "header Authorization" o "encabezado Authorization". El usuario dijo mantener términos técnicos en inglés cuando sea standard. "Header" es estándar pero "encabezado" es la traducción correcta y ampliamente usada. Sin embargo, en muchas docs técnicas hispanas se usa "header". Voy a optar por "header Authorization" para ser consistente con mantener términos técnicos en inglés. O quizás "encabezado Authorization" es mejor porque es la traducción directa y no forzada. Pero el usuario dijo "mantén los términos técnicos en inglés cuando es lo standard (API, endpoint, token, etc)". Header es técnico estándar en inglés pero tiene traducción natural. Creo que "header" es común. Usaré "header Authorization" para ser fiel al estilo técnico. O mejor: "header de Authorization". Pero espera, "Authorization header" -> "header Authorization" suena bien.
- "Rate limits" -> "Rate limits" (se mantiene en inglés, es estándar) o "Los límites de tasa". "Rate limits" es muy común en español técnico. Voy a mantener "Rate limits".
- "are set at 100 requests per minute" -> "están establecidos en 100 requests por minuto" (requests es estándar) o "peticiones". "Requests" es técnicamente estándar. Voy a usar "requests".
- "for the free tier" -> "para el free tier" (free tier es estándar) o "plan gratuito". "Free tier" es muy usado. Mantendré "free tier".
- "If you exceed the rate limit" -> "Si excedes el rate limit"
- "the API returns a 429 status code" -> "la API retorna un código de estado 429" (status code es estándar pero "código de estado" es perfectamente natural en español y no forzado). O "status code 429". Voy a usar "código de estado 429" porque es natural o "status code 429". El usuario dijo no inventar traducciones forzadas. "Código de estado" es la traducción natural.
- "with a Retry-After header" -> "con un header Retry-After" o "con un encabezado Retry-After". Mantendré "header Retry-After".
- "indicating when you can resume" -> "que indica cuándo puedes reanudar"
- "Webhook endpoints" -> "Webhook endpoints" (webhook y endpoints son estándar)
- "must respond within 30 seconds" -> "deben responder en un plazo de 30 segundos" o "dentro de 30 segundos"
- "or the delivery will be marked as failed" -> "o la entrega será marcada como fallida" (delivery podría ser "entrega", failed como "fallida")
- "and retried up to 3 times" -> "y se reintentará hasta 3 veces"
- "with exponential backoff" -> "con exponential backoff" (exponential backoff es término estándar)

Revisando la traducción completa:
"Para autenticarte con la API, incluye tu Bearer token en el header Authorization. Los Rate limits están establecidos en 100 requests por minuto para el free tier. Si excedes el rate limit, la API retorna un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los Webhook endpoints deben responder dentro de 30 segundos o la entrega será marcada como fallida y se reintentará hasta 3 veces con exponential backoff."

Ajustes:
- "Bearer token" -> se mantiene
- "header Authorization" -> quizás mejor "header de Authorization"? No, en docs técnicas es común "header Authorization" o directamente el nombre del header. Es mejor "header Authorization".
- "Rate limits" -> podría ir en minúscula "rate limits" a menos que inicie la oración. En la segunda oración inicia con "Los rate limits..." así que minúscula.
- "status code" -> usaré "código de estado" que es natural. Si quiero mantener más términos en inglés podría decir "status code", pero código de estado es perfectamente válido y natural.
- "Retry-After header" -> "header Retry-After"
- "Webhook endpoints" -> "Endpoints de webhook" o "Los webhook endpoints". Usaré "Los webhook endpoints".
- "failed" -> "fallida" es correcto.
- "exponential backoff" -> se mantiene.

Espera, el usuario pidió: "Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas."

Entonces:
- API -> API
- Bearer token -> Bearer token
- Authorization header -> Authorization header (o header Authorization)
- Rate limits -> Rate limits (o rate limits)
- requests -> requests
- free tier -> free tier
- rate limit -> rate limit
- status code -> status code? o código de estado? "Status code" es estándar, pero "código de estado" no es forzado. Sin embargo, si quiero ser estricto con mantener términos técnicos en inglés, quizás debería usar "status code".
- Retry-After header -> Retry-After header
- Webhook endpoints -> Webhook endpoints
- exponential backoff -> exponential backoff

Veamos:
"Para autenticarte con la API, incluye tu Bearer token en el Authorization header. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si excedes el rate limit, la API retorna un status code 429 con un Retry-After header que indica cuándo puedes reanudar. Los webhook endpoints deben responder dentro de 30 segundos o la entrega será marcada como failed y se reintentará hasta 3 veces con exponential backoff."

Pero "la entrega será marcada como failed" suena un poco raro. "Fallida" es mejor. Y "reintentará" está bien.

Refinando:
"Para autenticarte con la API, incluye tu Bearer token en el Authorization header. Los rate limits están establecidos en 100 requests por minuto para el free tier. Si excedes el rate limit, la API retorna un status code 429 con un Retry-After header que indica cuándo puedes reanudar. Los webhook endpoints deben responder dentro de 30 segundos o la entrega será marcada como fallida y se reintentará hasta 3 veces con exponential backoff."

Espera, "requests" se puede traducir como "peticiones" o "solicitudes", pero "requests" es ampliamente usado. El usuario incluyó ejemplos: "API, endpoint, token, etc". Requests es técnico estándar pero tiene traducción natural. Sin embargo, en contextos de rate limits, se dice mucho "100 requests por minuto". Lo dejaré así.

Creo que "header" debería ir en la forma que fluye mejor. "Authorization header" o "header Authorization". En inglés es "Authorization header", así que en español se puede decir "el header Authorization" o