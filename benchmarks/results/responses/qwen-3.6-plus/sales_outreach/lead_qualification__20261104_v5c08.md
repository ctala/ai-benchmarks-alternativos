# Qwen 3.6 Plus — sales_outreach/lead_qualification

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 4.28 | quality: 3.33
- latency_total: 9.18s | tokens_per_second: 53.5
- input_tokens: 262 | output_tokens: 491

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
    "score": 4,
    "bant": {
      "budget": "Desconocido/Probablemente bajo (Startup de 5 personas)",
      "authority": "Alto (CEO es decision maker)",
      "need": "Moderado (Explorando opciones para automatizar soporte)",
      "timeline": "Bajo/Indefinido (Fase de investigación temprana)"
    },
    "action": "Nurture",
    "reason": "Aunque tiene autoridad, el tamaño de la empresa sugiere un presupuesto limitado o nulo para soluciones enterprise. Al no haber urgencia ni mención de budget, es mejor mantenerlo en una secuencia de nurturing educativo hasta que madure la necesidad o la empresa crezca."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto (Serie B reciente implica capital disponible)",
      "authority": "Alto (VP of Operations suele tener poder de decisión operativa)",
      "need": "Alto (Solicitó demo activamente tras webinar)",
      "timeline": "Alto (Necesidad explícita de resolver antes de Q3)"
    },
    "action": "Contact Immediately",
    "reason": "Lead altamente calificado. Cumple con todos los criterios BANT: tiene el dinero (Serie B), la autoridad (VP), la necesidad clara (demo request) y la urgencia (deadline Q3). Prioridad máxima para ventas."
  },
  {
    "score": 1,
    "bant": {
      "budget": "Desconocido (No es su decisión)",
      "authority": "Nulo (Intern, no es decision maker)",
      "need": "Bajo (Solo está investigando por tarea asignada)",
      "timeline": "Bajo (Sin urgencia comercial real)"
    },
    "action": "Disqualify / Send Automated Info",
    "reason": "No es un prospecto viable actualmente. Es un estudiante/practicante sin poder de compra ni presupuesto propio. Se le debe enviar el PDF solicitado automáticamente para no perder tiempo humano, pero se descarta como oportunidad de venta directa."
  }
]
```