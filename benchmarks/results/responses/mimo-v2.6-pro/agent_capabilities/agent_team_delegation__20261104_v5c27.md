# MiMo V2.6 Pro — agent_capabilities/agent_team_delegation

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 8.59 | quality: 9.8
- latency_total: 14.579s | tokens_per_second: 42.2
- input_tokens: 987 | output_tokens: 615
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza adecuadamente en la coordinación de tareas, ofreciendo un plan estructurado que un emprendedor podría usar directamente.

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

## 🚀 Plan de Ejecución — Landing Page "AutoFlow AI"

He analizado las tareas y sus dependencias. Este es el plan coordinado:

```
FASE 1 (Investigación)     ──►  researcher 🔍
                                     │
                                     ▼
FASE 2 (Copywriting)       ──►  writer ✍️
                                     │
                    ┌────────────────┼────────────────┐
                    ▼                                 ▼
FASE 3a (Assets visuales)  ──►  designer 🎨    FASE 3b (Código) ──►  coder 👨‍💻
                    └────────────────┼────────────────┘
                                     ▼
FASE 4 (Control de calidad) ──►  reviewer ✅
                                     │
                                     ▼
                             📦 ENTREGA FINAL
```

**Dependencias clave:**
- El **writer** necesita el análisis competitivo para posicionar el copy.
- El **coder** necesita el copy final para construir la página.
- El **designer** puede trabajar en paralelo con el coder (imágenes genéricas de hero/features).
- El **reviewer** entra al final con todos los entregables.

Doy inicio a la **Fase 1** ahora mismo: