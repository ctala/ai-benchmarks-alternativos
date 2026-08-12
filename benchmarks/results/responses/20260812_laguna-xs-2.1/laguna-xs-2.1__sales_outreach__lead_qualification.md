# Poolside Laguna XS 2.1 — sales_outreach/lead_qualification

- model_id: `poolside/laguna-xs-2.1`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 4.23s | tokens_per_second: 170.7
- input_tokens: 299 | output_tokens: 722

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

{
  "leads": [
    {
      "name": "Juan Perez",
      "score": 4,
      "bant": {
        "budget": "unknown",
        "authority": "yes",
        "need": "yes",
        "timeline": "unknown"
      },
      "action": "follow_up",
      "reason": "CEO con autoridad y need identificado, pero falta información sobre presupuesto y timeline. Necesita un follow-up para calificar mejor."
    },
    {
      "name": "Ana Gomez",
      "score": 8,
      "bant": {
        "budget": "yes",
        "authority": "yes",
        "need": "yes",
        "timeline": "yes"
      },
      "action": "close_won",
      "reason": "VP of Operations con autoridad, presupuesto claro (Serie B), need identificado y timeline definido (antes de Q3). Lead calificado con alto potencial."
    },
    {
      "name": "Carlos Ruiz",
      "score": 2,
      "bant": {
        "budget": "unknown",
        "authority": "no",
        "need": "unknown",
        "timeline": "unknown"
      },
      "action": "disqualified",
      "reason": "Interno sin autoridad de decisión, sin presupuesto ni need claro. Solo solicita información básica. No es un lead caliente."
    }
  ]
}</think>{
  "leads": [
    {
      "name": "Juan Perez",
      "score": 4,
      "bant": {
        "budget": "unknown",
        "authority": "yes",
        "need": "yes",
        "timeline": "unknown"
      },
      "action": "follow_up",
      "reason": "CEO con autoridad y need identificado, pero falta información sobre presupuesto y timeline. Necesita un follow-up para calificar mejor."
    },
    {
      "name": "Ana Gomez",
      "score": 8,
      "bant": {
        "budget": "yes",
        "authority": "yes",
        "need": "yes",
        "timeline": "yes"
      },
      "action": "close_won",
      "reason": "VP of Operations con autoridad, presupuesto claro (Serie B), need identificado y timeline definido (antes de Q3). Lead calificado con alto potencial."
    },
    {
      "name": "Carlos Ruiz",
      "score": 2,
      "bant": {
        "budget": "unknown",
        "authority": "no",
        "need": "unknown",
        "timeline": "unknown"
      },
      "action": "disqualified",
      "reason": "Interno sin autoridad de decisión, sin presupuesto ni need claro. Solo solicita información básica. No es un lead caliente."
    }
  ]
}