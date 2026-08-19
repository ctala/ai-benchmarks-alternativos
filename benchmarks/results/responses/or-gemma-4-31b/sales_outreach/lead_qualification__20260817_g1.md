# Gemma 4 31B — sales_outreach/lead_qualification

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 4.73 | quality: 3.33
- latency_total: 4.853s | tokens_per_second: 72.3
- input_tokens: 277 | output_tokens: 351

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
    "score": 6,
    "bant": {
      "budget": "Desconocido",
      "authority": "Alta (CEO)",
      "need": "Confirmada (Automatizar soporte)",
      "timeline": "Desconocido"
    },
    "action": "Nutrir / Calificar",
    "reason": "Tiene la autoridad y la necesidad, pero falta definir presupuesto y urgencia. Al ser una startup pequeña, el presupuesto podría ser limitado."
  },
  {
    "score": 10,
    "bant": {
      "budget": "Probable (Serie B recién levantada)",
      "authority": "Alta (VP of Operations)",
      "need": "Confirmada (Solicitó demo)",
      "timeline": "Urgente (Antes de Q3)"
    },
    "action": "Prioridad Alta / Pasar a Ventas",
    "reason": "Cumple con todos los criterios BANT. Tiene el cargo, la urgencia temporal y respaldo financiero evidente."
  },
  {
    "score": 3,
    "bant": {
      "budget": "Desconocido",
      "authority": "Baja (Intern)",
      "need": "Indeterminada (Investigación)",
      "timeline": "Desconocido"
    },
    "action": "Nutrir / Automatizar",
    "reason": "No es el tomador de decisiones y está en fase de investigación temprana. Solo requiere envío de material informativo."
  }
]
```