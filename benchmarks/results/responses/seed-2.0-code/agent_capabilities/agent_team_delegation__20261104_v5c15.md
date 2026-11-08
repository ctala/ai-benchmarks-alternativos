# Seed 2.0 Code — agent_capabilities/agent_team_delegation

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 7.4 | quality: 8.2
- latency_total: 10.199s | tokens_per_second: 77.1
- input_tokens: 1268 | output_tokens: 786
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con una estructura bien organizada que un emprendedor podría usar directamente, aunque la profundidad podría mejorarse con más detalles sobre las tareas.

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

📋 **Plan de Ejecución para Landing Page AutoFlow AI**

He descompuesto el proyecto en 5 fases secuenciales respetando las dependencias:

| Fase | Tarea | Agente | Prioridad | Depende de |
|------|-------|--------|-----------|------------|
| 1 | Investigar 3 competidores | Researcher | High | - |
| 2 | Escribir copy (hero, features, pricing, CTA) | Writer | High | Fase 1 |
| 3 | Crear imágenes hero y features | Designer | Medium | Fase 2 |
| 4 | Generar HTML/CSS | Coder | High | Fase 2 y 3 |
| 5 | Revisión final | Reviewer | Urgent | Fase 4 |

---

🚀 **Iniciando Fase 1: Investigación de la Competencia**

Necesito que el researcher busque información detallada de 3 herramientas de automatización para startups.
