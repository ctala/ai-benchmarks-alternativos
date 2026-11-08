# Tencent Hy3 — agent_capabilities/agent_team_delegation

- model_id: `tencent/hy3`
- success: True  | final: 8.36 | quality: 9.52
- latency_total: 39.311s | tokens_per_second: 49.3
- input_tokens: 1151 | output_tokens: 1937
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

¡Perfecto! Voy a coordinar todo el equipo para crear la landing page de **AutoFlow AI**. Primero te presento el plan de ejecución y luego empiezo a delegar.

## 📋 Plan de Ejecución

| Fase | Agente | Tarea | Depende de | Prioridad |
|------|--------|-------|-----------|-----------|
| 1 | 🔍 **researcher** | Investigar 3 competidores (features, pricing, posicionamiento) | — | 🔴 Alta |
| 2 | ✍️ **writer** | Redactar copy (hero, features, pricing, CTA) usando el análisis competitivo | Fase 1 | 🔴 Alta |
| 3a | 🎨 **designer** | Crear imagen hero + imágenes de features | Fase 2 | 🟡 Media |
| 3b | 💻 **coder** | Generar HTML/CSS de la landing con el copy | Fase 2 | 🔴 Alta |
| 4 | ✅ **reviewer** | Revisar copy, código e imágenes antes de publicar | Fases 3a+3b | 🔴 Alta |

**Lógica de dependencias:**
- El **writer** necesita los datos del **researcher** para diferenciarse de la competencia.
- El **coder** y el **designer** necesitan el copy del **writer** para que imágenes y texto encajen.
- El **reviewer** va al final para validar el conjunto completo.

Empiezo ahora con la Fase 1 (única que puede correr de inmediato):

