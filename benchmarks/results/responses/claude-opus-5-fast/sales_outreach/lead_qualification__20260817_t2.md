# Claude Opus 5 Fast — sales_outreach/lead_qualification

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.1 | quality: 10.0
- latency_total: 11.681s | tokens_per_second: 185.1
- input_tokens: 410 | output_tokens: 2162

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
    "lead": "Juan Perez - CEO, startup 5 personas",
    "score": 6,
    "bant": {
      "budget": "Desconocido. Startup de 5 personas: ticket potencial bajo y probable sensibilidad al precio. No mencionó presupuesto ni ronda de inversión.",
      "authority": "Alta. Es CEO de una empresa pequeña, decide solo y sin comité de compras.",
      "need": "Real pero temprana. 'Automatizar soporte' encaja con lo que resolvemos, pero 'estamos viendo opciones' indica fase de exploración, no de compra.",
      "timeline": "Indefinido. No hay evento forzante ni fecha objetivo."
    },
    "action": "Discovery call corta (15-20 min) agendada por SDR esta semana. Si no califica en budget, mover a self-serve/plan starter.",
    "reason": "La autoridad total compensa la falta de presupuesto y timeline: con el CEO en la llamada se califica o descalifica en una sola conversación, sin costo de ciclo largo. El riesgo real es tamaño de cuenta, no acceso al decisor. No merece tiempo de AE senior hasta confirmar budget."
  },
  {
    "lead": "Ana Gomez - VP of Operations, 200 empleados",
    "score": 9,
    "bant": {
      "budget": "Fuerte señal indirecta. Serie B reciente = capital disponible y presión por escalar operaciones. Falta confirmar si hay línea presupuestal asignada este año o si sale de un budget nuevo.",
      "authority": "Alta como decisora funcional. VP of Ops típicamente aprueba o veta herramientas de su área; probable co-firma de Finance/CFO según el monto. Confirmar proceso de aprobación en la demo.",
      "need": "Explícita y priorizada. Pidió demo activamente después de contenido educativo, no llegó por curiosidad.",
      "timeline": "Concreto: antes de Q3. Hay un evento forzante con fecha, lo que acelera todo el ciclo."
    },
    "action": "Asignar a AE senior AHORA. Contactar en menos de 2 horas hábiles y agendar demo personalizada en 48h máximo. Preparar caso de uso de scaling post-Serie B.",
    "reason": "Es el único lead que cumple los cuatro criterios BANT con evidencia, no con supuestos. La combinación de timeline con fecha + funding reciente + solicitud proactiva de demo es el perfil de mayor tasa de cierre. El principal riesgo aquí es la velocidad de respuesta: leads así están evaluando 2-3 vendedores en paralelo. No pierde el punto 10 por calidad sino porque falta validar el proceso de aprobación de compra y el monto autorizado."
  },
  {
    "lead": "Carlos Ruiz - Intern de marketing",
    "score": 3,
    "bant": {
      "budget": "Nulo a nivel del contacto. Un intern no tiene ni visibilidad ni control sobre presupuesto.",
      "authority": "Ninguna. Es un recolector de información, no un influenciador. Su jefe es el verdadero contacto.",
      "need": "Indeterminada. 'Investigar herramientas de IA' es un mandato genérico; no sabemos si hay un dolor concreto de soporte detrás ni el tamaño de la empresa.",
      "timeline": "Desconocido. Una tarea de investigación no implica intención de compra en el corto plazo."
    },
    "action": "Enviar el PDF de precios sin fricción + secuencia de nurture automatizada. En el mismo email, pedir explícitamente una llamada de 15 min con él y su jefe para 'ahorrarle trabajo en la comparativa'. Cero tiempo de AE.",
    "reason": "No descartar: los mandatos de investigación suelen preceder a una compra real y el intern es una puerta de entrada barata a la cuenta. Pero tampoco invertir recursos humanos, porque el contacto no puede avanzar la venta. La jugada correcta es ser el proveedor más fácil de incluir en su comparativa (dar el PDF de inmediato, sin gatekeeping) mientras se intenta escalar al jefe. Si consigue la reunión con el manager, el lead se re-califica desde cero."
  }
]
```

**Resumen de priorización:** Ana (9) → Juan (6) → Carlos (3).

Dos observaciones sobre el proceso, más allá de los scores:

1. **El error caro sería tratar a Carlos como spam.** Un intern con la tarea de "investigar herramientas de IA" a menudo es la primera señal visible de un proceso de compra que ya arrancó internamente. Poner un formulario o un gatekeeper delante del PDF es la forma más rápida de quedar fuera de la comparativa que llegará al decisor.

2. **El riesgo con Ana no es la calificación, es la latencia.** Su score alto solo se convierte en revenue si el contacto ocurre hoy. Si el SLA de respuesta es de días, el lead se degrada a 6 por sí solo.