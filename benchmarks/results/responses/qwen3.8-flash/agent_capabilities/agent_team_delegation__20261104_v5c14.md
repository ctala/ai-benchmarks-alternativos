# Qwen 3.8 Flash — agent_capabilities/agent_team_delegation

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.75 | quality: 9.8
- latency_total: 16.531s | tokens_per_second: 97.1
- input_tokens: 1190 | output_tokens: 1605
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando una estructura detallada y organizada para la delegación de tareas con dependencias.

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

Voy a coordinarlo como un flujo con dependencias:

1. **Investigación** → `researcher` analiza 3 competidores de `AutoFlow AI`  
   - Qué ofrecen, a quién atacan, features, pricing, mensajes clave y ángulos de conversión.
2. **Copy** → `writer` usará los hallazgos del research para escribir:
   - Hero, features, pricing, CTA.
3. **Diseño visual** → `designer` generará dirección visual, hero image y imágenes de features.
4. **Código** → `coder` construirá HTML/CSS a partir del copy + assets.
5. **Revisión** → `reviewer` validará contenido, estructura, accesibilidad, consistencia y riesgos.
6. **Aprobación final** → si todo está correcto, preparo la versión publicable; no publicaré sin confirmación humana si hay decisiones de negocio pendientes.

Mientras tanto, empiezo con dos cosas en paralelo:
- investigación de competencia
- búsqueda de información interna sobre el producto

También necesito una aclaración rápida para no inventar datos críticos de negocio.

