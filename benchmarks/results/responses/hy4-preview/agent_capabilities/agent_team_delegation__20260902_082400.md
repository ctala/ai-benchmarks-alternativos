# Tencent Hy4 preview — agent_capabilities/agent_team_delegation

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.46 | quality: 9.8
- latency_total: 24.77s | tokens_per_second: 50.5
- input_tokens: 1073 | output_tokens: 1251
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente estructurada, ofreciendo un plan de ejecución detallado que un emprendedor podría usar directamente.

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

Voy a descomponer el proyecto en 5 fases con sus dependencias:

| Fase | Agente | Depende de |
|---|---|---|
| 1 | **researcher** → análisis de 3 competidores | — |
| 1 | **designer** → imagen hero + imágenes de features | — |
| 2 | **writer** → copy (hero, features, pricing, CTA) | researcher |
| 3 | **coder** → HTML/CSS | writer + designer |
| 4 | **reviewer** → revisión final | todo |

Las fases 1 (researcher y designer) son **independientes**, así que las lanzo en paralelo paraahorrar tiempo. El writer arrancará en cuanto tenga el análisis competitivo, y el coder cuando tenga copy + assets.

Lanzando fase 1: