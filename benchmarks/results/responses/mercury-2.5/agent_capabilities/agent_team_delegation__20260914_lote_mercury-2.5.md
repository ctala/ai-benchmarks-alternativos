# Mercury 2.5 — agent_capabilities/agent_team_delegation

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.2 | quality: 9.5
- latency_total: 2.259s | tokens_per_second: 418.8
- input_tokens: 1259 | output_tokens: 946
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un plan estructurado que un emprendedor podría implementar directamente.

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



Aquí está mi plan de coordinación para el lanzamiento de la landing page de **AutoFlow AI**:

1.  **Researcher:** Investigar 3 competidores directos (features, pricing, fortalezas/debilidades).
2.  **Writer:** Redactar el copy (hero, features, pricing, CTA) basado en la investigación.
3.  **Coder:** Generar el código HTML/CSS estructurado según el copy.
4.  **Designer:** Crear las imágenes hero y de features alineadas con el branding.
5.  **Reviewer:** Revisar todo el paquete antes de la publicación final.

Comienzo delegando la primera tarea crítica:

