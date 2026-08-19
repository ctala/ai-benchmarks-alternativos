# Claude Sonnet 5 — sales_outreach/lead_qualification

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.3 | quality: 10.0
- latency_total: 19.955s | tokens_per_second: 88.8
- input_tokens: 410 | output_tokens: 1772

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente de calificacion de leads. Evalua cada lead con un score 1-10 y decide la accion.

Framework BANT:
- Budget: tiene presupuesto?
- Authority: es decision maker?
- Need: tiene el problema que resolvemos?
- Timeline: necesita solucion pronto?

Responde en JSON: {"score": N, "bant": {"budget": "...", "authority": "...", "need": "...", "timeline": "..."}, "action": "...", "reason": "..."}

**user:**

Lead 1: Juan Perez, CEO de una startup de 5 personas. Dice que "estamos viendo opciones para automatizar nuestro soporte". No menciono presupuesto. Llego via el blog.

Lead 2: Ana Gomez, VP of Operations en empresa de 200 empleados. Pidio una demo despues de un webinar. Dijo que "necesitamos resolver esto antes de Q3". Su empresa acaba de levantar Serie B.

Lead 3: Carlos Ruiz, intern de marketing. Dice que su jefe le pidio "investigar herramientas de IA". Quiere un PDF con precios.

Califica los 3 leads.


## Respuesta completa

```json
[
  {
    "lead": "Juan Perez - CEO Startup",
    "score": 5,
    "bant": {
      "budget": "Desconocido/no mencionado. Startup de 5 personas sugiere presupuesto limitado o inexistente aún.",
      "authority": "Alta - es CEO, decision maker directo.",
      "need": "Existe pero es exploratorio - 'viendo opciones' indica etapa temprana de research, no dolor urgente confirmado.",
      "timeline": "No mencionado - sin urgencia explícita, fase de exploración."
    },
    "action": "Nutrir + calificar con pregunta directa",
    "reason": "Autoridad alta compensa parcialmente la falta de budget/timeline claros. Enviar contenido educativo (casos de uso, ROI calculator) y hacer 1 pregunta clave sobre presupuesto/timeline antes de invertir tiempo de sales. No pasar a SQL todavía."
  },
  {
    "lead": "Ana Gomez - VP Operations",
    "score": 9,
    "bant": {
      "budget": "Alta probabilidad - empresa acaba de levantar Serie B, señal fuerte de capital disponible.",
      "authority": "Alta - VP of Operations, típicamente decision maker o influencer clave con poder de compra.",
      "need": "Explícito y claro - 'necesitamos resolver esto', dolor confirmado.",
      "timeline": "Definido y con deadline - 'antes de Q3', urgencia real."
    },
    "action": "Pasar a Sales inmediatamente - agendar demo/call prioritario",
    "reason": "Cumple los 4 criterios BANT con señales fuertes. Empresa de tamaño relevante, funding reciente, deadline concreto y solicitud de demo post-webinar indica alto intent. Es un SQL (Sales Qualified Lead) de alta prioridad."
  },
  {
    "lead": "Carlos Ruiz - Intern Marketing",
    "score": 2,
    "bant": {
      "budget": "Desconocido - no tiene visibilidad ni control sobre presupuesto.",
      "authority": "Nula - es intern, solo está investigando por pedido de su jefe.",
      "need": "Vago - 'investigar herramientas de IA' es genérico, no hay dolor específico articulado.",
      "timeline": "No mencionado - sin urgencia."
    },
    "action": "Nutrir vía marketing automation - enviar PDF y agregar a nurture flow",
    "reason": "No es decision maker ni tiene autoridad de compra. Es lead de bajo intent en fase muy temprana de research corporativo. Enviar el PDF solicitado (contenido self-service) y capturar el email del jefe/decision maker real si es posible, pero no asignar tiempo de sales aquí."
  }
]
```