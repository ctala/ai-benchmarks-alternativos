# Claude Sonnet 5 — agent_capabilities/agent_team_delegation

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 7.67 | quality: 8.96
- latency_total: 10.929s | tokens_per_second: 75.7
- input_tokens: 1728 | output_tokens: 827
- judge_score: 4.4 | justificación: 

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

# Plan de Ejecución: Landing Page "AutoFlow AI"

Voy a coordinar este proyecto en **4 fases secuenciales**, respetando dependencias entre agentes:

## Fases y dependencias

**Fase 1 — Research (bloqueante, va primero)**
- `researcher` investiga 3 competidores (Zapier, Make/Integromat, n8n como candidatos probables) para entender posicionamiento, pricing y features. Esto alimenta al `writer` y al `designer`.

**Fase 2 — Contenido y Diseño (dependen de Fase 1, se ejecutan en paralelo entre sí)**
- `writer` redacta el copy (hero, features, pricing, CTA) usando los insights del research.
- `designer` crea conceptos visuales de hero y features en paralelo (puede trabajar con brief general mientras el copy se define, ajustando después).

**Fase 3 — Código (depende de Fase 2)**
- `coder` genera el HTML/CSS integrando copy final + assets del designer.

**Fase 4 — QA (depende de Fase 3)**
- `reviewer` revisa todo (copy, código, consistencia visual) antes de publicar.

Empiezo con la Fase 1, y lanzo en paralelo el research y el brief inicial de diseño (que no depende del copy final, solo del research básico de tono/estilo competitivo), para ganar tiempo: