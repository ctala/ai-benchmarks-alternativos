# Seed 2.0 Code — sales_outreach/lead_qualification

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 4.17 | quality: 3.33
- latency_total: 9.013s | tokens_per_second: 62.2
- input_tokens: 293 | output_tokens: 561

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
    "score": 5,
    "bant": {
      "budget": "Desconocido (no menciona presupuesto)",
      "authority": "Alta (CEO, aunque es startup pequeña)",
      "need": "Media (busca automatizar soporte, sin detalles de problema agudo)",
      "timeline": "Desconocido (sin plazo específico)"
    },
    "action": "Calificar presupuesto y timeline en una llamada rápida",
    "reason": "El lead es un tomador de decisiones con una necesidad alineada, pero faltan datos clave de presupuesto y plazo para priorizarlo más. Al venir del blog, se debe validar la urgencia real y la capacidad de inversión de la startup."
  },
  {
    "score": 9,
    "action": "Agendar demo prioritaria inmediata",
    "bant": {
      "budget": "Alto (empresa con Serie B levantada)",
      "authority": "Alta (VP of Operations en empresa de 200 empleados)",
      "need": "Alta (busca solución alineada con su puesto)",
      "timeline": "Alta (plazo límite antes de Q3)"
    },
    "reason": "Cumple con todos los criterios BANT de forma sólida: tomador de decisiones, presupuesto confirmado por la ronda de inversión, necesidad clara y plazo definido. Es un lead altamente cualificado que requiere atención inmediata para cerrar la venta."
  },
  {
    "score": 2,
    "bant": {
      "budget": "Desconocido (solicita PDF de precios, pero no tiene contexto de inversión)",
      "authority": "Nula (intern de marketing, sin poder de decisión)",
      "need": "Baja (investigación genérica solicitada por su jefe, sin problema específico)",
      "timeline": "Desconocido (sin plazo mencionado)"
    },
    "action": "Enviar PDF de precios y nurturing por email, sin asignar ejecutivo de ventas",
    "reason": "El lead no es un tomador de decisiones, su necesidad es genérica y no hay datos de presupuesto ni plazo. Solo cumple una función de investigación inicial, por lo que se le trata como lead frío hasta que su jefe o un decisor se involucre."
  }
]