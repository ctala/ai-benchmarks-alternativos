# Llama 4 Maverick — sales_outreach/lead_qualification

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 6.79 | quality: 6.67
- latency_total: 6.699s | tokens_per_second: 75.8
- input_tokens: 247 | output_tokens: 508

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

A continuación, te proporciono la evaluación de cada lead según el framework BANT y la acción recomendada:

### Lead 1: Juan Perez

* Budget: Desconocido (no mencionó presupuesto)
* Authority: Alta (es CEO)
* Need: Posible (están viendo opciones para automatizar soporte)
* Timeline: Desconocido (no dio plazos)

Evaluación: {"score": 6, "bant": {"budget": "Desconocido", "authority": "Alta", "need": "Posible", "timeline": "Desconocido"}, "action": "Responder con preguntas adicionales sobre presupuesto y necesidades específicas", "reason": "Tiene autoridad, pero falta información sobre presupuesto y plazos. Es una startup pequeña, lo que podría indicar un presupuesto limitado."}

### Lead 2: Ana Gomez

* Budget: Probablemente disponible (su empresa acaba de levantar Serie B, lo que sugiere recursos financieros)
* Authority: Alta (es VP of Operations)
* Need: Alta (necesitan resolver un problema antes de Q3)
* Timeline: Clara (antes de Q3, lo que da un plazo específico)

Evaluación: {"score": 9, "bant": {"budget": "Probablemente disponible", "authority": "Alta", "need": "Alta", "timeline": "Clara"}, "action": "Programar una demo o seguir la conversación para entender mejor sus necesidades y presentar soluciones personalizadas", "reason": "Tiene autoridad, necesidad clara, y probablemente tenga presupuesto. El plazo es claro, lo que sugiere urgencia."}

### Lead 3: Carlos Ruiz

* Budget: Desconocido (no tiene autoridad para decidir)
* Authority: Baja (es un intern de marketing)
* Need: Posible (su jefe está investigando herramientas de IA)
* Timeline: Desconocido (no dio plazos)

Evaluación: {"score": 3, "bant": {"budget": "Desconocido", "authority": "Baja", "need": "Posible", "timeline": "Desconocido"}, "action": "Responder con un PDF de precios y tratar de entender mejor su rol y si puede conectar con el decisor", "reason": "No tiene autoridad para tomar decisiones. Aunque puede ser un buen punto de entrada para llegar al decisor, la prioridad debería ser baja."}

Estas calificaciones y acciones recomendadas están basadas en la información proporcionada y el framework BANT.