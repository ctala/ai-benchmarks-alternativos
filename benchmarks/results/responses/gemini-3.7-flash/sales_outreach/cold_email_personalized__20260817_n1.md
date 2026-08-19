# Gemini 3.7 Flash — sales_outreach/cold_email_personalized

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 7.46 | quality: 8.0
- latency_total: 8.19s | tokens_per_second: 98.9
- input_tokens: 172 | output_tokens: 810

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

**Asunto:** Tu post sobre escalar contenido en FintechCo

Hola María,

Vi tu post de la semana pasada sobre el reto de escalar content marketing sin sumar headcount. Diste en el clavo, especialmente para la etapa post-Serie A en la que está FintechCo.

Estamos ayudando a startups fintech a triplicar su producción de contenido técnico mediante IA, manteniendo el control del tono de marca y sin contratar redactores adicionales. 

¿Tendrías 15 minutos este jueves para mostrarte cómo funciona el flujo y ver si les hace sentido?

Saludos,

[Tu Nombre]