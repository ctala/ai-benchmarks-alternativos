# Gemini 3.1 Flash Lite (GA) — sales_outreach/cold_email_personalized

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 8.1 | quality: 8.0
- latency_total: 1.565s | tokens_per_second: 99.1
- input_tokens: 172 | output_tokens: 155

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

Subject: Escalar el contenido en FintechCo

Hola Maria,

Leí tu post de la semana pasada sobre cómo escalar el marketing de contenidos sin aumentar el headcount. Coincido plenamente: en una Serie A, la eficiencia es la única forma de mantener el ritmo sin sacrificar calidad.

He ayudado a otras startups fintech a automatizar la producción de contenido técnico y de blog usando IA, reduciendo el tiempo de creación en un 70% sin perder el tono editorial.

¿Te interesaría ver cómo lo estamos implementando para que tu equipo pueda enfocarse en estrategia en lugar de ejecución operativa?

Si tienes 15 minutos la próxima semana, me encantaría compartirte un par de ideas.

Saludos,

[Tu Nombre]