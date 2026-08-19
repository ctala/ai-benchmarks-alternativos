# Llama 4 Maverick — agent_capabilities/agent_team_delegation

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 8.13 | quality: 9.5
- latency_total: 95.488s | tokens_per_second: 7.2
- input_tokens: 1365 | output_tokens: 686
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza adecuadamente en la delegación de tareas, ofreciendo un plan detallado que un emprendedor podría usar directamente.

## Respuesta completa

¡Claro! Para crear la landing page para "AutoFlow AI", voy a descomponer la tarea en sub-tareas para cada agente y explicar el plan de ejecución.

**Plan de Ejecución:**

1. **Investigar la competencia**: El agente `researcher` investigará qué hacen los 3 competidores principales en el mercado de herramientas de automatización para startups.
2. **Escribir el copy de la landing**: Una vez que tengamos la información de la competencia, el agente `writer` escribirá el copy para la landing page, incluyendo el hero, features, pricing y CTA.
3. **Crear las imágenes**: El agente `designer` creará las imágenes hero y de features para la landing page.
4. **Generar el código HTML/CSS**: El agente `coder` generará el código HTML/CSS para la landing page utilizando el copy y las imágenes creadas.
5. **Revisar todo**: Finalmente, el agente `reviewer` revisará todo el contenido y el código antes de publicar.

**Delegación de Tareas:**

1. [delegate_to_agent(agent_type=researcher, task="Investigar 3 competidores principales en herramientas de automatización para startups y analizar sus estrategias de marketing", priority=high)]
2. Una vez que el researcher complete su tarea, [delegate_to_agent(agent_type=writer, task="Escribir el copy para la landing page de AutoFlow AI incluyendo hero, features, pricing y CTA", context="Información de la competencia", priority=high)]
3. Paralelamente a la tarea del writer, [delegate_to_agent(agent_type=designer, task="Crear imágenes hero y de features para la landing page de AutoFlow AI", priority=medium)]
4. Una vez que el writer y el designer completen sus tareas, [delegate_to_agent(agent_type=coder, task="Generar código HTML/CSS para la landing page de AutoFlow AI", context="Copy e imágenes creadas", priority=high)]
5. Finalmente, [delegate_to_agent(agent_type=reviewer, task="Revisar todo el contenido y código de la landing page antes de publicar", priority=urgent)]

**Funciones a invocar:**

1. [delegate_to_agent(agent_type=researcher, task="Investigar 3 competidores principales en herramientas de automatización para startups y analizar sus estrategias de marketing", priority=high)]
2. [delegate_to_agent(agent_type=writer, task="Escribir el copy para la landing page de AutoFlow AI incluyendo hero, features, pricing y CTA", context="Información de la competencia", priority=high)]
3. [delegate_to_agent(agent_type=designer, task="Crear imágenes hero y de features para la landing page de AutoFlow AI", priority=medium)]
4. [delegate_to_agent(agent_type=coder, task="Generar código HTML/CSS para la landing page de AutoFlow AI", context="Copy e imágenes creadas", priority=high)]
5. [delegate_to_agent(agent_type=reviewer, task="Revisar todo el contenido y código de la landing page antes de publicar", priority=urgent)]

Comenzaré invocando la primera función: [delegate_to_agent(agent_type=researcher, task="Investigar 3 competidores principales en herramientas de automatización para startups y analizar sus estrategias de marketing", priority=high)]