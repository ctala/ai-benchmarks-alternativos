# Grok 4.6 — agent_capabilities/agent_team_delegation

- model_id: `x-ai/grok-4.6`
- success: True  | final: 7.92 | quality: 9.24
- latency_total: 19.217s | tokens_per_second: 55.2
- input_tokens: 1166 | output_tokens: 1060
- judge_score: 4.6 | justificación: 

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

| Fase | Agente | Tarea | Prioridad | Dependencia |
|------|--------|--------|-----------|-------------|
| 1 | **researcher** | Analizar 3 competidores (propuesta, pricing, messaging, diferenciadores) | urgent | Ninguna |
| 1b | Knowledge base | Datos internos del producto (si existen) | urgent | Ninguna |
| 2 | **writer** | Copy: hero, features, pricing, CTA | high | Research + producto |
| 2 | **designer** | Imágenes hero + features | high | Research (tono visual) |
| 3 | **coder** | HTML/CSS de la landing | high | Copy + assets |
| 4 | **reviewer** | QA de copy, código, consistencia visual y conversión | urgent | Todo lo anterior |

No publicamos hasta el OK del reviewer. Empiezo por investigación en paralelo (competencia + base de conocimiento interna).