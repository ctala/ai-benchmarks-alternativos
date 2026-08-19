# Step 3.5 Flash — sales_outreach/lead_qualification

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 4.32 | quality: 3.33
- latency_total: 26.554s | tokens_per_second: 66.3
- input_tokens: 274 | output_tokens: 1760

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

[
  {
    "score": 6,
    "bant": {
      "budget": "incierto",
      "authority": "sí",
      "need": "sí",
      "timeline": "incierto"
    },
    "action": "Calificar con llamada de descubrimiento para identificar presupuesto y timeline.",
    "reason": "CEO interesado en automatizar soporte, pero no hay claridad en presupuesto ni urgencia. Se necesita más información."
  },
  {
    "score": 9,
    "bant": {
      "budget": "sí",
      "authority": "sí",
      "need": "sí",
      "timeline": "corto plazo"
    },
    "action": "Proceder inmediatamente con demo y seguimiento para avanzar en el proceso de ventas.",
    "reason": "VP con autoridad, necesidad urgente (antes de Q3) y presupuesto disponible tras ronda Serie B. Lead altamente calificado."
  },
  {
    "score": 2,
    "bant": {
      "budget": "no/incierto",
      "authority": "no",
      "need": "potencial",
      "timeline": "incierto"
    },
    "action": "Enviar PDF de precios y mantener en nurture; no priorizar.",
    "reason": "Interno investigando sin autoridad de decisión y necesidad no validada. Bajo potencial de conversión."
  }
]