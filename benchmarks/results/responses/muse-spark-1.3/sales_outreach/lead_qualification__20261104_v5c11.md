# Muse Spark 1.3 — sales_outreach/lead_qualification

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 3.93 | quality: 3.33
- latency_total: 12.735s | tokens_per_second: 163.1
- input_tokens: 258 | output_tokens: 2077

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
  "lead1": {
    "score": 5,
    "bant": {
      "budget": "Desconocido / probablemente bajo - no mencionó presupuesto, startup de 5 personas",
      "authority": "Alta - CEO es decision maker total",
      "need": "Media - quiere automatizar soporte, pero aún exploratorio 'viendo opciones'",
      "timeline": "Baja - sin urgencia definida, llegó vía blog (top of funnel)"
    },
    "action": "Enviar a nurture",
    "reason": "Tiene autoridad y necesidad potencial, pero sin presupuesto ni timeline. Ideal para nutrición educativa, no para ventas aún."
  },
  "lead2": {
    "score": 9,
    "bant": {
      "budget": "Alta - empresa de 200 empleados que acaba de levantar Serie B",
      "authority": "Alta - VP of Operations es decisora clave",
      "need": "Alta - pidió demo activamente después de webinar",
      "timeline": "Alta y urgente - necesita resolver antes de Q3"
    },
    "action": "Pasar a ventas inmediatamente",
    "reason": "Cumple todo BANT: presupuesto probable, autoridad, necesidad clara y timeline urgente. Lead caliente listo para demo prioritaria."
  },
  "lead3": {
    "score": 2,
    "bant": {
      "budget": "Desconocido / Bajo - sin control presupuestal, solo pide PDF con precios",
      "authority": "Muy baja - intern de marketing investigando por encargo",
      "need": "Baja / Vaga - 'investigar herramientas de IA' sin problema específico",
      "timeline": "Nula - sin urgencia definida"
    },
    "action": "Descartar para ventas, enviar PDF automatizado",
    "reason": "Sin autoridad, sin necesidad clara ni timeline. No justifica esfuerzo comercial, solo nurture automatizado de bajo toque."
  }
}