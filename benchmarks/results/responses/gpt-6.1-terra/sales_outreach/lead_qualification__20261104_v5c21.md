# GPT-6.1 Terra — sales_outreach/lead_qualification

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 4.31 | quality: 3.33
- latency_total: 4.38s | tokens_per_second: 74.2
- input_tokens: 242 | output_tokens: 325

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
    "score": 6,
    "bant": {
      "budget": "No mencionado",
      "authority": "CEO; probable decisor",
      "need": "Busca opciones para automatizar soporte",
      "timeline": "No mencionado"
    },
    "action": "Contactar para explorar necesidades, presupuesto y plazo",
    "reason": "Tiene autoridad y una necesidad relevante, pero faltan datos sobre presupuesto y urgencia."
  },
  {
    "score": 9,
    "bant": {
      "budget": "No confirmado; la Serie B sugiere posibles recursos",
      "authority": "VP de Operaciones; probable influencia en la decisión",
      "need": "Solicitó una demo para evaluar la solución",
      "timeline": "Antes de Q3"
    },
    "action": "Priorizar y agendar una demo; confirmar presupuesto y proceso de decisión",
    "reason": "Muestra interés directo y un plazo definido, aunque su presupuesto y autoridad final deben confirmarse."
  },
  {
    "score": 3,
    "bant": {
      "budget": "No mencionado",
      "authority": "Intern; no parece ser el decisor",
      "need": "Investigación general de herramientas de IA",
      "timeline": "No mencionado"
    },
    "action": "Enviar el PDF de precios y solicitar contacto con su jefe",
    "reason": "Está en una fase inicial de investigación y no ha confirmado una necesidad específica, presupuesto ni plazo."
  }
]