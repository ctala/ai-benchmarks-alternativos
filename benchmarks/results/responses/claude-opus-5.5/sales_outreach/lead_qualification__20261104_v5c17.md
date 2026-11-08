# Claude Opus 5.5 — sales_outreach/lead_qualification

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.35 | quality: 10.0
- latency_total: 14.741s | tokens_per_second: 104.1
- input_tokens: 412 | output_tokens: 1534

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
      "authority": "Alta. Es CEO y decide en una empresa tan pequeña.",
      "need": "Media. Quiere automatizar el soporte, que encaja con lo que ofrecemos, pero aun esta explorando opciones.",
      "timeline": "No definido. 'Estamos viendo opciones' sugiere una evaluacion temprana sin urgencia."
    },
    "action": "Hacer una llamada corta de discovery (15 min) para confirmar presupuesto y plazo. Si no hay urgencia, pasarlo a nurturing con casos de exito de startups y el plan de entrada.",
    "reason": "Es decision maker con una necesidad alineada, pero llego por el blog (top of funnel), sin presupuesto ni plazo claros, y por el tamaño de la empresa el ticket seria pequeño."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Muy probable. La empresa acaba de levantar una Serie B y tiene 200 empleados.",
      "authority": "Alta. Como VP of Operations probablemente es la compradora economica o una influenciadora clave. Hay que confirmar si participan otros (CFO, IT).",
      "need": "Alta y explicita. Dijo 'necesitamos resolver esto' y pidio una demo por iniciativa propia.",
      "timeline": "Definido y cercano: antes de Q3."
    },
    "action": "Prioridad maxima. Asignar a un Account Executive y agendar la demo en las proximas 24-48 horas. Preparar una demo personalizada para operaciones y mapear el proceso de compra y a los demas stakeholders.",
    "reason": "Cumple los cuatro criterios BANT: fondos frescos, decision maker senior, necesidad explicita, plazo concreto y alta intencion (pidio la demo despues del webinar)."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 3,
    "bant": {
      "budget": "Desconocido. No tiene visibilidad ni control sobre el presupuesto.",
      "authority": "Baja. Es intern y solo recopila informacion para su jefe.",
      "need": "Vaga. 'Investigar herramientas de IA' es amplio y no confirma el problema concreto que resolvemos.",
      "timeline": "Desconocido."
    },
    "action": "Enviar el PDF con precios y materiales comparativos. Pedirle con amabilidad el nombre y rol de su jefe, y ofrecer una llamada breve con el. Pasarlo a nurturing automatizado.",
    "reason": "No tiene autoridad ni presupuesto y la necesidad es difusa. No conviene descartarlo, porque puede ser la puerta de entrada al verdadero decision maker, pero no merece tiempo de ventas por ahora."
  }
]
```

**Orden de prioridad:** Ana Gomez (9) → Juan Perez (5) → Carlos Ruiz (3)