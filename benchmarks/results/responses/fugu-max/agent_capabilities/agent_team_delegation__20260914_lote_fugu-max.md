# Fugu Max — agent_capabilities/agent_team_delegation

- model_id: `sakana/fugu-max`
- success: True  | final: 8.17 | quality: 9.5
- latency_total: 11.513s | tokens_per_second: 68.9
- input_tokens: 679 | output_tokens: 793
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, con una estructura bien organizada que un emprendedor podría aplicar directamente.

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

Plan de ejecución:

1. **Investigación competitiva**: el researcher analizará 3 competidores relevantes de automatización para startups, su propuesta de valor, funciones, precios y diferenciadores.
2. **Dirección visual**: en paralelo, el designer preparará los conceptos y assets de la imagen hero y las imágenes de features, usando como base el posicionamiento de AutoFlow AI.
3. **Copywriting**: cuando tengamos la investigación, el writer redactará el copy completo: hero, beneficios, features, pricing y CTAs. El pricing se tratará como propuesta inicial si no existe una estructura definida.
4. **Implementación**: después del copy, el coder generará una landing autocontenida en HTML/CSS, integrando los assets visuales o placeholders claramente identificados.
5. **Revisión final**: el reviewer comprobará consistencia del mensaje, claridad comercial, calidad visual, responsive design, accesibilidad, errores técnicos y posibles afirmaciones no verificadas. Entregaré un resumen consolidado con los archivos/contenidos resultantes y las observaciones pendientes antes de publicar.

Inicio ahora las tareas que pueden ejecutarse en paralelo: investigación competitiva y dirección visual.