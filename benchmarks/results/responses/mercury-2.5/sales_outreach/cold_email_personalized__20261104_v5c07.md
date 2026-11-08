# Mercury 2.5 — sales_outreach/cold_email_personalized

- model_id: `inception/mercury-2.5`
- success: True  | final: 8.45 | quality: 8.0
- latency_total: 0.959s | tokens_per_second: 137.6
- input_tokens: 202 | output_tokens: 132

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

Subject: Escalar contenido sin más hires

Hola Maria,

Vi tu post en LinkedIn sobre escalar contenido sin contratar. Como Head of Marketing en FintechCo, estoy segura de que ese es un reto constante con el crecimiento de la Serie A.

Nuestra herramienta de automatización con IA ayuda a startups fintech a generar y distribuir contenido a escala, manteniendo la voz de la marca sin aumentar el equipo. Ya estamos viendo resultados interesantes en empresas de tu etapa en LatAm.

¿Te gustaría una demo de 15 minutos la próxima semana para ver cómo funcionaría para FintechCo?

Saludos,
[Tu Nombre]