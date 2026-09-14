# Gemini 3.8 Flash — sales_outreach/cold_email_personalized

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 7.45 | quality: 8.0
- latency_total: 8.552s | tokens_per_second: 106.2
- input_tokens: 172 | output_tokens: 908

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

**Asunto:** Escalar contenido en FintechCo (tu post)

María,

Leí tu post de la semana pasada sobre el reto de escalar content marketing sin inflar el equipo. Es el dilema clásico post-Serie A: triplicar el volumen orgánico para sostener el crecimiento, pero con el mismo headcount.

Ayudamos a startups fintech a multiplicar su producción de contenido técnico x4 usando flujos de IA entrenados con su propio tono de marca, liberándole unas 15 horas semanales al equipo. 

No pretendo venderte nada en frío; solo me gustaría mostrarte el framework que usamos y cómo lo están aplicando otras fintechs de la región.

¿Tendrías 15 minutos este jueves para ver si te hace sentido para FintechCo?