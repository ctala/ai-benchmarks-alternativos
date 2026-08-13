# Claude Opus 5 (suscripción) — agent_capabilities/agent_team_delegation

- model_id: `claude-opus-5`
- success: True  | final: 8.0 | quality: 10.0
- latency_total: 64.94s | tokens_per_second: 54.5
- input_tokens: 2 | output_tokens: 3541
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un plan detallado y estructurado para la delegación de tareas con dependencias claras.

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

# Plan de ejecución — Landing "AutoFlow AI"

Antes de delegar, el mapa. Hay una dependencia dura que define todo: **el copy no se escribe sin la investigación, y el código no se escribe sin el copy.** Si lo corro todo en paralelo, termino con un HTML precioso que dice lo mismo que Zapier y hay que rehacerlo.

## Grafo de dependencias

```
OLA 1 (bloqueante)        OLA 2                    OLA 3              OLA 4
┌──────────────┐         ┌──────────────┐        ┌──────────┐      ┌──────────┐
│ researcher   │────┬───▶│ writer       │───┬───▶│ coder    │─────▶│ reviewer │
│ 3 competidores│    │    │ copy completo│   │    │ HTML/CSS │      │ gate final│
└──────────────┘    │    └──────┬───────┘   │    └──────────┘      └──────────┘
                    │           │            │         ▲
                    │           ▼            │         │
                    │    ┌──────────────┐   │    ┌──────────┐
                    └───▶│ designer     │   └───▶│ designer │
                         │ sistema visual│        │ hero+feats│
                         └──────────────┘        └──────────┘
                          (no depende de copy)   (sí depende)
```

**Lo que sí paralelizo:** designer arranca el sistema visual (paleta, tipografía, dirección de arte) en cuanto researcher entrega, sin esperar el copy. Los assets finales sí esperan, porque una imagen hero que no ilustra la promesa del hero no sirve.

**Lo que no paralelizo:** coder con lorem ipsum. Suena eficiente, no lo es: el largo real del copy cambia el layout y termina siendo reescritura, no ajuste.

## Asignación y prioridades

| # | Agente | Tarea | Prioridad | Depende de | Est. |
|---|---|---|---|---|---|
| 1 | **researcher** | 3 competidores: posicionamiento, pricing, hero copy, gaps | **P0 — bloquea todo** | — | 1er turno |
| 2 | **designer** | Sistema visual (paleta, tipo, dirección de arte) | P1 | #1 | Paralelo |
| 3 | **writer** | Copy completo: hero, features, pricing, CTA, objeciones | **P0** | #1 | 2do turno |
| 4 | **reviewer** | Revisión **temprana** del copy (gate barato) | **P0** | #3 | 2do turno |
| 5 | **designer** | Hero image + 3-4 imágenes de features | P1 | #3, #2 | 3er turno |
| 6 | **coder** | HTML/CSS responsive, semántico, SEO, sin JS pesado | P1 | #3 aprobado, #2 | 3er turno |
| 7 | **reviewer** | QA final: copy, código, accesibilidad, links, mobile | **P0 — veto** | todo | 4to turno |

**Dos pasadas de reviewer, no una.** Corregir un mensaje flojo en el copy cuesta 10 minutos; corregirlo cuando ya está en HTML y con imágenes generadas cuesta rehacer tres entregables. El reviewer entra antes de que el coder toque una línea.

## Briefs de delegación

**→ researcher (P0, arranca ahora)**
Competidores sugeridos: Zapier, Make y **una** herramienta AI-native (Lindy, Gumloop o Relay.app) — confirmá cuál es la comparación real según el ángulo. Para cada uno: hero headline y subheadline textuales, promesa central, 3 features destacadas, estructura de pricing con números, a quién le hablan explícitamente, y qué objeción no responden. Entregable: tabla comparativa + **lista de gaps** (qué dicen los tres que nosotros no deberíamos repetir). Ese último punto es el que le sirve al writer.

**→ writer (P0, tras researcher + reviewer temprano)**
Copy completo en español neutro, founder-a-founder, sin relleno. Hero (headline + sub + CTA), 3-4 features en formato *problema → qué hace → resultado*, tabla de pricing, CTA final, y 2-3 objeciones respondidas. Regla dura: **no repetir el ángulo de ninguno de los tres competidores**. Cifras concretas antes que adjetivos.

**→ designer**
Fase A: sistema visual coherente con el gap detectado (si los tres competidores son azul corporativo, no seamos el cuarto). Fase B: hero image + assets de features que ilustren la promesa del copy aprobado, no decoración genérica.

**→ coder**
HTML semántico + CSS, mobile-first, sin framework pesado, Core Web Vitals en verde, meta tags y OG completos, formulario de captura listo para conectar. Cero texto inventado: solo el copy aprobado.

**→ reviewer (veto)**
Pasada 1 sobre copy: claridad, diferenciación real, promesa verificable. Pasada 2 sobre todo: consistencia copy↔imagen↔código, responsive, accesibilidad, links, ortografía, y que el pricing del HTML coincida con el aprobado.

## Lo que necesito de ti antes de que el writer arranque

Tres cosas que ningún agente puede inventar sin que la landing mienta:

1. **Pricing real** — tiers y precios. Sin esto el writer inventa números y hay que rehacer la sección.
2. **ICP concreto** — ¿founder solo, equipo de 5-20, o startup con equipo técnico? Cambia el copy entero.
3. **La diferencia real** — ¿qué hace AutoFlow AI que Zapier/Make no? Si no la tenemos clara, la landing va a sonar a las otras tres y el researcher solo confirmará que somos genéricos.

**Arranco ya con el researcher** (no depende de esas respuestas) mientras me las confirmás. Y nada se publica sin tu "ok" explícito tras la pasada 2 del reviewer.

¿Lanzo el researcher con esa shortlist de competidores o querés cambiar alguno?