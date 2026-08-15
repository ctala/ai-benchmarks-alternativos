# Gemini 3.6 Flash — sales_outreach/cold_email_personalized

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 7.43 | quality: 8.0
- latency_total: 6.313s | tokens_per_second: 160.1
- input_tokens: 174 | output_tokens: 1011

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

Asunto: Tu post sobre escalar contenido sin contratar

Hola María,

Vi tu publicación de la semana pasada en LinkedIn sobre el reto de escalar el marketing de contenidos en FintechCo sin sumar headcount. Un desafío clave en fase Serie A.

Justo para resolver eso creamos una plataforma de IA que automatiza la generación y adaptación de contenido técnico en español, manteniendo la voz y autoridad de la marca. 

Permite que tu equipo actual multiplique por tres su volumen de publicación semanal sin dedicarle más horas ni descuidar la estrategia.

¿Tiene sentido conversar 15 minutos este jueves para mostrarte brevemente cómo lo están aplicando otras startups?

Un saludo,

[Tu Nombre]