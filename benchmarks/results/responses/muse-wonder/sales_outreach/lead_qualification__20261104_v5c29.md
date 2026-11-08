# Muse Wonder — sales_outreach/lead_qualification

- model_id: `meta/muse-wonder`
- success: True  | final: 8.38 | quality: 10.0
- latency_total: 12.229s | tokens_per_second: 109.2
- input_tokens: 258 | output_tokens: 1335

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
    "score": 4,
    "bant": {
      "budget": "desconocido - no mencionado, startup pequeña de 5 personas",
      "authority": "alta - es CEO y decision maker",
      "need": "media - interés exploratorio en automatizar soporte, sin problema definido",
      "timeline": "bajo - está viendo opciones, sin urgencia ni fecha"
    },
    "action": "nurture - enviar contenido y agendar llamada de descubrimiento de baja prioridad",
    "reason": "Tiene autoridad pero necesidad, presupuesto y timeline no están calificados. Lead temprano llegado vía blog."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "alto probable - empresa de 200 empleados que acaba de levantar Serie B, falta confirmar monto",
      "authority": "alta - VP of Operations, decision maker",
      "need": "alta - necesidad clara y pidió una demo",
      "timeline": "alto - necesita resolverlo antes de Q3"
    },
    "action": "contactar inmediatamente - prioridad alta, pasar a ventas y agendar demo",
    "reason": "Cumple casi todo BANT: autoridad, necesidad clara, urgencia definida y señales fuertes de presupuesto."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "desconocido - solo pide PDF de precios, sin presupuesto confirmado",
      "authority": "nula - es intern, no es decision maker",
      "need": "baja - investigación delegada por su jefe, sin problema propio definido",
      "timeline": "bajo - sin fecha ni urgencia mencionada"
    },
    "action": "no pasar a ventas - enviar PDF y pedir ser referido al decision maker",
    "reason": "Sin autoridad, presupuesto ni timeline. Es un investigador inicial, no un comprador calificado."
  }
]