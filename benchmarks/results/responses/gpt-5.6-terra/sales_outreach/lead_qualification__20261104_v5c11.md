# GPT-5.6 Terra — sales_outreach/lead_qualification

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 3.94 | quality: 3.33
- latency_total: 5.234s | tokens_per_second: 83.9
- input_tokens: 242 | output_tokens: 439

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
      "budget": "No mencionado; probable presupuesto limitado por ser una startup de 5 personas.",
      "authority": "Alta: es CEO y probablemente decisor.",
      "need": "Moderada: está explorando automatización de soporte, pero no describe un dolor específico.",
      "timeline": "No definido."
    },
    "action": "Nutrir y calificar con preguntas de descubrimiento; ofrecer una llamada breve o demo.",
    "reason": "Tiene autoridad y un caso de uso relevante, pero faltan señales de urgencia, presupuesto y alcance del problema."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto potencial: la empresa acaba de levantar Serie B, aunque no confirmó presupuesto asignado.",
      "authority": "Alta: como VP of Operations probablemente influye fuertemente o decide la compra.",
      "need": "Alta: expresa una necesidad concreta de resolver el problema.",
      "timeline": "Alta urgencia: necesita una solución antes de Q3."
    },
    "action": "Prioridad alta: contactar inmediatamente, agendar demo y preparar propuesta basada en su caso de uso.",
    "reason": "Combina una necesidad clara, plazo definido, seniority relevante y fuerte capacidad potencial de compra."
  },
  {
    "score": 3,
    "bant": {
      "budget": "Desconocido; solicita precios, pero no indica presupuesto ni capacidad de compra.",
      "authority": "Baja: es intern y está realizando investigación para su jefe.",
      "need": "Baja a moderada: existe interés en herramientas de IA, pero no hay problema o caso de uso definido.",
      "timeline": "No definido."
    },
    "action": "Enviar PDF de precios y contenido de calificación; intentar identificar al responsable o decisor.",
    "reason": "Es un contacto inicial sin autoridad ni necesidad concreta. Puede convertirse en oportunidad si se conecta con el jefe o equipo que lidera la evaluación."
  }
]