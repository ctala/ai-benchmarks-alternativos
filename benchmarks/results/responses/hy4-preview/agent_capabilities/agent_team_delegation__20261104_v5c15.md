# Tencent Hy4 preview — agent_capabilities/agent_team_delegation

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.17 | quality: 9.6
- latency_total: 25.928s | tokens_per_second: 49.1
- input_tokens: 1073 | output_tokens: 1273
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

Voy a coordinar este proyecto en 4 fases, respetando las dependencias entre agentes:

**Fase 0 — Datos y definiciones (paralelo)**
- `researcher`: análisis de 3 competidores
- `ask_human`: aclararte 3-4 decisiones clave antes de escribir (si no, el copy y el código se hacen sobre supuestos)

**Fase 1 — Copy** → `writer` (depende de la investigación + tus respuestas)

**Fase 2 — Ejecución (paralelo)** → `coder` (HTML/CSS) + `designer` (hero + imágenes de features), ambos sobre el copy ya cerrado

**Fase 3 — Control de calidad** → `reviewer` (depende de código + assets)

Empiezo con la Fase 0: