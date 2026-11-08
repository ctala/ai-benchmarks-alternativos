# Step 3.5 Flash — sales_outreach/lead_qualification

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 4.42 | quality: 3.33
- latency_total: 22.54s | tokens_per_second: 106.1
- input_tokens: 274 | output_tokens: 2392

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
    "score": 6,
    "bant": {
      "budget": "No claro/desconocido",
      "authority": "Alto (CEO)",
      "need": "Sí (automatización de soporte)",
      "timeline": "No especificado"
    },
    "action": "Nurturing/Contactar para calificar más",
    "reason": "CEO con necesidad clara pero sin presupuesto ni timeline definido. Requiere más calificación para confirmar interés y capacidad de pago."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto (empresa con Serie B)",
      "authority": "Alto (VP of Operations)",
      "need": "Sí (resolver antes de Q3)",
      "timeline": "Antes de Q3"
    },
    "action": "Priorizar, enviar demo, avanzar a ventas",
    "reason": "VP con necesidad urgente, autoridad alta, presupuesto disponible por financiación reciente. Lead muy calificado y listo para avanzar."
  },
  {
    "score": 2,
    "bant": {
      "budget": "No claro",
      "authority": "Bajo (interno)",
      "need": "Posible (investigando por jefe)",
      "timeline": "No especificado"
    },
    "action": "Baja prioridad, enviar PDF pero identificar decision maker",
    "reason": "Contacto no decision maker, solo recopila información. Baja probabilidad de conversión sin involucrar al verdadero decisor."
  }
]