# Grok 4.7 — sales_outreach/lead_qualification

- model_id: `x-ai/grok-4.7`
- success: True  | final: 3.89 | quality: 3.33
- latency_total: 8.835s | tokens_per_second: 87.1
- input_tokens: 1479 | output_tokens: 770

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
      "budget": "desconocido; startup de 5 personas, sin mencion de presupuesto",
      "authority": "alta; es CEO y decision maker",
      "need": "debil; exploratorio ('viendo opciones'), sin dolor confirmado",
      "timeline": "desconocida; sin urgencia"
    },
    "action": "nurture",
    "reason": "Tiene autoridad pero el interes es temprano y no hay senales de presupuesto ni plazo. Educar y recontactar cuando haya dolor o timing claros."
  },
  {
    "score": 9,
    "bant": {
      "budget": "probable; Serie B reciente implica capacidad de inversion",
      "authority": "alta; VP of Operations en empresa de 200",
      "need": "alta; pidio demo y declara que hay que resolver el problema",
      "timeline": "alta; antes de Q3"
    },
    "action": "priorizar y agendar demo ya",
    "reason": "Cumple BANT de forma solida: autoridad, necesidad explicita, plazo y senal de presupuesto. Lead caliente."
  },
  {
    "score": 2,
    "bant": {
      "budget": "desconocido",
      "authority": "nula; intern, no decide",
      "need": "no confirmada; encargo de investigacion de su jefe",
      "timeline": "desconocida"
    },
    "action": "enviar material basico y pedir intro al decision maker",
    "reason": "Solo esta recolectando info. Sin autoridad ni necesidad propia, no invertir ciclo de venta hasta llegar al jefe."
  }
]
```