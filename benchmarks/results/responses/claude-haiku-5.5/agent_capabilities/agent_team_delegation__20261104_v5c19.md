# Claude Haiku 5.5 — agent_capabilities/agent_team_delegation

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.93 | quality: 9.8
- latency_total: 9.944s | tokens_per_second: 198.7
- input_tokens: 1662 | output_tokens: 1976
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza en la estructura de las fases de trabajo, ofreciendo un plan detallado que un emprendedor podría usar directamente.

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

## Plan de ejecución: landing de AutoFlow AI

Las tareas tienen dependencias, así que las organizo en cuatro fases:

- **Fase 1 (paralela, ahora):** El *researcher* analiza 3 competidores. El *designer* define la dirección visual (paleta, estilo, conceptos de imágenes hero y features), que no depende del copy.
- **Fase 2 (depende de Fase 1):** El *writer* redacta hero, features, pricing y CTA usando los hallazgos de la competencia. El *coder* prepara la estructura HTML/CSS y el sistema de diseño en paralelo.
- **Fase 3 (depende de Fase 2):** El *designer* produce las imágenes finales con el copy definitivo. El *coder* integra copy e imágenes en la página.
- **Fase 4 (depende de Fase 3):** El *reviewer* revisa copy, diseño, código, responsive y enlaces antes de publicar.

Para el *writer* necesito datos que no tengo, sobre todo el pricing. Lo pregunto ahora para no bloquear la fase 2.

Arranco la fase 1 y te pregunto por los datos que faltan: