# Mercury 2.5 — sales_outreach/lead_qualification

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.49 | quality: 10.0
- latency_total: 3.472s | tokens_per_second: 535.4
- input_tokens: 260 | output_tokens: 1859

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
    "lead": "Juan Perez",
    "score": 6,
    "bant": {
      "budget": "No mencionado",
      "authority": "CEO (Alta)",
      "need": "Automatizar soporte",
      "timeline": "Vago"
    },
    "action": "Nurture",
    "reason": "Alta autoridad y necesidad clara, pero falta confirmar presupuesto y urgencia."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Alto (Serie B)",
      "authority": "VP Operations (Alta)",
      "need": "Resolver problema",
      "timeline": "Antes de Q3"
    },
    "action": "Priorizar Venta",
    "reason": "Cumple BANT fuertemente: presupuesto disponible, decisión clara y plazo corto."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 3,
    "bant": {
      "budget": "Incógnita",
      "authority": "Intern (Baja)",
      "need": "Investigar por jefe",
      "timeline": "No especificado"
    },
    "action": "Educación",
    "reason": "Baja autoridad y etapa temprana de investigación."
  }
]