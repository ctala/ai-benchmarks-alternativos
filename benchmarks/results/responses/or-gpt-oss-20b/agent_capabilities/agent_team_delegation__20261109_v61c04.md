# GPT-OSS 20B — agent_capabilities/agent_team_delegation

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.52 | quality: 7.1
- latency_total: 1.596s | tokens_per_second: 89.0
- input_tokens: 684 | output_tokens: 142
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante, clara y útil, con una estructura adecuada para coordinar tareas, aunque carece de algunos insights más profundos.

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

We need to coordinate tasks. Outline plan: researcher gather competitor info; writer craft copy; coder produce HTML/CSS; designer create hero and feature images; reviewer review all. Map priorities: researcher high priority to get data. So delegate tasks sequentially with dependencies.

We will need to call delegate_to_agent function multiple times. We'll do researcher first. We'll set task details. Then proceed.

We'll explain plan then delegate.