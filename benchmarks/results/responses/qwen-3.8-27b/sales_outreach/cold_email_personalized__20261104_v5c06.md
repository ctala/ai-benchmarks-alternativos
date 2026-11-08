# Qwen 3.8 27B — sales_outreach/cold_email_personalized

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 7.71 | quality: 8.0
- latency_total: 4.56s | tokens_per_second: 34.0
- input_tokens: 198 | output_tokens: 155

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

Asunto: Sobre escalar sin contratar

Hola, María:

Leí tu post sobre escalar content marketing sin contratar más gente. Dado que FintechCo está en Serie A, ese margen de maniobra se estrecha rápido.

En lugar de añadir más recursos humanos, usamos IA para automatizar el 70% del flujo de contenido, manteniendo la voz de marca. Esto permite a equipos de ~50 personas operar con la capacidad de uno de 150, sin diluir la calidad.

¿Te interesa ver cómo otros startups fintech en la región han aplicado esto en las últimas 4 semanas?

Quedo atento a una llamada de 15 min.

Saludos,

[Tu Nombre]