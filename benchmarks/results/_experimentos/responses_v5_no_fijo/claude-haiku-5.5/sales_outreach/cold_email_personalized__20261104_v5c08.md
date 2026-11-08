# Claude Haiku 5.5 — sales_outreach/cold_email_personalized

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.3 | quality: 8.0
- latency_total: 1.905s | tokens_per_second: 111.8
- input_tokens: 298 | output_tokens: 213

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

**Asunto:** Tu post sobre escalar content sin contratar

Hola María,

Leí tu post de LinkedIn sobre escalar content marketing sin contratar. El punto de que la consistencia pesa más que el volumen me hizo pensar en cómo equipos pequeños en FintechCo podrían sostener ese ritmo.

Hemos visto a startups de tu etapa cortar el tiempo de producción de contenido a la mitad sin perder voz de marca. ¿Tendrías 15 minutos la próxima semana para que te muestre cómo lo hacen?

Saludos,
[Tu nombre]