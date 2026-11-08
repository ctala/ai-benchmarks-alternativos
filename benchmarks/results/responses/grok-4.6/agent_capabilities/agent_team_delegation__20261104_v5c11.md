# Grok 4.6 — agent_capabilities/agent_team_delegation

- model_id: `x-ai/grok-4.6`
- success: True  | final: 8.12 | quality: 9.52
- latency_total: 15.955s | tokens_per_second: 66.9
- input_tokens: 1122 | output_tokens: 1068
- judge_score: 4.8 | justificación: 

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

Descompongo el lanzamiento de la landing de **AutoFlow AI** en 4 fases, respetando dependencias:

| Fase | Agente | Qué hace | Prioridad | Depende de |
|------|--------|----------|-----------|------------|
| 1 | `researcher` + knowledge base | Competidores (3) y ficha interna del producto | urgent | — |
| 2a | `writer` | Copy: hero, features, pricing, CTA | high | Fase 1 |
| 2b | `designer` | Imágenes hero y features | high | Fase 1 (brief) |
| 3 | `coder` | HTML/CSS de la landing | high | 2a + 2b |
| 4 | `reviewer` | QA de copy, código y assets antes de publicar | high | Fase 3 |

**Paralelismo:** writer y designer arrancan juntos cuando exista el brief competitivo. El coder espera copy + assets. El reviewer es el último filtro.

Empiezo ya la Fase 1: busco en la base de productos y delego la investigación de competencia.