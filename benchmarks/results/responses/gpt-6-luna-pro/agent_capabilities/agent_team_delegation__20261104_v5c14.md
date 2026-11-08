# GPT-6 Luna Pro — agent_capabilities/agent_team_delegation

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 8.49 | quality: 9.5
- latency_total: 17.932s | tokens_per_second: 92.2
- input_tokens: 3982 | output_tokens: 1654
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un plan estructurado que un emprendedor podría implementar directamente.

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
1. **Investigación** de tres competidores y sus posicionamientos, funciones y precios públicos, para fundamentar la propuesta de AutoFlow AI.
2. **Confirmación de producto**: en paralelo, pediré los datos que no conviene inventar (precios, capacidades, marca y destino del CTA).
3. Con esos insumos, encargaré el **copy** al writer y los **assets visuales** al designer.
4. Cuando estén listos, el coder integrará copy y assets en HTML/CSS responsive.
5. Un reviewer revisará coherencia, afirmaciones, accesibilidad y calidad antes de considerar la página lista para publicar.

Primero inicio la investigación y solicito las definiciones de producto necesarias; respetaré esa dependencia antes de encargar el copy final.