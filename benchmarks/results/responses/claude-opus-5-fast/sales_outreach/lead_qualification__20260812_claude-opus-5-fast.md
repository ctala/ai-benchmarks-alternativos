# Claude Opus 5 Fast — sales_outreach/lead_qualification

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.14 | quality: 10.0
- latency_total: 11.377s | tokens_per_second: 156.4
- input_tokens: 410 | output_tokens: 1779

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
    "lead": "Juan Perez — CEO, startup 5 personas",
    "score": 5,
    "bant": {
      "budget": "Desconocido. Startup de 5 personas: ticket probablemente bajo. Sin señal de presupuesto asignado.",
      "authority": "Alta. Como CEO de una empresa de 5 personas, es el decisor único.",
      "need": "Media-real pero difusa. 'Automatizar soporte' es un dolor genuino, aunque con 5 personas el volumen de tickets puede no justificar la compra todavía.",
      "timeline": "Indefinido. 'Estamos viendo opciones' = fase de exploración, sin evento forzante."
    },
    "action": "Nurture activo + llamada de descubrimiento de 15 min (self-serve si existe tier bajo)",
    "reason": "Autoridad perfecta pero sin presupuesto ni urgencia confirmados. No consume tiempo de AE todavía: una llamada corta debe validar volumen de tickets, costo actual del soporte y si hay evento que fuerce decisión. Si el volumen es bajo, dirigir a plan self-serve. Es el clásico lead de blog: intención informativa, no de compra."
  },
  {
    "lead": "Ana Gomez — VP of Operations, 200 empleados",
    "score": 9,
    "bant": {
      "budget": "Fuerte. Serie B reciente = capital fresco y presión por escalar operaciones. Empresa de 200 personas soporta ticket medio-alto.",
      "authority": "Alta como campeón, no necesariamente firmante. VP of Ops es dueño del problema y del presupuesto departamental; compra de este tamaño puede requerir CFO o CEO.",
      "need": "Explícita y validada. Pidió demo proactivamente después del webinar: ya se auto-identificó con el problema.",
      "timeline": "Definido. 'Antes de Q3' es un evento forzante con fecha, el señalizador BANT más valioso."
    },
    "action": "Asignar a AE senior, agendar demo en menos de 24h",
    "reason": "Los cuatro criterios alineados con timeline explícito. La velocidad de respuesta es el factor determinante aquí: si pidió demo post-webinar probablemente está evaluando 2-3 vendors en paralelo. Objetivo de la demo: mapear el proceso de aprobación (quién firma además de ella), cuantificar el costo del status quo y anclar el deadline de Q3 a un plan de implementación con fechas hacia atrás."
  },
  {
    "lead": "Carlos Ruiz — intern de marketing",
    "score": 3,
    "bant": {
      "budget": "Nulo. Un intern no tiene presupuesto ni visibilidad sobre él.",
      "authority": "Nula directa, pero es un proxy. El valor real no es Carlos: es el jefe que emitió el encargo.",
      "need": "Indeterminada. 'Herramientas de IA' es demasiado genérico; no sabemos qué problema intenta resolver el jefe.",
      "timeline": "Desconocido. Un encargo de investigación puede ser urgente o un side project sin fecha."
    },
    "action": "Enviar el PDF sin fricción + pedir referral al decisor",
    "reason": "No descartar, pero no invertir tiempo de ventas. Los encargos de research a interns muchas veces vienen de un directivo con un problema real detrás. Enviar el material solicitado de inmediato (ser útil genera reciprocidad) y acompañarlo de una pregunta simple: qué problema específico busca resolver su jefe y si querría una sesión de 20 min con él. Si el jefe aparece, se recalifica desde cero como lead nuevo. Si no responde, secuencia automatizada y cero seguimiento manual."
  }
]
```

**Priorización:** Ana (contactar hoy) → Juan (esta semana, llamada corta) → Carlos (automatizado).

Dos notas sobre el marco: el score de Ana asume que la Serie B es reciente y verificable — vale confirmarlo en la demo, porque el presupuesto post-ronda suele estar comprometido a headcount antes que a herramientas. Y el 3 de Carlos es un score de *prioridad*, no de valor potencial: el lead real es su jefe, que podría perfectamente puntuar 8.