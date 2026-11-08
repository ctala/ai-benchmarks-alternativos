# Nemotron 3.5 Lightning — sales_outreach/lead_qualification

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 3.013s | tokens_per_second: 181.6
- input_tokens: 264 | output_tokens: 547

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

{"leads": [{"name": "Juan Perez", "score": 3, "bant": {"budget": "Desconocido - no mencionó presupuesto en la primera interacción", "authority": "Alto - es CEO y toma decisiones estratégicas", "need": "Alto - menciona explícitamente la necesidad de automatizar soporte", "timeline": "Desconocido - no especifica urgencia"}, "action": "Nurturing - Agendar una llamada de descubrimiento para calibrar presupuesto y timeline", "reason": "Es el decisor (CEO) y tiene una necesidad clara (automatizar soporte), pero falta información crítica sobre presupuesto y urgencia. Al venir del blog, es un lead frío que requiere educación."}, {"name": "Ana Gomez", "score": 8, "bant": {"budget": "Alto - empresa reciente Serie B típicamente tiene presupuesto disponible para crecer", "authority": "Alto - VP of Operations es decision maker clave", "need": "Alto - menciona dolor específico y urgencia (resolver antes de Q3)", "timeline": "Alto - Q3 es un deadline claro"}, "action": "Close - Proponer demo inmediata y discutir contrato", "reason": "Tiene los 4 elementos BANT alineados: es la decision maker, tiene necesidad urgente antes de Q3, su empresa tiene presupuesto (Serie B) y tiene un timeline claro. El webinar demuestra interés activo."}, {"name": "Carlos Ruiz", "score": 2, "bant": {"budget": "Desconocido - intern buscando opciones, probable bajo presupuesto", "authority": "Nulo - es intern, no es decision maker, su jefe lo mandó", "need": "Medio - su jefe necesita IA, pero no está claro si es el problema que resolvemos", "timeline": "Desconocido - intern investigando, no hay deadline definido"}, "action": "Descartar - Enviar información general de precios y dejar nurturing para cuando haya un decision maker real", "reason": "Baja puntuación por falta de authority (es intern, no decide) y budget desconocido. Al pedir solo un PDF de precios, muestra interés táctico pero no estratégico. Se requiere un decision maker real para calificar adecuadamente."}], "summary": "Ana Gomez es el lead caliente listo para cerrar, Juan Perez es una oportunidad calificada que necesita nurturing, y Carlos Ruiz es un lead bajo que requiere filtración a decision maker."}