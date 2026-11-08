# Muse Wonder — agent_capabilities/agent_team_delegation

- model_id: `meta/muse-wonder`
- success: True  | final: 6.15 | quality: 6.85
- latency_total: 11.052s | tokens_per_second: 113.5
- input_tokens: 1331 | output_tokens: 1254
- judge_score: 4.0 | justificación: La respuesta es relevante y clara, desglosando las tareas y considerando las dependencias, pero carece de detalles específicos y profundidad en la ejecución de cada tarea.

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

Descomponiendo la creación de la landing page en sub-tareas y asignando dependencias a los cinco sub-agentes.Secuenciando las delegaciones para respetar dependencias y permitir tareas paralelas sin violar el orden.