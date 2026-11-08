# Claude Sonnet 5.5 — sales_outreach/cold_email_personalized

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 7.28 | quality: 8.0
- latency_total: 7.654s | tokens_per_second: 104.9
- input_tokens: 299 | output_tokens: 803

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

**Subject:** Tu post sobre escalar contenido sin contratar

Hola María,

Leí tu post sobre cómo escalar content marketing sin ampliar el equipo. Es un dilema que se repite mucho en startups después de una Serie A: hay presión por producir más, pero no siempre por contratar más.

Me quedé con una pregunta: en FintechCo, ¿dónde se va hoy más tiempo, en investigación, redacción o distribución?

Lo pregunto porque trabajamos con equipos de marketing de startups automatizando justo esa parte con IA, y hemos visto un patrón que casi nadie espera en los primeros 30 días.

¿Te parece una llamada de 15 minutos esta semana o la próxima para contarte qué encontramos? Si te va mejor, dime martes o jueves y me adapto.

Saludos,
[Tu nombre]
[Empresa]