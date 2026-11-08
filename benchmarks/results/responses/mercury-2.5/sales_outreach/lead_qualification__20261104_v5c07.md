# Mercury 2.5 — sales_outreach/lead_qualification

- model_id: `inception/mercury-2.5`
- success: True  | final: 5.03 | quality: 3.33
- latency_total: 1.423s | tokens_per_second: 213.7
- input_tokens: 265 | output_tokens: 304

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

{"leads": [{"lead_id": 1, "score": 6, "bant": {"budget": "Desconocido (no lo mencionó)", "authority": "Alta (CEO)", "need": "Media (busca automatizar soporte)", "timeline": "Baja (no especificó urgencia)"}, "action": "Nurturing por email con casos de éxito", "reason": "Es el decision maker con necesidad clara, pero falta claridad en presupuesto y timeline."}, {"lead_id": 2, "score": 9, "bant": {"budget": "Probablemente alto (levantaron Serie B)", "authority": "Alta (VP Operations)", "need": "Alta (necesitan resolver antes de Q3)", "timeline": "Alta (antes de Q3)"}, "action": "Agendar demo inmediata con equipo de ventas", "reason": "Cumple todos los criterios BANT con alta urgencia y capacidad de compra."}, {"lead_id": 3, "score": 3, "bant": {"budget": "Baja (no es decision maker)", "authority": "Baja (intern)", "need": "Baja (investigación en nombre de jefe)", "timeline": "Baja (no especificó)"}, "action": "Enviar PDF con precios y prospectar en el largo plazo", "reason": "Es un lead bajo (intern) pero tiene intención de compra; calificar al jefe si posible."}]}