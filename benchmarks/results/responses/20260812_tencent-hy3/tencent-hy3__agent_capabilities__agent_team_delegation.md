# Tencent Hy3 — agent_capabilities/agent_team_delegation

- model_id: `tencent/hy3`
- success: True  | final: 8.87 | quality: 9.8
- latency_total: 13.936s | tokens_per_second: 125.1
- input_tokens: 1152 | output_tokens: 1744
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente estructurada, ofreciendo un plan detallado que un emprendedor podría usar directamente.

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

¡Perfecto! Como coordinador del Agent Team, voy a orquestar este proyecto de landing page para **AutoFlow AI**. Primero te presento el plan de ejecución y luego empiezo a delegar.

## 📋 Plan de Ejecución

**Fase 1 — Investigación y base visual (paralelo, sin dependencias)**
- 🔍 **Researcher** (prioridad alta): investiga 3 competidores de automatización para startups, sus features, pricing y propuesta de valor.
- 🎨 **Designer** (prioridad media): crea el concepto de la imagen hero basado en el brief del producto.

**Fase 2 — Copy (depende de Researcher)**
- ✍️ **Writer** (prioridad alta): redacta hero, features, pricing y CTA usando los datos de la competencia para diferenciarnos.

**Fase 3 — Activos y código (dependen de Writer)**
- 🎨 **Designer** (prioridad alta): crea las imágenes de las secciones de features.
- 💻 **Coder** (prioridad alta): genera el HTML/CSS completo con el copy y los assets.

**Fase 4 — Control de calidad (depende de todo)**
- ✅ **Reviewer** (prioridad urgente): revisa copy, código, imágenes y coherencia antes de publicar.

---

Empiezo con la **Fase 1** (llamadas en paralelo):