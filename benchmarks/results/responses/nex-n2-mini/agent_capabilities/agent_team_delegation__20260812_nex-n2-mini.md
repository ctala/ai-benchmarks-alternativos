# Nex-N2-Mini — agent_capabilities/agent_team_delegation

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 9.7 | quality: 10.0
- latency_total: 1.878s | tokens_per_second: 152.3
- input_tokens: 1174 | output_tokens: 286
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza adecuadamente en la coordinación de tareas, ofreciendo un plan de ejecución útil para un emprendedor.

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

Perfecto, voy a coordinar todo el flujo de trabajo para la landing page de AutoFlow AI siguiendo el orden correcto de dependencias.

## Plan de ejecución

1. **Investigación de competencia** (researcher) - Primero necesito entender el mercado
2. **Copywriting** (writer) - Con los datos de investigación, crear el contenido
3. **Desarrollo frontend** (coder) - Implementar el código HTML/CSS
4. **Diseño de assets** (designer) - Crear imágenes hero y de features
5. **Revisión final** (reviewer) - Validar calidad antes de publicar

Vamos a empezar con la primera etapa:

