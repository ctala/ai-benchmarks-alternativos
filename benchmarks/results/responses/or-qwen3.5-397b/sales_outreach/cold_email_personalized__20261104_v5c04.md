# Qwen 3.5 397B — sales_outreach/cold_email_personalized

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 7.63 | quality: 8.0
- latency_total: 3.771s | tokens_per_second: 42.2
- input_tokens: 198 | output_tokens: 159

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

Leí tu post en LinkedIn sobre el desafío de escalar la estrategia de contenidos en FintechCo sin expandir la plantilla. Es justo la barrera que frenan a muchas startups en Serie A al intentar mantener la consistencia.

Nuestra herramienta de automatización con IA está diseñada específicamente para resolver esa ecuación: permite multiplicar la producción de activos relevantes manteniendo el equipo actual. No se trata de reemplazar creativos, sino de eliminar el trabajo manual repetitivo que consume sus horas.

¿Te vendría bien una llamada de 15 minutos el jueves para mostrarte cómo otras fintechs latinas están aplicando este modelo?

Saludos,

[Tu Nombre]