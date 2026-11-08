# GLM 5.3 Flash — agent_capabilities/agent_team_delegation

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.54 | quality: 9.8
- latency_total: 51.474s | tokens_per_second: 43.7
- input_tokens: 1001 | output_tokens: 2247
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente estructurada, proporcionando un plan detallado que un emprendedor podría usar directamente.

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

Perfecto. Voy a coordinar este proyecto. Primero, te explico mi plan de ejecución y las dependencias:

## 📋 Plan de Ejecución

**Fase 1 — Investigación** 🔍
- **researcher**: Analizar 3 competidores directos (features, pricing, messaging, posicionamiento). *Es la base de todo, va primero.*

**Fase 2 — Copy** ✍️ *(depende de Fase 1)*
- **writer**: Redactar hero, features, pricing y CTAs usando los insights de la competencia para diferenciarnos.

**Fase 3 — Construcción (en paralelo)** 🛠️ *(ambos dependen del copy, pero son independientes entre sí)*
- **coder**: HTML/CSS de la landing, con rutas de assets acordadas de antemano.
- **designer**: Imagen hero + ilustraciones de features, con naming y dimensiones acordadas.

**Fase 4 — QA** ✅
- **reviewer**: Revisión integral de código, copy y coherencia visual antes de publicar.

**Reglas de coordinación:** acordaré convenciones de nombres de assets (`/assets/hero.png`, `/assets/feature-1.png`, etc.) para que coder y designer trabajen en paralelo sin bloquearse.

---

Arranco con la **Fase 1**, que bloquea todo lo demás: