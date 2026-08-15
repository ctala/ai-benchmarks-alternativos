# Gemini 3.6 Flash — sales_outreach/lead_qualification

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 6.43 | quality: 6.67
- latency_total: 7.622s | tokens_per_second: 186.2
- input_tokens: 245 | output_tokens: 1419

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
    "lead": "Lead 1: Juan Perez",
    "score": 5,
    "bant": {
      "budget": "Incierto (no mencionado, startup de 5 personas con presupuesto probablemente limitado)",
      "authority": "Alta (CEO, tomador de decisiones)",
      "need": "Media (interés en automatizar soporte, pero en fase exploratoria)",
      "timeline": "Sin definir (\"viendo opciones\")"
    },
    "action": "Nurturing / Enviar secuencia de correos y agendar llamada corta de calificación",
    "reason": "Tiene la autoridad total por ser CEO, pero la startup es pequeña, está en etapa muy temprana de exploración y no hay presupuesto ni urgencia confirmada."
  },
  {
    "lead": "Lead 2: Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Alto (empresa de 200 empleados con recién financiamiento Serie B)",
      "authority": "Alta (VP of Operations, influenciadora principal o decisora)",
      "need": "Alta (solicitó demo activamente tras webinar)",
      "timeline": "Definida y urgente (resolver antes de Q3)"
    },
    "action": "Asignar de inmediato a un Account Executive (AE) para agendar la Demo",
    "reason": "Cumple excelentemente con los 4 criterios de BANT. Tiene alto presupuesto, autoridad, necesidad clara y una fecha límite definida."
  },
  {
    "lead": "Lead 3: Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido",
      "authority": "Nula (pasante/intern de marketing)",
      "need": "Baja/Investigación (tarea encomendada por su jefe)",
      "timeline": "Desconocido / Larga duración"
    },
    "action": "Enviar PDF de precios por automatización e intentar conseguir los datos de contacto de su jefe",
    "reason": "Sin autoridad ni poder de decisión. Está haciendo una investigación básica. No justifica tiempo de un representante de ventas directo en este momento."
  }
]
```