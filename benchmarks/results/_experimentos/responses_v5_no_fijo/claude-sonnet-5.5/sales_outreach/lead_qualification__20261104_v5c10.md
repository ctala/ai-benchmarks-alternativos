# Claude Sonnet 5.5 — sales_outreach/lead_qualification

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.5 | quality: 10.0
- latency_total: 10.289s | tokens_per_second: 131.8
- input_tokens: 412 | output_tokens: 1356

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
      "budget": "Desconocido. No lo menciono. Una startup de 5 personas probablemente tiene presupuesto limitado, aunque el interes en automatizar soporte sugiere que el volumen de tickets ya le pesa.",
      "authority": "Alta. Es CEO y en una empresa de 5 personas decide solo.",
      "need": "Media-alta. Menciona explicitamente automatizar soporte, pero con lenguaje exploratorio ('viendo opciones').",
      "timeline": "Indefinido. No hay urgencia ni fecha. Fase temprana de investigacion."
    },
    "action": "Nurturing con seguimiento ligero. Enviar caso de exito de una startup similar y una guia de precios o plan de entrada. Hacer una pregunta de descubrimiento sobre volumen de tickets y presupuesto estimado. Ofrecer una llamada corta, sin presionar.",
    "reason": "Es decision maker y reconoce la necesidad, pero faltan presupuesto y urgencia, y el tamano de la empresa limita el valor potencial del deal. Vale la pena cultivarlo sin invertir tiempo de ventas intensivo todavia."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Alto. La empresa acaba de levantar Serie B, lo que indica capital disponible y presion por invertir en eficiencia operativa y escalar.",
      "authority": "Alta. VP of Operations suele ser decision maker o influenciador clave en compras operativas. Falta confirmar el proceso de aprobacion y si hay otros stakeholders (finanzas, IT).",
      "need": "Alta. Pidio una demo despues del webinar y habla de 'resolver esto' como un problema concreto.",
      "timeline": "Alta. Tiene un plazo definido: antes de Q3."
    },
    "action": "Priorizar. Pasar a un AE/ventas de inmediato y agendar la demo en 24-48 horas. Antes de la demo, investigar su stack y contexto. Durante el descubrimiento, mapear stakeholders, criterios de decision y proceso de compra para trabajar hacia atras desde la fecha de Q3.",
    "reason": "Cumple los cuatro criterios de BANT: capital reciente, cargo con autoridad, necesidad explicita y deadline claro. Es el lead con mayor probabilidad de cierre y de mayor valor."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Ninguno. Es un intern sin presupuesto propio. Su jefe podria tenerlo, pero no hay senal de que este asignado.",
      "authority": "Muy baja. Es investigador, no decide ni influye directamente en la compra.",
      "need": "Vaga. 'Investigar herramientas de IA' es una tarea generica, sin problema especifico identificado.",
      "timeline": "Sin urgencia. Es una tarea de investigacion, no un proyecto con fecha."
    },
    "action": "Nurturing automatizado. Enviar el PDF de precios o material generico y agregarlo a una secuencia de email educativa. Intentar identificar a su jefe preguntando amablemente quien lidera la evaluacion, y no invertir tiempo de ventas hasta que haya un contacto con autoridad.",
    "reason": "No cumple ningun criterio BANT de forma solida. Aun asi, puede ser una via de entrada a un decision maker (su jefe), por lo que conviene mantener el contacto con bajo esfuerzo."
  }
]
```

**Prioridad de seguimiento:** Ana (inmediato) > Juan (nurturing activo) > Carlos (automatizado).