# Claude Fable 5.1 — sales_outreach/lead_qualification

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 5.79 | quality: 6.67
- latency_total: 11.164s | tokens_per_second: 76.4
- input_tokens: 412 | output_tokens: 853

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
    "score": 5,
    "bant": {
      "budget": "Desconocido. No menciono presupuesto y una startup de 5 personas suele tener capacidad limitada.",
      "authority": "Alta. Es CEO, decide directamente.",
      "need": "Media. Expresa interes en automatizar soporte, pero en etapa exploratoria ('viendo opciones').",
      "timeline": "Indefinido. No hay urgencia explicita."
    },
    "action": "nurture",
    "reason": "Decision maker con necesidad real pero sin presupuesto ni timeline claros. Llego via blog (inbound temprano). Enviar contenido relevante y hacer una llamada corta de descubrimiento para validar presupuesto y urgencia antes de invertir tiempo de ventas."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Alta probabilidad. Empresa de 200 empleados que acaba de levantar Serie B, con capital fresco para herramientas.",
      "authority": "Alta. VP of Operations, decisora o influenciadora directa en compras operativas.",
      "need": "Alta. Pidio demo proactivamente despues de un webinar, indica interes concreto.",
      "timeline": "Definido y cercano. 'Antes de Q3' marca una fecha limite clara."
    },
    "action": "contactar_inmediatamente",
    "reason": "Cumple los 4 criterios BANT. Asignar a un AE senior, agendar la demo en las proximas 24-48 horas y preparar propuesta alineada al deadline de Q3."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido. Sin informacion.",
      "authority": "Nula. Es intern; solo recopila informacion para su jefe.",
      "need": "Baja/indefinida. 'Investigar herramientas de IA' es una tarea generica, no un problema identificado.",
      "timeline": "Indefinido. Sin urgencia."
    },
    "action": "descalificar_con_seguimiento_ligero",
    "reason": "No tiene autoridad ni necesidad clara. Enviar material general de precios/casos de uso de forma automatizada y pedir el contacto del jefe. Reevaluar solo si el decision maker se involucra directamente."
  }
]