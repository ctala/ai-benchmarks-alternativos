# Nemotron 3.5 Lightning — agent_capabilities/agent_team_delegation

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 7.47 | quality: 6.82
- latency_total: 1.298s | tokens_per_second: 250.4
- input_tokens: 1350 | output_tokens: 325
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

We need to coordinate sub-agents. First, explain plan. Then delegate tasks: researcher to investigate competitors, writer to copy, coder to HTML/CSS, designer to images, reviewer to review. Need dependencies: researcher first, then writer, then coder/designer concurrently, then reviewer last.

We must use delegate_to_agent for each task. Also possibly use run_skill? Not needed. We'll delegate.

We need to output plan then call delegate_to_agent for each. Probably sequence: researcher first with high priority. Then after researcher returns, we delegate writer with context from researcher. But as ChatGPT we can just issue delegations; maybe we need to wait for results? Not possible; we just delegate and maybe combine.

We'll explain plan then invoke delegate_to_agent for researcher, writer (maybe with placeholder), coder, designer, reviewer. Provide priorities.

Let's do it.