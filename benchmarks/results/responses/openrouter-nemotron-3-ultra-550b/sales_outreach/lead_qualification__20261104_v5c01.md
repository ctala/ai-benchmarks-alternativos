# Nemotron 3 Ultra 550B — sales_outreach/lead_qualification

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 4.54 | quality: 3.33
- latency_total: 2.838s | tokens_per_second: 159.2
- input_tokens: 264 | output_tokens: 452

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
    "score": 4,
    "bant": {
      "budget": "Desconocido - no mencionado",
      "authority": "Alta - CEO, decision maker final",
      "need": "Media - explorando opciones para automatizar soporte",
      "timeline": "Desconocida - sin urgencia declarada"
    },
    "action": "Nurture - enviar caso de estudio + agendar discovery call",
    "reason": "Buen authority y need presente, pero falta budget y timeline. Origen inbound (blog) sugiere etapa temprana. Requiere discovery para calificar budget/timeline."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alta - Serie B recien levantada",
      "authority": "Alta - VP Operations, decision maker operativo",
      "need": "Alta - solicito demo activamente tras webinar",
      "timeline": "Alta - necesita resolver antes de Q3"
    },
    "action": "Hot - pasar a sales inmediatamente para demo + proposal",
    "reason": "Cumple los 4 criterios BANT fuertemente. Budget confirmado (Serie B), authority clara, need activo (pidio demo), timeline urgente (pre-Q3). Lead listo para cierre."
  },
  {
    "score": 2,
    "bant": {
      "budget": "Desconocido - solo quiere PDF precios",
      "authority": "Baja - intern, no decision maker",
      "need": "Baja - investigando por pedido del jefe, no dolor propio",
      "timeline": "Desconocida - fase research temprana"
    },
    "action": "Disqualify / Low priority - enviar PDF automatizado, no asignar rep",
    "reason": "No es decision maker (authority baja), need indirecto, sin timeline ni budget visible. Es un influencer en etapa research. Automatizar respuesta y nutrir por email hasta que el decision maker aparezca."
  }
]