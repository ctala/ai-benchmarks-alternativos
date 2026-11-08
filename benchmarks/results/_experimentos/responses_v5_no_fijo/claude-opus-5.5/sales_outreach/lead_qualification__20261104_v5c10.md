# Claude Opus 5.5 — sales_outreach/lead_qualification

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.21 | quality: 10.0
- latency_total: 15.139s | tokens_per_second: 94.1
- input_tokens: 412 | output_tokens: 1425

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
      "budget": "Desconocido. No lo menciono y una startup de 5 personas probablemente tiene presupuesto limitado.",
      "authority": "Alta. Como CEO es el decision maker final.",
      "need": "Media. Busca automatizar soporte, que encaja con nuestra solucion, pero esta en fase exploratoria ('viendo opciones').",
      "timeline": "Indefinido. No hay fecha ni urgencia."
    },
    "action": "Agendar una llamada de discovery corta y agregarlo a una secuencia de nurturing.",
    "reason": "Tiene autoridad y una necesidad real, pero llego por el blog (top of funnel) sin presupuesto ni urgencia claros. La llamada debe validar el volumen de soporte, el presupuesto y si hay un evento que dispare la compra. Conviene ofrecerle el plan para startups o pymes."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Probable. La empresa acaba de levantar Serie B, aunque falta confirmar el monto asignado.",
      "authority": "Alta. Como VP of Operations es decision maker o influenciadora clave; hay que confirmar si existen otros firmantes, como Finanzas o el CTO.",
      "need": "Alta. Necesidad explicita ('necesitamos resolver esto') y pidio una demo por iniciativa propia.",
      "timeline": "Definido y cercano: antes de Q3."
    },
    "action": "Asignarla de inmediato a un Account Executive y agendar la demo en las proximas 24-48 horas.",
    "reason": "Cumple los cuatro criterios BANT, con alta intencion: viene de un webinar y pidio la demo ella misma. Solo falta confirmar el presupuesto exacto y el proceso de compra (stakeholders, legal, procurement) para cerrar antes de Q3. Lead prioritario."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 3,
    "bant": {
      "budget": "Desconocido. No tiene visibilidad ni control del presupuesto.",
      "authority": "Baja. Es intern; el decision maker es su jefe, a quien no conocemos.",
      "need": "Vaga. 'Investigar herramientas de IA' es generico y no confirma que tengan el problema que resolvemos.",
      "timeline": "Desconocido."
    },
    "action": "Enviarle el PDF de precios junto con un caso de exito, y pedirle el nombre y rol de su jefe o proponerle una llamada que incluya al jefe. Agregarlo a nurturing.",
    "reason": "Sin autoridad ni necesidad definida, todavia no es un lead calificado para ventas. Aun asi, hay alguien con poder de decision que inicio la busqueda. El objetivo es usar a Carlos como puente hacia su jefe y descubrir el problema especifico que quieren resolver."
  }
]
```

**Prioridad sugerida:** Ana (9) → Juan (5) → Carlos (3)