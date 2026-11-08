# MiniMax M3 — agent_capabilities/agent_team_delegation

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.94 | quality: 8.8
- latency_total: 12.859s | tokens_per_second: 79.6
- input_tokens: 1263 | output_tokens: 1024
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

### Plan de ejecución

1. **Investigación (prioridad alta):** identificar 3 competidores directos, sus funciones, precios, propuesta de valor y opportunities de diferenciación para AutoFlow AI.
2. **Copy (depende de la investigación):** redactar hero, features, pricing y CTA con mensajes coherentes y basados en esos hallazgos.
3. **Producción paralela:**
   - **Código:** HTML y CSS responsive, semántico y listo para publicar.
   - **Diseño:** imagen hero y recursos visuales para las features, usando el copy ya aprobado.
4. **Revisión (depende de todo lo anterior):** comprobar calidad, coherencia, accesibilidad, responsive, errores técnicos y claims.
5. **Publicación:** dejaré el paquete final listo y, si no existe un mecanismo directo de publicación en el entorno, señalaré exactamente qué debe aprobarse o desplegarse. No simularé una publicación sin destino real.

Para avanzar sin bloquear el trabajo, asumiré un producto SaaS aimed a startups early-stage, con precios y claims propuestos claramente editables.