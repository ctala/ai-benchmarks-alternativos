# Fugu Max — sales_outreach/lead_qualification

- model_id: `sakana/fugu-max`
- success: True  | final: 6.34 | quality: 6.67
- latency_total: 6.262s | tokens_per_second: 93.4
- input_tokens: 315 | output_tokens: 585

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
      "budget": "Desconocido; no mencionó presupuesto.",
      "authority": "Alto; es CEO y probablemente participa en la decisión.",
      "need": "Moderado; busca automatizar soporte, pero está en fase exploratoria.",
      "timeline": "Desconocido; no indicó una fecha concreta."
    },
    "action": "Calificar mediante llamada de descubrimiento y explorar presupuesto, volumen de soporte y plazo de implementación.",
    "reason": "Tiene autoridad y una necesidad potencial relevante, pero faltan señales claras de urgencia y presupuesto."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Probable; la Serie B sugiere capacidad de inversión, aunque debe confirmarse.",
      "authority": "Alto; es VP of Operations y probablemente influye directamente en la decisión.",
      "need": "Alto; expresó una necesidad concreta que requiere resolver.",
      "timeline": "Alto; necesita una solución antes de Q3."
    },
    "action": "Priorizar para contacto inmediato, realizar la demo y avanzar hacia una propuesta comercial con los decisores involucrados.",
    "reason": "Cumple claramente necesidad, autoridad y urgencia, y existen indicios sólidos de presupuesto."
  },
  {
    "score": 3,
    "bant": {
      "budget": "Desconocido; solo solicitó precios.",
      "authority": "Bajo; es intern y está investigando por encargo de su jefe.",
      "need": "Bajo a moderado; existe interés general en herramientas de IA, pero no un problema definido.",
      "timeline": "Desconocido; no indicó fecha de decisión."
    },
    "action": "Enviar el PDF de precios y solicitar los datos del jefe o decisor para una conversación de descubrimiento.",
    "reason": "Puede estar realizando una investigación inicial, pero no tiene autoridad ni una necesidad o plazo claramente establecidos."
  }
]