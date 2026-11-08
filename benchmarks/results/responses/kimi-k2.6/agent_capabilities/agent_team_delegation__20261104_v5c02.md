# Kimi K2.6 — agent_capabilities/agent_team_delegation

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 8.01 | quality: 9.8
- latency_total: 94.566s | tokens_per_second: 48.1
- input_tokens: 726 | output_tokens: 4545
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un plan estructurado que un emprendedor podría implementar directamente.

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

 Perfecto. Voy a coordinar el proyecto completo de la landing page para **AutoFlow AI** siguiendo un flujo con dependencias claras. Aquí está el plan de ejecución:

---

### 🎯 Plan de Ejecución

**Fase 1: Investigación**
- Sub-agente `researcher` analizará a 3 competidores directos en automatización para startups (probablemente Zapier, Make/n8n) para identificar propuestas de valor, estructuras de landing y gaps que AutoFlow AI puede aprovechar.

**Fase 2: Contenido y Creatividad (depende de Fase 1)**
- Sub-agente `writer` redactará el copy completo (hero, features, pricing, CTA) basándose en la investigación de competencia y posicionamiento diferenciado de AutoFlow AI.
- Sub-agente `designer` creará los assets visuales: imagen hero principal y 3 imágenes representativas para la sección de features.

**Fase 3: Desarrollo (depende de Fase 2)**
- Sub-agente `coder` generará el código HTML/CSS responsive de la landing page, integrando el copy y preparando placeholders/estructura para las imágenes del designer.

**Fase 4: Control de Calidad (depende de Fase 3)**
- Sub-agente `reviewer` revisará coherencia entre copy, código y diseño, verificando calidad, errores ortográficos, responsive design y consistencia de marca.

---

Ahora delego todas las tareas a los sub-agentes especializados: 