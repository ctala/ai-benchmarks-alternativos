# Tencent Hy4 preview — sales_outreach/lead_qualification

- model_id: `tencent/hy4-preview`
- success: True  | final: 5.99 | quality: 6.67
- latency_total: 89.242s | tokens_per_second: 75.2
- input_tokens: 283 | output_tokens: 6712

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
  "Lead 1": {
    "score": 5,
    "bant": {
      "budget": "Desconocido / no confirmado (startup de 5 personas, no mencionó presupuesto)",
      "authority": "Alta (CEO de startup pequeña; es el decision maker)",
      "need": "Moderada (quiere automatizar soporte, pero está en fase exploratoria)",
      "timeline": "No definido (sin urgencia ni fecha límite)"
    },
    "action": "Nurturing + discovery: enviar casos de éxito y agendar llamada para descubrir presupuesto, urgencia y fit.",
    "reason": "Tiene autoridad y una necesidad inicial, pero faltan presupuesto y timeline; vale calificar por ser CEO, aunque no es prioritario."
  },
  "Lead 2": {
    "score": 9,
    "bant": {
      "budget": "Alto / probable (empresa acaba de levantar Serie B; hay capacidad de inversión)",
      "authority": "Alta (VP of Operations; influencer clave y posible decisora, validar aprobación final)",
      "need": "Alta (pidió demo y tiene claro que deben resolver el problema)",
      "timeline": "Urgente / definido (necesitan resolverlo antes de Q3)"
    },
    "action": "Prioridad alta: asignar AE senior, agendar demo inmediata, preparar propuesta y siguientes pasos.",
    "reason": "Cumple fuertemente BANT: necesidad urgente, timeline claro, presupuesto probable por Serie B y autoridad suficiente para avanzar."
  },
  "Lead 3": {
    "score": 2,
    "bant": {
      "budget": "Desconocido / sin autoridad (intern pidiendo precios, sin presupuesto asignado)",
      "authority": "Nula/Baja (intern de marketing; no es decisor, solo investiga para su jefe)",
      "need": "Baja / vaga (investigación genérica de IA, sin problema específico confirmado)",
      "timeline": "No definido (sin urgencia ni fecha)"
    },
    "action": "Nurturing automatizado: enviar PDF de precios/recursos e intentar obtener el contacto del decisor real (su jefe); no invertir tiempo de ventas.",
    "reason": "No cumple BANT: sin autoridad, sin presupuesto, necesidad vaga y sin timeline. Solo merece nutrición de bajo costo."
  }
}