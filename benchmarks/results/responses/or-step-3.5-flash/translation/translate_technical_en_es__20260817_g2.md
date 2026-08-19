# Step 3.5 Flash — translation/translate_technical_en_es

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 7.71 | quality: 8.2
- latency_total: 29.038s | tokens_per_second: 70.5
- input_tokens: 161 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo términos técnicos en inglés según lo solicitado, y ofrece una traducción clara y útil, aunque carece de profundidad adicional más allá de la traducción.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Primero, el usuario pide traducir documentación técnica de inglés a español. Debo mantener los términos técnicos en inglés cuando sea estándar, como API, endpoint, token, etc. No inventar traducciones forzadas.

El texto original es:

"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Ahora, voy a traducirlo frase por frase:

1. "To authenticate with the API" -> "Para autenticarse con la API" (API se mantiene en inglés porque es estándar).

2. "include your Bearer token in the Authorization header" -> "incluye tu token Bearer en el encabezado Authorization" (Bearer token y Authorization header son términos técnicos, así que los dejo en inglés. "Encabezado" es la traducción común para "header", pero en contexto técnico a veces se usa "header" también. Sin embargo, "Authorization header" es un término específico, y en español se suele traducir como "encabezado de Autorización". Pero el usuario dice mantener términos en inglés cuando es estándar. "Authorization" es parte del nombre del header, así que quizás lo deje como "Authorization header". Revisando: en muchos contextos hispanohablantes, se usa "header" o "encabezado". Para ser consistente, si "header" se traduce, pero "Authorization" es un nombre propio. Decido: "en el encabezado Authorization" o "en el header Authorization". Pero "Bearer token" sí es un término que a veces se traduce como "token de portador", pero el usuario dice no forzar. En la práctica, "Bearer token" se usa a menudo en inglés incluso en español. Para seguir la instrucción, mantengo "Bearer token" en inglés. Lo mismo para "Authorization header" – quizás "encabezado Authorization" o dejar "Authorization header". Mejor: "en el encabezado de Autorización" suena más natural. Pero el usuario dice "mantén los términos técnicos en inglés cuando es lo standard". "Authorization" en este contexto es parte del nombre del header HTTP, que en estándar es "Authorization", así que lo dejo en inglés. Entonces: "incluye tu token Bearer en el header Authorization".

3. "Rate limits are set at 100 requests per minute for the free tier." -> "Los límites de tasa están configurados en 100 solicitudes por minuto para el nivel gratuito." "Rate limits" se traduce como "límites de tasa" o "límites de velocidad", pero en API comúnmente se usa "límites de tasa". "Free tier" es "nivel gratuito" o "plan gratuito".

4. "If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume." -> "Si excedes el límite de tasa, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar." "Status code" se deja como "código de estado", pero "429" es un número. "Retry-After header" – similar a antes, mantengo "Retry-After" en inglés.

5. "Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff." -> "Los endpoints de webhook deben responder dentro de los 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con retroceso exponencial." "Webhook endpoints" – "webhook" se suele dejar en inglés, y "endpoints" también. "Exponential backoff" es "retroceso exponencial", que es la traducción estándar.

Ahora, reviso para asegurar que los términos técnicos estén en inglés cuando corresponda:

- API: en inglés.

- Bearer token: en inglés.

- Authorization header: "Authorization" en inglés, "header" podría ser "encabezado", pero en combinación, a veces se deja "Authorization header". Para ser preciso, en traducciones técnicas, "header" a menudo se traduce como "encabezado", pero el nombre propio "Authorization" se mantiene. Entonces, "encabezado Authorization" o "header Authorization". Decido usar "encabezado Authorization" para que sea más comprensible en español, pero manteniendo "Authorization" en inglés. Otra opción: "el encabezado de Autorización" – pero "Autorización" con mayúscula no es estándar. Mejor: "en el encabezado Authorization".

- Rate limits: "límites de tasa" – "tasa" es la traducción, pero en algunos contextos se usa "rate limiting". Aquí, "rate limits" se refiere a los límites, así que está bien.

- Free tier: "nivel gratuito" – estándar.

- Status code: "código de estado" – común.

- Retry-After header: similar, "header Retry-After".

- Webhook endpoints: "endpoints de webhook" – webhook en inglés, endpoints en inglés.

- Exponential backoff: "retroceso exponencial" – traducción aceptada.

El usuario dice "SOLO la traducción", así que debo output solo el texto traducido, sin explicaciones.

Texto traducido completo:

"Para autenticarse con la API, incluye tu token Bearer en el encabezado Authorization. Los límites de tasa están configurados en 100 solicitudes por minuto para el nivel gratuito. Si excedes el límite de tasa, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los endpoints de webhook deben responder dentro de los 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con retroceso exponencial."

Reviso si "header" lo dejé en inglés en algunos lugares. En la primera parte, dije "encabezado Authorization", pero en la segunda, "header Retry-After". Para ser consistente, debería usar lo mismo. Dado que "header" es un término técnico que a menudo se deja en inglés, pero en español se entiende "encabezado". El usuario dice mantener términos en inglés cuando es standard. "Header" en HTTP es estándar en inglés, pero en documentación en español a veces se traduce. Para seguir la instrucción al pie de la letra, si es standard en inglés, lo dejo en inglés. Pero "header" no es como "API" que siempre se deja; a veces se traduce. Sin embargo, en nombres como "Authorization header", "Authorization" es el nombre del header, y "header" es la palabra genérica. En muchos contextos hispanos, se dice "el header Authorization". Pero para evitar forzar, puedo dejarlo como "header" en inglés.

Decido: en la primera frase, "in the Authorization header" -> "en el header Authorization". En la segunda, "with a Retry-After header" -> "con un header Retry-After". Así mantengo "header" en inglés.

También, "Bearer token" – lo dejo en inglés.

"Webhook endpoints" – "webhook endpoints" en inglés, pero "webhook" es un término, así que "endpoints de webhook" o "webhook endpoints". Para mantenerlo en inglés, "webhook endpoints" directamente.

Pero el usuario dice "mantiene los terminos tecnicos en ingles cuando es lo standard". "Endpoint" es un término que se usa en inglés en español también. Así que puedo dejarlo como "endpoints".

Voy a ajustar:

"Para autenticarse con la API, incluye tu token Bearer en el header Authorization. Los límites de tasa están configurados en 100 solicitudes por minuto para el free tier. Si excedes el límite de tasa, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar. Los webhook endpoints deben responder dentro de los 30 segundos o la entrega se marcará como fallida y se reintentará hasta 3 veces con exponential backoff."

Pero "free tier" lo traduje como "nivel gratuito", pero si es standard en inglés, quizás dejarlo como "free tier". En muchos contextos, se traduce. El usuario no especifica, pero dice "cuando es lo standard". "Free tier" es un término común en servicios en la nube, y a menudo se deja en inglés o se traduce. Para ser seguro, lo dejo en inglés? Pero en la instrucción, dice "no inventes traducciones forzadas", así que si hay una traducción natural, la uso. "Free tier" se traduce comúnmente como "n