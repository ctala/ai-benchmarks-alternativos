# Gemini 3.6 Flash — sales_outreach/cold_email_personalized

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 7.44 | quality: 8.0
- latency_total: 6.296s | tokens_per_second: 158.0
- input_tokens: 174 | output_tokens: 995

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

**Asunto:** Escalar contenido en FintechCo sin contratar

María,

Leí tu post de la semana pasada sobre cómo escalar el marketing de contenidos sin aumentar el headcount. Me pareció un enfoque muy acertado para la etapa actual de FintechCo.

Ayudamos a startups Serie A a ejecutar justamente esa estrategia: automatizamos la investigación, redacción y distribución de contenido con IA, manteniendo el tono técnico que exige el sector fintech.

Equipos de marketing similares al tuyo están multiplicando su producción x3 sin sumar contrataciones.

¿Tienes 15 minutos este jueves para mostrarte cómo funcionaría directamente con el contenido de FintechCo?

Un saludo,

[Tu Nombre]