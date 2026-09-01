# Qwen 3.8 Flash — sales_outreach/lead_qualification

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 9.0 | quality: 10.0
- latency_total: 10.425s | tokens_per_second: 98.6
- input_tokens: 298 | output_tokens: 1028

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

{
  "leads": [
    {
      "lead": "Juan Perez",
      "score": 5,
      "bant": {
        "budget": "Desconocido; startup pequeña, probable presupuesto limitado",
        "authority": "Alta; CEO y decision maker",
        "need": "Media/alta; está evaluando automatizar soporte",
        "timeline": "Poco clara; fase de exploración"
      },
      "action": "Nurturing y calificación",
      "reason": "Es decision maker y tiene necesidad, pero no hay presupuesto ni timeline confirmados."
    },
    {
      "lead": "Ana Gomez",
      "score": 9,
      "bant": {
        "budget": "Probable alto; empresa de 200 empleados y Serie B reciente",
        "authority": "Alta; VP of Operations",
        "need": "Alta; solicitó demo para resolver un problema operativo",
        "timeline": "Clara y cercano; antes de Q3"
      },
      "action": "Agendar demo y enviar propuesta",
      "reason": "Cumple BANT con fuerza: presupuesto probable, autoridad, necesidad y urgencia."
    },
    {
      "lead": "Carlos Ruiz",
      "score": 2,
      "bant": {
        "budget": "Desconocido",
        "authority": "Baja; intern investigando por encargo",
        "need": "Baja/media; solo está recopilando información",
        "timeline": "Desconocido"
      },
      "action": "Baja prioridad; enviar PDF y pedir contacto del decision maker",
      "reason": "No tiene autoridad, presupuesto ni timeline claros; es un lead de investigación temprana."
    }
  ]
}