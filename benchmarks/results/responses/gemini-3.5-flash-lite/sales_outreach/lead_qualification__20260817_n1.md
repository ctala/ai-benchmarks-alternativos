# Gemini 3.5 Flash Lite — sales_outreach/lead_qualification

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 9.24 | quality: 10.0
- latency_total: 2.76s | tokens_per_second: 143.9
- input_tokens: 245 | output_tokens: 397

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
    "lead": "Lead 1: Juan Perez",
    "score": 5,
    "bant": {
      "budget": "No mencionado",
      "authority": "Alto (CEO)",
      "need": "Medio (buscan opciones de automatización)",
      "timeline": "Indefinido (están viendo opciones)"
    },
    "action": "Nurturing",
    "reason": "Es el tomador de decisiones y tiene la necesidad, pero el timeline es exploratorio y no hay claridad de presupuesto dado el tamaño temprano de la startup."
  },
  {
    "lead": "Lead 2: Ana Gomez",
    "score": 10,
    "bant": {
      "budget": "Alto (acaban de levantar Serie B)",
      "authority": "Alto (VP of Operations)",
      "need": "Alto (pidió demo tras webinar, urgencia clara)",
      "timeline": "Urgente (antes de Q3)"
    },
    "action": "Contacto Inmediato",
    "reason": "Cumple perfectamente con todos los criterios BANT. Alta intención, presupuesto disponible por ronda reciente, tomadora de decisiones y urgencia definida."
  },
  {
    "lead": "Lead 3: Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido (pide PDF de precios)",
      "authority": "Bajo (intern/pasante)",
      "need": "Bajo (investigación por encargo)",
      "timeline": "Indefinido"
    },
    "action": "Descartar o Automatizar",
    "reason": "No es tomador de decisiones y su rol es puramente de investigación preliminar. Enviar el PDF automáticamente sin gastar tiempo de ventas."
  }
]
```