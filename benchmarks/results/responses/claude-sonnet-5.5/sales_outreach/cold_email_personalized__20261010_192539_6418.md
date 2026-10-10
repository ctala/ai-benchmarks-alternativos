# Claude Sonnet 5.5 — sales_outreach/cold_email_personalized

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 7.45 | quality: 8.0
- latency_total: 4.369s | tokens_per_second: 69.6
- input_tokens: 299 | output_tokens: 304

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

**Subject:** Tu post sobre escalar contenido sin contratar

Hola Maria,

Leí tu post sobre escalar content marketing sin ampliar el equipo. Lo que dices sobre que el cuello de botella casi nunca es la creatividad sino la producción me hizo pensar en algo.

Trabajamos con startups en etapa Serie A que enfrentan justo eso: el equipo de marketing ya sabe qué decir, pero no da abasto para decirlo en todos los canales.

Hay un enfoque que algunos equipos están usando para duplicar su output sin sumar headcount, y no es lo que probablemente imaginas al oír "IA para contenido".

¿Te haría sentido una call de 15 minutos esta semana o la próxima para contártelo y conocer cómo lo estás resolviendo en FintechCo?

Un saludo,
[Tu nombre]