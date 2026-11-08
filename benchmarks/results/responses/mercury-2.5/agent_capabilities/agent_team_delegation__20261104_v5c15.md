# Mercury 2.5 — agent_capabilities/agent_team_delegation

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.13 | quality: 9.5
- latency_total: 4.063s | tokens_per_second: 424.6
- input_tokens: 1150 | output_tokens: 1725
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza adecuadamente en la coordinación de tareas, ofreciendo un plan práctico y útil para un emprendedor.

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



Aquí está mi plan de coordinación para el lanzamiento de la landing page de "AutoFlow AI":

**Plan de Ejecución:**

1.  **Investigación (Researcher):** Analizar 3 competidores clave en automatización para startups para identificar fortalezas, debilidades y estrategias de precios.
2.  **Contenido y Diseño (Writer & Designer):**
    *   *Writer:* Redactar el copy (Hero, Features, Pricing, CTA) basado en los insights de la investigación.
    *   *Designer:* Crear los assets visuales (hero y features) alineados con el copy.
    *   *Estas tareas se ejecutan en paralelo una vez tengamos la investigación.*
3.  **Desarrollo (Coder):** Construir la estructura HTML/CSS integrando el texto y los visuales.
4.  **Revisión (Reviewer):** Validar calidad de código, consistencia del mensaje y diseño final antes de publicar.

Priorizaré la investigación como paso crítico. Procederé a delegar ahora.

