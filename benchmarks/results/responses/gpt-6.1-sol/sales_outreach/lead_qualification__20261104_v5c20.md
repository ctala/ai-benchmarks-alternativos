# GPT-6.1 Sol — sales_outreach/lead_qualification

- model_id: `openai/gpt-6.1-sol`
- success: True  | final: 3.97 | quality: 3.33
- latency_total: 7.276s | tokens_per_second: 62.5
- input_tokens: 242 | output_tokens: 455

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
      "authority": "Alta: es CEO y probablemente participa en la decisión de compra.",
      "need": "Identificada: busca automatizar el soporte, aunque falta conocer el problema y su impacto.",
      "timeline": "No definido; está explorando opciones."
    },
    "action": "Agendar una llamada breve de descubrimiento para validar presupuesto, necesidades y plazo.",
    "reason": "Tiene autoridad y una necesidad relevante, pero su interés es exploratorio. Llegar por el blog no demuestra intención de compra inmediata."
  },
  {
    "score": 8,
    "bant": {
      "budget": "No confirmado; la Serie B sugiere capacidad financiera, pero no garantiza presupuesto asignado.",
      "authority": "Probablemente alta por su cargo de VP of Operations; confirmar quién aprueba la compra.",
      "need": "Expresada como prioritaria; falta precisar el problema y los requisitos.",
      "timeline": "Quiere resolverlo antes de Q3; confirmar año y fecha objetivo."
    },
    "action": "Priorizar la demo y validar presupuesto, proceso de decisión y calendario de implementación.",
    "reason": "Combina una solicitud de demo, un cargo con influencia y un plazo declarado. Es el lead con mayor intención, aunque quedan aspectos de BANT por confirmar."
  },
  {
    "score": 3,
    "bant": {
      "budget": "No confirmado; solicitar precios no implica tener presupuesto aprobado.",
      "authority": "No parece ser decisor; investiga por encargo de su jefe.",
      "need": "No validada: la búsqueda de herramientas de IA es general y no identifica un problema concreto.",
      "timeline": "No indicado."
    },
    "action": "Enviar el PDF de precios solicitado, preguntar por el caso de uso y proponer incluir a su jefe en una conversación.",
    "reason": "Hay interés inicial, pero no se han confirmado necesidad específica, presupuesto ni plazo. Puede servir como contacto de entrada al decisor."
  }
]