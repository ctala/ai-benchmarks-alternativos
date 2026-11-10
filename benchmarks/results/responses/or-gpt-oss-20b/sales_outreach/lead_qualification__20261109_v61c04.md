# GPT-OSS 20B — sales_outreach/lead_qualification

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 7.829s | tokens_per_second: 128.9
- input_tokens: 307 | output_tokens: 1009

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
      "lead_id": 1,
      "name": "Juan Perez",
      "score": 6,
      "bant": {
        "budget": "unknown",
        "authority": "yes",
        "need": "yes",
        "timeline": "unknown"
      },
      "action": "Nurture lead: send relevant case studies and pricing overview, then schedule a discovery call to clarify budget and timeline.",
      "reason": "Juan is the CEO, so he has decision‑making authority and a clear need. Budget and timeline are not disclosed, so the lead is moderately qualified."
    },
    {
      "lead_id": 2,
      "name": "Ana Gomez",
      "score": 9,
      "bant": {
        "budget": "likely",
        "authority": "yes",
        "need": "yes",
        "timeline": "urgent"
      },
      "action": "Schedule a demo immediately and assign a senior sales rep. Follow up with a proposal that meets the Q3 deadline.",
      "reason": "Ana is a VP, has a clear need, a recent Series B funding indicates available budget, and she has a tight timeline. This lead is highly qualified."
    },
    {
      "lead_id": 3,
      "name": "Carlos Ruiz",
      "score": 3,
      "bant": {
        "budget": "unknown",
        "authority": "no",
        "need": "yes",
        "timeline": "unknown"
      },
      "action": "Send the requested PDF, ask Carlos to forward it to the decision maker, and add him to the marketing nurture list for future educational content.",
      "reason": "Carlos is an intern with no decision‑making authority; budget and timeline are not known. The lead is unqualified for immediate sales action."
    }
  ]
}
```