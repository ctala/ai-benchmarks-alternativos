# Qwen 3.7 Max — sales_outreach/cold_email_personalized

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 7.4 | quality: 8.0
- latency_total: 5.01s | tokens_per_second: 31.5
- input_tokens: 198 | output_tokens: 158

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

Asunto: Escalar contenido sin contratar (tu post)

Maria,

Tu post de la semana pasada sobre escalar content marketing sin aumentar el headcount resonó mucho. Es el desafío exacto tras levantar una Serie A: la presión por crecer choca con la realidad operativa de un equipo de 50.

Hemos desarrollado una automatización con IA diseñada específicamente para startups fintech en esta etapa, permitiendo multiplicar la producción manteniendo la calidad y sin nuevas contrataciones. No es una herramienta genérica, sino una solución al cuello de botella que describiste.

¿Tendrías 15 minutos este jueves para mostrarte cómo funciona en un contexto como el de FintechCo?

Saludos,

[Tu Nombre]