# Mercury 2.5 — sales_outreach/cold_email_personalized

- model_id: `inception/mercury-2.5`
- success: True  | final: 8.3 | quality: 8.0
- latency_total: 1.615s | tokens_per_second: 691.6
- input_tokens: 198 | output_tokens: 1117

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



Subject: Tu post de LinkedIn: escalar contenido sin contratar

Hola María,

Vi tu post sobre escalar content marketing sin contratar. Es un desafío clave para FintechCo en Series A.

Hemos visto que equipos de marketing en fintech están generando 3x más contenido usando automatización con IA, sin añadir headcount. Un cliente en LATAM logró escalar su blog en 2 meses así.

¿Tienes 15 minutos esta semana para ver cómo lo hicieron?

Saludos,
[Tu Nombre]