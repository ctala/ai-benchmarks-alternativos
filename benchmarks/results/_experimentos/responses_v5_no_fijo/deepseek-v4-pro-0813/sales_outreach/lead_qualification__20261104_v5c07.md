# DeepSeek V4 Pro (0813) — sales_outreach/lead_qualification

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.86 | quality: 10.0
- latency_total: 5.936s | tokens_per_second: 71.9
- input_tokens: 331 | output_tokens: 427

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
    "lead": "Lead 1: Juan Perez",
    "score": 6,
    "bant": {
      "budget": "Desconocido, no mencionado",
      "authority": "Sí, es CEO",
      "need": "Sí, busca automatizar soporte",
      "timeline": "Explorando opciones, sin urgencia"
    },
    "action": "Calificar y nutrir",
    "reason": "Tiene autoridad y necesidad, pero falta presupuesto y timeline. Startup de 5 personas podría tener presupuesto limitado. Llegó por blog, interés inicial."
  },
  {
    "lead": "Lead 2: Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Sí, Serie B reciente",
      "authority": "Sí, VP of Operations",
      "need": "Sí, necesidad explícita",
      "timeline": "Urgente, antes de Q3"
    },
    "action": "Contactar inmediatamente",
    "reason": "Cumple todos los criterios BANT. Presupuesto asegurado por Serie B, autoridad clara, necesidad explícita y timeline urgente. Pidió demo activamente."
  },
  {
    "lead": "Lead 3: Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido",
      "authority": "No, es intern sin poder de decisión",
      "need": "Investigación por delegación, no necesidad propia",
      "timeline": "Sin timeline definido"
    },
    "action": "Descartar o enviar información básica",
    "reason": "Sin autoridad ni necesidad real. Es un intern investigando por encargo. Solo pide precios, no demuestra intención de compra."
  }
]
```