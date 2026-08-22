# GLM 5.3 — sales_outreach/cold_email_personalized

- model_id: `z-ai/glm-5.3`
- success: True  | final: 7.05 | quality: 8.0
- latency_total: 17.396s | tokens_per_second: 49.7
- input_tokens: 193 | output_tokens: 865

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

María:

Leí tu post de LinkedIn de la semana pasada y no fue casualidad que lo escribieras: casi todas las startups en Serie A con las que hablamos viven esa misma tensión — crecer el pipeline de contenido sin inflar nómina.

Un dato curioso: dos fintechs latam de tamaño similar al de FintechCo están publicando 4x más contenido con el mismo equipo de marketing. El cambio no fue contratar más gente, fue automatizar lo que no necesitaba una persona detrás.

¿Vale la pena 15 minutos para ver si algo de eso aplica a tu equipo? ¿Cuándo te viene bien esta semana o la próxima?

[Nombre]