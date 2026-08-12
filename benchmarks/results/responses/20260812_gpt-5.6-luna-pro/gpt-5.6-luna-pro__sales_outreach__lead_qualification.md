# GPT-5.6 Luna Pro — sales_outreach/lead_qualification

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 9.478s | tokens_per_second: 194.8
- input_tokens: 4105 | output_tokens: 1846

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
      "budget": "No mencionado; startup pequeña, capacidad presupuestaria incierta.",
      "authority": "Alta; es CEO y probablemente decision maker.",
      "need": "Moderado; está evaluando automatizar soporte, pero el problema no está claramente definido.",
      "timeline": "No definido; solo está viendo opciones."
    },
    "action": "Calificar como lead en desarrollo y enviar contenido sobre ROI, casos de uso y precios; hacer seguimiento para descubrir presupuesto y urgencia.",
    "reason": "Tiene autoridad y una necesidad potencial relevante, pero faltan presupuesto, urgencia y claridad sobre el problema."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Probablemente disponible; la empresa acaba de levantar Serie B.",
      "authority": "Alta; VP of Operations, probablemente participa directamente en la decisión.",
      "need": "Alta; expresó una necesidad concreta que busca resolver.",
      "timeline": "Alta; necesita una solución antes de Q3."
    },
    "action": "Contactar de inmediato para agendar una demo personalizada y coordinar una evaluación con los demás decisores.",
    "reason": "Cumple fuertemente los cuatro criterios BANT: tiene una necesidad clara, plazo definido, autoridad relevante y señales positivas de presupuesto."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 3,
    "bant": {
      "budget": "Desconocido; solicita precios, pero no confirma presupuesto.",
      "authority": "Baja; es intern y está investigando por encargo de su jefe.",
      "need": "Baja o preliminar; solo busca investigar herramientas de IA, sin problema específico.",
      "timeline": "Desconocido; no indicó cuándo necesitan una solución."
    },
    "action": "Enviar el PDF de precios y material introductorio; solicitar los datos del jefe o decisor para continuar la calificación.",
    "reason": "Está en una fase temprana de investigación y no tiene autoridad ni urgencia confirmadas, aunque puede servir como punto de entrada hacia el decisor."
  }
]