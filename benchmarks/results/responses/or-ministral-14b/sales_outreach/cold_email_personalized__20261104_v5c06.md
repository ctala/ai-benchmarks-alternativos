# Ministral 14B — sales_outreach/cold_email_personalized

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 7.7 | quality: 8.0
- latency_total: 6.205s | tokens_per_second: 40.0
- input_tokens: 191 | output_tokens: 248

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

**Subject:** María, tu post sobre escalar *sin contratar* me hizo pensar en esto

---
**Hola María,**

Vi tu post sobre escalar el content marketing sin aumentar el equipo y me llamó la atención cómo destacaste lo crítico que es **automatizar procesos sin perder calidad** (algo que en startups como FintechCo debe ser clave).

En [Nombre de tu empresa], ayudamos a equipos como el tuyo a **generar contenido personalizado a escala** usando IA, pero sin que parezca robótico. Por ejemplo, [Startup X] redujo su tiempo en un 70% en campañas de email + redes.

¿Te apetece una llamada de 15 min la próxima semana para ver si encaja con lo que buscas? Sin compromiso, solo ideas.

Un saludo,
[Tu nombre]
[Tu cargo]
[Enlace a calendario o "Responde con tu disponibilidad"]

---
*P.D.: Si prefieres, puedo enviarte un caso concreto de una fintech que usó la herramienta para [resultado específico, ej. "aumentar leads en LinkedIn un 40% con posts semanales"].*