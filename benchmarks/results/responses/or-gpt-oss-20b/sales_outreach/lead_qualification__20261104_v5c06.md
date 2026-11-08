# GPT-OSS 20B — sales_outreach/lead_qualification

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.07 | quality: 6.67
- latency_total: 5.341s | tokens_per_second: 127.1
- input_tokens: 293 | output_tokens: 679

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
    "action": "Qualify budget and timeline",
    "reason": "CEO authority and clear need, but no budget or timeline information."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "likely",
      "authority": "yes",
      "need": "yes",
      "timeline": "yes"
    },
    "action": "Schedule demo and move to proposal",
    "reason": "Strong BANT alignment: budget (Series B), decision maker, clear need, and an urgent timeline."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "no",
      "authority": "no",
      "need": "yes",
      "timeline": "unknown"
    },
    "action": "Nurture or re‑qualify",
    "reason": "Intern lacks decision authority and budget; need exists but not directly actionable."
  }
]
```