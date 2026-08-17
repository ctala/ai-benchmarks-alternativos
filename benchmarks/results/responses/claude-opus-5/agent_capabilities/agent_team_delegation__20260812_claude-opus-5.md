# Claude Opus 5 — agent_capabilities/agent_team_delegation

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.99 | quality: 9.8
- latency_total: 22.166s | tokens_per_second: 68.7
- input_tokens: 1660 | output_tokens: 1523
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente estructurada, ofreciendo un plan detallado que un emprendedor podría usar directamente.

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

## Plan de ejecución

Antes de delegar, dejo claro el grafo de dependencias para no bloquear a nadie:

| Wave | Agente / Acción | Depende de |
|------|-----------------|-----------|
| **0** | Recolección de contexto interno (KB: producto, pricing) + `researcher` (3 competidores) | — |
| **1** | `writer` (hero, features, pricing, CTA) | Wave 0 |
| **2** | `coder` (HTML/CSS) + `designer` (hero + feature images) — **en paralelo**, ambos con el copy final | Wave 1 |
| **3** | `reviewer` (QA de copy, código, accesibilidad, assets) | Wave 2 |
| **4** | Publicación (con aprobación humana) | Wave 3 |

Puntos críticos que vigilo: el **pricing** no puede inventarse (necesita dato real o aprobación), y el `designer`/`coder` deben compartir el mismo sistema visual para que los assets encajen en el layout.

Arranco Wave 0 — todo en paralelo porque no hay dependencias entre estas tres llamadas: