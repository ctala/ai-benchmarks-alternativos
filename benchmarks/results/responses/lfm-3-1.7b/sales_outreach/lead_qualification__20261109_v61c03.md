# LFM-3 1.7B — sales_outreach/lead_qualification

- model_id: `liquid/lfm-3-1.7b`
- success: True  | final: 4.53 | quality: 3.33
- latency_total: 7.473s | tokens_per_second: 391.6
- input_tokens: 267 | output_tokens: 2926

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
    "score": 7,
    "bant": {
      "budget": "No mencionado (información limitada)",
      "authority": "Sí – CEO",
      "need": "Automatizar soporte",
      "timeline": "No especificado"
    },
    "action": "Contactar mediante el enlace del blog donde apareció su publicación para ofrecer una propuesta de automatización; preguntar sobre presupuesto y plazos.",
    "reason": "El ejecutivo tiene máxima autoridad y expresa una necesidad clara, pero falta detalle sobre presupuesto y plazo, lo que reduce la urgencia."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Probablemente disponible (empresa con Serie B)",
      "authority": "Sí – VP de Operaciones",
      "need": "Resolver un problema operativo antes del Q3",
      "timeline": "Antes del tercer trimestre"
    },
    "action": "Organizar una demo inmediatamente después del webinar y definir una solución que cumpla los objetivos del Q3.",
    "reason": "Alta autoridad, presupuesto probable gracias a la融资 Serie B, necesidad definida y fecha límite concreta (antes del Q3)."
  },
  {
    "score": 4,
    "bant": {
      "budget": "No mencionado",
      "authority": "Bajo – Interno, no toma decisiones",
      "need": "Investigar herramientas de IA (pedido de su jefe)",
      "timeline": "No especificado"
    },
    "action": "Entregar el PDF con precios de las herramientas de IA una vez recopilados los datos; también solicitar más detalles al supervisor de Carlos.",
    "reason": "La autoridad es baja (interno), faltan datos sobre presupuesto y la necesidad específica; es una consulta informativa y poco urgente."
  }
]
```