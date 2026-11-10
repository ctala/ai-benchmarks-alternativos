# Qwen 3.7 Flash — sales_outreach/cold_email_personalized

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 7.85 | quality: 8.0
- latency_total: 3.098s | tokens_per_second: 48.4
- input_tokens: 198 | output_tokens: 150

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

Subject: Tu post sobre escalar contenido sin contratar

Hola Maria,

Vi tu publicación de la semana pasada sobre cómo escalar el content marketing sin aumentar el headcount. Coincido totalmente: en una Serie A, cada hora debe generar valor directo.

Justamente por eso te escribo. Ayudamos a startups como FintechCo a automatizar la producción de contenido con IA, manteniendo la voz de marca pero reduciendo el tiempo de creación en un 70%.

No se trata de reemplazar la creatividad, sino de eliminar el cuello de botella operativo.

¿Tienes 15 minutos este jueves o viernes para ver una demo rápida de cómo funciona?

Un saludo,

[Tu Nombre]