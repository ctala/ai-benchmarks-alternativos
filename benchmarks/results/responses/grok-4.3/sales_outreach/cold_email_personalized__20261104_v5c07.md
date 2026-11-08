# Grok 4.3 — sales_outreach/cold_email_personalized

- model_id: `x-ai/grok-4.3`
- success: True  | final: 7.48 | quality: 8.0
- latency_total: 3.023s | tokens_per_second: 29.1
- input_tokens: 356 | output_tokens: 88

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

Subject: tu post sobre escalar content sin contratar

Maria,

Vi tu post sobre escalar content marketing sin contratar más gente. En una startup en etapa Serie A, entiendo que cada hire cuenta.

Mi equipo ha estado probando una forma diferente de resolver ese mismo problema: automatizar el 80% del contenido con IA manteniendo voz de marca.

¿Te interesaría 15 minutos para ver si esto aplica a FintechCo?