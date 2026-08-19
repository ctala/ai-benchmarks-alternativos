# Claude Opus 5 Fast — agent_capabilities/agent_team_delegation

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 7.56 | quality: 8.96
- latency_total: 5.808s | tokens_per_second: 168.4
- input_tokens: 1660 | output_tokens: 978
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

# Plan de ejecución — Landing Page "AutoFlow AI"

Antes de delegar, dejo claro el orden y las dependencias:

| Fase | Agente(s) | Depende de | Prioridad |
|------|-----------|------------|-----------|
| 1 | researcher (competencia) + búsqueda interna de specs del producto | — | urgent |
| 2 | writer (copy completo) | Fase 1 | high |
| 3 | coder (HTML/CSS) + designer (hero + features) — **en paralelo** | Fase 2 | high |
| 4 | reviewer (QA final) | Fase 3 | high |
| 5 | Publicación | Aprobación humana | — |

**Racional:** las fases 1 y 3 permiten paralelismo. El copy es el cuello de botella: tanto el código como el diseño dependen del texto final (número de features, tiers de pricing, tono visual). Por eso el writer va solo y con prioridad alta.

Arranco la Fase 1 ahora, lanzando en paralelo la investigación externa y la consulta a nuestra base de conocimiento interna sobre el producto.