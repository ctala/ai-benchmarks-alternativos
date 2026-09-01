# GLM 5.3 Flash — sales_outreach/lead_qualification

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 9.2 | quality: 10.0
- latency_total: 13.583s | tokens_per_second: 116.0
- input_tokens: 255 | output_tokens: 1575

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
    "lead": "Juan Perez (CEO, startup 5 personas)",
    "score": 5,
    "bant": {
      "budget": "desconocido - startup temprana, presupuesto probablemente limitado y no confirmado",
      "authority": "alto - es CEO, decision maker directo",
      "need": "parcial - está explorando automatización de soporte, pero en fase temprana ('viendo opciones')",
      "timeline": "indefinido - sin urgencia expresada"
    },
    "action": "discovery call de bajo compromiso / nurturing activo",
    "reason": "Autoridad clara y necesidad potencial, pero falta calificar presupuesto y timeline. Al ser CEO y llegar orgánicamente vía blog, vale la pena una llamada discovery corta para calificar B y T antes de invertir más tiempo."
  },
  {
    "lead": "Ana Gomez (VP Operations, 200 empleados, Serie B)",
    "score": 9,
    "bant": {
      "budget": "alto - Serie B recién levantada, capital disponible",
      "authority": "alto - VP level, probablemente decisor o con influencia directa en la compra",
      "need": "claro - 'necesitamos resolver esto', problema explícito",
      "timeline": "urgente - 'antes de Q3', deadline definido y cercano"
    },
    "action": "asignar a AE de inmediato y agendar demo prioritaria esta semana",
    "reason": "Cumple los 4 criterios BANT: presupuesto probable (Serie B), autoridad (VP), necesidad explícita y timeline con deadline. Además, engagement alto (pidió demo post-webinar). Lead de máxima prioridad: velocidad de respuesta es crítica."
  },
  {
    "lead": "Carlos Ruiz (intern de marketing)",
    "score": 2,
    "bant": {
      "budget": "desconocido - un intern no maneja ni conoce presupuesto",
      "authority": "nulo - sin poder de decisión, actúa por encargo de su jefe",
      "need": "vago - 'herramientas de IA' genérico, no confirma el problema que resolvemos",
      "timeline": "indefinido - 'investigar' sugiere fase exploratoria sin fecha"
    },
    "action": "enviar PDF automatizado + secuencia de nurturing; no asignar tiempo de sales",
    "reason": "Falla authority y budget, y need/timeline son débiles. Nota: el pedido viene del jefe, lo que indica interés real en la empresa. Registrar la compañía en el CRM para que sales prospecte directamente al decisor más adelante."
  }
]
```

**Priorización sugerida:** Lead 2 primero (contacto hoy), Lead 1 segundo (discovery esta semana), Lead 3 en flujo automatizado.