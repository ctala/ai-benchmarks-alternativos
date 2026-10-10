# Claude Fable 5.1 — agent_capabilities/agent_team_delegation

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.88 | quality: 9.8
- latency_total: 17.193s | tokens_per_second: 74.9
- input_tokens: 1662 | output_tokens: 1288
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando un plan detallado y estructurado que un emprendedor podría implementar directamente.

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

## Plan de ejecución

Antes de delegar, así voy a organizar el trabajo en 4 fases respetando las dependencias:

**Fase 1 — Base de información (en paralelo)**
- 🔍 Consulto la base de conocimiento interna para obtener los datos reales de AutoFlow AI (features, precios, posicionamiento).
- 🔍 **Researcher**: análisis de 3 competidores (propuesta de valor, features, pricing, mensajes clave).

**Fase 2 — Copy** *(depende de Fase 1)*
- ✍️ **Writer**: redacta hero, features, pricing y CTA usando los datos del producto y los insights de la competencia.

**Fase 3 — Producción (en paralelo)** *(depende de Fase 2)*
- 💻 **Coder**: HTML/CSS responsive con el copy final.
- 🎨 **Designer**: imagen hero + ilustraciones de cada feature, alineadas con el copy.

**Fase 4 — QA** *(depende de Fase 3)*
- ✅ **Reviewer**: revisa copy, código, accesibilidad y coherencia visual antes de publicar.

Arranco con la Fase 1: