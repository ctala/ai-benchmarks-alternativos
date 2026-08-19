# KAT Coder Air v2.5 — sales_outreach/lead_qualification

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 4.72 | quality: 3.33
- latency_total: 4.212s | tokens_per_second: 180.2
- input_tokens: 260 | output_tokens: 759

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
    "score": 4,
    "bant": {
      "budget": "No mencionado. No hay indicios claros de disponibilidad.",
      "authority": "Sí. Es CEO de una startup de 5 personas, tiene autoridad directa.",
      "need": "Sí. Explora opciones de automatización de soporte, pero aún está en fase de investigación.",
      "timeline": "No especificado. No hay urgencia ni plazo definido."
    },
    "action": "Nutrición",
    "reason": "Tiene autoridad y una necesidad latente, pero al no mencionar presupuesto ni timeline, y provenir del blog (canal frío), se necesita un proceso de nurturing para calificarlo mejor antes de cerrar."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto. La empresa acaba de levantar Serie B, lo que indica disponibilidad financiera significativa.",
      "authority": "Alto. Es VP of Operations, rol con poder de decisión en compras operativas.",
      "need": "Alto. Necesita resolver un problema concreto antes de Q3, no solo explorar.",
      "timeline": "Alto. Plazo definido (antes de Q3) genera urgencia real."
    },
    "action": "Cierre inmediato",
    "reason": "Lead caliente con todas las variables BANT alineadas: tiene presupuesto, autoridad, necesidad clara y urgencia temporal. Es prioridad alta para cerrar."
  },
  {
    "score": 2,
    "bant": {
      "budget": "No. Solo pide un PDF con precios, sin indicio de presupuesto asignado.",
      "authority": "Bajo. Es un intern; su jefe es quien tiene la autoridad real. No es decision maker.",
      "need": "Bajo. La necesidad la tiene su jefe, no él. Solo está investigando por encargo.",
      "timeline": "No especificado. No hay urgencia."
    },
    "action": "Descartar / Nutrición a largo plazo",
    "reason": "No es decision maker, no tiene necesidad propia ni urgencia. Podría derivarse a nurture para futuros roles de mayor autoridad, pero no justifica esfuerzo de ventas activo."
  }
]
```