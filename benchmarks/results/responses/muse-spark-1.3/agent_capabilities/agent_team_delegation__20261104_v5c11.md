# Muse Spark 1.3 — agent_capabilities/agent_team_delegation

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.42 | quality: 9.5
- latency_total: 6.588s | tokens_per_second: 134.6
- input_tokens: 1390 | output_tokens: 887
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza adecuadamente en la coordinación de tareas, ofreciendo un plan estructurado que un emprendedor podría usar directamente.

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

¡Perfecto! Voy a coordinar la creación de la landing page de **AutoFlow AI** con el equipo.

### 📋 Plan de Ejecución:
**Fase 1 - Investigación (bloqueante):**
- `researcher` → Analizar 3 competidores de automatización para startups [Prioridad: HIGH]

**Fase 2 - Contenido en paralelo (depende de Fase 1):**
- `writer` → Copy: hero, features, pricing, CTA [Prioridad: HIGH]
- `designer` → Imágenes hero + features [Prioridad: MEDIUM]

**Fase 3 - Desarrollo (depende de Fase 2):**
- `coder` → Código HTML/CSS de la landing [Prioridad: HIGH]

**Fase 4 - Control de calidad (depende de todo):**
- `reviewer` → Revisión final antes de publicar [Prioridad: URGENT]

Empezamos con la Fase 1:
