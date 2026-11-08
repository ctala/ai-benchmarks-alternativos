# Nemotron 3 Nano 30B — sales_outreach/lead_qualification

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 4.58 | quality: 3.33
- latency_total: 5.264s | tokens_per_second: 57.2
- input_tokens: 264 | output_tokens: 301

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
    "lead": "Lead 1",
    "score": 3,
    "bant": {
      "budget": "No mencionado",
      "authority": "CEO, posible decisión",
      "need": "Busca automatizar soporte",
      "timeline": "No especificado"
    },
    "action": "Nurturing",
    "reason": "Es CEO pero no hay información de presupuesto ni necesidad concreta ni plazo."
  },
  {
    "lead": "Lead 2",
    "score": 9,
    "bant": {
      "budget": "Implicado por Serie B y necesidad urgente",
      "authority": "VP de Operations",
      "need": "Resolver problema antes de Q3",
      "timeline": "Antes de Q3"
    },
    "action": "Prioritize",
    "reason": "Tiene autoridad, presupuesto probable, necesidad clara y plazo definido."
  },
  {
    "lead": "Lead 3",
    "score": 2,
    "bant": {
      "budget": "No mencionado",
      "authority": "Intern, no decisor",
      "need": "Información de precios",
      "timeline": "Sin plazo definido"
    },
    "action": "Nurture",
    "reason": "Solo busca información básica y no tiene autoridad ni presupuesto definido."
  }
]