# Nemotron 3 Nano 30B — agent_capabilities/agent_team_delegation

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 8.75 | quality: 9.6
- latency_total: 19.573s | tokens_per_second: 97.1
- input_tokens: 1350 | output_tokens: 1901
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza adecuadamente en la estructura y dependencias de las tareas, ofreciendo un plan util para un emprendedor.

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


**Plan de ejecución coordinado**

| Fase | Agente asignado | Tarea concreta | Entrada requerida | Prioridad |
|------|----------------|----------------|-------------------|-----------|
| 1️⃣ | **researcher** | Investiga a 3 competidores directos de *AutoFlow AI* (producto, características, precios, posicionamiento). | Contexto: “AutoFlow AI – herramienta de automatización para startups”. | **urgent** |
| 2️⃣ | **writer** | Redacta el copy de la landing page (hero, características, pricing, CTA) usando la información del research. | Resultado del agente *researcher*. | **high** |
| 3️⃣ | **coder** | Genera el código HTML/CSS de la página siguiendo el copy entregado. | Texto del agente *writer*. | **high** |
| 4️⃣ | **designer** | Crea los assets visuales: imagen hero y gráficos de características, basados en el copy y la identidad de marca. | Copy del agente *writer* (y cualquier guía de estilo que se tenga). | **medium** |
| 5️⃣ | **reviewer** | Revisa todos los entregables (informe de investigación, copy, código, imágenes) en busca de errores, consistencia y calidad. | Todos los artefactos anteriores. | **urgent** |
| 6️⃣ | **(opcional) human approval** | Si se requiere, solicitar autorización final antes de publicar. | Informe de revisión. | — |

**Dependencias**  
- El *writer* no puede iniciar hasta que el *researcher* entregue su análisis.  
- El *coder* y el *designer* esperan el copy del *writer*.  
- El *reviewer* solo actúa una vez que todas las piezas estén listas.

**Próximo paso**: iniciar la investigación de competidores delegando la tarea al agente **researcher**.

¿Te parece bien este plan? Si estás de acuerdo, procederé con la primera delegación.