# KAT Coder Air v2.5 — agent_capabilities/agent_team_delegation

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 8.99 | quality: 9.52
- latency_total: 4.586s | tokens_per_second: 179.2
- input_tokens: 1211 | output_tokens: 822
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

## Dependencias y Fases

| Fase | Tarea | Agente | Depende de |
|------|-------|--------|------------|
| **1** | Investigar 3 competidores | `researcher` | — |
| **2a** | Escribir copy (hero, features, pricing, CTA) | `writer` | Fase 1 |
| **2b** | Crear imágenes hero y features | `designer` | Fase 1 |
| **3** | Generar código HTML/CSS | `coder` | Fase 2a |
| **4** | Revisión final de calidad | `reviewer` | Fases 2b + 3 |

**Fases 2a y 2b son paralelas** (ambas solo necesitan la investigación).

---

Iniciamos con la **Fase 1: Investigación de competencia**.

