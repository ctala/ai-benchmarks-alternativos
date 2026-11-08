# GPT-6.1 Terra — translation/translate_technical_en_es

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 7.62 | quality: 8.0
- latency_total: 2.327s | tokens_per_second: 46.4
- input_tokens: 149 | output_tokens: 108
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, manteniendo los términos técnicos en inglés y proporcionando detalles adicionales útiles sobre el manejo de webhooks, aunque no se menciona en el texto original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion.


## Respuesta completa

Para autenticarte en la API, incluye tu Bearer token en el header Authorization. El límite de solicitudes del plan gratuito es de 100 por minuto. Si superas este límite, la API devuelve un código de estado 429 con un header Retry-After que indica cuándo puedes reanudar las solicitudes. Los endpoints de webhook deben responder en un plazo de 30 segundos; de lo contrario, la entrega se marcará como fallida y se reintentará hasta 3 veces con backoff exponencial.