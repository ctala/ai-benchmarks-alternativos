# Gemini 3.1 Flash Lite (GA) — sales_outreach/lead_qualification

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 4.83 | quality: 3.33
- latency_total: 1.862s | tokens_per_second: 194.4
- input_tokens: 243 | output_tokens: 362

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
{
  "lead_1": {
    "score": 6,
    "bant": {
      "budget": "Desconocido",
      "authority": "Alto (CEO)",
      "need": "Clara (automatización de soporte)",
      "timeline": "Indefinido"
    },
    "action": "Agendar llamada de descubrimiento",
    "reason": "Es el tomador de decisiones y tiene una necesidad clara, pero falta calificar el presupuesto y la urgencia."
  },
  "lead_2": {
    "score": 10,
    "bant": {
      "budget": "Probablemente alto (Serie B)",
      "authority": "Alto (VP of Operations)",
      "need": "Alta (solicitó demo)",
      "timeline": "Definido (antes de Q3)"
    },
    "action": "Prioridad alta: agendar demo inmediata",
    "reason": "Cumple con todos los criterios BANT. La empresa tiene capital y la ejecutiva tiene poder de decisión y un plazo claro."
  },
  "lead_3": {
    "score": 2,
    "bant": {
      "budget": "No disponible",
      "authority": "Bajo (Intern)",
      "need": "Exploratoria",
      "timeline": "Indefinido"
    },
    "action": "Enviar material informativo por email y nutrir",
    "reason": "No es un tomador de decisiones. Es una tarea de investigación delegada sin intención de compra inmediata."
  }
}
```