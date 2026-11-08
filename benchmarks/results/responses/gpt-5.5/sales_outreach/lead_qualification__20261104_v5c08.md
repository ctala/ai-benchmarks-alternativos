# GPT-5.5 — sales_outreach/lead_qualification

- model_id: `gpt-5.5`
- success: True  | final: 8.44 | quality: 10.0
- latency_total: 5.879s | tokens_per_second: 68.9
- input_tokens: 242 | output_tokens: 405

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

[
  {
    "lead": "Lead 1 - Juan Perez",
    "score": 6,
    "bant": {
      "budget": "No mencionado",
      "authority": "Alta: es CEO, aunque en una startup pequeña",
      "need": "Media/alta: está evaluando automatizar soporte",
      "timeline": "No claro: está explorando opciones"
    },
    "action": "Nutrir y agendar llamada de discovery",
    "reason": "Tiene autoridad y un posible need relevante, pero falta validar presupuesto, urgencia y alcance del problema."
  },
  {
    "lead": "Lead 2 - Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Probable: empresa Serie B con capacidad de inversión",
      "authority": "Alta: VP of Operations, probablemente influye o decide",
      "need": "Alta: expresó necesidad concreta de resolver el problema",
      "timeline": "Alta urgencia: necesita solución antes de Q3"
    },
    "action": "Priorizar para contacto inmediato y agendar demo con sales senior",
    "reason": "Cumple muy bien con BANT: tiene necesidad clara, urgencia definida, autoridad relevante y probable presupuesto."
  },
  {
    "lead": "Lead 3 - Carlos Ruiz",
    "score": 3,
    "bant": {
      "budget": "No mencionado; solo pide precios",
      "authority": "Baja: es intern y está investigando por encargo",
      "need": "Baja/media: interés general en herramientas de IA, sin problema específico",
      "timeline": "No claro"
    },
    "action": "Enviar PDF con precios y contenido educativo; intentar identificar al jefe o decision maker",
    "reason": "Tiene baja autoridad y la necesidad no está definida. Puede ser un lead temprano, pero requiere calificación adicional."
  }
]