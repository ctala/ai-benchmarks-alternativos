# DeepSeek V4 Flash 0731 — sales_outreach/lead_qualification

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 4.88 | quality: 3.33
- latency_total: 2.195s | tokens_per_second: 179.0
- input_tokens: 262 | output_tokens: 393

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
    "score": 5,
    "bant": {
      "budget": "Desconocido, no mencionado",
      "authority": "CEO, tiene autoridad",
      "need": "Interes en automatizar soporte, necesidad clara",
      "timeline": "No especificado, 'viendo opciones' indica fase de evaluacion"
    },
    "action": "Nurturing",
    "reason": "Es CEO con necesidad potencial, pero falta informacion de presupuesto y timeline. Requiere educacion y seguimiento para calificar."
  },
  "lead_2": {
    "score": 9,
    "bant": {
      "budget": "Alto (Serie B reciente)",
      "authority": "VP of Operations, decision maker",
      "need": "Necesidad urgente de resolver antes de Q3",
      "timeline": "Corto plazo (antes de Q3)"
    },
    "action": "Contactar inmediatamente para demo",
    "reason": "Alta calificacion: presupuesto disponible, autoridad, necesidad urgente y timeline definido. Es un lead caliente."
  },
  "lead_3": {
    "score": 2,
    "bant": {
      "budget": "No aplica (intern)",
      "authority": "Sin autoridad, solo investiga",
      "need": "No es el problema directo, solo tarea asignada",
      "timeline": "No definido"
    },
    "action": "Enviar material basico y descalificar",
    "reason": "Intern sin autoridad ni presupuesto. Solo busca informacion, no es un comprador potencial. Descalificar de ventas directas."
  }
}