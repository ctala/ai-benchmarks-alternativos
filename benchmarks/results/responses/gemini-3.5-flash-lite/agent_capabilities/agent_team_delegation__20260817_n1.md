# Gemini 3.5 Flash Lite — agent_capabilities/agent_team_delegation

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 9.37 | quality: 10.0
- latency_total: 1.771s | tokens_per_second: 201.5
- input_tokens: 878 | output_tokens: 357
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

¡Hola! Me encargo de coordinar a todo el equipo para crear la landing page de **AutoFlow AI**. 

Para asegurar un resultado óptimo, seguiremos un flujo de trabajo estructurado con dependencias claras (por ejemplo, el copy depende de la investigación, el diseño del copy, el código del diseño y el copy, y finalmente la revisión evalúa el conjunto).

---

### 📋 Plan de Ejecución

1. **Fase de Investigación (Researcher):** Analizar 3 competidores principales de herramientas de automatización para startups para identificar fortalezas, debilidades y oportunidades de diferenciación. *(Prioridad: alta)*
2. **Fase de Contenido (Writer):** Escribir el copy completo de la landing (Hero, Features, Pricing y CTA) basado en los insights del investigador. *(Prioridad: alta - Depende de #1)*
3. **Fase de Diseño Visual (Designer):** Crear las especificaciones o assets visuales para la imagen Hero y las secciones de Features basándose en el copy. *(Prioridad: media - Depende de #2)*
4. **Fase de Desarrollo (Coder):** Desarrollar el código HTML/CSS limpio, responsive y moderno de la landing page integrando el copy y los placeholders/diseños visuales. *(Prioridad: alta - Depende de #2 y #3)*
5. **Fase de Control de Calidad (Reviewer):** Revisar ortografía, coherencia del copy, calidad del código, diseño responsive y propuesta de valor frente a la competencia. *(Prioridad: urgente - Depende de #4)*

---

Comenzaremos activando al primer agente: **Researcher**.