# GLM 5.3 — sales_outreach/lead_qualification

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.43 | quality: 10.0
- latency_total: 23.09s | tokens_per_second: 92.9
- input_tokens: 255 | output_tokens: 2144

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
    "lead": "Lead 1 - Juan Perez (CEO, startup 5 personas)",
    "score": 4,
    "bant": {
      "budget": "Desconocido - no lo mencionó; startup pequeña puede tener presupuesto limitado",
      "authority": "Alta - es CEO y decisor final, aunque el tamaño de empresa limita el valor del deal",
      "need": "Medio - tiene el problema (soporte manual) y está explorando, pero en etapa temprana",
      "timeline": "Desconocido - sin fecha objetivo; origen orgánico (blog) sugiere investigación pasiva"
    },
    "action": "Nurture + calificación por SDR: llamada breve para explorar presupuesto y urgencia; agregar a secuencia de emails educativos",
    "reason": "Decisor correcto pero sin presupuesto confirmado, timeline incierto y necesidad en fase exploratoria. Vale la pena calificar antes de consumir tiempo de un AE."
  },
  {
    "lead": "Lead 2 - Ana Gomez (VP Operations, 200 empleados)",
    "score": 9,
    "bant": {
      "budget": "Señal fuerte - empresa de 200 empleados que acaba de levantar Serie B; nivel VP puede aprobar compra",
      "authority": "Alta - VP of Operations, típicamente decisor o influyente clave en herramientas operativas",
      "need": "Alto - pidió demo de forma activa y expresa necesidad explícita de resolver el problema",
      "timeline": "Definido y urgente - 'antes de Q3'"
    },
    "action": "Prioridad máxima: contactar en menos de 24 horas, agendar demo con AE senior, preparar propuesta mid-market",
    "reason": "Cumple los 4 criterios BANT: presupuesto probable (Serie B reciente), autoridad (VP), necesidad explícita y deadline claro. Lead caliente listo para ciclo de ventas."
  },
  {
    "lead": "Lead 3 - Carlos Ruiz (intern de marketing)",
    "score": 2,
    "bant": {
      "budget": "Nulo - es intern, sin acceso a presupuesto ni poder de compra",
      "authority": "Muy baja - el decisor real es su jefe, que aún no conocemos",
      "need": "Posible a nivel empresa (jefe pidió investigar herramientas de IA), pero no validado",
      "timeline": "Desconocido - tarea de investigación sin fecha definida"
    },
    "action": "Enviar PDF de precios por self-service, agregar a nurture, e intentar identificar y contactar al jefe (decisor real)",
    "reason": "El contacto no tiene autoridad ni presupuesto. Existe una señal de interés organizacional, pero hay que escalar hasta el decisor antes de invertir esfuerzo de ventas."
  }
]
```