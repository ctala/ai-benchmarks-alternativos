# GPT-6 Luna — sales_outreach/lead_qualification

- model_id: `openai/gpt-6-luna`
- success: True  | final: 9.22 | quality: 10.0
- latency_total: 5.982s | tokens_per_second: 74.4
- input_tokens: 242 | output_tokens: 445

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
    "score": 4,
    "bant": {
      "budget": "No mencionado; startup pequeña, capacidad de compra incierta.",
      "authority": "Probable decisor por ser CEO.",
      "need": "Interés general en automatizar el soporte; problema potencial, pero poco definido.",
      "timeline": "No indicado; está explorando opciones."
    },
    "action": "Calificar con preguntas de descubrimiento sobre presupuesto, volumen de soporte y plazo; ofrecer una conversación inicial.",
    "reason": "Tiene autoridad y una necesidad posible, pero no hay señales claras de urgencia ni presupuesto."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "No confirmado; la Serie B sugiere capacidad potencial para invertir.",
      "authority": "Probable influenciadora o decisora por su cargo de VP of Operations.",
      "need": "Alta intención: solicita una demo y busca resolver un problema concreto.",
      "timeline": "Urgente; quiere resolverlo antes de Q3."
    },
    "action": "Priorizar y agendar una demo pronto; confirmar presupuesto, criterios de compra y participantes en la decisión.",
    "reason": "Presenta una necesidad clara, urgencia y señales de capacidad de inversión. Falta confirmar presupuesto y autoridad final."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido; solo pidió un PDF con precios.",
      "authority": "Baja; es intern y está investigando por encargo de su jefe.",
      "need": "Interés exploratorio en herramientas de IA; el problema específico no está identificado.",
      "timeline": "No indicado."
    },
    "action": "Enviar el PDF de precios y solicitar el contacto de su jefe o del responsable de la evaluación.",
    "reason": "Puede aportar información inicial, pero no parece tener autoridad de compra y no hay necesidad ni plazo concretos."
  }
]