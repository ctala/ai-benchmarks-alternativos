# GPT-6 Astra — agent_capabilities/agent_team_delegation

- model_id: `openai/gpt-6-astra`
- success: True  | final: 7.19 | quality: 8.6
- latency_total: 8.874s | tokens_per_second: 43.7
- input_tokens: 606 | output_tokens: 388
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza adecuadamente en las fases necesarias para crear una landing page, ofreciendo una guía práctica y útil para un emprendedor.

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

Voy a coordinarlo en cinco fases:

1. **Investigación:** analizar tres competidores y buscar información interna de AutoFlow AI para no inventar funcionalidades ni precios.
2. **Copy:** con esos datos, redactar hero, funcionalidades, pricing y CTA.
3. **Diseño y desarrollo:** con el copy definido, crear las imágenes y desarrollar el HTML/CSS en paralelo; después integrar los assets.
4. **Revisión:** comprobar coherencia, accesibilidad, adaptación móvil, enlaces y afirmaciones comerciales.
5. **Entrega:** dejar la landing lista para tu aprobación. No la publicaré sin tu visto bueno.

Si faltan datos del producto o de marca, te pediré los imprescindibles; el resto quedará identificado como propuesta.
