# Nex-N2-Mini — sales_outreach/lead_qualification

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 4.88 | quality: 3.33
- latency_total: 3.701s | tokens_per_second: 202.6
- input_tokens: 259 | output_tokens: 750

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
      "budget": "No mencionado. Requiere validación.",
      "authority": "Alta: es CEO de una startup de 5 personas.",
      "need": "Media: está evaluando automatizar soporte, pero aún no expresa urgencia clara.",
      "timeline": "No especificado."
    },
    "action": "Contactar para cualificar y descubrir presupuesto, urgencia y próximos pasos.",
    "reason": "Tiene autoridad y una necesidad inicial, pero falta información clave sobre presupuesto y timeline. Lead temprano pero potencial."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto: la empresa acaba de levantar Serie B.",
      "authority": "Alta: VP of Operations, probablemente decisora o influencer clave.",
      "need": "Alta: necesita resolver un problema operativo.",
      "timeline": "Alta: necesita solución antes de Q3."
    },
    "action": "Priorizar y contactar de inmediato para agendar demo.",
    "reason": "Tiene necesidad clara, autoridad relevante, buena capacidad presupuestaria y una ventana de decisión concreta."
  },
  {
    "score": 2,
    "bant": {
      "budget": "No mencionado.",
      "authority": "Baja: es interno de marketing y no parece tomador de decisión.",
      "need": "Media: está investigando herramientas de IA, pero no confirma necesidad concreta.",
      "timeline": "No especificado."
    },
    "action": "Nutrir y enviar material informativo, pero no priorizar venta directa.",
    "reason": "Hay curiosidad inicial, pero baja autoridad y falta de contexto sobre presupuesto, problema real y urgencia. Conviene identificar al decisor."
  }
]