# DeepSeek V4 Pro — agent_capabilities/agent_team_delegation

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 8.18 | quality: 9.52
- latency_total: 17.853s | tokens_per_second: 75.6
- input_tokens: 1165 | output_tokens: 1350
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

# 🚀 Plan de Ejecución: Landing Page "AutoFlow AI"

Antes de delegar, aquí está el plan maestro con dependencias y prioridades:

---

## 📋 Plan de Ejecución

| Fase | Agente | Tarea | Prioridad | Depende de |
|------|--------|-------|-----------|------------|
| **1** | `researcher` | Investigar 3 competidores | 🔴 Urgente | — |
| **1** | `designer` | Conceptualizar hero + features (brief inicial) | 🟡 Medium | — |
| **2** | `writer` | Copy completo (hero, features, pricing, CTA) | 🔴 Urgente | Fase 1 (researcher) |
| **2** | `designer` | Refinar assets con copy final | 🟡 Medium | Fase 2 (writer) |
| **3** | `coder` | HTML/CSS completo | 🔴 Urgente | Fase 2 (writer + designer) |
| **4** | `reviewer` | Revisión integral pre-publicación | 🔴 Urgente | Fase 3 (coder) |

---

## ⚡ Iniciando Fase 1: Researcher + Designer (en paralelo)

> El researcher es el **bloqueo crítico**: sin sus datos, el writer no puede redactar. El designer arranca con un brief conceptual mientras tanto.

