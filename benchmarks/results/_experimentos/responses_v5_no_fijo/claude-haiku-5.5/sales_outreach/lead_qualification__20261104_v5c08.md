# Claude Haiku 5.5 — sales_outreach/lead_qualification

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.2 | quality: 10.0
- latency_total: 5.746s | tokens_per_second: 197.0
- input_tokens: 411 | output_tokens: 1132

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
    "lead": "Juan Perez",
    "score": 5,
    "bant": {
      "budget": "No mencionado. Una startup de 5 personas puede tener presupuesto limitado; hay que confirmarlo.",
      "authority": "Alta. Es CEO, por lo que probablemente es decision maker.",
      "need": "Medio. Indica que 'estamos viendo opciones para automatizar nuestro soporte', lo que sugiere una necesidad, pero no es un dolor urgente ni esta cuantificado.",
      "timeline": "Desconocido. No hay fecha ni urgencia expresada."
    },
    "action": "Nurturing con seguimiento por email personalizado. Hacer preguntas de descubrimiento sobre volumen de soporte, herramientas actuales y presupuesto aproximado antes de ofrecer demo.",
    "reason": "Autoridad y necesidad probable, pero sin presupuesto confirmado, sin urgencia y con empresa pequena. Vale la pena calificarlo mejor antes de invertir tiempo de ventas. Llego por el blog, lo que indica interes inicial."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Alto probable. Empresa de 200 empleados que acaba de levantar Serie B, con capital disponible.",
      "authority": "Alta. Es VP of Operations, con poder de decision o influencia directa en la compra.",
      "need": "Alto. Pidio demo tras un webinar y menciona que necesita resolver el problema, senal de dolor activo.",
      "timeline": "Urgente. 'Antes de Q3' define una fecha concreta y cercana."
    },
    "action": "Prioridad maxima. Agendar demo en las proximas 48 horas con un ejecutivo senior. Preparar caso de uso y referencias de empresas similares. Confirmar stakeholders y proceso de compra.",
    "reason": "Cumple los cuatro criterios BANT con fuerza: presupuesto probable por la reciente ronda, autoridad ejecutiva, necesidad expresada y plazo definido. Es el lead mas calificado."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "No es decision maker de presupuesto. Solo esta investigando por encargo.",
      "authority": "Baja. Es intern, sin poder de compra.",
      "need": "Bajo a medio. Su jefe pidio investigar herramientas de IA, pero no hay un problema concreto identificado.",
      "timeline": "Sin urgencia. Es una tarea de investigacion."
    },
    "action": "No enviar PDF con precios de forma directa. Enviar material general de producto y case studies, y solicitar contacto con su jefe o responsable de la decision para una conversacion de descubrimiento. Mantener en lista de nurturing de bajo esfuerzo.",
    "reason": "Es un influenciador temprano, no un comprador. Vale la pena dejar la puerta abierta a su jefe, pero no invertir esfuerzo de ventas en el. Un PDF de precios sin contexto tampoco genera conversion."
  }
]
```