# Mistral Large 3 675B — sales_outreach/cold_email_personalized

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 7.93 | quality: 8.0
- latency_total: 2.411s | tokens_per_second: 59.3
- input_tokens: 191 | output_tokens: 143

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

**Subject:** Tu post sobre escalar content marketing sin contratar

María,

Vi tu post en LinkedIn sobre escalar content marketing sin aumentar el equipo. Coincido en que la automatización es clave, pero sé que herramientas genéricas no siempre se adaptan a las necesidades de una fintech en crecimiento (como FintechCo).

Por eso creamos [Nombre de tu herramienta]: IA que genera contenido alineado con tu tono de marca y objetivos, sin perder autenticidad. ¿Te interesa ver cómo lo hacemos en 15 minutos? Podemos agendar [enlace a calendario] cuando mejor te venga.

Saludos,
[Tu nombre]