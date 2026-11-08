# GPT-OSS 120B — sales_outreach/lead_qualification

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 6.69 | quality: 6.67
- latency_total: 20.588s | tokens_per_second: 41.1
- input_tokens: 293 | output_tokens: 846

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

```json
[
  {
    "lead": "Juan Perez",
    "score": 5,
    "bant": {
      "budget": "unknown",
      "authority": "yes",
      "need": "yes",
      "timeline": "unknown"
    },
    "action": "Follow up to uncover budget and timeline",
    "reason": "Como CEO tiene autoridad y ha expresado una necesidad clara de automatizar el soporte, pero no ha mencionado presupuesto ni urgencia, lo que impide calificarlo como lead caliente."
  },
  {
    "lead": "Ana Gomez",
    "score": 8,
    "bant": {
      "budget": "likely",
      "authority": "yes",
      "need": "yes",
      "timeline": "yes"
    },
    "action": "Schedule demo / move to qualified",
    "reason": "VP of Operations con autoridad, necesita solución antes del Q3 y proviene de una empresa que acaba de levantar Serie B, lo que indica disponibilidad de presupuesto."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 3,
    "bant": {
      "budget": "unknown",
      "authority": "no",
      "need": "partial",
      "timeline": "unknown"
    },
    "action": "Request referral to decision‑maker",
    "reason": "Intern no tiene autoridad de compra y no se ha hablado de presupuesto ni de urgencia; solo hay una indicación de necesidad a nivel de investigación."
  }
]
```