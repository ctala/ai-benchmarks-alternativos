# Gemma 4 26B MoE (3.8B activos) — sales_outreach/cold_email_personalized

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 7.85 | quality: 8.0
- latency_total: 4.324s | tokens_per_second: 31.0
- input_tokens: 191 | output_tokens: 134

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

Subject: Tu post sobre escalar contenido en FintechCo

Hola Maria,

Leí tu publicación de la semana pasada sobre cómo escalar el content marketing sin inflar la nómina; me pareció muy acertada la visión para startups en fase de Serie A.

Precisamente ayudamos a equipos de marketing como el de FintechCo a ejecutar esa estrategia mediante automatización de contenido con IA, permitiendo que un equipo pequeño produzca volumen de calidad sin necesidad de nuevas contrataciones.

¿Tendrías 15 minutos la próxima semana para mostrarte cómo estamos optimizando los tiempos de creación en otras fintechs?

Un saludo,

[Tu Nombre]