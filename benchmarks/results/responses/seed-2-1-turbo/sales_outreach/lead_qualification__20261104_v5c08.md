# Seed 2.1 Turbo — sales_outreach/lead_qualification

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.74 | quality: 10.0
- latency_total: 11.565s | tokens_per_second: 63.9
- input_tokens: 293 | output_tokens: 739

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

[
  {
    "lead": "Juan Perez",
    "score": 4,
    "bant": {
      "budget": "Desconocido",
      "authority": "Alta (es CEO de la startup, es decision maker final)",
      "need": "Media (menciona que evalúa opciones de automatización de soporte, coincide con la solución pero no detalla urgencia o dolor específico)",
      "timeline": "Desconocido (solo indica que está viendo opciones, sin plazo definido)"
    },
    "action": "Nutrir lead con contenido educativo y calificar presupuesto/timeline en siguiente contacto",
    "reason": "Aunque es autoridad decisoria y tiene una necesidad alineada, no hay información de presupuesto ni de plazo de implementación, por lo que no se puede priorizar como lead calificado de inmediato. Se debe profundizar en el tamaño del problema de soporte y la disponibilidad de recursos para avanzar."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Alto (empresa de 200 empleados que acaba de levantar Serie B, cuenta con recursos para invertir en herramientas operativas)",
      "authority": "Alta (VP of Operations, cargo con poder de decisión para inversiones en herramientas de su área)",
      "need": "Alta (solicitó demo después de un webinar, confirmó que necesita resolver la necesidad alineada con la solución)",
      "timeline": "Alto (necesita resolverlo antes de Q3, plazo definido y cercano)"
    },
    "action": "Agendar demo inmediatamente y pasar a equipo de ventas para cierre",
    "reason": "Cumple con todos los criterios BANT de forma positiva: tiene presupuesto disponible por la ronda de inversión, es autoridad decisoria, tiene una necesidad confirmada y un plazo límite cercano para implementar la solución. Es un lead altamente calificado con alta probabilidad de cierre."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido (solicita PDF de precios, pero no tiene visibilidad directa del presupuesto aprobado)",
      "authority": "Baja (es intern de marketing, no tiene poder de decisión, solo cumple con una tarea de investigación asignada por su jefe)",
      "need": "Baja (la investigación es genérica de herramientas de IA, no hay un problema específico alineado ni confirmación de que la solución sea la que buscan)",
      "timeline": "Desconocido (no menciona plazo para la decisión o implementación)"
    },
    "action": "Enviar material informativo genérico y solicitar contacto con el jefe decisor para avanzar",
    "reason": "El lead no es tomador de decisiones, solo realiza una investigación genérica sin detalle de necesidad específica ni presupuesto o plazo. Se debe usar su investigación para acceder al cargo con autoridad y calificar los criterios BANT faltantes directamente con el decisor."
  }
]