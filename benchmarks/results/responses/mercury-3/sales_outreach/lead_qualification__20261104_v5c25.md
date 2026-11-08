# Mercury 3 — sales_outreach/lead_qualification

- model_id: `inception/mercury-3`
- success: True  | final: 2.85 | quality: 0.0
- latency_total: 0.989s | tokens_per_second: 400.4
- input_tokens: 270 | output_tokens: 396

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
{
  "lead_1": {
    "score": 6,
    "bant": {
      "budget": "No mencionado, desconocido",
      "authority": "Alta - es CEO",
      "need": "Moderada - quiere automatizar soporte",
      "timeline": "No especificado, parece exploratorio"
    },
    "action": "Calificar y nutrir",
    "reason": "Tiene autoridad total pero falta presupuesto y urgencia. Es una startup pequeña, el presupuesto puede ser limitado. Requiere más calificación."
  },
  "lead_2": {
    "score": 9,
    "bant": {
      "budget": "Alto - acaba de levantar Serie B",
      "authority": "Alta - VP of Operations",
      "need": "Alta - necesita resolver el problema",
      "timeline": "Urgente - antes de Q3"
    },
    "action": "Contactar inmediatamente para agendar demo",
    "reason": "Lead altamente calificado: tiene presupuesto, autoridad, necesidad clara y urgencia definida. Es una prioridad máxima."
  },
  "lead_3": {
    "score": 2,
    "bant": {
      "budget": "Desconocido, probablemente bajo",
      "authority": "Baja - es intern, no decision maker",
      "need": "No clara - solo investiga",
      "timeline": "No urgente - fase de investigación"
    },
    "action": "Enviar PDF de precios y agregar a lista de email marketing",
    "reason": "No tiene autoridad ni necesidad clara. Solo está investigando. Debe ser nutrido vía contenido automatizado, no requiere atención directa de ventas."
  }
}
```