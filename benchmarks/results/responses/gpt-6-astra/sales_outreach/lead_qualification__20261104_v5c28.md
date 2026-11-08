# GPT-6 Astra — sales_outreach/lead_qualification

- model_id: `openai/gpt-6-astra`
- success: True  | final: 1.09 | quality: 0.0
- latency_total: 10.514s | tokens_per_second: 44.8
- input_tokens: 242 | output_tokens: 471

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
    "score": 5,
    "bant": {
      "budget": "No confirmado; no mencionó presupuesto.",
      "authority": "Alta: como CEO, probablemente tiene poder de decisión.",
      "need": "Interés explícito en automatizar el soporte, pero falta validar el problema y su impacto.",
      "timeline": "No definido; está explorando opciones."
    },
    "action": "Agendar una llamada breve de descubrimiento para validar necesidad, presupuesto y plazo.",
    "reason": "Tiene autoridad y una necesidad potencialmente alineada, pero aún no hay señales claras de urgencia ni presupuesto. La llegada por el blog indica interés inicial."
  },
  {
    "score": 8,
    "bant": {
      "budget": "No confirmado; la Serie B sugiere capacidad financiera, pero no garantiza presupuesto asignado.",
      "authority": "Alta influencia por su cargo de VP of Operations; falta confirmar quién aprueba la compra.",
      "need": "Reconoce un problema y pidió una demo; falta precisar el caso de uso y el impacto.",
      "timeline": "Plazo declarado: antes de Q3; confirmar año y fecha objetivo."
    },
    "action": "Priorizar la demo y validar presupuesto, proceso de aprobación y calendario de implementación.",
    "reason": "Combina intención de compra, un cargo relevante y un plazo explícito. Es el lead más prometedor, aunque la financiación no confirma presupuesto disponible para esta solución."
  },
  {
    "score": 3,
    "bant": {
      "budget": "No confirmado; pedir precios no implica tener presupuesto asignado.",
      "authority": "Baja: actúa como investigador por encargo de su jefe, sin autoridad de compra confirmada.",
      "need": "No validada; investigar herramientas de IA no identifica un problema concreto que resolver.",
      "timeline": "No definido."
    },
    "action": "Enviar el PDF de precios, preguntar por el caso de uso y solicitar una conexión con su jefe si existe encaje.",
    "reason": "Está en una etapa exploratoria y faltan señales de necesidad concreta, presupuesto y urgencia. Puede facilitar el acceso al responsable de la evaluación."
  }
]