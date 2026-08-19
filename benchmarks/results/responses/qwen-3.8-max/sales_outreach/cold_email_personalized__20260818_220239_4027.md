# Qwen 3.8 Max — sales_outreach/cold_email_personalized

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 6.94 | quality: 8.0
- latency_total: 23.314s | tokens_per_second: 46.9
- input_tokens: 234 | output_tokens: 1094

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

Asunto: Tu post sobre escalar contenido sin contratar

Maria:

Vi tu post en LinkedIn sobre cómo escalar content marketing sin contratar y me hizo pensar en el momento de FintechCo tras la Serie A.

Algunas startups fintech están logrando más contenido sin sumar headcount, usando automatización con IA para mantener calidad. Me da curiosidad saber si ya lo están evaluando.

¿Tienes 15 minutos esta semana para mostrarte dos ejemplos aplicables a FintechCo?

[Tu nombre]