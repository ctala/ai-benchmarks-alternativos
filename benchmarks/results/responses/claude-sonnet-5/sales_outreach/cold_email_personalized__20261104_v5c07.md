# Claude Sonnet 5 — sales_outreach/cold_email_personalized

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 7.3 | quality: 8.0
- latency_total: 5.131s | tokens_per_second: 57.7
- input_tokens: 297 | output_tokens: 296

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

**Subject: lo de escalar contenido sin contratar**

María,

Tu post de la semana pasada sobre escalar content marketing sin contratar me quedó rondando.

Pregunta directa: si hoy tuvieras que duplicar tu output de contenido (blog, LinkedIn, newsletters) con el mismo equipo, ¿qué se rompería primero? ¿Ideación, producción o distribución?

Trabajamos con marketing teams en fintech que enfrentan ese mismo cuello de botella post Serie A — crecer la demanda de contenido sin inflar headcount.

No te voy a vender nada en este email. Solo quiero entender cómo lo estás resolviendo en FintechCo y compartir qué ha funcionado para otros casos similares.

¿15 minutos esta semana para comparar notas?

Saludos,
[Tu nombre]