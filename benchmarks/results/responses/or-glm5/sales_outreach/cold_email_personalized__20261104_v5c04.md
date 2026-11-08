# GLM 5 — sales_outreach/cold_email_personalized

- model_id: `z-ai/glm-5`
- success: True  | final: 7.74 | quality: 8.0
- latency_total: 4.442s | tokens_per_second: 31.3
- input_tokens: 187 | output_tokens: 139

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

Subject: Escalar contenido en FintechCo sin contratar

Maria,

Vi tu post en LinkedIn sobre escalar content marketing sin aumentar la plantilla. Concuerdo: en etapa Serie A, el cuello de botella nunca es la falta de ideas, sino la ejecución.

En FintechCo ya tienen el equipo y el mensaje claros. Mi herramienta usa IA para automatizar justamente la parte pesada de la producción, permitiendo a un equipo de 50 personas publicar como si fueran 200, sin tocar el headcount.

¿Tienes 15 minutos el próximo martes para ver si esto encaja con lo que estás construyendo?