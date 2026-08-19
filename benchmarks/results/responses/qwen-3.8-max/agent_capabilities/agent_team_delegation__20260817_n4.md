# Qwen 3.8 Max — agent_capabilities/agent_team_delegation

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 7.91 | quality: 9.52
- latency_total: 32.047s | tokens_per_second: 47.2
- input_tokens: 1190 | output_tokens: 1514
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

# 📋 Plan de Ejecución — Landing Page "AutoFlow AI"

Perfecto. Antes de delegar, aquí está el desglose del flujo de trabajo respetando dependencias:

## 🗺️ Mapa de fases y dependencias

```
FASE 1 ──→ FASE 2 ──→ ┬── FASE 3a ──→ ┐
                      └── FASE 3b ──→ ┴── FASE 4
```

| Fase | Agente | Tarea | Prioridad | Depende de |
|------|--------|-------|-----------|------------|
| **1. Research** | 🔍 researcher | Análisis de 3 competidores: features, pricing, posicionamiento y diferenciadores | 🔴 Alta | — |
| **2. Copywriting** | ✍️ writer | Copy completo: hero, features, pricing, CTA (usando insights del research) | 🔴 Alta | Fase 1 |
| **3a. Desarrollo** | 💻 coder | HTML/CSS responsive de la landing basado en el copy | 🟠 Media-Alta | Fase 2 |
| **3b. Diseño** | 🎨 designer | Imagen hero + gráficos de features alineados al tono del copy | 🟠 Media-Alta | Fase 2 |
| **4. QA** | ✅ reviewer | Revisión integral: copy, código, consistencia visual, errores | 🔴 Alta | Fases 3a + 3b |

> ⚡ **Optimización:** Las fases 3a y 3b se ejecutarán **en paralelo** para ahorrar tiempo, ya que son independientes entre sí.

---

## 🚀 Arrancando Fase 1: Research de competencia

Dado que **todo depende de esta fase**, delego primero al researcher:

