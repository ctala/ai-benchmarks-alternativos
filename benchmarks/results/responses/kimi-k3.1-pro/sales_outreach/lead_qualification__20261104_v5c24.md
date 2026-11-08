# Kimi K3.1 Pro — sales_outreach/lead_qualification

- model_id: `moonshotai/kimi-k3.1-pro`
- success: True  | final: 8.21 | quality: 10.0
- latency_total: 21.579s | tokens_per_second: 27.6
- input_tokens: 296 | output_tokens: 596

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
      "budget": "No confirmado; startup de 5 personas sugiere presupuesto limitado",
      "authority": "Alta; es CEO y puede decidir",
      "need": "Media-alta; busca automatizar soporte, aunque esta explorando opciones",
      "timeline": "No definido; no indica urgencia"
    },
    "action": "Nutrir y calificar con discovery call breve",
    "reason": "Tiene autoridad y una necesidad relevante, pero faltan presupuesto y urgencia. Conviene validar volumen de soporte, problema actual, rango de inversion y fecha objetivo antes de una demo."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Probable; empresa de 200 empleados con Serie B reciente, aunque el monto no esta confirmado",
      "authority": "Alta; VP of Operations probablemente decide o lidera la compra",
      "need": "Alta; solicito demo y expreso necesidad de resolver el problema",
      "timeline": "Alta; necesita una solucion antes de Q3"
    },
    "action": "Priorizar y agendar demo con discovery comercial",
    "reason": "Es el lead mas calificado: combina autoridad, necesidad explicita, plazo definido y capacidad financiera probable. Deben confirmarse presupuesto, proceso de aprobacion y fecha exacta de implementacion."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 4,
    "bant": {
      "budget": "No confirmado; solicita precios, pero no indica presupuesto disponible",
      "authority": "Baja; es intern y esta investigando por encargo de su jefe",
      "need": "Potencial, pero poco especifica; solo menciona investigacion de herramientas de IA",
      "timeline": "No definido; no hay urgencia ni fecha de compra"
    },
    "action": "Enviar informacion y nutrir; intentar involucrar al jefe",
    "reason": "Puede ser el inicio de una oportunidad, pero actualmente no tiene autoridad ni requisitos claros. Conviene entregar el PDF, pedir contexto del caso de uso y solicitar una reunion con su jefe antes de asignar recursos comerciales."
  }
]
```