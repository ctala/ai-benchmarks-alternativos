# GLM-5.1 — sales_outreach/lead_qualification

- model_id: `z-ai/glm-5.1`
- success: True  | final: 8.56 | quality: 10.0
- latency_total: 13.79s | tokens_per_second: 49.8
- input_tokens: 249 | output_tokens: 687

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
      "budget": "Desconocido. No mencionó presupuesto, pero como CEO de una startup de 5 personas, podría haber limitaciones de capital.",
      "authority": "Sí. Es el CEO, por lo que es el tomador de decisiones.",
      "need": "Sí. Está buscando opciones para automatizar su soporte.",
      "timeline": "Bajo/Medio. Llegó vía blog y está en etapa de "viendo opciones", lo que indica exploración temprana."
    },
    "action": "Nurturing. Enviar contenido relevante sobre automatización de soporte y agendar una llamada de descubrimiento para identificar presupuesto y timeline.",
    "reason": "Tiene la autoridad y la necesidad, pero falta definir presupuesto y urgencia. Su origen (blog) indica etapa temprana del embudo."
  },
  {
    "lead": "Lead 2 - Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Sí. La empresa acaba de levantar una Serie B, lo que indica disponibilidad de capital para invertir en soluciones.",
      "authority": "Sí. VP of Operations es un rol de alto nivel con poder de decisión directa en procesos operativos.",
      "need": "Sí. Pidió una demo de forma proactiva después de un webinar.",
      "timeline": "Sí. Tiene una fecha límite clara: necesita resolverlo antes de Q3."
    },
    "action": "Contacto inmediato por ventas. Agendar la demo lo antes posible y preparar un caso de negocio enfocado en implementación rápida para cumplir con el cierre de Q3.",
    "reason": "Cumple con todos los criterios BANT. Tiene presupuesto (Serie B), autoridad (VP), necesidad explícita (pidió demo) y un timeline definido y cercano (Q3). Es un lead altamente cualificado."
  },
  {
    "lead": "Lead 3 - Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido. Pidió un PDF con precios, pero no tiene poder de decisión sobre el presupuesto.",
      "authority": "No. Es un intern de marketing. Su jefe es quien tomará la decisión, Carlos solo es un investigador.",
      "need": "Posible. Su jefe le pidió investigar herramientas de IA, pero no hay un problema o dolor específico mencionado.",
      "timeline": "Desconocido/Bajo. La tarea de "investigar" sugiere una etapa muy preliminar sin urgencia definida."
    },
    "action": "Marketing automation. Enviar el PDF de precios solicitado y incluirlo en campañas de email para mantenerlo en radar. Preguntar por el nombre de su jefe para intentar llegar al decision maker en el futuro.",
    "reason": "Falla en el criterio más importante: Autoridad. Al ser un intern, solo está recopilando información. No hay presupuesto confirmado ni urgencia."
  }
]
```