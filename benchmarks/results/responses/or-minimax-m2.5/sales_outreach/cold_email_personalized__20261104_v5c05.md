# MiniMax M2.5 — sales_outreach/cold_email_personalized

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 7.88 | quality: 8.0
- latency_total: 3.384s | tokens_per_second: 94.8
- input_tokens: 183 | output_tokens: 321

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

**Subject:** Tu post sobre escalar sin contratar

Hola Maria,

Vi tu post sobre escalar content marketing sin contratar y me quedé pensando: ¿cómo lo están manejando hoy con un equipo de marketing pequeño en FintechCo?

We internally use AI to automate content creation at early-stage startups. Basically, one person puede generar lo que hoy produce un equipo entero.

No te vendo nada. Solo quiero entender si el problema de volumen de contenido es algo que te quita el sueño.

¿Te parece si hablamos 15 minutos esta semana?

Saludos,
[Tu nombre]