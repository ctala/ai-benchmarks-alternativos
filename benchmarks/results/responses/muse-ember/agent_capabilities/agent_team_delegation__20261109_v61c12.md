# Muse Ember — agent_capabilities/agent_team_delegation

- model_id: `meta/muse-ember`
- success: True  | final: 8.31 | quality: 8.5
- latency_total: 2.072s | tokens_per_second: 416.4
- input_tokens: 1331 | output_tokens: 863
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una estructura detallada para investigar a la competencia, lo cual es esencial para el desarrollo de la landing page.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres el agente coordinador de un Agent Team. Tienes 5 sub-agentes:
- researcher: busca informacion y datos
- writer: redacta contenido
- coder: genera codigo y automatizaciones
- reviewer: revisa calidad y errores
- designer: crea assets visuales

Reglas:
- Descompone tareas complejas en sub-tareas para cada agente
- Respeta dependencias (el writer necesita los datos del researcher primero)
- Asigna prioridades correctamente
- Explica el plan de ejecucion antes de delegar

**user:**

Necesito crear una landing page para el lanzamiento de nuestro nuevo producto "AutoFlow AI" (herramienta de automatizacion para startups). Incluye:
1. Investigar que hace la competencia (3 competidores)
2. Escribir el copy de la landing (hero, features, pricing, CTA)
3. Generar el codigo HTML/CSS de la pagina
4. Crear las imagenes hero y de features
5. Revisar todo antes de publicar

Coordinalo todo.


## Respuesta completa

[tool_call] delegate_to_agent({"agent_type":"researcher","context":"Producto: AutoFlow AI, herramienta de automatización para startups. Objetivo: landing page de lanzamiento. Necesitamos diferenciación frente a competencia para guiar copy y diseño.","priority":"high","task":"Investiga 3 competidores directos de AutoFlow AI en el mercado de automatización para startups (ej. Make/Zapier, n8n, Activepieces o similares). Para cada uno entrega: nombre, posicionamiento/target, 3-5 features principales, modelo de pricing, propuesta de valor y debilidades/oportunidades que AutoFlow AI puede explotar. Cierra con 3 conclusiones accionables para nuestra landing (diferenciadores clave y mensajes recomendados)."})