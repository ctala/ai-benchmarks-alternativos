# Tencent Hy3 — sales_outreach/cold_email_personalized

- model_id: `tencent/hy3`
- success: True  | final: 7.55 | quality: 8.0
- latency_total: 6.095s | tokens_per_second: 27.2
- input_tokens: 215 | output_tokens: 166

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

Vi tu post de la semana pasada en LinkedIn sobre cómo escalar content marketing sin sumar cabeza a tu equipo en FintechCo. Justo el problema que más veo en startups Serie A en Colombia.

Construí una herramienta de IA que automatiza la producción de contenido para startups y está generando resultados interesantes en equipos de tu tamaño (50 personas, recursos limitados).

Me gustaría mostrarte en 15 minutos cómo otras fintechs están resolviendo eso sin romper el presupuesto. ¿Te acomoda un slot el jueves?

Saludos,
[Tu nombre]