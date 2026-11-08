# Granite 4.2 8B — sales_outreach/lead_qualification

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 4.73 | quality: 3.33
- latency_total: 5.42s | tokens_per_second: 131.2
- input_tokens: 279 | output_tokens: 711

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
    "score": 6,
    "bant": {
      "budget": "Desconocido (no mencionó presupuesto)",
      "authority": "CEO de startup de 5 personas → probablemente decision maker para estrategia y adquisición de soluciones",
      "need": "Menciona deseo de automatizar soporte → probable need real, aunque aún exploratorio",
      "timeline": "No especifica plazo; probablemente en etapa temprana de evaluación"
    },
    "action": "Enviar un mensaje breve de seguimiento personalizado: confirmar interés, preguntar qué aspectos del soporte les preocupa más (ej. volumen, calidad, tiempos) y ofrecer una demo rápida de 15 min sin compromiso. Preguntar si tienen un presupuesto aproximado o plazo para decidir.",
    "reason": "Autoridad válida (CEO), need claro (automatizar soporte), pero falta budget y timeline. Un seguimiento rápido y sin presión ayuda a definir presupuesto y plazo."
  },
  "lead_2": {
    "score": 9,
    "bant": {
      "budget": "Probablemente disponible (empresa recién levantó Serie B, suele tener presupuesto para soluciones de operaciones)",
      "authority": "VP of Operations en empresa de 200 empleados → decision maker para procesos y adquisición de herramientas de soporte",
      "need": "Necesita resolver el problema antes de Q3 → need claro y urgente",
      "timeline": "Plazo antes de Q3 (timeline definido)"
    },
    "action": "Programar la demo solicitada lo antes posible (preferiblemente dentro de la próxima semana) y enviar una propuesta breve con casos de uso relevantes para operaciones. Incluir preguntas de budget y opciones de implementación.",
    "reason": "Autoridad sólida, need explícito, timeline claro (antes de Q3) y probable budget disponible tras Serie B. Acción urgente para demo y propuesta."
  },
  "lead_3": {
    "score": 3,
    "bant": {
      "budget": "No menciona presupuesto; como intern, probablemente no tenga autoridad para decidir",
      "authority": "Intern de marketing → no es decision maker; su jefe haría la decisión",
      "need": "Solo investigar herramientas de IA por solicitud del jefe; no ha identificado un problema concreto que requiera solución ahora",
      "timeline": "No especifica plazo; probablemente investigación preliminar"
    },
    "action": "Responder amablemente solicitando que el intern comparta la consulta con su jefe (VP/manager) y ofrecer un PDF resumen de precios y casos de uso. No avanzar con demo ni propuesta directa.",
    "reason": "Autoridad limitada (intern), need aún conceptual, sin timeline ni budget. Mejor canalizar a quien tenga decision making."
  }
}