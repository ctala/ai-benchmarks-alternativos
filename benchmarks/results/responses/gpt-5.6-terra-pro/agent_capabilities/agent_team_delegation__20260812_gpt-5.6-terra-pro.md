# GPT-5.6 Terra Pro — agent_capabilities/agent_team_delegation

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 8.3 | quality: 9.8
- latency_total: 19.727s | tokens_per_second: 122.5
- input_tokens: 5341 | output_tokens: 2416
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, ofreciendo un plan detallado que un emprendedor podría seguir directamente.

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

Plan de ejecución:

1. **Researcher** analizará 3 competidores relevantes y extraerá patrones de posicionamiento, funcionalidades, precios y CTAs.
2. **Designer** definirá y creará los assets visuales (hero y recursos de features) con una dirección visual SaaS moderna orientada a startups.
3. Con la investigación disponible, **Writer** redactará el copy completo de la landing: hero, beneficios, features, pricing y CTAs.
4. Con copy y dirección visual, **Coder** implementará una landing HTML/CSS responsive.
5. **Reviewer** realizará una revisión final de coherencia, UX, copy, accesibilidad y posibles errores antes de dejarla lista para publicar.

Primero ejecutaré en paralelo la investigación competitiva y la dirección/creación visual; después encadenaré copy, desarrollo y QA respetando sus dependencias.