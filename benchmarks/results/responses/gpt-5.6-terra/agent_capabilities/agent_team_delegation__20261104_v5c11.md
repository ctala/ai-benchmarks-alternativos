# GPT-5.6 Terra — agent_capabilities/agent_team_delegation

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.21 | quality: 9.5
- latency_total: 6.058s | tokens_per_second: 86.8
- input_tokens: 606 | output_tokens: 526
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un plan estructurado y detallado que un emprendedor podría usar directamente.

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

1. **Researcher (prioridad alta):** analizará 3 competidores relevantes de automatización para startups, con foco en propuesta de valor, funcionalidades, estructura de pricing y CTAs.
2. **Writer (alta, dependiente de research):** usará esos hallazgos para redactar el copy completo: hero, beneficios/features, pricing y CTAs, posicionando AutoFlow AI de forma diferenciada.
3. **Designer (alta, dependiente del brief/copy):** definirá y producirá los assets visuales para hero y features, alineados con la propuesta y la estructura de página.
4. **Coder (alta, dependiente de copy y assets):** construirá una landing responsive en HTML/CSS, con secciones y espacios/integración para los recursos visuales.
5. **Reviewer (urgente, al final):** verificará consistencia del mensaje, UX, responsive, accesibilidad, calidad de código y posibles errores antes de solicitar aprobación para publicar.

Comenzaré por la investigación competitiva; no publicaré nada sin una revisión final y tu aprobación.