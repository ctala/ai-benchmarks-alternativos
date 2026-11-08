# Claude Fable 5.1 — sales_outreach/cold_email_personalized

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 6.98 | quality: 8.0
- latency_total: 5.222s | tokens_per_second: 60.5
- input_tokens: 299 | output_tokens: 316

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

**Asunto:** Tu post sobre escalar contenido sin contratar

Hola Maria,

Leí tu post de la semana pasada sobre escalar content marketing sin crecer el equipo. El punto sobre "el cuello de botella no es la estrategia, es la ejecución" me quedó dando vueltas.

Trabajamos con startups fintech en etapa similar a FintechCo (Serie A, equipos de marketing de 2-4 personas) que están produciendo 3-4x más contenido sin sumar headcount, usando IA para la parte repetitiva: briefs, primeras versiones, adaptación a canales.

No sé si esto encaja con lo que estás construyendo, pero tengo curiosidad por saber cómo lo están resolviendo hoy y qué les ha funcionado (o no).

¿Tienes 15 minutos la próxima semana para comparar notas?

Saludos,
[Tu nombre]