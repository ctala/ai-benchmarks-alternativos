# GPT-5.6 Sol — sales_outreach/lead_qualification

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 6.45 | quality: 6.67
- latency_total: 4.86s | tokens_per_second: 95.1
- input_tokens: 242 | output_tokens: 462

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
    "score": 6,
    "bant": {
      "budget": "Desconocido; no mencionó presupuesto.",
      "authority": "Alta; es CEO, aunque la empresa es pequeña.",
      "need": "Media; está evaluando automatizar el soporte, pero el problema aún no parece urgente ni definido.",
      "timeline": "Desconocido; no indicó una fecha de implementación."
    },
    "action": "Nutrir y realizar discovery breve para validar volumen de soporte, presupuesto y plazo.",
    "reason": "Tiene autoridad y una necesidad potencial, pero faltan presupuesto, urgencia y señales claras de intención de compra."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Probable; la empresa acaba de levantar una Serie B, aunque debe confirmarse la partida específica.",
      "authority": "Alta; como VP of Operations probablemente influye o decide sobre la solución.",
      "need": "Alta; expresó que necesitan resolver el problema.",
      "timeline": "Alta urgencia; requiere una solución antes de Q3."
    },
    "action": "Priorizar contacto comercial inmediato, agendar la demo y avanzar a discovery con decisores y validación de presupuesto.",
    "reason": "Presenta una necesidad explícita, plazo definido, cargo relevante y capacidad financiera probable."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 3,
    "bant": {
      "budget": "Desconocido; solo solicitó información de precios.",
      "authority": "Baja; es intern y está realizando una investigación para su jefe.",
      "need": "Baja o no validada; el interés general en herramientas de IA no define un problema concreto.",
      "timeline": "Desconocido; no indicó urgencia ni fecha de compra."
    },
    "action": "Enviar el PDF de precios y contenido educativo; solicitar una presentación con su jefe o el responsable del proyecto.",
    "reason": "Es un contacto informativo sin autoridad, necesidad concreta, presupuesto confirmado ni plazo definido."
  }
]