# Llama 3.1 8B Instant — sales_outreach/cold_email_personalized

- model_id: `meta-llama/llama-3.1-8b-instruct`
- success: True  | final: 8.3 | quality: 8.0
- latency_total: 1.399s | tokens_per_second: 127.9
- input_tokens: 202 | output_tokens: 179

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

Asunto: "Me gustó tu post sobre escalando content marketing sin contratar"

Hola María,

Me alegró verte hablar sobre la importancia de escalar el content marketing sin necesidad de contratar, en tu último post en LinkedIn. Me parece que tienes una visión clara de la realidad de las startups como FintechCo.

En nuestra experiencia, vemos que la automatización del contenido con IA puede ser un aliado valioso para startups como la tuya, aliviando la carga de trabajo y permitiendo enfocarse en estrategias más creativas. Me gustaría compartir contigo cómo hemos ayudado a otras startups a lograr una mayor eficiencia en su contenido y cómo podría aplicarse a FintechCo.

¿Te gustaría hablar más sobre esto durante 15 minutos? 

Atentamente, [Tu nombre]