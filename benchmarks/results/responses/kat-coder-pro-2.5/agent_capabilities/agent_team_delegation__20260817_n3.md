# KAT Coder Pro v2.5 — agent_capabilities/agent_team_delegation

- model_id: `kwaipilot/kat-coder-pro-v2.5`
- success: True  | final: 8.05 | quality: 8.96
- latency_total: 6.879s | tokens_per_second: 76.6
- input_tokens: 1211 | output_tokens: 527
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



## Plan de Ejecución - Landing Page "AutoFlow AI"

Voy a coordinar a los 5 sub-agentes en el siguiente orden, respetando dependencias:

### Fase 1: Investigación (researcher)
- Investigar 3 competidores de automatización para startups
- Extraer: propuesta de valor, precios, features clave

### Fase 2: Copywriting + Diseño (writer + designer en paralelo)
- **writer**: Redactar hero, features, pricing, CTA basado en la investigación
- **designer**: Crear brief y conceptos visuales para hero + features (puede avanzar con info general del producto)

### Fase 3: Desarrollo (coder)
- Generar HTML/CSS completo usando el copy final

### Fase 4: Revisión (reviewer)
- Revisar coherencia, errores, calidad del conjunto

---

Comienzo con la **Fase 1** - delegando al researcher:

