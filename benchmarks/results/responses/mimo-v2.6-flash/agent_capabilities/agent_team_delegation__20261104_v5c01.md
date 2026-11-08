# MiMo V2.6 Flash — agent_capabilities/agent_team_delegation

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 8.13 | quality: 8.96
- latency_total: 33.567s | tokens_per_second: 38.2
- input_tokens: 1017 | output_tokens: 1282
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

# Plan de Ejecución: Landing Page para AutoFlow AI

## 📋 Descomposición de tareas

| # | Tarea | Agente | Prioridad | Dependencia |
|---|-------|--------|-----------|-------------|
| 1 | Investigar 3 competidores | `researcher` | 🔴 Alta | Ninguna |
| 2 | Copy de landing (hero, features, pricing, CTA) | `writer` | 🔴 Alta | Tarea 1 |
| 3 | Código HTML/CSS | `coder` | 🔴 Alta | Tarea 2 |
| 4 | Imágenes hero y de features | `designer` | 🟡 Media | Tarea 2 (contexto de copy) |
| 5 | Revisión final | `reviewer` | 🔴 Alta | Tareas 2, 3, 4 |

## 🔄 Estrategia de ejecución

```
researcher ──→ writer ──┬──→ coder ──────┐
                        └──→ designer ───┼──→ reviewer ✅
                                         │
                                         └──→ Publicar
```

- **Fase 1**: Investigación de competidores (desbloquea todo lo demás)
- **Fase 2**: Copy del writer (basado en insights de investigación)
- **Fase 3**: Código + imágenes en paralelo (independientes entre sí)
- **Fase 4**: Revisión integral antes de publicar

---

## 🚀 Iniciando Fase 1: Investigación de competidores