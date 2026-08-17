# Nemotron 3.5 Lightning — agent_capabilities/agent_team_delegation

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 7.32 | quality: 6.82
- latency_total: 2.215s | tokens_per_second: 104.3
- input_tokens: 1350 | output_tokens: 231
- judge_score: 3.8 | justificación: 

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

We need to coordinate the tasks. We'll need to delegate to researcher, writer, coder, designer, reviewer. We should explain plan. Then start delegating. Probably start with researcher. Then after researcher results, give to writer. Then coder uses that copy. Then designer creates images (maybe need to describe). Then reviewer reviews. We'll need to use delegate_to_agent calls. We'll need to pass context and priority.

We need to output plan first. Then we can start calls. Probably need to call researcher first. Let's do that.