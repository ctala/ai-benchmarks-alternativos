# Qwen 3.6 35B base (OpenRouter FP8) — sales_outreach/lead_qualification

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 4.73 | quality: 3.33
- latency_total: 4.316s | tokens_per_second: 114.7
- input_tokens: 262 | output_tokens: 495

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
    "score": 3,
    "bant": {
      "budget": "No mencionado explícitamente.",
      "authority": "Es CEO (Decision Maker), pero en una startup muy pequeña, lo que podría indicar bajo presupuesto o alta flexibilidad.",
      "need": "Tiene necesidad clara (automatizar soporte), pero está solo en fase de investigación.",
      "timeline": "Vago ("viendo opciones"), sin urgencia definida."
    },
    "action": "Nurturing",
    "reason": "Aunque es un decision-maker, la etapa es muy temprana. No hay urgencia ni confirmación de presupuesto. Es mejor mantenerlo en un flujo de nutrición para educarlo sobre el valor de la solución."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alta probabilidad. La empresa acaba de levantar Serie B, lo que indica liquidez y presión para escalar.",
      "authority": "VP of Operations es un rol clave para la adopción de herramientas operativas y suele tener poder de decisión o influencia directa.",
      "need": "Necesidad explícita y dolor identificado.",
      "timeline": "Urgente ("antes de Q3")."
    },
    "action": "Contact Immediately",
    "reason": "Lead altamente calificado. Tiene presupuesto reciente, autoridad, necesidad clara y una fecha límite concreta. Es el candidato ideal para cerrar una venta rápida."
  },
  {
    "score": 2,
    "bant": {
      "budget": "Desconocido.",
      "authority": "No es decision-maker. Es un intern que solo recopila información para su jefe.",
      "need": "Necesidad detectada por el jefe, no necesariamente validada por el intern.",
      "timeline": "Desconocido."
    },
    "action": "Disqualify / Nurture",
    "reason": "El contacto no tiene autoridad de compra. Pedir un PDF de precios es una acción de investigación inicial común en estudiantes o juniors. No invertir tiempo de ventas aquí hasta que el jefe (decision-maker) haya sido identificado y contactado."
  }
]
```