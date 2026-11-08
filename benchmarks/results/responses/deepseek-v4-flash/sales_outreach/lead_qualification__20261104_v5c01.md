# DeepSeek V4 Flash (OpenRouter) — sales_outreach/lead_qualification

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 4.43 | quality: 3.33
- latency_total: 7.523s | tokens_per_second: 48.0
- input_tokens: 261 | output_tokens: 361

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
      "score": 6,
      "bant": {
        "budget": "Desconocido, no mencionó presupuesto",
        "authority": "Alta, es CEO",
        "need": "Media, está explorando opciones",
        "timeline": "No especificada"
      },
      "action": "Nutrir",
      "reason": "Tiene autoridad y necesidad potencial, pero falta claridad en presupuesto y timeline. Requiere más información."
    },
    {
      "score": 9,
      "bant": {
        "budget": "Alta, empresa con Serie B",
        "authority": "Alta, VP of Operations",
        "need": "Alta, necesita solución antes de Q3",
        "timeline": "Urgente, antes de Q3"
      },
      "action": "Contactar inmediatamente para demo",
      "reason": "Cumple todos los criterios BANT: tiene presupuesto, autoridad, necesidad urgente y timeline claro. Lead calificado."
    },
    {
      "score": 3,
      "bant": {
        "budget": "No aplica, es intern",
        "authority": "Baja, no es decision maker",
        "need": "Baja, solo investiga por encargo",
        "timeline": "No definida"
      },
      "action": "Enviar material informativo genérico y calificar después",
      "reason": "No tiene autoridad ni necesidad directa. Solo investiga. No es un lead calificado en este momento."
    }
  ]
}