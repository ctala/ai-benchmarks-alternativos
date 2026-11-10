# Gemini 3.1 Flash Lite (GA) — agent_capabilities/agent_team_delegation

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 9.14 | quality: 9.7
- latency_total: 2.136s | tokens_per_second: 146.1
- input_tokens: 571 | output_tokens: 312
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una estructura bien organizada que proporciona un plan de acción detallado y útil para un emprendedor.

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

Para ejecutar este proyecto de manera eficiente, he diseñado el siguiente plan de trabajo que delegaré a los agentes especializados. Seguiremos una estructura secuencial para asegurar la coherencia:

### Plan de Ejecución

1.  **Fase 1: Investigación (Researcher)** - Identificar puntos fuertes y débiles de 3 competidores directos en el sector de automatización para startups.
2.  **Fase 2: Redacción (Writer)** - Crear el copy persuasivo basado en el análisis de mercado.
3.  **Fase 3: Diseño y Desarrollo (Designer & Coder)** - Diseño visual de los assets y codificación de la estructura HTML/CSS.
4.  **Fase 4: Control de Calidad (Reviewer)** - Revisión integral del producto final antes de su despliegue.

---

### Paso 1: Investigación de competencia
Delegaré al **researcher** la tarea de analizar tres competidores clave para "AutoFlow AI".

