# Claude Opus 5 — sales_outreach/lead_qualification

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.1 | quality: 10.0
- latency_total: 29.983s | tokens_per_second: 66.5
- input_tokens: 410 | output_tokens: 1995

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
      "budget": "Desconocido. No mencionó presupuesto. Startup de 5 personas sugiere capacidad limitada, aunque el ticket de un plan pequeño podría encajar. Riesgo de que busque el tier gratuito.",
      "authority": "Alta. Como CEO de una empresa de 5 personas es el decision maker único y puede firmar sin comité.",
      "need": "Media-confirmada. 'Automatizar soporte' es exactamente nuestro caso de uso, pero el lenguaje ('estamos viendo opciones') indica exploración, no dolor agudo.",
      "timeline": "Débil. Sin fecha ni evento forzador. Fase de research."
    },
    "action": "Secuencia de nurture comercial ligera: email personalizado del AE ofreciendo una llamada de 15 min de discovery, no una demo completa. Objetivo de la llamada: cuantificar el dolor (tickets/mes, horas dedicadas) y detectar presupuesto.",
    "reason": "Authority perfecta compensa un timeline y budget flojos. El coste de un discovery de 15 min es bajo y el upside es un ciclo de venta cortísimo si el dolor es real. No merece prioridad de demo hasta validar presupuesto."
  },
  {
    "lead": "Ana Gomez — VP of Operations, 200 empleados",
    "score": 9,
    "bant": {
      "budget": "Fuerte (inferido). Serie B reciente implica capital disponible y presión por escalar operaciones. Una empresa de 200 empleados tiene línea presupuestaria para herramientas de ops. Falta confirmar el monto y si el budget es suyo o de otro centro de coste.",
      "authority": "Alta. VP of Operations es el buyer natural para automatización de soporte. Probablemente necesite validación de Finance/IT para el contrato, pero es quien impulsa la decisión.",
      "need": "Fuerte y explícita. 'Necesitamos resolver esto' — lenguaje de problema, no de curiosidad. Pidió demo activamente tras consumir contenido educativo.",
      "timeline": "Fuerte. Deadline concreto: antes de Q3. Evento forzador claro (probablemente escalado post-Serie B)."
    },
    "action": "Ruta directa a ventas con prioridad máxima. Agendar demo en menos de 24h con el AE senior. Preparar la demo con caso de uso de escalado post-funding y traer un cliente de referencia de tamaño similar. Confirmar en la llamada: monto de presupuesto, proceso de compra y quién más firma.",
    "reason": "BANT completo en los cuatro ejes con señales explícitas, no inferidas, en Need y Timeline. Es el perfil ideal (ICP) y el deadline de Q3 crea urgencia natural que acelera el cierre. Cualquier fricción o retraso en la respuesta es el mayor riesgo aquí."
  },
  {
    "lead": "Carlos Ruiz — intern de marketing",
    "score": 3,
    "bant": {
      "budget": "Nulo. Un intern no tiene ni presupuesto ni visibilidad sobre él.",
      "authority": "Nula. Es un investigador delegado, no un influenciador. No participará en la decisión.",
      "need": "Indeterminado. 'Herramientas de IA' es un mandato genérico, no nuestro problema específico. No hay evidencia de que necesiten automatizar soporte.",
      "timeline": "Desconocido. La urgencia del jefe es invisible desde aquí."
    },
    "action": "No asignar a ventas. Responder con la página pública de precios y un one-pager, sin exigir formulario. En el mismo email, pedir explícitamente una introducción: '¿Te ayudaría que preparásemos un resumen para tu jefe? ¿Cómo se llama y cuál es su rol?'. Meter en nurture de marketing y crear alerta: si aparece otro contacto del mismo dominio, elevar prioridad.",
    "reason": "El lead en sí no es cualificable, pero es un proxy de un decision maker invisible que ya inició un proceso de evaluación. El valor está en convertirlo en canal hacia su jefe, no en trabajarlo como oportunidad. Tratarlo mal o ignorarlo quema el acceso a esa cuenta; gastar tiempo de AE en él lo desperdicia. Coste bajo, opción de upside."
  }
]
```

**Nota sobre los inferidos:** los scores de Budget en los leads 1 y 2 son inferencias a partir de tamaño y funding, no datos confirmados. En el lead 2 esa inferencia es sólida pero sigue siendo el único eje sin evidencia directa — es lo primero que debe confirmarse en la demo. Si el presupuesto no existe o pertenece a otro departamento, el score real baja de 9 a ~6.