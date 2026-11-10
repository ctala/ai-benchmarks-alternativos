# Claude Fable 5.2 — sales_outreach/lead_qualification

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 8.04 | quality: 10.0
- latency_total: 19.798s | tokens_per_second: 85.8
- input_tokens: 412 | output_tokens: 1699

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
    "score": 5,
    "bant": {
      "budget": "Desconocido. No lo mencionó y una startup de 5 personas probablemente tiene presupuesto limitado.",
      "authority": "Alta. Es el CEO y decide directamente.",
      "need": "Media. Quiere automatizar soporte, pero está en fase exploratoria ('viendo opciones').",
      "timeline": "Indefinido. No hay urgencia ni fecha."
    },
    "action": "Nurturing y llamada corta de discovery para calificar presupuesto, volumen de soporte y timeline. Ofrecer plan de entrada o trial si existe.",
    "reason": "Es decision maker con una necesidad real, pero faltan presupuesto y urgencia, y la cuenta es pequeña. Puede subir de prioridad si la llamada confirma presupuesto y fecha."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Probable. La empresa acaba de levantar Serie B, aunque falta confirmar la partida específica.",
      "authority": "Alta. Como VP of Operations es decisora o influenciadora clave; falta confirmar si participan otros (CFO, IT).",
      "need": "Alta. Pidió demo por iniciativa propia y habla de un problema concreto ('necesitamos resolver esto').",
      "timeline": "Definido y cercano: antes de Q3."
    },
    "action": "Prioridad máxima: asignar a un Account Executive y agendar la demo en 24-48 horas. En la llamada, confirmar presupuesto, proceso de compra y stakeholders.",
    "reason": "Cumple los cuatro criterios BANT: financiamiento reciente, cargo senior, necesidad explícita y fecha límite. Es una cuenta de 200 empleados con alta intención."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 3,
    "bant": {
      "budget": "Desconocido. No tiene visibilidad ni control del presupuesto.",
      "authority": "Nula. Es intern y solo recopila información para su jefe.",
      "need": "Vaga. 'Investigar herramientas de IA' no describe un problema concreto.",
      "timeline": "Indefinido. Está en etapa de investigación temprana."
    },
    "action": "Enviar el PDF de precios y material self-service. Preguntar quién es su jefe y qué problema quieren resolver, y ofrecer una llamada con el decisor. Pasar a nurturing automatizado, sin tiempo de ventas por ahora.",
    "reason": "No tiene autoridad, y la necesidad y el timeline no están definidos. Aun así, hay un decisor detrás con interés, así que conviene usar a Carlos como puente y recalificar si el jefe se involucra."
  }
]
```