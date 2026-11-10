# GPT-OSS 120B — sales_outreach/lead_qualification

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 7.07 | quality: 6.67
- latency_total: 5.857s | tokens_per_second: 157.2
- input_tokens: 306 | output_tokens: 921

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
{
  "leads": [
    {
      "name": "Juan Perez",
      "score": 6,
      "bant": {
        "budget": "unknown",
        "authority": "yes",
        "need": "yes",
        "timeline": "unknown"
      },
      "action": "Send discovery email to clarify budget and timeline",
      "reason": "Como CEO tiene autoridad y muestra una necesidad clara de automatizar soporte, pero no ha mencionado presupuesto ni urgencia, por lo que necesita más información antes de avanzar."
    },
    {
      "name": "Ana Gomez",
      "score": 9,
      "bant": {
        "budget": "likely",
        "authority": "yes",
        "need": "yes",
        "timeline": "yes"
      },
      "action": "Schedule product demo",
      "reason": "VP of Operations tiene autoridad, la empresa cuenta con financiación Serie B (presupuesto probable), hay una necesidad explícita y una fecha límite antes del Q3, lo que la convierte en una oportunidad de alta prioridad."
    },
    {
      "name": "Carlos Ruiz",
      "score": 3,
      "bant": {
        "budget": "unknown",
        "authority": "no",
        "need": "possible",
        "timeline": "unknown"
      },
      "action": "Request conversation with the decision‑maker",
      "reason": "El interno no tiene autoridad de compra; la necesidad y el presupuesto son inciertos, por lo que el lead se considera de baja prioridad hasta que se contacte al responsable."
    }
  ]
}
```