# Muse Ember — sales_outreach/lead_qualification

- model_id: `meta/muse-ember`
- success: True  | final: 4.63 | quality: 3.33
- latency_total: 3.262s | tokens_per_second: 465.3
- input_tokens: 258 | output_tokens: 1518

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

[{"lead": 1, "score": 5, "bant": {"budget": "Desconocido, no mencionado; startup de 5 personas sugiere presupuesto incierto/limitado", "authority": "Alta, es CEO y decision maker", "need": "Media-baja, interés general en automatizar soporte sin problema concreto definido", "timeline": "Baja/desconocida, dice 'estamos viendo opciones', sin fecha"}, "action": "Nurturing y discovery: enviar contenido relevante y agendar llamada breve para calificar presupuesto, necesidad y timeline", "reason": "Tiene autoridad pero faltan budget, need específico y timeline para ser oportunidad activa"}, {"lead": 2, "score": 9, "bant": {"budget": "Alta probabilidad, empresa de 200 empleados que acaba de levantar Serie B", "authority": "Alta, VP of Operations, decision maker/influyente", "need": "Alta, solicitó demo tras webinar con problema identificado", "timeline": "Alta, necesita resolverlo antes de Q3"}, "action": "Pasar a ventas como prioridad y agendar demo esta semana", "reason": "Cumple los 4 criterios BANT con presupuesto, autoridad, necesidad clara y urgencia definida"}, {"lead": 3, "score": 2, "bant": {"budget": "No, sin presupuesto propio, solo está investigando", "authority": "Nula, es intern sin poder de decisión", "need": "Baja, tarea delegada de investigar herramientas, sin problema propio", "timeline": "Ninguna, sin urgencia ni fecha"}, "action": "Enviar PDF con precios de forma automatizada y mantener en nurture, no escalar a ventas", "reason": "No cumple BANT, solo recopila información para su jefe"}]