# MiniMax M3 — sales_outreach/lead_qualification

- model_id: `minimax/minimax-m3`
- success: True  | final: 6.65 | quality: 6.67
- latency_total: 9.063s | tokens_per_second: 157.8
- input_tokens: 425 | output_tokens: 1430

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
    "lead": "Lead 1 - Juan Perez",
    "score": 6,
    "bant": {
      "budget": "No indicado; debe confirmarse.",
      "authority": "Alta: es el CEO de una startup pequeña.",
      "need": "Clara: está evaluando opciones para automatizar el soporte.",
      "timeline": "No indicado; no menciona urgencia ni fecha de compra."
    },
    "action": "Contactar para cualificación y ofrecer una demo breve; descubrir presupuesto, impacto y plazo.",
    "reason": "La autoridad y la necesidad justificaneted跟进, pero la ausencia de presupuesto y timeline reduce la prioridad."
  },
  {
    "lead": "Lead 2 - Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Probablemente disponible tras la ronda Serie B, aunque falta confirmar la asignación.",
      "authority": "Alta: es VP of Operations en una empresa de 200 empleados.",
      "need": "Clara y expresada: necesitan resolver el problema antes de Q3.",
      "timeline": "Urgente: busca una solución antes de Q3."
    },
    "action": "Agendar demo de inmediato y descubrir requisitos, interlocutores técnicos y presupuesto.",
    "reason": "Presenta una necesidad concreta, alta autoridad, señales de capacidad presupuestaria y un timeline cercano."
  },
  {
    "lead": "Lead 3 - Carlos Ruiz",
    "score": 3,
    "bant": {
      "budget": "No indicado.",
      "authority": "Baja: es un intern y solo está investigando por petición de su jefe.",
      "need": "Indirecta: el problema o interés pertenece a su jefe.",
      "timeline": "No indicado."
    },
    "action": "Enviar el PDF con precios, solicitar contexto e intentar involucrar a su jefe o responsable de compras.",
    "reason": "Hay una señal de interés y una solicitud concreta, pero no hay autoridad, presupuesto ni urgencia; debe tratarse como lead de nurture."
  }
]