# Gemini 3.8 Flash — sales_outreach/cold_email_personalized

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 7.44 | quality: 8.0
- latency_total: 7.027s | tokens_per_second: 138.7
- input_tokens: 172 | output_tokens: 975

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

Asunto: Escalar contenido en FintechCo sin contratar

Hola María,

Leí tu post de la semana pasada sobre el reto de escalar content marketing sin sumar headcount. Diste en el clavo: para una fintech en Serie A, educar al usuario suele chocar de frente con la capacidad del equipo.

Ayudamos a startups en tu misma etapa a triplicar su producción de contenido técnico mediante flujos de IA que replican su tono de marca, sin contratar redactores ni sacrificar calidad. 

¿Tendrías 15 minutos este jueves para mostrarte cómo lo están resolviendo equipos similares en la región?

Saludos,

[Tu Nombre]