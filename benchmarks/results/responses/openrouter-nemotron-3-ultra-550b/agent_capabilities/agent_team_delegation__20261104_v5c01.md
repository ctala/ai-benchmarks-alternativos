# Nemotron 3 Ultra 550B — agent_capabilities/agent_team_delegation

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.76 | quality: 9.5
- latency_total: 4.135s | tokens_per_second: 126.7
- input_tokens: 1350 | output_tokens: 524
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, con una estructura bien organizada que un emprendedor podría usar directamente.

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

Voy a coordinar la creación completa de la landing page para "AutoFlow AI". Aquí está mi plan de ejecución:

## Plan de Ejecución

**Fase 1 - Investigación (Prioridad: High)**
- **Researcher**: Investigar 3 competidores principales en automatización para startups

**Fase 2 - Contenido (Prioridad: High, depende de investigación)**
- **Writer**: Redactar copy completo (Hero, Features, Pricing, CTA) basado en hallazgos

**Fase 3 - Implementación Paralela (Prioridad: Medium, dependen del copy)**
- **Coder**: Generar HTML/CSS responsive de la landing page
- **Designer**: Crear imagen hero + 3-4 imágenes de features

**Fase 4 - Revisión Final (Prioridad: High, depende de todo lo anterior)**
- **Reviewer**: Revisión completa de calidad, copy, código y assets visuales

---

Iniciando con la investigación de competidores:

