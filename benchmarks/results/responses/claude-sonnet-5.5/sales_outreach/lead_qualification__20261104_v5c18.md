# Claude Sonnet 5.5 — sales_outreach/lead_qualification

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 10.368s | tokens_per_second: 117.7
- input_tokens: 412 | output_tokens: 1220

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
      "budget": "Desconocido. Startup de 5 personas, probablemente con recursos limitados, pero no se menciono presupuesto.",
      "authority": "Alta. Es CEO y decide directamente.",
      "need": "Medio-alto. Busca automatizar soporte, lo cual coincide con lo que resolvemos, aunque el interes es generico.",
      "timeline": "Bajo/indefinido. 'Estamos viendo opciones' indica fase temprana de exploracion."
    },
    "action": "Nurturing activo: enviar caso de uso para startups pequenas y hacer una pregunta de calificacion (volumen de tickets, presupuesto aproximado, urgencia). Si responde con urgencia, escalar a ventas.",
    "reason": "Tiene autoridad y un need alineado, pero faltan presupuesto y urgencia. El tamano del equipo sugiere un ticket pequeno. Vale la pena una secuencia ligera sin consumir tiempo de un AE todavia."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Alto. Recien levanto Serie B, lo que indica capital disponible para inversion operativa.",
      "authority": "Alta. VP of Operations suele ser decisora o influenciadora clave en este tipo de compra (confirmar si hay comite o aprobacion de CFO/CEO).",
      "need": "Alto. Pidio una demo y dijo que necesitan resolver 'esto', lo que muestra un problema activo.",
      "timeline": "Alto. Quiere resolverlo antes de Q3, con fecha limite concreta."
    },
    "action": "Escalar de inmediato a ventas (AE senior). Agendar la demo en menos de 24-48 horas, personalizarla a operaciones y preguntar por el proceso de decision y otros stakeholders.",
    "reason": "Cumple los cuatro criterios BANT: presupuesto probable, autoridad, necesidad explicita y plazo definido. Es un lead caliente con ventana de tiempo, por lo que la velocidad de respuesta es critica."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Ninguno visible. Un intern no controla presupuesto; solo busca precios para su jefe.",
      "authority": "Muy baja. Es investigador, no decisor ni influenciador formal.",
      "need": "Incierto. Es una tarea de investigacion generica ('herramientas de IA'), sin problema especifico.",
      "timeline": "Indefinido. No hay urgencia ni fecha mencionada."
    },
    "action": "Envio automatizado del PDF de precios y comparativa, sin tiempo de ventas. Agregar a nurturing de bajo esfuerzo y pedir (opcionalmente) el contacto de su jefe o un reenvio del material.",
    "reason": "Bajo score por falta de autoridad y presupuesto, y una necesidad poco definida. Sin embargo, puede ser un camino hacia el decisor real, asi que conviene entregar el material y dejar la puerta abierta sin invertir recursos de ventas."
  }
]
```

**Prioridad de seguimiento:** Ana (inmediato) → Juan (secuencia de nurturing con pregunta de calificacion) → Carlos (automatizado).