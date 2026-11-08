# Gemma 4 31B — sales_outreach/lead_qualification

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 3.72s | tokens_per_second: 100.8
- input_tokens: 261 | output_tokens: 375

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
    "score": 6,
    "bant": {
      "budget": "Desconocido",
      "authority": "Alta (CEO)",
      "need": "Confirmada (automatizar soporte)",
      "timeline": "Desconocido"
    },
    "action": "Calificación adicional / Discovery Call",
    "reason": "Es el tomador de decisiones y tiene la necesidad, pero falta validar presupuesto y urgencia."
  },
  {
    "lead": "Ana Gomez",
    "score": 10,
    "bant": {
      "budget": "Probable (Serie B levantada)",
      "authority": "Alta (VP of Operations)",
      "need": "Confirmada (solicitó demo)",
      "timeline": "Urgente (antes de Q3)"
    },
    "action": "Prioridad Alta / Agendar Demo inmediatamente",
    "reason": "Cumple con todos los criterios BANT. Empresa con capital fresco, cargo decisor y fecha límite clara."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 3,
    "bant": {
      "budget": "Desconocido",
      "authority": "Nula (Intern)",
      "need": "Indirecta (investigación)",
      "timeline": "Desconocido"
    },
    "action": "Nutrición automatizada / Enviar PDF",
    "reason": "No es el decisor. Es un lead informativo que requiere ser nutrido hasta que pueda conectarnos con su jefe."
  }
]
```