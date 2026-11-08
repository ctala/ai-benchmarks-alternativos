# Fugu Max — sales_outreach/lead_qualification

- model_id: `sakana/fugu-max`
- success: True  | final: 6.33 | quality: 6.67
- latency_total: 6.275s | tokens_per_second: 94.7
- input_tokens: 333 | output_tokens: 594

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
      "authority": "Alta; es CEO.",
      "need": "Potencial; está explorando opciones para automatizar soporte.",
      "timeline": "Indefinido; no indicó cuándo quiere implementar."
    },
    "action": "Nutrir y calificar; preguntar por presupuesto, alcance y plazo.",
    "reason": "Tiene autoridad y un posible caso de uso, pero todavía está en fase exploratoria y faltan datos clave."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Probable, aunque no confirmado; la Serie B sugiere capacidad de inversión.",
      "authority": "Alta; es VP de Operations y probablemente influye en la decisión.",
      "need": "Alta; busca resolver un problema concreto.",
      "timeline": "Urgente; necesita una solución antes de Q3."
    },
    "action": "Priorizar y agendar una demo; confirmar presupuesto y proceso de decisión.",
    "reason": "Solicitó una demo, tiene un plazo claro y trabaja en una empresa con señales de capacidad de inversión."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido; solo pidió precios.",
      "authority": "Baja; es intern y está investigando por encargo de su jefe.",
      "need": "Poco definida; busca información general sobre herramientas de IA.",
      "timeline": "Desconocido; no indicó plazo."
    },
    "action": "Enviar el PDF de precios y pedir contacto o presentación con su jefe.",
    "reason": "Puede facilitar una evaluación inicial, pero no tiene autoridad confirmada ni una necesidad o plazo específicos."
  }
]