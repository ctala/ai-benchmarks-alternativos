# Grok 4.7 — sales_outreach/cold_email_personalized

- model_id: `x-ai/grok-4.7`
- success: True  | final: 7.1 | quality: 8.0
- latency_total: 6.471s | tokens_per_second: 46.1
- input_tokens: 1415 | output_tokens: 298

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

Subject: Escalar content sin contratar — una idea corta

Maria,

Vi tu post de la semana pasada sobre escalar content marketing sin sumar headcount. En una fintech Serie A de ~50 personas, esa tensión suele aparecer justo cuando el pipeline pide más contenido y el equipo de marketing no puede crecer al mismo ritmo.

Trabajamos con startups en una forma de producir y adaptar contenido con IA sin convertir el proceso en un segundo trabajo. No es “más posts”: es menos fricción entre idea, borrador y publicación.

¿Te encaja una call de 15 min esta semana para ver si aplica a FintechCo? Si no, lo dejamos ahí.