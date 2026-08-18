# Gemini 3.6 Flash — sales_outreach/lead_qualification

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.64 | quality: 10.0
- latency_total: 10.36s | tokens_per_second: 178.8
- input_tokens: 243 | output_tokens: 1852

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
    "lead": "Lead 1: Juan Perez",
    "score": 5,
    "bant": {
      "budget": "Desconocido / Probablemente bajo (startup de 5 personas)",
      "authority": "Alta (CEO / Toma la decisión final)",
      "need": "Media (Busca automatizar soporte, en etapa exploratoria)",
      "timeline": "Baja (No menciona plazo, está 'viendo opciones')"
    },
    "action": "Nutrir a través de secuencias de email y agendar llamada de descubrimiento para calificar presupuesto y urgencia.",
    "reason": "Tiene la autoridad máxima al ser CEO y una necesidad identificada, pero el tamaño de la empresa sugiere presupuesto limitado y no hay un tiempo de compra definido."
  },
  {
    "lead": "Lead 2: Ana Gomez",
    "score": 10,
    "bant": {
      "budget": "Alto (200 empleados y recién levantó Serie B)",
      "authority": "Alta (VP of Operations / Decision maker clave)",
      "need": "Alta (Solicitó demo activamente tras un webinar)",
      "timeline": "Alta (Plazo claro: resolver antes de Q3)"
    },
    "action": "Asignar inmediatamente a un Ejecutivo de Ventas (AE) para agendar demo prioritaria.",
    "reason": "Es un lead SQL perfecto. Cumple con los 4 criterios de BANT: presupuesto garantizado, alta autoridad, urgencia clara y necesidad demostrada."
  },
  {
    "lead": "Lead 3: Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido",
      "authority": "Nula (Intern / Pasante)",
      "need": "Baja / Exploratoria (Investigación encargada)",
      "timeline": "Baja / Indefinida"
    },
    "action": "Enviar correo automatizado con el PDF de precios/información y agregar a flujo de nutrición de Marketing (Lead Nurturing).",
    "reason": "El contacto no tiene autoridad de compra ni poder de decisión. Está haciendo una investigación preliminar sin una intención de compra o presupuesto calificado en este momento."
  }
]