# Step 3.5 Flash — agent_capabilities/agent_team_delegation

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 8.69 | quality: 9.5
- latency_total: 13.626s | tokens_per_second: 75.7
- input_tokens: 1166 | output_tokens: 1031
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un plan detallado y estructurado que un emprendedor podría implementar directamente.

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

Voy a coordinar este proyecto de landing page para AutoFlow AI siguiendo un enfoque estructurado. Antes de delegar, te presento el plan de ejecución completo:

## Plan de Ejecución

**Fase 1: Investigación Estratégica (Prioridad: Alta)**
- researcher investigará 3 competidores directos de herramientas de automatización para startups
- Se enfocará en: propuesta de valor, features, pricing, diseño y messaging
- Esta información es CRÍTICA para que el writer cree un copy diferenciador

**Fase 2: Copywriting (Prioridad: Alta)**
- writer redactará todo el copy: hero section, features, pricing, CTA
- Se basará en la investigación para destacar ventajas competitivas
- Incluirá llamado a la acción claro y persuasivo

**Fase 3: Creación de Assets Visuales (Prioridad: Media)**
- designer creará imágenes hero y para features
- Coordinará con writer para alinear el estilo visual con el mensaje
- Puede iniciar cuando writer tenga el borrador del copy

**Fase 4: Desarrollo Técnico (Prioridad: Media)**
- coder generará código HTML/CSS completo y responsive
- Implementará el copy y estructurará para las imágenes del designer
- Puede trabajar en paralelo con designer

**Fase 5: Revisión Integral (Prioridad: Alta - Final)**
- reviewer validará: coherencia del mensaje, calidad del código, diseño visual, SEO basics
- Producirá informe de calidad antes de la publicación

---

Vamos a comenzar con la **Fase 1: Investigación**. Delego ahora al researcher: