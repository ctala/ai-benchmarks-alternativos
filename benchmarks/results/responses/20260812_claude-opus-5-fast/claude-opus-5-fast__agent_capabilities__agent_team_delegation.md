# Claude Opus 5 Fast — agent_capabilities/agent_team_delegation

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 7.69 | quality: 9.22
- latency_total: 7.695s | tokens_per_second: 174.5
- input_tokens: 1660 | output_tokens: 1343
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

# Plan de ejecución — Landing Page "AutoFlow AI"

Antes de delegar, te dejo el mapa de dependencias para que veas cómo lo voy a orquestar:

```
FASE 0 (paralelo)  →  Contexto interno (KB: producto + pricing) 
                      Research competencia (3 competidores)
                                 ↓
FASE 1             →  WRITER: copy (hero, features, pricing, CTA)
                                 ↓
FASE 2 (paralelo)  →  CODER: HTML/CSS       |  DESIGNER: hero + feature images
                                 ↓
FASE 3             →  REVIEWER: QA técnico, copy y visual
                                 ↓
FASE 4             →  Publicación (con tu aprobación)
```

**Criterio de paralelización:** research y contexto interno no dependen de nada → van juntos. Coder y designer sí dependen del copy (el código necesita la estructura de secciones; el designer necesita el tono y el mensaje del hero), pero entre ellos son independientes → van en paralelo. El reviewer siempre al final.

Arranco con la Fase 0: