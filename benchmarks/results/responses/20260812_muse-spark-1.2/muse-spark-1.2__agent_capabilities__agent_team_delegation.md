# Muse Spark 1.2 — agent_capabilities/agent_team_delegation

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 8.65 | quality: 9.8
- latency_total: 5.276s | tokens_per_second: 137.8
- input_tokens: 1388 | output_tokens: 727
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, con una estructura bien organizada que un emprendedor podría aplicar directamente.

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

Perfecto, voy a coordinar la creación completa de la landing page para **AutoFlow AI**.

### Plan de Ejecución - AutoFlow AI Landing Page

He descompuesto tu solicitud en 5 fases con dependencias claras:

**FASE 1 - Investigación (Base para todo)**
→ **researcher** | Prioridad: **URGENT**
Investigar 3 competidores directos de herramientas de automatización para startups. Sin esto no podemos posicionarnos correctamente.

**FASE 2 - Contenido y Diseño (En paralelo, dependen de Fase 1)**
→ **writer** | Prioridad: **HIGH** - Creará el copy (hero, features, pricing, CTA) basado en los insights de la competencia.
→ **designer** | Prioridad: **HIGH** - Creará imagen hero y visuales de features alineados al posicionamiento.

**FASE 3 - Desarrollo (Depende de Fase 2)**
→ **coder** | Prioridad: **HIGH** - Generará el código HTML/CSS integrando copy y assets.

**FASE 4 - Control de Calidad (Depende de Fase 3)**
→ **reviewer** | Prioridad: **URGENT** - Revisión final de todo antes de publicar.

Iniciamos con la FASE 1:
