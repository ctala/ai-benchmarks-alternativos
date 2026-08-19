# Claude Sonnet 5 — sales_outreach/lead_qualification

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.31 | quality: 10.0
- latency_total: 20.816s | tokens_per_second: 83.6
- input_tokens: 410 | output_tokens: 1741

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
      "lead": "Juan Perez - CEO Startup",
      "score": 5,
      "bant": {
        "budget": "Desconocido - no mencionado, startup pequeña (5 personas) sugiere presupuesto limitado o inexistente",
        "authority": "Alta - es CEO, decision maker directo",
        "need": "Parcial - esta 'viendo opciones', fase de exploracion sin dolor especifico articulado",
        "timeline": "No definido - sin urgencia expresada"
      },
      "action": "Nurture + calificar",
      "reason": "Tiene autoridad total (CEO) pero el need y budget son vagos y no hay timeline. Llego via blog, canal de bajo intent. Enviar contenido educativo y agendar llamada de descubrimiento para validar budget y urgencia antes de invertir tiempo de ventas."
    },
    {
      "lead": "Ana Gomez - VP Operations",
      "score": 9,
      "bant": {
        "budget": "Alto - empresa acaba de cerrar ronda Serie B, hay capital disponible para inversion",
        "authority": "Alta - VP of Operations, tipicamente tiene poder de decision o gran influencia en compras de su area",
        "need": "Claro y explicito - 'necesitamos resolver esto'",
        "timeline": "Definido y con urgencia - deadline antes de Q3"
      },
      "action": "Escalar a AE / agendar demo inmediata",
      "reason": "Cumple los 4 criterios BANT: presupuesto respaldado por funding reciente, autoridad de VP, necesidad explicita y deadline concreto. Ademas el intent es alto (pidio demo tras webinar). Priorizar como Sales Qualified Lead (SQL) y contactar en menos de 24h."
    },
    {
      "lead": "Carlos Ruiz - Intern Marketing",
      "score": 2,
      "bant": {
        "budget": "No aplica - no tiene visibilidad ni control de presupuesto",
        "authority": "Nula - es intern, solo ejecuta una tarea asignada por su jefe",
        "need": "Indirecto - la necesidad es de su jefe, no articulada con detalle",
        "timeline": "Desconocido"
      },
      "action": "Enviar PDF automatizado + nutrir por email marketing",
      "reason": "No cumple ningun criterio BANT de forma solida. Es investigacion de bajo nivel sin poder de decision. No asignar recursos de ventas; automatizar respuesta con material generico e intentar identificar al verdadero decision maker (su jefe) para reabrir la conversacion."
    }
  ]
}
```

**Resumen de priorizacion:**
1. **Ana Gomez (9)** → Contactar ya, alta probabilidad de cierre.
2. **Juan Perez (5)** → Vale la pena calificar mas, pero no urgente.
3. **Carlos Ruiz (2)** → Bajo esfuerzo, automatizar y dejar en nurture pasivo.