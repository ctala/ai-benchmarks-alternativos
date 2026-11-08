# GLM 5.3 — sales_outreach/cold_email_personalized

- model_id: `z-ai/glm-5.3`
- success: True  | final: 7.08 | quality: 8.0
- latency_total: 22.048s | tokens_per_second: 74.9
- input_tokens: 193 | output_tokens: 1652

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

**Asunto:** Tu post sobre escalar contenido sin contratar

Hola María,

Leí tu post de LinkedIn de la semana pasada sobre escalar content marketing sin contratar. Me quedó una pregunta: ¿cuál es hoy el cuello de botella real de tu equipo?

En las startups Serie A con las que trabajamos, casi siempre es lo mismo: no falta talento, falta tiempo. Investigación, borradores, adaptar cada pieza a cada canal.

Una fintech colombiana de tamaño similar a FintechCo pasó de 6 a 25 piezas mensuales automatizando exactamente esas tareas con IA. Mismo headcount.

No sé si en tu caso aplicaría igual. 15 minutos bastan para averiguarlo, ¿tienes hueco el jueves a las 10am, hora Colombia?

[Nombre]