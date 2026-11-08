# Ling 3.0 Flash — sales_outreach/lead_qualification

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.17 | quality: 10.0
- latency_total: 11.213s | tokens_per_second: 82.1
- input_tokens: 304 | output_tokens: 921

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
    "lead": "Lead 1 - Juan Perez",
    "score": 4,
    "bant": {
      "budget": "Desconocido - No menciono presupuesto. Startup de 5 personas podría tener recursos limitados.",
      "authority": "Alto - Es CEO, decision maker final de la empresa.",
      "need": "Medio-Alto - Tiene un problema claro (soporte manual) y está evaluando opciones, pero el lenguaje es exploratorio ('estamos viendo opciones'), no urgente.",
      "timeline": "Bajo - No menciono fecha ni urgencia. Esta en fase temprana de exploración."
    },
    "action": "Nutrir (Lead nurturing) - Enviar contenido educativo, case studies de startups similares, y programar una llamada de descubrimiento para entender presupuesto y timeline.",
    "reason": "Tiene autoridad y una necesidad real, pero carece de urgencia y no hay señal de presupuesto. Es un lead a largo plazo. El hecho de que haya llegado por el blog indica fase de investigación. No descartarlo, pero no priorizarlo por encima de leads con urgencia y presupuesto confirmado."
  },
  {
    "lead": "Lead 2 - Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Alta probabilidad - Empresa que acaba de levantar Serie B, lo que implica capital disponible e inversión en crecimiento operativo.",
      "authority": "Alto - VP of Operations con poder de decisión sobre herramientas operativas. Probablemente influye directamente en compras de su área.",
      "need": "Alto - Pidio una demo activamente después de un webinar, confirmando que tiene un problema concreto que resolver.",
      "timeline": "Alto - 'Necesitamos resolver esto antes de Q3' es una fecha concreta y urgente. Deadline clara."
    },
    "action": "Priorizar - Contactar inmediatamente, agendar demo lo antes posible, y preparar propuesta comercial con ROI estimado. Involucrar al equipo de ventas.",
    "reason": "Lead calificado con los 4 criterios BANT favorablemente cubiertos: presupuesto probable (Serie B), autoridad (VP), necesidad confirmada (demo solicitada) y timeline urgente (antes de Q3). Es el lead con mayor potencial de cierre inmediato."
  },
  {
    "lead": "Lead 3 - Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido - Es un intern, no tiene acceso a presupuesto. La solicitud de un PDF de precios no implica capacidad de compra.",
      "authority": "Bajo - Intern de marketing. No es decision maker. Su jefe le pidió investigar, pero Carlos es solo un ejecutor de la tarea.",
      "need": "Bajo - No es el usuario final ni el tomador de decisiones. Su interés es académico/informativo, no de compra.",
      "timeline": "Bajo - No hay indicacion de urgencia. Pide un PDF, lo que sugiere fase de investigación sin presión."
    },
    "action": "Reasignar - Enviar el PDF solicitado, registrar datos del jefe (contacto real), y derivar el lead al equipo de marketing para nurturing. No invertir tiempo de ventas en este contacto.",
    "reason": "Carlos no tiene autoridad, presupuesto ni urgencia. Es un lead de inteligencia, no de venta. Sin embargo, vale la pena capturar la información del supervisor para abrir un canal de comunicación real. Score bajo pero no cero porque hay una puerta abierta a través de su jefe."
  }
]
```