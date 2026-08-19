# GPT-5.6 Terra Pro — sales_outreach/lead_qualification

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 3.94 | quality: 3.33
- latency_total: 9.529s | tokens_per_second: 149.2
- input_tokens: 3747 | output_tokens: 1422

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
      "budget": "No mencionado; probable sensibilidad al precio por tamaño de startup.",
      "authority": "Alta: es CEO y probablemente decision maker.",
      "need": "Moderada-alta: busca automatizar soporte, aunque no detalla el problema ni alcance.",
      "timeline": "No especificado."
    },
    "action": "Enviar email de discovery y ofrecer una llamada breve para entender volumen de soporte, casos de uso, presupuesto y plazo.",
    "reason": "Tiene autoridad y una necesidad relevante, pero faltan datos críticos sobre presupuesto, urgencia y requisitos."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto potencial: la empresa acaba de levantar una Serie B, aunque no confirmó presupuesto asignado.",
      "authority": "Alta: como VP of Operations es probablemente influencer clave o decision maker.",
      "need": "Alta: expresó una necesidad concreta de resolver el problema.",
      "timeline": "Alta urgencia: necesita una solución antes de Q3."
    },
    "action": "Prioridad alta: contactar en menos de 24 horas, agendar demo personalizada y preparar propuesta con plan de implementación antes de Q3.",
    "reason": "Combina fuerte necesidad, plazo definido, seniority relevante y señales positivas de capacidad de compra."
  },
  {
    "score": 3,
    "bant": {
      "budget": "Desconocido; solicita precios, pero no indica presupuesto disponible.",
      "authority": "Baja: es intern y está investigando por solicitud de su jefe.",
      "need": "Baja-media: existe interés exploratorio, pero no hay problema concreto ni caso de uso definido.",
      "timeline": "No especificado."
    },
    "action": "Enviar PDF de precios y material introductorio; solicitar contacto del jefe o responsable de evaluación y activar nutrición por email.",
    "reason": "Es un contacto de investigación sin autoridad ni urgencia demostrada. Puede convertirse en oportunidad si se identifica al decision maker y una necesidad concreta."
  }
]