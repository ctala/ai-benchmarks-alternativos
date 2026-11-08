# Gemini 4 Argon — sales_outreach/lead_qualification

- model_id: `google/gemini-4-argon`
- success: True  | final: 8.6 | quality: 10.0
- latency_total: 9.531s | tokens_per_second: 57.8
- input_tokens: 274 | output_tokens: 551

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
    "score": 6,
    "bant": {
      "budget": "Incierto/Bajo (Startup de 5 personas, no mencionado)",
      "authority": "Alta (Es el CEO)",
      "need": "Media-Alta (Busca automatizar soporte)",
      "timeline": "Baja/Indefinida ('Viendo opciones', etapa de exploración)"
    },
    "action": "Enviar secuencia de emails automatizada (Nurturing) e invitar a una llamada de descubrimiento rápida de 15 min para validar presupuesto.",
    "reason": "Tiene la autoridad máxima y una necesidad clara, pero el tamaño de su empresa sugiere un presupuesto limitado y aún está en fase de investigación sin urgencia."
  },
  {
    "lead": "Lead 2: Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Alto (Acaban de levantar Serie B)",
      "authority": "Alta (VP of Operations en empresa de 200 empleados)",
      "need": "Alta (Pidió una demo proactivamente)",
      "timeline": "Alta (Necesita resolverlo antes de Q3)"
    },
    "action": "Asignar inmediatamente a un Account Executive Senior para agendar la demo en las próximas 24 horas (Fast-track).",
    "reason": "Cumple con todos los criterios BANT a la perfección. Es un lead caliente (SQL) con liquidez financiera, urgencia temporal y poder de decisión."
  },
  {
    "lead": "Lead 3: Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido (Sensible al precio al pedir solo el PDF)",
      "authority": "Nula (Intern de marketing, solo recopila información)",
      "need": "Baja/Vaga ('Herramientas de IA' es muy genérico)",
      "timeline": "Baja (Fase de investigación inicial encargada por un tercero)"
    },
    "action": "Enviar el PDF con precios de forma automatizada y pedir el contacto de su jefe para dar seguimiento futuro. No asignar a ventas.",
    "reason": "No tiene poder de decisión ni un problema específico definido. Invertir tiempo de un vendedor aquí tiene un ROI muy bajo, a menos que logremos contactar a su jefe."
  }
]
```