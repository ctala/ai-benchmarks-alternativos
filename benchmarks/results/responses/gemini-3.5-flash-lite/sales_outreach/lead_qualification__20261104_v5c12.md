# Gemini 3.5 Flash Lite — sales_outreach/lead_qualification

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 9.21 | quality: 10.0
- latency_total: 2.251s | tokens_per_second: 203.9
- input_tokens: 243 | output_tokens: 459

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
    "score": 5,
    "bant": {
      "budget": "Desconocido (startup pequeña)",
      "authority": "Alto (es CEO, toma decisiones en empresa pequeña)",
      "Need": "Medio (buscan opciones de automatización)",
      "timeline": "Bajo (solo 'están viendo opciones')"
    },
    "action": "Nurturing / Seguimiento suave",
    "reason": "Es el tomador de decisiones pero el proyecto no es urgente y no hay claridad de presupuesto. Requiere educarlo sobre el valor."
  },
  {
    "lead": "Lead 2: Ana Gomez",
    "score": 10,
    "bant": {
      "budget": "Alto (acaban de levantar Serie B y empresa de 200 empleados)",
      "authority": "Alto (VP of Operations, alta influencia/decisión)",
      "Need": "Alto (pidió demo tras webinar, necesidad clara)",
      "timeline": "Alto (necesitan resolver antes de Q3)"
    },
    "action": "Contacto inmediato / Agendar demo",
    "reason": "Cumple perfectamente con todos los criterios BANT. Alta intención de compra, presupuesto disponible y urgencia clara."
  },
  {
    "lead": "Lead 3: Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido (rol de intern)",
      "Authority": "Bajo (es becario/intern, investiga por encargo)",
      "Need": "Bajo (tarea exploratoria asignada por su jefe)",
      "timeline": "Bajo (sin urgencia explícita, solo pide información)"
    },
    "action": "Enviar recurso automatizado (PDF de precios)",
    "reason": "No tiene autoridad para decidir ni presupuesto propio. Está haciendo una tarea de investigación preliminar (gatekeeper indirecto)."
  }
]
```