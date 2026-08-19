# Gemma 4 31B — sales_outreach/cold_email_personalized

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 8.15 | quality: 8.0
- latency_total: 1.89s | tokens_per_second: 57.1
- input_tokens: 191 | output_tokens: 108

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

Asunto: Escalar el contenido de FintechCo

Hola Maria,

Leí tu post de la semana pasada sobre cómo escalar el content marketing sin ampliar el equipo. Me llamó la atención tu enfoque, especialmente considerando que están en plena fase de Serie A.

He ayudado a otras startups fintech a automatizar la producción de contenido mediante IA, logrando el volumen de un equipo grande sin aumentar la nómina.

¿Tendrías 15 minutos el jueves para mostrarte cómo podrías aplicar esto en FintechCo?