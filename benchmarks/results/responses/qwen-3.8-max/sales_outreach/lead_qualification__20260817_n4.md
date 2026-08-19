# Qwen 3.8 Max — sales_outreach/lead_qualification

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 8.29 | quality: 10.0
- latency_total: 30.587s | tokens_per_second: 47.0
- input_tokens: 298 | output_tokens: 1438

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
    "score": 5,
    "bant": {
      "budget": "Desconocido; no mencionó presupuesto.",
      "authority": "Alta; es CEO de la startup.",
      "need": "Alta; está buscando automatizar soporte.",
      "timeline": "Bajo; solo está viendo opciones sin urgencia clara."
    },
    "action": "Enviar a SDR para calificar presupuesto y urgencia.",
    "reason": "Tiene autoridad y necesidad, pero faltan presupuesto y timeline; startup pequeña puede tener presupuesto limitado."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Probable alto; acaba de levantar Serie B.",
      "authority": "Alta; VP of Operations y solicitó demo.",
      "need": "Alta; necesita resolver el problema antes de Q3.",
      "timeline": "Alto; tiene deadline clara antes de Q3."
    },
    "action": "Priorizar demo inmediata y avanzar a propuesta.",
    "reason": "Lead enterprise con funding, urgencia, autoridad y solicitud de demo; alta probabilidad de cierre."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido o bajo; solo pide PDF con precios.",
      "authority": "Baja; es intern y no es decision maker.",
      "need": "Media/baja; investigación general de herramientas de IA.",
      "timeline": "Desconocido; sin urgencia definida."
    },
    "action": "Enviar contenido self-service y descartar para ventas.",
    "reason": "No cumple BANT; solo investigación inicial sin autoridad ni urgencia."
  }
]