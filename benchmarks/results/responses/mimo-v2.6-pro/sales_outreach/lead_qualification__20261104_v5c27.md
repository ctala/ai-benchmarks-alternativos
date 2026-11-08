# MiMo V2.6 Pro — sales_outreach/lead_qualification

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 8.82 | quality: 10.0
- latency_total: 17.536s | tokens_per_second: 32.8
- input_tokens: 266 | output_tokens: 575

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

{"leads": [{"name": "Juan Perez", "score": 5, "bant": {"budget": "No mencionado. Startup de 5 personas sugiere presupuesto limitado.", "authority": "CEO de startup pequeña, probablemente es el decision maker.", "need": "Interés en automatizar soporte, pero está en fase de exploración ('viendo opciones').", "timeline": "Sin timeline claro. Solo explorando."}, "action": "Nurture - Enviar contenido educativo y agendar llamada de descubrimiento de bajo compromiso.", "reason": "Autoridad clara (CEO) y necesidad alineada, pero sin presupuesto definido ni urgencia. Startup pequeña puede tener capacidad de compra limitada. Vale la pena cultivar pero no invertir esfuerzo de venta pesado todavía."}, {"name": "Ana Gomez", "score": 9, "bant": {"budget": "Alto. Empresa de 200 empleados con Serie B reciente = capital disponible.", "authority": "VP of Operations = fuerte influencia en decisiones operativas, probablemente decision maker o co-decision maker.", "need": "Necesidad explícita y urgente ('necesitamos resolver esto').", "timeline": "Timeline claro y urgente: antes de Q3."}, "action": "Contactar inmediatamente - Agendar demo y preparar propuesta comercial.", "reason": "Lead calificado en los 4 criterios BANT. Alto poder adquisitivo, autoridad real, necesidad explícita y urgencia con deadline definido. Prioridad máxima."}, {"name": "Carlos Ruiz", "score": 3, "bant": {"budget": "Desconocido. Solo pide PDF de precios, probablemente investigación inicial.", "authority": "Ninguna. Es un intern haciendo research para su jefe.", "need": "Necesidad no validada. Solo 'investigar herramientas de IA' sin problema específico.", "timeline": "Sin timeline claro."}, "action": "Calificar y escalar - Enviar PDF pero pedir intro con su jefe / decision maker real.", "reason": "Sin autoridad, sin presupuesto confirmado, necesidad vaga y sin timeline. Es un gatekeeper o investigador, no un comprador. Solo vale la pena si se puede escalar al verdadero decision maker."}], "summary": "Ana Gomez es el lead prioritario y debe atenderse hoy. Juan Perez es un lead medio que requiere nurturing. Carlos Ruiz es lead de baja calificación — solo útil como puerta de entrada hacia su jefe."}