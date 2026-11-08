# Grok 4.3 — sales_outreach/lead_qualification

- model_id: `x-ai/grok-4.3`
- success: True  | final: 4.42 | quality: 3.33
- latency_total: 4.345s | tokens_per_second: 51.1
- input_tokens: 420 | output_tokens: 222

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

{"score": 6, "bant": {"budget": "No mencionado", "authority": "CEO (alta)", "need": "Automatizar soporte", "timeline": "No mencionado"}, "action": "Follow-up", "reason": "Autoridad alta pero falta info de presupuesto y timeline"}
{"score": 9, "bant": {"budget": "Empresa levantó Serie B (presupuesto probable)", "authority": "VP of Operations (alta)", "need": "Resolver problema antes de Q3", "timeline": "Q3 (pronto)"}, "action": "Priorizar", "reason": "BANT completo: presupuesto implícito, autoridad alta, necesidad clara y timeline definido"}
{"score": 2, "bant": {"budget": "Pide precios (puede indicar interés)", "authority": "Intern (baja)", "need": "Investigación (no decisión)", "timeline": "No mencionado"}, "action": "Descartar", "reason": "Autoridad baja, rol de investigación, no es decision maker"}