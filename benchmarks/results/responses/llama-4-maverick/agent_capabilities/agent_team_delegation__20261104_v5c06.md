# Llama 4 Maverick — agent_capabilities/agent_team_delegation

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 8.52 | quality: 9.3
- latency_total: 7.876s | tokens_per_second: 88.4
- input_tokens: 1269 | output_tokens: 696
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente estructurada, proporcionando un plan detallado que un emprendedor podría usar directamente.

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

¡Claro! Aquí te presento el plan de ejecución para crear la landing page de "AutoFlow AI":

**Paso 1: Investigar a la competencia**

* Delegar tarea a `researcher`: investigar qué hacen los 3 competidores principales en el mercado de herramientas de automatización para startups.
* Tarea: "Investigar competidores de AutoFlow AI"
* Contexto: "herramientas de automatización para startups"
* Prioridad: "high"

[delegate_to_agent(agent_type='researcher', task='Investigar competidores de AutoFlow AI', context='herramientas de automatización para startups', priority='high')]

**Paso 2: Escribir el copy de la landing**

* Esperar a que `researcher` complete la tarea y proporcione la información sobre los competidores.
* Delegar tarea a `writer`: escribir el copy de la landing page (hero, features, pricing, CTA) basado en la investigación realizada.
* Tarea: "Escribir copy de landing page de AutoFlow AI"
* Contexto: "información sobre competidores proporcionada por researcher"
* Prioridad: "high"

**Paso 3: Generar el código HTML/CSS**

* Esperar a que `writer` complete la tarea y proporcione el copy de la landing page.
* Delegar tarea a `coder`: generar el código HTML/CSS de la página basado en el copy proporcionado.
* Tarea: "Generar código HTML/CSS de landing page de AutoFlow AI"
* Contexto: "copy de landing page proporcionado por writer"
* Prioridad: "high"

**Paso 4: Crear las imágenes**

* Delegar tarea a `designer`: crear las imágenes hero y de features para la landing page.
* Tarea: "Crear imágenes para landing page de AutoFlow AI"
* Contexto: "copy de landing page proporcionado por writer"
* Prioridad: "medium"

**Paso 5: Revisar todo antes de publicar**

* Esperar a que `coder` y `designer` completen sus tareas.
* Delegar tarea a `reviewer`: revisar todo el contenido (copy, código, imágenes) antes de publicar.
* Tarea: "Revisar landing page de AutoFlow AI"
* Contexto: "todo el contenido proporcionado por writer, coder y designer"
* Prioridad: "urgent"

Aquí están las llamadas a las funciones correspondientes:

[delegate_to_agent(agent_type='researcher', task='Investigar competidores de AutoFlow AI', context='herramientas de automatización para startups', priority='high')]
[delegate_to_agent(agent_type='writer', task='Escribir copy de landing page de AutoFlow AI', context='información sobre competidores proporcionada por researcher', priority='high')]
[delegate_to_agent(agent_type='coder', task='Generar código HTML/CSS de landing page de AutoFlow AI', context='copy de landing page proporcionado por writer', priority='high')]
[delegate_to_agent(agent_type='designer', task='Crear imágenes para landing page de AutoFlow AI', context='copy de landing page proporcionado por writer', priority='medium')]
[delegate_to_agent(agent_type='reviewer', task='Revisar landing page de AutoFlow AI', context='todo el contenido proporcionado por writer, coder y designer', priority='urgent')]