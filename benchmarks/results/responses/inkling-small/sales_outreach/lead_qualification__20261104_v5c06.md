# Inkling Small — sales_outreach/lead_qualification

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 4.68 | quality: 3.33
- latency_total: 3.823s | tokens_per_second: 109.1
- input_tokens: 247 | output_tokens: 417

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

{"score": 1, "bant": {"budget": "No menciona presupuesto; startup de 5 personas sugiere recursos limitados", "authority": "CEO; es decision maker", "need": "Bajo/Exploratorio: 'estamos viendo opciones' para automatizar soporte", "timeline": "No definido; exploración temprana via blog"}, "action": "Nurture / Descalificar para venta inmediata: enviar contenido educativo y esperar señales de intención de compra", "reason": "Alta autoridad pero baja necesidad confirmada, sin presupuesto declarado ni urgencia; lead de awareness temprano que requiere nurturing antes de calificar."}

{"score": 9, "bant": {"budget": "Alto: empresa de 200 empleados con Serie B reciente indica capacidad de inversión", "authority": "VP of Operations; alta autoridad y decision maker", "need": "Alto: solicita demo post-webinar con problema claro de operaciones", "timeline": "Crítico: 'antes de Q3' define urgencia inmediata"}, "action": "Calificar como SQL / Agendar demo urgente y asignar a ventas inmediatamente", "reason": "Cumple BANT completo: presupuesto implícito fuerte, autoridad alta, necesidad clara, timeline urgente; lead de webinar con intención de compra explícita."}

{"score": 2, "bant": {"budget": "No indicado; solicita PDF de precios sin contexto de compra", "authority": "Baja: intern de marketing; no es decision maker", "need": "Bajo: investigación delegada ('su jefe pidió investigar') sin problema propio definido", "timeline": "No definido; sin urgencia ni plazo"}, "action": "Nurture / Rechazar para venta directa: enviar PDF de precios genérico y solicitar contacto con el decision maker", "reason": "Sin autoridad ni necesidad real; es un influencer/recopilador de información sin poder de compra ni urgencia; riesgo de perder tiempo de ventas."}