# Nemotron 3 Super — sales_outreach/lead_qualification

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 5.03 | quality: 3.33
- latency_total: 1.094s | tokens_per_second: 301.7
- input_tokens: 264 | output_tokens: 330

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
    "score": 4,
    "bant": {
      "budget": "No mencionado",
      "authority": "Alta (CEO)",
      "need": "Media (en etapa de exploración)",
      "timeline": "No definido"
    },
    "action": "Nurturing / Seguimiento",
    "reason": "Tiene autoridad de decisión y un interés inicial, pero falta presupuesto, necesidad urgente y timeline definido."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto (empresa con Serie B)",
      "authority": "Alta (VP of Operations)",
      "need": "Alta (pidió demo y busca resolver el problema)",
      "timeline": "Alto (antes de Q3)"
    },
    "action": "Prioridad máxima / Agendar demo inmediata",
    "reason": "Cumple con todos los criterios BANT: presupuesto, autoridad, necesidad clara y plazo definido."
  },
  {
    "score": 2,
    "bant": {
      "budget": "Desconocido",
      "authority": "Baja (intern)",
      "need": "Baja (está investigando por encargo)",
      "timeline": "No definido"
    },
    "action": "Descartar o enviar material informativo",
    "reason": "Carece de autoridad de decisión y no es el usuario final ni el comprador; solo está recopilando información."
  }
]