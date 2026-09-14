# Muse Spark 1.3 — agent_capabilities/agent_team_delegation

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 5.75 | quality: 5.76
- latency_total: 7.698s | tokens_per_second: 157.2
- input_tokens: 1401 | output_tokens: 1210
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con una estructura útil para la delegación de tareas, aunque podría profundizar más en detalles específicos de cada tarea.

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

Decomposing landing page tasks with dependencies and priorities for five agents before delegation.