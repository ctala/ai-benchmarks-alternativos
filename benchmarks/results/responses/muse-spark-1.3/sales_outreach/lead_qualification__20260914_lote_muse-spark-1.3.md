# Muse Spark 1.3 — sales_outreach/lead_qualification

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.6 | quality: 10.0
- latency_total: 12.686s | tokens_per_second: 156.7
- input_tokens: 257 | output_tokens: 1988

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
    "lead": "Lead 1: Juan Perez",
    "score": 5,
    "bant": {
      "budget": "Desconocido / Bajo - startup de 5 personas, no menciono presupuesto, probablemente limitado",
      "authority": "Alta - CEO, es decision maker",
      "need": "Media - interes exploratorio en automatizar soporte, sin dolor especifico confirmado",
      "timeline": "Baja - 'viendo opciones', sin urgencia, llegado via blog"
    },
    "action": "Nurture - no pasar a ventas, enviar contenido educativo y seguimiento en 2-4 semanas",
    "reason": "Tiene autoridad pero le falta presupuesto confirmado, necesidad poco definida y sin timeline. Intencion baja, requiere nutricion."
  },
  {
    "lead": "Lead 2: Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Alta - empresa de 200 empleados con Serie B reciente, alta probabilidad de presupuesto",
      "authority": "Alta - VP of Operations, decisora o champion fuerte",
      "need": "Alta - pidio demo despues de webinar, tiene problema especifico",
      "timeline": "Alta / Urgente - necesita resolver antes de Q3"
    },
    "action": "Pasar a ventas inmediatamente - SQL, agendar demo prioritaria",
    "reason": "Cumple los 4 criterios BANT con necesidad clara, urgencia definida, autoridad y capacidad de compra. Perfil ideal y alta intencion."
  },
  {
    "lead": "Lead 3: Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido - solo pide PDF con precios, sin presupuesto",
      "authority": "Nula - intern de marketing, sin poder de decision",
      "need": "Baja - encargo generico de 'investigar herramientas de IA', sin problema definido",
      "timeline": "Ninguna - sin urgencia"
    },
    "action": "Descalificar para ventas - enviar PDF self-service y dejar en nutricion de marketing",
    "reason": "Sin autoridad, necesidad vaga y sin timeline ni presupuesto. Es solo research, no es SQL."
  }
]