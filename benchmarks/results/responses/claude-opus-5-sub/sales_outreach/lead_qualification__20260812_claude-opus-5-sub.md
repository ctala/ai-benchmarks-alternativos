# Claude Opus 5 (suscripción) — sales_outreach/lead_qualification

- model_id: `claude-opus-5`
- success: True  | final: 8.01 | quality: 10.0
- latency_total: 38.018s | tokens_per_second: 41.7
- input_tokens: 2 | output_tokens: 1584

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
    "score": 6,
    "bant": {
      "budget": "Desconocido. No menciona presupuesto y una startup de 5 personas suele tener capacidad limitada; asumir ticket bajo hasta validar.",
      "authority": "Alta. Es CEO: en una empresa de 5 personas decide y firma él mismo.",
      "need": "Declarada pero genérica. 'Automatizar soporte' es el problema que resolvemos, aunque no hay dolor cuantificado (volumen de tickets, costo actual, tiempo perdido).",
      "timeline": "Indefinido. 'Estamos viendo opciones' = fase de exploración, sin fecha ni evento forzante."
    },
    "action": "Nurture activo + llamada de descubrimiento de 15 min",
    "reason": "Authority perfecta compensa un Budget y Timeline débiles. El riesgo real no es que no pueda comprar, es que no tenga urgencia. La llamada debe cuantificar el dolor (¿cuántos tickets al mes? ¿cuánto tiempo del equipo se va en soporte?) para convertir 'estamos viendo' en un caso de negocio. Llegó vía blog, así que ya consume contenido: mantenerlo en la secuencia educativa y no forzar propuesta todavía."
  },
  {
    "lead": "Ana Gomez — VP of Operations, 200 empleados",
    "score": 9,
    "bant": {
      "budget": "Muy probable. Serie B recién levantada = presupuesto asignado para eficiencia operativa. Confirmar monto y quién aprueba el gasto.",
      "authority": "Alta, con matiz. VP of Ops decide o co-decide en su área; en una empresa de 200 personas es probable que necesite firma de finanzas o del CEO sobre cierto monto.",
      "need": "Fuerte y validada. Asistió al webinar, pidió demo por iniciativa propia y habla de 'resolver esto', no de explorar. Dolor reconocido internamente.",
      "timeline": "Explícito y corto. 'Antes de Q3' es una fecha real con presión interna; probablemente atada a un objetivo del equipo."
    },
    "action": "Agendar demo esta semana + fast-track al pipeline comercial",
    "reason": "Es el único lead con los 4 criterios cubiertos y el único con un deadline autoimpuesto. La demo debe ser específica a su caso, no genérica: mostrar el flujo de operaciones que ella describió y salir con próximo paso agendado, no con 'te mando info'. Dos cosas a cerrar en la llamada: (1) qué pasa el 1 de julio si esto no está resuelto, y (2) quién más firma. Es el lead que justifica el trimestre."
  },
  {
    "lead": "Carlos Ruiz — intern de marketing",
    "score": 2,
    "bant": {
      "budget": "Nulo. Un intern no tiene presupuesto ni visibilidad sobre él.",
      "authority": "Nula. Es un investigador delegado, no un decisor. Ni siquiera es el usuario del producto.",
      "need": "Sin verificar. El encargo es 'investigar herramientas de IA', un mandato abierto sin problema concreto detrás. No sabemos si existe dolor real.",
      "timeline": "Inexistente. Una tarea de investigación no tiene fecha de compra asociada."
    },
    "action": "Enviar el PDF de precios + pedir el contacto del jefe",
    "reason": "No descalificar, pero tampoco invertir tiempo de vendedor. El valor de este lead no es Carlos: es el jefe que le encargó la tarea. Enviar el material que pide (es barato y lo posiciona bien internamente) y responder con una pregunta concreta: '¿quién está liderando esta evaluación? Puedo agendar 20 min con esa persona para ahorrarles la comparación'. Si el jefe aparece, el lead renace con otro score. Si no aparece, era curiosidad y el PDF ya cumplió. Cero seguimiento manual: todo por secuencia automatizada."
  }
]
```

**Orden de atención:** Ana (hoy) → Juan (esta semana, llamada corta) → Carlos (respuesta automatizada, sin tiempo de vendedor).