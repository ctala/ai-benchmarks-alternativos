# MiniMax M3 — sales_outreach/lead_qualification

- model_id: `minimax/minimax-m3`
- success: True  | final: 4.54 | quality: 3.33
- latency_total: 3.887s | tokens_per_second: 98.5
- input_tokens: 403 | output_tokens: 383

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
    "score": 6,
    "bant": {
      "budget": "No mencionado; startup pequeña, presupuesto probablemente limitado.",
      "authority": "Sí, es CEO y tiene capacidad de decisión.",
      "need": "Sí, está evaluando opciones para automatizar el soporte.",
      "timeline": "No indicado; está comparando opciones, pero sin urgencia declarada."
    },
    "action": "Contactar yPCT para descubrir presupuesto, alcance y urgencia.",
    "reason": "Buena autoridad y una necesidad clara, aunque la procedencia por blog y la ausencia de presupuesto y timeline requieren calificación."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alta probabilidad: la empresa acaba de levantar Serie B.",
      "authority": "Sí, como VP de Operations probablemente influye y decide en operaciones.",
      "need": "Sí, necesita resolver un problema concreto de operaciones.",
      "timeline": "Sí, lo necesita antes de Q3."
    },
    "action": "Priorizar y agendar una demo con seguimiento inmediato.",
    "reason": "Lead con señales，眼前较高，需求明确，时间节点紧迫，且刚完成融资，具备较强的预算能力。"
  },
  {
    "score": 4,
    "bant": {
      "budget": "No mencionado; solo solicita precios y un PDF.",
      "authority": "No; es un pasante tasked仅仅 con investigar herramientas.",
      "need": "Potencial, pero no ha articulated un problema propio o operativo.",
      "timeline": "No indicado."
    },
    "action": "Enviar recursos y solicitar Derivation del jefe y contexto de la evaluación.",
    "reason": "Existe intención de investigación, pero el contacto carece de autoridad, no muestra urgencia y no hay señales suficientes de presupuesto o necesidad."
  }
]