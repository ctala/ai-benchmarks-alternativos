# Gemini 3.1 Pro — agent_capabilities/agent_team_delegation

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 8.21 | quality: 10.0
- latency_total: 26.004s | tokens_per_second: 92.1
- input_tokens: 571 | output_tokens: 2394
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza adecuadamente en la estructuración de tareas con dependencias, proporcionando un plan detallado y útil para un emprendedor.

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

¡Excelente iniciativa! Para asegurar un lanzamiento exitoso de **AutoFlow AI**, he estructurado un plan de ejecución por fases. Esto garantiza que cada sub-agente tenga la información necesaria antes de comenzar su trabajo, respetando las dependencias del proyecto.

### 📋 Plan de Ejecución:

1. **Fase 1: Investigación Competitiva (Agente: `researcher`)**
   - **Tarea:** Investigar a 3 competidores en el mercado de herramientas de automatización para startups.
   - **Objetivo:** Identificar sus propuestas de valor, funcionalidades principales y modelos de precios (pricing) para encontrar nuestro ángulo diferenciador.
   - **Prioridad:** Urgente (Esta tarea bloquea el trabajo del redactor).

2. **Fase 2: Contenido y Diseño (Agentes: `writer` y `designer`)**
   - **Tarea Writer:** Con los datos de la competencia listos, redactará el copy de la landing page (Hero, Features, Pricing, CTA) destacando por qué AutoFlow AI es superior.
   - **Tarea Designer:** En paralelo, creará la imagen principal (Hero) y los recursos visuales o iconos para la sección de características (Features) basándose en la identidad de una startup de IA.
   - **Prioridad:** Alta (Depende de la Fase 1).

3. **Fase 3: Desarrollo Web (Agente: `coder`)**
   - **Tarea:** Maquetar la landing page escribiendo el código HTML y CSS limpio y responsivo. Integrará los textos del *writer* y las imágenes del *designer*.
   - **Prioridad:** Alta (Depende de la Fase 2).

4. **Fase 4: Control de Calidad (Agente: `reviewer`)**
   - **Tarea:** Revisar la página ensamblada. Comprobará que no haya errores ortográficos, que el código no tenga bugs, que el diseño sea adaptable a móviles y que el CTA funcione correctamente.
   - **Prioridad:** Alta (Depende de la Fase 3).

Como regla de oro, el equipo de redacción y diseño no puede avanzar a ciegas. Por lo tanto, daré inicio a la **Fase 1** delegando inmediatamente la tarea de investigación a nuestro `researcher`. Una vez obtenga los resultados, activaré al resto del equipo. 

Procedo a enviar la orden al investigador: