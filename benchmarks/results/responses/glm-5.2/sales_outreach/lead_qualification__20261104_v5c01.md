# GLM 5.2 — sales_outreach/lead_qualification

- model_id: `z-ai/glm-5.2`
- success: True  | final: 8.89 | quality: 10.0
- latency_total: 8.476s | tokens_per_second: 66.5
- input_tokens: 249 | output_tokens: 564

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
    "lead": "Lead 1 - Juan Perez",
    "score": 5,
    "bant": {
      "budget": "Desconocido. No mencionó presupuesto.",
      "authority": "Alta. Es CEO, por lo que es tomador de decisiones.",
      "need": "Medio. Está explorando opciones para automatizar soporte, pero no es una urgencia crítica.",
      "timeline": "Desconocido/Bajo. Está en etapa de "viendo opciones", lo que sugiere exploración temprana."
    },
    "action": "Nurturing. Enviar caso de estudio sobre startups y agendar llamada de descubrimiento.",
    "reason": "Tiene el poder de decisión pero llegó por contenido de blog en etapa de investigación. Falta definir presupuesto y urgencia para considerarlo Sales Ready."
  },
  {
    "lead": "Lead 2 - Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Alto. La empresa acaba de levantar una Serie B, por lo que hay capital disponible.",
      "authority": "Alto. VP of Operations suele ser el tomador de decisiones o influencer clave para este tipo de software.",
      "need": "Alto. Pidió una demo de forma proactiva.",
      "timeline": "Alto. Tiene una fecha límite clara: antes de Q3."
    },
    "action": "Contacto inmediato por ventas (Sales Qualified Lead). Priorizar agendamiento de demo.",
    "reason": "Cumple con todos los criterios BANT. Tiene urgencia, presupuesto (Serie B), autoridad y necesidad explícita. Es el lead más caliente del grupo."
  },
  {
    "lead": "Lead 3 - Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido. Pide precios, pero no revela el poder adquisitivo.",
      "authority": "Nulo. Es un intern de marketing, no es tomador de decisiones.",
      "need": "Bajo. Solo cumple con la tarea de "investigar herramientas".",
      "timeline": "Desconocido. Depende de la revisión que haga su jefe luego."
    },
    "action": "Enviar material informativo y precios (Auto-respuesta). No pasar a ventas aún.",
    "reason": "Es un investigador de bajo nivel jerárquico sin autoridad de compra. No hay necesidad real ni urgencia propia. Intentar identificar y contactar a su jefe en el futuro."
  }
]
```