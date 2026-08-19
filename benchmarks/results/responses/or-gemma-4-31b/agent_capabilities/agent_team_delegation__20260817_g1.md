# Gemma 4 31B — agent_capabilities/agent_team_delegation

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 8.28 | quality: 9.16
- latency_total: 13.316s | tokens_per_second: 29.4
- input_tokens: 898 | output_tokens: 391
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

Entendido. Como agente coordinador, he diseñado el siguiente plan de ejecución para el lanzamiento de la landing page de **AutoFlow AI**. 

Debido a que existen dependencias críticas (el copy depende de la investigación y el código depende del copy), seguiremos este flujo de trabajo secuencial:

### 📋 Plan de Ejecución

1.  **Fase de Inteligencia (Prioridad: Alta):** El `researcher` analizará a 3 competidores para identificar propuestas de valor y puntos débiles que podamos aprovechar.
2.  **Fase de Contenido (Prioridad: Alta):** Con los datos del investigador, el `writer` redactará el copy persuasivo (Hero, Features, Pricing, CTA).
3.  **Fase de Activos Visuales (Prioridad: Media):** Paralelamente al copy, el `designer` creará los assets visuales basados en la propuesta de valor.
4.  **Fase de Desarrollo (Prioridad: Alta):** El `coder` implementará el HTML/CSS utilizando el copy final y los assets visuales.
5.  **Fase de Calidad (Prioridad: Urgente):** El `reviewer` auditará el copy, el diseño y el código para asegurar que todo sea coherente y esté libre de errores antes de la entrega.

---

### 🚀 Delegación de Tareas

Comienzo activando la primera fase:

