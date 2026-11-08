# Qwen 3.6 27B base (OpenRouter FP8) — sales_outreach/cold_email_personalized

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 7.75 | quality: 8.0
- latency_total: 4.202s | tokens_per_second: 36.7
- input_tokens: 198 | output_tokens: 154

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

Asunto: Escalar sin contratar (tu post de LinkedIn)

Hola Maria,

Leí tu post sobre escalar content marketing sin aumentar la nómina. Totalmente de acuerdo: en una Serie A como FintechCo, cada hora dedicada a crear contenido es una hora no invertida en estrategia o producto.

Ayudamos a startups fintech a automatizar la producción de contenido con IA, manteniendo el tono de marca pero eliminando la carga operativa. El resultado suele ser un aumento del 3x en volumen de publicaciones sin necesidad de nuevos headcounts.

Me gustaría mostrarte cómo funciona en 15 minutos. ¿Te parece bien si agendamos una breve llamada la próxima semana?

Saludos,

[Tu Nombre]