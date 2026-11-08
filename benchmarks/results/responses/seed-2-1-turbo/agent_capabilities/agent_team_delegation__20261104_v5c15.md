# Seed 2.1 Turbo — agent_capabilities/agent_team_delegation

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.41 | quality: 9.6
- latency_total: 13.733s | tokens_per_second: 55.2
- input_tokens: 1268 | output_tokens: 758
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

**Plan de ejecución para la landing page de AutoFlow AI:**

Voy a coordinar las 5 tareas respetando las dependencias entre agentes. El trabajo se organizará en 4 fases:

```
FASE 1 (Paralela - Prioridad: High)
├── Researcher: Analiza 3 competidores directos
└── Designer: Crea conceptos iniciales de imágenes

FASE 2 (Depende de Fase 1)
└── Writer: Redacta copy de la landing (con insights de competencia)

FASE 3 (Depende de Fase 1 y 2)
└── Coder: Genera HTML/CSS integrando copy + imágenes

FASE 4 (Depende de Fase 3)
└── Reviewer: Revisión final de calidad
```

Ahora inicio la Fase 1 con las tareas que pueden ejecutarse en paralelo:

