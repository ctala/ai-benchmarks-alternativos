# Mercury 3 — agent_capabilities/agent_team_delegation

- model_id: `inception/mercury-3`
- success: True  | final: 9.06 | quality: 9.5
- latency_total: 2.237s | tokens_per_second: 418.0
- input_tokens: 1143 | output_tokens: 935
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, con una estructura bien organizada que un emprendedor podría usar directamente.

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

¡Perfecto! Voy a coordinar todo el proceso para crear la landing page de **AutoFlow AI**. Aquí está mi plan de ejecución:

## 📋 Plan de Ejecución

**Fase 1 — Investigación (researcher)** 🟢 Prioridad: Alta
- Analizar 3 competidores: sus propuestas de valor, pricing, features y mensajes clave
- *Es la base: el writer necesita estos datos para diferenciar el producto*

**Fase 2 — Copywriting (writer)** 🟢 Prioridad: Alta
- Depende de la Fase 1
- Redactar: hero, features, pricing, CTA

**Fase 3 — Desarrollo y Diseño (coder + designer)** 🟡 Prioridad: Media
- Pueden correr en paralelo tras tener el copy y dirección de marca
- coder: HTML/CSS de la página
- designer: imágenes hero y de features

**Fase 4 — Revisión (reviewer)** 🔴 Prioridad: Final
- Revisar todo: copy, código, imágenes, consistencia visual
- Corregir antes de publicar

---

**Comenzando con la Fase 1: Investigación de competencia.** Delegando al researcher:

