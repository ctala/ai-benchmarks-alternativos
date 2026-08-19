# DeepSeek V4 Pro (0813) — agent_capabilities/agent_team_delegation

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 7.94 | quality: 9.24
- latency_total: 42.164s | tokens_per_second: 33.7
- input_tokens: 1244 | output_tokens: 1422
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

¡Perfecto! Como coordinador, voy a orquestar el lanzamiento de la landing page de **AutoFlow AI** siguiendo un flujo que respete las dependencias entre agentes. Aquí está el plan de ejecución:

## 📋 Plan de ejecución

| # | Agente | Tarea | Prioridad | Depende de |
|---|--------|-------|-----------|------------|
| 1 | 🔍 Researcher | Investigar 3 competidores | Alta | — |
| 2 | ✍️ Writer | Redactar copy (hero, features, pricing, CTA) | Alta | Researcher |
| 3 | 💻 Coder | Generar HTML/CSS | Alta | Writer |
| 3 | 🎨 Designer | Crear imágenes hero y features | Media | Writer (para alinear el mensaje) |
| 4 | ✅ Reviewer | Revisar todo antes de publicar | Urgente | Coder + Designer |

**Dependencias clave:**
- El **writer** no puede empezar sin los datos del **researcher**.
- El **coder** necesita el copy final para estructurar la página.
- El **designer** necesita el copy para que las imágenes refuercen el mensaje (no solo decorar).
- El **reviewer** es el último gate de calidad antes de publicar.

**Punto de decisión:** asumiré pricing estándar SaaS (3 tiers) y una identidad visual alineada con "automatización + IA", salvo que quieras ajustar algo. Puedes corregirme más adelante.

Empiezo ahora con la **Fase 1: Investigación de competencia