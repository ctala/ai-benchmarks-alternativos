# LFM-3 1.7B — agent_capabilities/agent_team_delegation

- model_id: `liquid/lfm-3-1.7b`
- success: True  | final: 8.34 | quality: 8.4
- latency_total: 4.864s | tokens_per_second: 286.2
- input_tokens: 924 | output_tokens: 1392
- judge_score: 4.0 | justificación: 

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

We need to coordinate a landing page creation for "AutoFlow AI" product. The user lists tasks:

1. Investigate competition (3 competitors)
2. Write copy of landing (hero, features, pricing, CTA) -> writer
3. Generate HTML/CSS code -> coder
4. Create hero and feature images -> designer
5. Review everything before publishing -> reviewer

We have 5 sub-agents: researcher, writer, coder, reviewer, designer.

We must break down tasks into sub-tasks per agent, respect dependencies (writer needs data from researcher first; maybe coder needs writer's copy? Typically yes). Also assign priorities.

Plan:
- Researcher: find info on AutoFlow AI competitor landscape. Need to identify 3 competitors. Use search_knowledge_base or maybe we can do web research? There's no direct tool for web search but there is `search_knowledge_base`. Might be internal docs. Could also use `delegate_to_agent` to assign to researcher. Let's see tools: `search_knowledge_base(query, collection)`. We'll likely need to query "competitors AutoFlow AI" or similar. But we don't know exact collection. Maybe "docs", "faq", "policies", "products". Not sure. Possibly we can just delegate to researcher to gather that info.

- Writer: write copy based on gathered data. Depends on researcher output.

- Coder: generate HTML/CSS. May depend on writer's copy.

- Designer: create images hero and features. Depends on writer's copy and maybe visual direction.

- Reviewer: review all before publish. Likely after others produce.

Thus we should orchestrate steps sequentially with delegation calls.

Let's start by delegating the researcher task: "Investigar que hace la competencia (3 competidores)" for AutoFlow AI. Use `delegate_to_agent` with agent_type "researcher", task description, context "landing page for AutoFlow AI startup automation tool", priority maybe medium/high. Then wait for result? In this environment, we might not get immediate results but we can simulate by calling appropriate functions. However we cannot actually run external searches. So we may need to ask human? Usually in these prompts, we are expected to outline plan and possibly call tools. Since we lack actual knowledge base, we could use `search_knowledge_base` with query "AutoFlow AI competitors". That might return something. Let's try using `search_knowledge_base` with query "AutoFlow AI competitors" and collection "docs"? Or maybe "products"? Not sure. I think best approach: Use `delegate_to_agent` to assign to researcher, then later we will get output. But as an assistant, we can propose next steps and perhaps ask for clarification if needed.

Given the instruction: "Descompone tareas complejas en sub-tareas para cada agente. Respeta dependencias (el writer necesita los datos del researcher primero)". So we need to explicitly state decomposition.

Thus I'll design a plan:

**Overall Plan:**

- Phase 1: Research Competitors.
   - Sub-task: Identify top 3 competitors in AI automation for startups. Search market reports, news, etc. Use researcher.

- Phase 2: Draft Landing Copy.
   - Sub-task: Write hero section, features list, pricing tiers, CTA. Use writer, inputting data from phase 1.

- Phase 3: Code Generation.
   - Sub-task: Generate HTML/CSS skeleton and integrate copy. Use coder, depends on writer's copy.

- Phase 4: Visual Assets.
   - Sub-task: Create hero image and feature images. Use designer, based on copy and brand guidelines.

- Phase 5: Review & Publish.
   - Sub-task: Full review for quality, errors, consistency. Use reviewer.

Assign priorities: Researcher high (needs data), Writer medium-high, Coder medium, Designer medium, Reviewer high (before publish).

Now implement via tool calls:

First, delegate researcher task: `delegate_to_agent(agent_type="researcher", task="Investigar las tres principales competidoras de la herramienta AutoFlow AI (automatización para startups)", context="Para crear una landing page de AutoFlow AI", priority="high")`.

Second, after researcher returns data, we would delegate writer: `delegate_to_agent(agent_type="writer", task="Redactar copy de la landing page: hero, features, pricing, CTA basado en la investigación de competidores", context="Utilizar hallazgos del researcher", priority="medium")`.

Third, coder: `delegate_to_agent(agent_type="coder", task="Generar código HTML/CSS para la landing page usando el copy escrito", context="Del escritor", priority="medium")`.

Fourth, designer: `delegate_to_agent(agent_type="designer", task="Crear imágenes hero y de features para la landing page", context="Basado en copy y branding de AutoFlow AI", priority="medium")`.

Fifth, reviewer: `delegate_to_agent(agent_type="reviewer", task="Revisar todo (HTML, copy, imágenes) antes de publicar", context="Todos los agentes anteriores", priority="high")`.

But we need to ensure dependencies: writer waits for researcher; coder waits for writer; designer maybe independent but uses copy; reviewer last.

Thus we can issue sequential delegation calls. However, we can only make one tool call at a time? Usually we can chain. Let's start with researcher.

I'll use `delegate_to_agent` for each step. Perhaps combine multiple tasks? The function signature requires agent_type and task; optional context and priority. So we can include them.

Proceed:

Call 1: researcher.

Then after response, we'd proceed to writer, etc. Since we can't get real responses, we can still structure the plan and indicate next steps. But the instructions say "Coordinalo todo." So we should provide a coordinated execution plan, maybe also initiate the first delegation.

Thus I'll start by delegating the researcher task.