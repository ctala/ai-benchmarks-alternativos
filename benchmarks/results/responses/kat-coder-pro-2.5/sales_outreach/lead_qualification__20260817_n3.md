# KAT Coder Pro v2.5 — sales_outreach/lead_qualification

- model_id: `kwaipilot/kat-coder-pro-v2.5`
- success: True  | final: 6.59 | quality: 6.67
- latency_total: 7.333s | tokens_per_second: 105.4
- input_tokens: 260 | output_tokens: 773

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



[{"score": 6, "bant": {"budget": "No mencionado", "authority": "Alta (CEO)", "need": "Si - automatizar soporte", "timeline": "No especificado"}, "action": "Nurturing - enviar caso de uso y agendar llamada de descubrimiento", "reason": "Es decision maker con necesidad clara, pero no hay urgencia ni presupuesto confirmado. Startup pequena puede tener budget limitado."}, {"score": 9, "bant": {"budget": "Alto (Serie B reciente)", "authority": "Alta (VP Operations)", "need": "Si - implicito en solicitud de demo", "timeline": "Urgente - antes de Q3"}, "action": "Prioritario - agendar demo inmediatamente y preparar propuesta", "reason": "Cumple BANT completo: decision maker, presupuesto disponible, necesidad activa y timeline definido. Lead caliente listo para venta."}, {"score": 2, "bant": {"budget": "Desconocido", "authority": "Baja (Intern, no decision maker)", "need": "Indirecto - investigacion solicitada por jefe", "timeline": "No especificado"}, "action": "Enviar PDF solicitado y capturar datos del decision maker real", "reason": "No es decision maker ni tiene autoridad de compra. Solo esta recolectando informacion. Bajo potencial de conversion inmediata."}]