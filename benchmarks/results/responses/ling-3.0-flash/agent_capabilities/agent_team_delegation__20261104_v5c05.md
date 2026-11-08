# Ling 3.0 Flash — agent_capabilities/agent_team_delegation

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.07 | quality: 9.52
- latency_total: 9.206s | tokens_per_second: 114.2
- input_tokens: 1264 | output_tokens: 1051
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

## 📋 Plan de Ejecución — Landing Page "AutoFlow AI"

Voy a coordinar este proyecto en **4 fases** respetando las dependencias entre agentes:

| Fase | Agente | Dependencia |
|------|--------|-------------|
| **1** (Paralelo) | 🔍 Researcher + 🎨 Designer | Ninguna (arrancan juntos) |
| **2** | ✍️ Writer | Necesita datos del Researcher |
| **3** | 💻 Coder | Necesita copy del Writer + assets del Designer |
| **4** | 🔎 Reviewer | Necesita todo lo anterior |

**Arranca ahora la Fase 1 con dos agentes en paralelo:**

