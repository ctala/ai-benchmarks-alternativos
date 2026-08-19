# Seed 2.1 Turbo — agent_capabilities/agent_team_delegation

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.41 | quality: 9.8
- latency_total: 16.491s | tokens_per_second: 45.1
- input_tokens: 1268 | output_tokens: 743
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza adecuadamente en la estructura y coordinación de tareas, proporcionando un plan util para un emprendedor.

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

### 📋 Plan de Ejecución - Landing Page AutoFlow AI

He descompuesto el proyecto en 5 fases secuenciales respetando dependencias:

| Fase | Agente | Tarea | Dependencia | Prioridad |
|------|--------|-------|-------------|-----------|
| 1 | 🔬 **researcher** | Investigar 3 competidores directos + analizar sus landings | Ninguna | ⭐ urgent |
| 2 | ✍️ **writer** | Redactar copy completo (hero, features, pricing, CTA) | Datos del researcher | ⭐ high |
| 3 | 🎨 **designer** | Crear imagen hero + 3 imágenes de features | Brief del researcher + referencia del copy | ⭐ high |
| 4 | 💻 **coder** | Generar HTML/CSS responsive de la landing | Copy del writer + imágenes del designer | ⭐ medium |
| 5 | ✅ **reviewer** | Auditoría completa (calidad de copy, código, diseño, UX) | Todo el material generado | ⭐ medium |

---

**Iniciando Fase 1 - Investigación de competencia:**
