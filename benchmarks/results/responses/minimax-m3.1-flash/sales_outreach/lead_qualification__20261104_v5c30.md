# MiniMax M3.1 Flash — sales_outreach/lead_qualification

- model_id: `minimax/minimax-m3.1-flash`
- success: True  | final: 4.69 | quality: 3.33
- latency_total: 6.807s | tokens_per_second: 113.3
- input_tokens: 429 | output_tokens: 771

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
      "score": 5,
      "bant": {
        "budget": "Desconocido; no se menciona presupuesto.",
        "authority": "Alta; es CEO y probablemente puede tomar la decisión.",
        "need": "Claro; quiere automatizar el soporte.",
        "timeline": "Desconocido; no indica urgencia."
      },
      "action": "Calificar en una llamada corta: confirmar presupuesto,疼 timeline, volumen de tickets y objetivos.",
      "reason": "Lead con autoridad y una necesidad explícita, pero sin señales de presupuesto ni urgencia. Debedatasetsceeding discover to qualify."
    },
    {
      "score": 9,
      "bant": {
        "budget": "Alta probabilidad; la empresa levantó una Serie B, aunque falta confirmar el presupuesto disponible.",
        "authority": "Alta; VP of Operations puede impulsivear o aprobar la solución.",
        "need": "Muy clara; necesita resolver el problema antes de Q3.",
        "timeline": "Alta; existe un plazo concreto."
      },
      "action": "Priorizar, agendar una demo personalizada y preparar propuesta comercial con próximos pasos.",
      "reason": "Lead con intención alta, autoridad, una necesidad urgente y señales de capacidad presupuestaria. Es la mejor oportunidad del lote."
    },
    {
      "score": 3,
      "bant": {
        "budget": "Desconocido; únicamente solicita precios.",
        "authority": "Baja; es un intern y su jefe es el posible decideactor.",
        "need": "Exploratoria; estáorkaizco de investigar herramientas de IA, no confirmó un problema operativo concreto.",
        "timeline": "Desconocido; no menciona urgencia."
      },
      "action": "Enviar el PDF de precios, solicitar criterios de evaluación e intentar involucrar a su jefe.",
      "reason": "Existe interés inicial, pero no hay autoridad, presupuesto, necesidad validada ni timeline. Debe tratarse como lead en formación o investigación."
    }
  ]
}