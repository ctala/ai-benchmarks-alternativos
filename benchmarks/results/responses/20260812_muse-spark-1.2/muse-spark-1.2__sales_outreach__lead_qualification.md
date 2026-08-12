# Muse Spark 1.2 — sales_outreach/lead_qualification

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 8.71 | quality: 10.0
- latency_total: 6.434s | tokens_per_second: 251.5
- input_tokens: 243 | output_tokens: 1618

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
      "lead": 1,
      "nombre": "Juan Perez - CEO startup 5 personas",
      "score": 5,
      "bant": {
        "budget": "Desconocido/Bajo - Startup pequeña de 5 personas, no mencionó presupuesto",
        "authority": "Alto - CEO es decision maker",
        "need": "Medio - Interés en automatizar soporte pero aún exploratorio ('viendo opciones')",
        "timeline": "Bajo - Sin deadline definido, llegó inbound por blog"
      },
      "action": "Nurture + Discovery Call",
      "reason": "Lead con autoridad y necesidad potencial pero sin presupuesto validado ni urgencia. No es prioridad para ventas directas, requiere calificar presupuesto y timeline antes de pasar a AE."
    },
    {
      "lead": 2,
      "nombre": "Ana Gomez - VP of Operations empresa 200 empleados",
      "score": 9,
      "bant": {
        "budget": "Alto - Empresa de 200 empleados que acaba de levantar Serie B",
        "authority": "Alto - VP of Operations es decisora/influenciadora clave",
        "need": "Alto - Necesidad explícita y proactiva (pidió demo)",
        "timeline": "Alto - Urgencia definida 'antes de Q3'"
      },
      "action": "Prioridad Alta - Pasar a ventas inmediatamente y agendar demo",
      "reason": "Lead ideal que cumple las 4 de BANT. Alta probabilidad de cierre y con timeline cercano. Acción inmediata de Account Executive."
    },
    {
      "lead": 3,
      "nombre": "Carlos Ruiz - Intern de marketing",
      "score": 2,
      "bant": {
        "budget": "Desconocido/Nulo - Intern sin poder de compra ni acceso a presupuesto",
        "authority": "Nulo - No es decision maker, solo investiga por encargo de su jefe",
        "need": "Bajo - Investigación genérica 'herramientas de IA', sin problema específico",
        "timeline": "Nulo - Sin timeline ni urgencia"
      },
      "action": "No contactar por ventas - Enviar PDF y dejar en nurture automatizado",
      "reason": "Lead no calificado. Sin autoridad, sin necesidad clara y sin timeline. No vale tiempo de ventas, solo nutrir con contenido hasta que el decision maker aparezca."
    }
  ]
}
```