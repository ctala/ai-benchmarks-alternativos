# Kimi K2.6 — sales_outreach/lead_qualification

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 3.84 | quality: 3.33
- latency_total: 16.568s | tokens_per_second: 41.5
- input_tokens: 280 | output_tokens: 688

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
    "score": 5,
    "bant": {
      "budget": "Desconocido - no mencionó presupuesto, startup pequeña de 5 personas sugiere recursos limitados",
      "authority": "Alto - CEO, tiene poder de decisión total",
      "need": "Medio - está explorando opciones, no hay urgencia declarada ni dolor específico",
      "timeline": "Largo - fase de exploración temprana, sin fecha definida"
    },
    "action": "Nurture educativo - enviar case studies de startups similares, invitar a webinar. No asignar SDR todavía.",
    "reason": "CEO con autoridad pero en etapa muy temprana de investigación. Sin presupuesto visible ni urgencia. Riesgo de ser solo curiosidad de blog. Necesita calentamiento antes de demo."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto - Serie B reciente, empresa de 200 empleados, capacidad de inversión confirmada",
      "authority": "Alto - VP of Operations, típicamente owner del área y con poder de decisión o fuerte influencia",
      "need": "Alto - necesidad explícita, llegó post-webinar con intención demostrada",
      "timeline": "Corto y definido - antes de Q3, deadline claro que crea urgencia"
    },
    "action": "Prioridad máxima - contacto en menos de 2 horas, preparar demo personalizada enfocada en operaciones, involucrar AE senior inmediatamente.",
    "reason": "Lead caliente con perfil ideal: autoridad, necesidad confirmada, presupuesto disponible post-Series B, y timeline urgente. Pidió demo explícitamente. Alta probabilidad de cierre rápido."
  },
  {
    "score": 3,
    "bant": {
      "budget": "Desconocido - intern sin visibilidad de presupuesto, solicita PDF de precios (típico de gatherer de información)",
      "authority": "Muy bajo - intern de marketing, no es decision maker ni influencer directo",
      "need": "Bajo - investiga por encargo de jefe, no hay necesidad personal ni profundidad en el problema",
      "timeline": "Desconocido/extendido - no menciona urgencia, solo recolección de información"
    },
    "action": "Descalificar o dejar en drip de contenido - enviar brochure público, no invertir tiempo de ventas. Intentar identificar al jefe real si es posible via LinkedIn.",
    "reason": "Classic 'information gatherer' sin poder de decisión. Solicitar PDF de precios es red flag de comparador de precios o tarea administrativa. Sin acceso al budget owner, costo de oportunidad de seguirlo es alto. Solo vale nurturing pasivo."
  }
]
```