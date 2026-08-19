# Claude Sonnet 5 (suscripción) — sales_outreach/lead_qualification

- model_id: `claude-sonnet-5`
- success: True  | final: 8.29 | quality: 10.0
- latency_total: 33.42s | tokens_per_second: 59.8
- input_tokens: 2 | output_tokens: 1997

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
    "lead": "Juan Pérez - CEO startup (5 personas)",
    "score": 5,
    "bant": {
      "budget": "Desconocido — startup de 5 personas, probablemente presupuesto ajustado, no lo mencionó",
      "authority": "Alta — es CEO, decision maker directo en empresa chica",
      "need": "Presente pero exploratorio — 'viendo opciones' es fase de investigación, no dolor urgente confirmado",
      "timeline": "No mencionado — sin urgencia explícita"
    },
    "action": "Nurture — enviar contenido educativo (caso de uso, comparativa) y calificar con 1-2 preguntas (presupuesto, cuándo quieren resolverlo) antes de agendar call de ventas",
    "reason": "Tiene autoridad y necesidad real, pero falta budget y timeline. Llegó por blog (intención fría vs. demo request). No descartar, pero no es prioridad de agenda inmediata."
  },
  {
    "lead": "Ana Gómez - VP Operations (200 empleados)",
    "score": 9,
    "bant": {
      "budget": "Alto probable — empresa acaba de levantar Serie B, señal fuerte de capital disponible",
      "authority": "Alta — VP of Operations, decision maker o influencer clave en compras operativas",
      "need": "Confirmado explícitamente — 'necesitamos resolver esto'",
      "timeline": "Urgente y concreto — antes de Q3"
    },
    "action": "SQL inmediato — pasar a ventas hoy, agendar demo prioritaria",
    "reason": "BANT completo: budget probable, autoridad real, necesidad explícita, deadline concreto. Pidió demo tras webinar (alta intención). Es el lead con mayor probabilidad de cerrar en el trimestre."
  },
  {
    "lead": "Carlos Ruiz - Intern Marketing",
    "score": 2,
    "bant": {
      "budget": "Desconocido, no es quien maneja presupuesto",
      "authority": "Nula — es intern ejecutando una tarea de su jefe, no decide",
      "need": "Indirecto — la necesidad es de su jefe, no confirmada de primera mano",
      "timeline": "No mencionado"
    },
    "action": "Enviar el PDF de precios vía flujo automatizado (sin involucrar a ventas) y etiquetar para nurture de largo plazo",
    "reason": "No hay autoridad de decisión ni contacto directo con el buyer real. Es investigación de tercero. Responder rápido con material self-service, pero no asignar tiempo de sales."
  }
]
```

**Resumen de priorización:** Ana Gómez (9) → agendar ya. Juan Pérez (5) → nurture con 1-2 preguntas de calificación. Carlos Ruiz (2) → self-service, cero tiempo humano.