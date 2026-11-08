# Tencent Hy4 — agent_capabilities/agent_team_delegation

- model_id: `tencent/hy4`
- success: True  | final: 8.42 | quality: 9.8
- latency_total: 47.059s | tokens_per_second: 80.3
- input_tokens: 1073 | output_tokens: 3780
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando un plan detallado y bien estructurado que un emprendedor podría implementar directamente.

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

He descompuesto el encargo en un **pipeline de 5 fases con dependencias explícitas**. La regla clave: nadie trabaja sobre contenido que aún no existe (evita que el `coder` invente copy o que el `writer` invente precios).

```
FASE 1  ┌─ researcher ......................... (sin dependencias)  [URGENT]
        ├─ ask_human: pricing ................ (sin dependencias)  [URGENT]
        └─ ask_human: tono/claims ............ (sin dependencias)  [HIGH]
              │
              ▼  (benchmarks + gaps + precios + tono)
FASE 2  ┌─ writer ....... copy hero/features/pricing/CTA          [HIGH]
        └─ designer ..... hero + features + paleta + nombres de archivo [HIGH]
              │            (en paralelo: comparten solo el brief de F1)
              ▼  (copy real + rutas de assets reales)
FASE 3  └── coder ....... HTML/CSS integrando ambos                [HIGH]
              │
              ▼  (los 4 entregables)
FASE 4  └── reviewer .... checklist bloqueante de calidad          [URGENT]
              │
              ▼
FASE 5  └── ask_human: aprobación → publicación + aviso al equipo
```

**Decisiones de coordinación:**
- `researcher` va **primero y con prioridad urgent** porque bloquea a todos: el posicionamiento del copy y la dirección visual salen de los gaps de la competencia.
- `writer` y `designer` van **en paralelo** (no se necesitan entre sí si ambos reciben el mismo brief de la Fase 1). Exijo al designer que fije **nombres de archivo exactos y alt-text** para que el coder no tenga que adivinar rutas.
- `coder` va **después de ambos**: es el único que consume dos salidas. Sin lorem ipsum, sin placeholders de imágenes.
- `reviewer` va **al final, con los 4 entregables**, y su visto bueno es condición necesaria para publicar.
- **No publico automáticamente**: no existe un skill de "publicar landing" (`publish_blog_post` aplica a blog, no a landing), así que cierro con una compuerta de aprobación humana.
- El **pricing es una decisión de negocio**, no un dato que el researcher pueda inventar: lo pido al humano en paralelo con la investigación para no perder tiempo.

Arranco la Fase 1 👇