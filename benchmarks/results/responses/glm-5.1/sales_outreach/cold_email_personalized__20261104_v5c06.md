# GLM-5.1 — sales_outreach/cold_email_personalized

- model_id: `z-ai/glm-5.1`
- success: True  | final: 7.52 | quality: 8.0
- latency_total: 4.376s | tokens_per_second: 27.0
- input_tokens: 187 | output_tokens: 118

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

Subject: Escalar contenido sin contratar (tu post de LinkedIn)

Hola Maria,

Vi tu post en LinkedIn sobre escalar content marketing sin aumentar headcount. Tener 50 personas en Serie A exige optimizar recursos al máximo.

Acabamos de ayudar a una fintech similar en Colombia a triplicar su output de contenido usando automatización con IA, sin tocar su equipo actual. Literalmente hacen en horas lo que antes les tomaba semanas.

¿Tienes 15 minutos el próximo martes para ver cómo encajaría esto en el radar de FintechCo?