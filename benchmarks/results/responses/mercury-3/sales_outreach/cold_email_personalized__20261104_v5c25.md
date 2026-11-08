# Mercury 3 — sales_outreach/cold_email_personalized

- model_id: `inception/mercury-3`
- success: True  | final: 8.45 | quality: 8.0
- latency_total: 0.848s | tokens_per_second: 226.4
- input_tokens: 204 | output_tokens: 192

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

**Subject:** Tu post sobre escalar content marketing

Maria,

Tu post sobre escalar content marketing sin contratar me hizo pensar en algo concreto: la mayoría de startups en Serie A terminan quemando presupuesto en herramientas que prometen automatización pero exigen más gestión humana.

Nosotros construimos una herramienta que genera contenido listo para publicar (blog, LinkedIn, email) con IA, adaptado a tu voz de marca, y se integra con tu stack actual. No es un "contenido genérico" — es contenido que pasa por tu revisión en minutos, no horas.

Vi que FintechCo está en plena expansión de contenido. Me encantaría mostrarte cómo una startup de 50 personas puede producir el equivalente a un equipo de 5 sin contratar a nadie.

¿Tienes 15 minutos esta semana para una llamada rápida?

Saludos,
[Tu Nombre]