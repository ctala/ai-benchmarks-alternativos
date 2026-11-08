# Fugu Max — agent_capabilities/agent_team_delegation

- model_id: `sakana/fugu-max`
- success: True  | final: 6.5 | quality: 7.0
- latency_total: 8.675s | tokens_per_second: 89.6
- input_tokens: 697 | output_tokens: 777
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante, y clara, con una estructura bien organizada que ofrece un plan de ejecución detallado, proporcionando utilidad práctica para un emprendedor.

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

1. Investigar tres competidores y resumir sus funciones, posicionamiento, precios publicados y oportunidades para diferenciar AutoFlow AI.
2. Confirmar los datos del producto que no conviene inventar —capacidades, precio, público, diferenciadores y marca—. Mientras tanto, avanzaré con la investigación.
3. Con los hallazgos y esos datos, encargar el copy; después, producir en paralelo el diseño visual y el HTML/CSS basados en ese copy.
4. Hacer una revisión final de coherencia, afirmaciones, accesibilidad y funcionamiento. No publicaré nada sin tu aprobación explícita.

Empiezo con la investigación y te pido los datos del producto en paralelo.