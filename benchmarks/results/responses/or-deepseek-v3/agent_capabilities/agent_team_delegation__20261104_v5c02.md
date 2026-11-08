# DeepSeek V3 — agent_capabilities/agent_team_delegation

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 8.51 | quality: 9.5
- latency_total: 12.97s | tokens_per_second: 36.2
- input_tokens: 1220 | output_tokens: 470
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

Perfecto, voy a coordinar la creación completa de la landing page para "AutoFlow AI". Primero, voy a descomponer esta tarea compleja en sub-tareas secuenciales para cada agente especializado.

## Plan de Ejecución:

**Fase 1 - Investigación** → researcher
- Analizar 3 competidores principales en automatización para startups
- Identificar puntos fuertes/débiles de cada uno
- Recolectar información sobre precios y características

**Fase 2 - Diseño Visual** → designer  
- Crear imágenes hero (principal y secundarias)
- Diseñar ilustraciones para cada feature
- Establecer paleta de colores y estilo visual

**Fase 3 - Redacción** → writer  
- Escribir copy basado en investigación y assets visuales
- Definir estructura: hero, features, pricing, CTA
- Optimizar mensajes de conversión

**Fase 4 - Desarrollo** → coder  
- Generar código HTML/CSS responsive
- Implementar interacciones y animaciones
- Optimizar para performance

**Fase 5 - Revisión** → reviewer  
- Revisar calidad, errores y consistencia
- Asegurar compatibilidad cross-browser
- Verificar mensajería y UX

Empezaré con la investigación de la competencia: