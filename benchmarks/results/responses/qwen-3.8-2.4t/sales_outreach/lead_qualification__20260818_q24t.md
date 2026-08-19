# Qwen 3.8 2.4T (A95B) — sales_outreach/lead_qualification

- model_id: `qwen/qwen3.8-2.4t-a95b`
- success: True  | final: 8.37 | quality: 10.0
- latency_total: 20.611s | tokens_per_second: 43.8
- input_tokens: 298 | output_tokens: 903

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

{
  "leads": [
    {
      "lead": "Juan Perez",
      "score": 5,
      "bant": {
        "budget": "Desconocido; no mencionó presupuesto y es una startup pequeña de 5 personas.",
        "authority": "Alta; es CEO, probablemente decision maker.",
        "need": "Claro; está explorando automatizar soporte.",
        "timeline": "Incieto; solo está viendo opciones, sin urgencia explícita."
      },
      "action": "Nurture y calificación adicional",
      "reason": "Tiene autoridad y una necesidad relevante, pero falta confirmar presupuesto y urgencia. Conviene enviar casos de éxito y agendar una llamada de descubrimiento."
    },
    {
      "lead": "Ana Gomez",
      "score": 9,
      "bant": {
        "budget": "Probablemente alto; empresa de 200 empleados y recién levantó Serie B.",
        "authority": "Alta; VP of Operations, probablemente decisora o muy influyente.",
        "need": "Claro; pidió una demo y necesita resolver una necesidad operativa.",
        "timeline": "Urgente; necesita resolver antes de Q3."
      },
      "action": "Priorizar demo inmediata",
      "reason": "Lead caliente con autoridad, necesidad clara, presupuesto probable y timeline urgente. Debe pasar a ventas de inmediato."
    },
    {
      "lead": "Carlos Ruiz",
      "score": 2,
      "bant": {
        "budget": "Desconocido; solo pidió un PDF con precios.",
        "authority": "Baja; es intern y está investigando para su jefe.",
        "need": "Débil o exploratorio; busca información general sobre herramientas de IA.",
        "timeline": "Desconocido; no indicó urgencia."
      },
      "action": "Enviar material automático y pedir contacto del decision maker",
      "reason": "Es un perfil de baja intención y sin autoridad. Se le puede nutrir con contenido, pero no vale la pena priorizarlo para ventas hasta identificar al responsable de la decisión."
    }
  ]
}