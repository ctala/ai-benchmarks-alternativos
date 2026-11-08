# Gemini 3.1 Pro — sales_outreach/lead_qualification

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 8.22 | quality: 10.0
- latency_total: 26.96s | tokens_per_second: 87.1
- input_tokens: 243 | output_tokens: 2348

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
  "leads": [
    {
      "id": "Lead 1: Juan Perez",
      "score": 5,
      "bant": {
        "budget": "Desconocido. Al ser una startup de 5 personas, el presupuesto podría ser limitado.",
        "authority": "Alta. Es el CEO, por lo que es el tomador de decisiones final.",
        "need": "Media. Tienen la necesidad de automatizar soporte, pero están en fase exploratoria.",
        "timeline": "Baja. Solo están 'viendo opciones', no hay un sentido de urgencia claro."
      },
      "action": "Agendar llamada de descubrimiento (Discovery call)",
      "reason": "Tiene la autoridad y una necesidad latente, pero es vital calificar su presupuesto y definir un timeline antes de avanzar a una demostración técnica."
    },
    {
      "id": "Lead 2: Ana Gomez",
      "score": 10,
      "bant": {
        "budget": "Alta. Acaban de levantar una ronda Serie B, por lo que tienen liquidez y presupuesto para operaciones.",
        "authority": "Alta. VP of Operations en una empresa de 200 empleados es una tomadora de decisiones clave o sponsor principal.",
        "need": "Alta. Pidió una demo proactivamente para resolver un problema específico.",
        "timeline": "Alta. Tiene una fecha límite estricta y cercana ('antes de Q3')."
      },
      "action": "Asignar a Account Executive (Ventas) inmediatamente para realizar la Demo",
      "reason": "Es un lead 'Hot' que cumple perfectamente con los 4 criterios del framework BANT. Requiere atención prioritaria y personalizada."
    },
    {
      "id": "Lead 3: Carlos Ruiz",
      "score": 2,
      "bant": {
        "budget": "Desconocido. Solo está pidiendo precios para evaluar.",
        "authority": "Baja. Es un intern (pasante), no tiene poder de decisión (el jefe decide).",
        "need": "Baja. Es una investigación general sobre 'herramientas de IA', no un dolor específico del negocio.",
        "timeline": "Baja. Están en fase de investigación inicial sin urgencia."
      },
      "action": "Enviar PDF de precios de forma automatizada y agregar a campaña de Nurturing (Newsletter)",
      "reason": "No cumple con autoridad, urgencia ni necesidad clara. No se debe invertir tiempo de ventas directas, pero se le entrega el material para que se lo pase a su jefe (el verdadero decision maker)."
    }
  ]
}
```