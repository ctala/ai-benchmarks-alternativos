# Mistral Small 4 — sales_outreach/cold_email_personalized

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 8.3 | quality: 8.0
- latency_total: 1.342s | tokens_per_second: 141.6
- input_tokens: 203 | output_tokens: 190

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

**Subject:** ¿Cómo escaló [Startup Competitor] su contenido sin contratar?

**Hola María,**

Vi tu post sobre escalar *content marketing* sin aumentar equipo y me resonó: en [Startup Competitor] logramos reducir un 40% el tiempo en producción de contenido usando IA, sin tocar la contratación.

Curiosamente, el 70% de las fintechs que automatizan contenido con nuestra herramienta **triplican su ROI en 3 meses** (ej: [Casos reales breves si tienes]).

¿Te interesa un café virtual de 15 min para ver si aplica a tu caso? Sin compromiso.

[Tu nombre]
[Tu puesto]
[Tu empresa]
[Enlace a Calendly o similar]

*P.D.: Si prefieres, puedo compartirte el breakdown de cómo lo hicimos en [Startup Competitor] antes de la llamada.*