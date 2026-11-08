# Gemini 3.8 Flash — sales_outreach/lead_qualification

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.7 | quality: 10.0
- latency_total: 11.083s | tokens_per_second: 124.4
- input_tokens: 243 | output_tokens: 1379

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
      "budget": "Desconocido; probable presupuesto limitado por el tamaño de la empresa (5 personas)",
      "authority": "Alta (CEO, tomador de decisiones final)",
      "need": "Media (exploratoria; 'viendo opciones' para automatizar soporte)",
      "timeline": "Baja / Indefinida (sin fecha objetivo)"
    },
    "action": "Lead Nurturing / Secuencia de email automatizada",
    "reason": "Aunque tiene autoridad como CEO, el tamaño del equipo, la falta de urgencia y la ausencia de presupuesto confirmado no justifican asignación a ventas directas por ahora."
  },
  {
    "lead": "Lead 2: Ana Gomez",
    "score": 10,
    "bant": {
      "budget": "Alta probabilidad (empresa de 200 empleados con reciente levantamiento de Serie B)",
      "authority": "Alta (VP of Operations, tomadora de decisiones en operaciones)",
      "need": "Alta y explícita (solicitó demo activamente tras un webinar)",
      "timeline": "Urgente y definida (requiere solución antes de Q3)"
    },
    "action": "Agendar demo inmediatamente con un Account Executive (AE)",
    "reason": "Cumple los 4 criterios BANT de forma óptima: presupuesto respaldado por Serie B, alta jerarquía, dolor claro y ventana de compra definida."
  },
  {
    "lead": "Lead 3: Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido",
      "authority": "Nula (pasante/intern de marketing sin poder de decisión)",
      "need": "Baja / Muy preliminar ('investigar herramientas de IA')",
      "timeline": "Indefinida"
    },
    "action": "Automatizar envío de PDF y solicitar datos de contacto de su responsable",
    "reason": "No tiene autoridad ni urgencia definida; enviar la información solicitada vía flujo automatizado para intentar acceder al decisor real sin consumir tiempo del equipo de ventas."
  }
]
```