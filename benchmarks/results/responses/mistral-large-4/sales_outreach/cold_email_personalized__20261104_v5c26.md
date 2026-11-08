# Mistral Large 4.0 — sales_outreach/cold_email_personalized

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 7.34 | quality: 8.0
- latency_total: 11.879s | tokens_per_second: 170.4
- input_tokens: 186 | output_tokens: 2024

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

Subject: Tu post sobre escalar content sin contratar

Hola Maria,

Vi tu publicación de la semana pasada sobre cómo escalar content marketing sin sumar headcount. Con 50 personas en FintechCo y en Serie A, seguramente ese balance entre volumen y calidad es el desafío constante.

Estamos trabajando con startups fintech similares que lograron triplicar su producción de contenido sin agregar escritores — usando IA para los primeros borradores y automatizando la distribución.

¿Te interesa una call de 15 min la semana que viene para ver si encaja con lo que están armando?

Saludos,
[Tu nombre]