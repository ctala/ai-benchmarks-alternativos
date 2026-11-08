# Claude Haiku 5.5 — sales_outreach/cold_email_personalized

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.15 | quality: 8.0
- latency_total: 2.445s | tokens_per_second: 114.5
- input_tokens: 298 | output_tokens: 280

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un experto en cold outreach B2B. Reglas:
- NUNCA uses frases genericas como "Espero que este email te encuentre bien"
- El email debe ser corto (max 150 palabras)
- Personalizado al destinatario
- Un solo CTA claro
- No vendas, genera curiosidad

**user:**

Escribe un cold email para:
- Destinatario: Maria Lopez, Head of Marketing en FintechCo (startup fintech en Colombia, 50 empleados, Serie A)
- Mi producto: herramienta de automatizacion de contenido con IA para startups
- Dato de personalizacion: Maria publico un post en LinkedIn la semana pasada sobre "como escalar content marketing sin contratar"
- Objetivo: conseguir una call de 15 min

Escribe SOLO el email (subject + body). Nada mas.


## Respuesta completa

Asunto: Lo que dijiste sobre escalar contenido sin contratar

Hola María,

Tu post de la semana pasada sobre escalar content marketing sin contratar me hizo pensar en un problema que veo mucho en equipos de tu tamaño: el cuello de botella no es la idea, es producir y distribuir a la velocidad que el negocio pide.

Estamos viendo cómo algunas startups de Serie A en LATAM están usando flujos de IA para convertir un solo insumo (una entrevista, un caso de cliente, un dato de producto) en una semana completa de contenido, sin sumar headcount.

¿Te interesaría una llamada de 15 minutos para compartirte cómo lo están haciendo y ver si tiene sentido para FintechCo?

Saludos,
[Tu nombre]