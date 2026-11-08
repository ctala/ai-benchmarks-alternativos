# Qwen 3.8 27B — sales_outreach/lead_qualification

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 3.96 | quality: 3.33
- latency_total: 14.148s | tokens_per_second: 45.3
- input_tokens: 262 | output_tokens: 641

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

{
  "lead_1": {
    "score": 4,
    "bant": {
      "budget": "Desconocido. No menciona presupuesto, pero al ser una startup de 5 personas, el gasto discrecional es limitado.",
      "authority": "Alto. Es el CEO, por lo que es el tomador de decisiones final.",
      "need": "Moderado. Menciona 'ver opciones', lo que indica interés inicial pero no una urgencia crítica o dolor agudo.",
      "timeline": "Bajo/Moderado. No hay una fecha límite definida, es una evaluación exploratoria."
    },
    "action": "Nurturing",
    "reason": "Aunque es el decisor (Authority), la falta de presupuesto definido y la etapa temprana de la compra (exploración) sugieren que no está listo para una venta inmediata. Requiere educación sobre el producto y construcción de confianza."
  },
  "lead_2": {
    "score": 9,
    "bant": {
      "budget": "Alto. La empresa acaba de levantar una Serie B, lo que implica capital fresco disponible para inversión en tecnología y operaciones.",
      "authority": "Alto. El VP de Operaciones tiene autoridad directa sobre la implementación de herramientas operativas.",
      "need": "Alto. Ha solicitado una demo, lo que indica una necesidad validada y un entendimiento claro de la solución.",
      "timeline": "Alto/Urgente. Tiene un plazo duro ('antes de Q3'), lo que acelera el ciclo de ventas."
    },
    "action": "Sales Call / Demo Scheduling",
    "reason": "Lead calificado de alta calidad. Tiene presupuesto (Serie B), autoridad (VP), necesidad clara (demo solicitada) y urgencia (Q3). Debe ser contactado inmediatamente por ventas."
  },
  "lead_3": {
    "score": 2,
    "bant": {
      "budget": "Bajo/Ninguno. Como intern, no gestiona presupuesto. La solicitud de 'PDF con precios' suele ser una señal de baja intención de compra real.",
      "authority": "Bajo. Es un intern que cumple con una tarea asignada; no es el decisor.",
      "need": "Bajo/Indirecto. La necesidad es de 'investigar', no de resolver un problema operativo propio. Es un requisito administrativo, no un dolor de negocio.",
      "timeline": "Indefinido. Depende de la tarea del jefe, no de una necesidad operativa crítica."
    },
    "action": "Self-Service / Automated Response",
    "reason": "Lead descalificado para venta directa. No tiene autoridad ni presupuesto. La mejor acción es enviar el PDF solicitado automáticamente y añadirlo a una secuencia de nurturing de largo plazo, o descartar si la estrategia es solo leads de alta intención."
  }
}