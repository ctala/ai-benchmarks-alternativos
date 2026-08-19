# Qwen 3.8 27B — sales_outreach/cold_email_personalized

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 6.85 | quality: 8.0
- latency_total: 84.307s | tokens_per_second: 8.8
- input_tokens: 234 | output_tokens: 741

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



Subject: Escalar contenido sin contratar

Hola Maria,

Tu post sobre escalar content marketing sin contratar me hizo pensar en FintechCo.

En startups fintech, el cuello de botella suele ser convertir insights de producto en contenido repetible, no solo producir más posts.

Una herramienta que automatiza ese flujo puede ayudar a mantener cadencia sin sumar headcount.

¿Te interesa ver cómo se aplica a un caso fintech en 15 min?

Saludos,
[Tu nombre]