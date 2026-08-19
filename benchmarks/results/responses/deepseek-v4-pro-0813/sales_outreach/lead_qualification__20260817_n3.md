# DeepSeek V4 Pro (0813) — sales_outreach/lead_qualification

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 3.64 | quality: 3.33
- latency_total: 92.394s | tokens_per_second: 44.6
- input_tokens: 340 | output_tokens: 4123

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
    "lead": "Lead 1",
    "score": 6,
    "bant": {
      "budget": "No mencionado; startup pequeña sugiere presupuesto limitado",
      "authority": "Sí, CEO y tomador de decisión",
      "need": "Sí, busca automatizar soporte",
      "timeline": "No definido; en exploración"
    },
    "action": "Contactar para calificar presupuesto y urgencia; enviar caso de uso para startups.",
    "reason": "CEO con autoridad y necesidad clara, pero falta validar presupuesto y timeline."
  },
  {
    "lead": "Lead 2",
    "score": 9,
    "bant": {
      "budget": "Sí, Serie B reciente sugiere presupuesto disponible",
      "authority": "Sí, VP Operations con poder de decisión/influencia",
      "need": "Sí, necesidad explícita de resolver antes de Q3",
      "timeline": "Urgente, antes de Q3"
    },
    "action": "Priorizar y agendar demo inmediata; involucrar a ventas.",
    "reason": "BANT completo, alta intención y urgencia."
  },
  {
    "lead": "Lead 3",
    "score": 3,
    "bant": {
      "budget": "Desconocido; pide precios pero sin autoridad",
      "authority": "No, intern sin poder de decisión",
      "need": "No clara; solo investiga para su jefe",
      "timeline": "Sin timeline definido"
    },
    "action": "Enviar PDF de precios y solicitar contacto con el jefe/decision maker; mantener en nurture.",
    "reason": "Sin autoridad ni urgencia; requiere contacto con tomador de decisión."
  }
]