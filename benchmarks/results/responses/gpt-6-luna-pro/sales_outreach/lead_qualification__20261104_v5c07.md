# GPT-6 Luna Pro — sales_outreach/lead_qualification

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 9.16 | quality: 10.0
- latency_total: 5.537s | tokens_per_second: 158.2
- input_tokens: 2960 | output_tokens: 876

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
        "budget": "No mencionado",
        "authority": "Probable decision maker; es CEO",
        "need": "Posible: está explorando opciones para automatizar soporte",
        "timeline": "No especificado; parece estar en etapa inicial de investigación"
      },
      "action": "Calificar más: preguntar por presupuesto, urgencia y proceso de compra",
      "reason": "Tiene autoridad y un posible encaje, pero no hay señales claras de presupuesto ni de plazo de compra."
    },
    {
      "lead": "Ana Gomez",
      "score": 9,
      "bant": {
        "budget": "Probable; la empresa acaba de levantar Serie B, aunque no confirmó presupuesto",
        "authority": "Alta influencia como VP of Operations; confirmar quién aprueba la compra",
        "need": "Alta: necesita resolver un problema concreto",
        "timeline": "Urgente: antes de Q3"
      },
      "action": "Priorizar y agendar demo; confirmar presupuesto y proceso de decisión",
      "reason": "Solicitó una demo, tiene una necesidad y un plazo definidos, y la empresa parece contar con capacidad de inversión."
    },
    {
      "lead": "Carlos Ruiz",
      "score": 3,
      "bant": {
        "budget": "No mencionado; solicita información de precios",
        "authority": "Baja: es intern y está investigando por encargo de su jefe",
        "need": "Posible, pero no está descrito con claridad",
        "timeline": "No especificado"
      },
      "action": "Enviar PDF de precios y pedir contacto o introducción con su jefe",
      "reason": "Puede ayudar a iniciar una evaluación, pero no es el decisor y faltan datos sobre necesidad, presupuesto y plazo."
    }
  ]
}