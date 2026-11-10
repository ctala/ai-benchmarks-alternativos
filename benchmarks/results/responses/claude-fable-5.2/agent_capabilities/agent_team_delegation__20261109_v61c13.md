# Claude Fable 5.2 — agent_capabilities/agent_team_delegation

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 7.81 | quality: 9.5
- latency_total: 15.979s | tokens_per_second: 110.1
- input_tokens: 1662 | output_tokens: 1760
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

## Plan de ejecución: landing page de "AutoFlow AI"

| Fase | Agente | Tarea | Depende de | Prioridad |
|---|---|---|---|---|
| **1a** | researcher | Análisis de 3 competidores (mensajes, features, pricing, CTAs) | — | Alta |
| **1b** | coordinador | Buscar en la base de conocimiento los datos internos de AutoFlow AI (features, precios, guía de marca) | — | Alta |
| **2** | writer | Copy de la landing: hero, features, pricing, CTA | 1a y 1b | Alta |
| **3a** | coder | HTML/CSS responsive con el copy final | 2 | Alta |
| **3b** | designer | Imagen hero e imágenes de features | 2 | Alta |
| **4** | reviewer | Revisión integral de copy, código, assets y coherencia | 3a y 3b | Alta |
| **5** | coordinador | Entregarte el resultado para tu aprobación antes de publicar | 4 | — |

- **En paralelo:** 1a con 1b, y 3a con 3b, porque no dependen entre sí.
- **Datos internos:** busco la información real del producto para que el writer no invente features ni precios.
- **Publicación:** no publicaré nada sin tu aprobación.

Arranco con la fase 1: investigación de competidores y búsqueda de datos internos.