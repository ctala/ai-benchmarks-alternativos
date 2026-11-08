# Claude Opus 5 — sales_outreach/lead_qualification

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.11 | quality: 10.0
- latency_total: 29.58s | tokens_per_second: 63.7
- input_tokens: 410 | output_tokens: 1883

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
    "lead": 1,
    "nombre": "Juan Perez",
    "score": 6,
    "bant": {
      "budget": "Desconocido — no mencionó presupuesto. Startup de 5 personas sugiere capacidad limitada, probablemente tier self-serve o starter.",
      "authority": "Fuerte — CEO de startup de 5 personas es el decision maker único, sin comité de compra ni procurement.",
      "need": "Confirmado pero genérico — 'automatizar soporte' es el problema que resolvemos, aunque no hay señal de dolor cuantificado (volumen de tickets, costo actual, SLA roto).",
      "timeline": "Débil — 'estamos viendo opciones' indica fase de exploración temprana, sin evento forzante ni fecha."
    },
    "action": "Nurture con toque humano ligero: secuencia de 3 emails con casos de uso de soporte para equipos pequeños + oferta de trial self-serve. Un solo intento de llamada de 15 min para descubrir volumen de tickets y trigger.",
    "reason": "Authority máxima compensa un timeline flojo y budget desconocido. El ciclo de venta en startups con CEO involucrado puede colapsar de meses a días si aparece un evento forzante. No merece recurso de AE senior todavía, pero sí vigilancia activa: si responde con volumen de tickets o menciona contratar soporte, sube a 8 inmediatamente. Riesgo principal: ACV bajo que no justifica venta asistida."
  },
  {
    "lead": 2,
    "nombre": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Fuerte — Serie B reciente implica capital fresco asignado a eficiencia operativa y escalamiento. 200 empleados sitúa el deal en rango mid-market.",
      "authority": "Fuerte — VP of Operations es típicamente el economic buyer o el sponsor principal para herramientas de automatización de soporte. Probablemente necesite firma de CFO/CEO, pero controla la decisión.",
      "need": "Fuerte y validado — asistió a un webinar completo y pidió demo proactivamente. 'Necesitamos resolver esto' es lenguaje de dolor, no de curiosidad.",
      "timeline": "Fuerte y explícito — 'antes de Q3' es una fecha concreta con urgencia implícita, probablemente atada a objetivos post-funding."
    },
    "action": "Ruta directa a AE senior con SLA de contacto de 1 hora. Agendar demo personalizada en menos de 48h, no demo genérica. Pre-llamada de descubrimiento de 20 min para mapear stack actual, volumen de tickets y proceso de aprobación.",
    "reason": "Los cuatro criterios BANT están presentes y dos son explícitos en palabras del propio lead. El evento forzante (Q3) más el capital fresco crean la ventana de compra ideal. No bajo a 10 solo porque falta confirmar quién firma y si hay competidores ya en evaluación —ambos son riesgos reales en empresas de este tamaño. La mayor amenaza aquí no es perder el deal, es responder lento: un lead con esta urgencia está hablando con 2-3 vendors."
  },
  {
    "lead": 3,
    "nombre": "Carlos Ruiz",
    "score": 3,
    "bant": {
      "budget": "Ausente — intern sin ownership de presupuesto. El presupuesto, si existe, vive con el jefe no identificado.",
      "authority": "Ausente — rol de investigación delegada, cero poder de decisión o influencia documentada.",
      "need": "No calificado — 'herramientas de IA' es demasiado amplio. No hay evidencia de que el problema sea soporte ni de que exista dolor real versus curiosidad del jefe.",
      "timeline": "Desconocido — una tarea de investigación no implica intención de compra en ningún horizonte."
    },
    "action": "Enviar el PDF de precios solicitado con un email corto que agregue valor y pida un pivot: ofrecer una sesión de 20 min para el jefe, preguntando explícitamente por su nombre y rol. Encolar en nurture educativo de bajo costo. No asignar a ventas.",
    "reason": "Score bajo refleja que no hay deal aquí hoy, pero no es cero por dos razones: (1) este lead es una sonda de una cuenta posiblemente valiosa, y el jefe anónimo es el verdadero prospecto; (2) negar el PDF daña la marca y cierra la puerta al nivel superior. La estrategia correcta es tratarlo como un camino hacia el decision maker, no como el lead. Nota importante: enviar precios a un investigador sin contexto arriesga que la herramienta sea descartada por precio en una hoja de cálculo comparativa, sin que nadie vea el valor —de ahí la insistencia en conseguir la reunión con el jefe."
  }
]
```

**Observación transversal:** los scores 6 y 3 son los que más se moverían con una sola pregunta bien hecha. Para Juan, el volumen mensual de tickets define si es ACV viable. Para Carlos, el nombre del jefe convierte un lead muerto en una oportunidad enterprise. Vale la pena instrumentar esas dos preguntas en el formulario o en el primer email automático.