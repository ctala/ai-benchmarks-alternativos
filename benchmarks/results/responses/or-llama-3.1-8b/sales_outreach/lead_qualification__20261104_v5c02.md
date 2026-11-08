# Llama 3.1 8B Instant — sales_outreach/lead_qualification

- model_id: `meta-llama/llama-3.1-8b-instruct`
- success: True  | final: 7.22 | quality: 6.67
- latency_total: 3.392s | tokens_per_second: 143.6
- input_tokens: 266 | output_tokens: 487

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

Aquí están las calificaciones de cada lead:

**Lead 1: Juan Perez**

* BANT:
	+ Budget: Desconocido (no mencionado)
	+ Authority: Posible (es CEO, pero no hay información adicional)
	+ Need: Moderado (dice que "estamos viendo opciones", no que tienen un problema urgente)
	+ Timeline: Desconocido (no mencionado)
* Score: 4
* Acción: "Contactar para obtener más información sobre presupuesto y necesidades específicas"
* Razón: Necesitamos saber si tienen presupuesto y qué tan urgente es resolver el problema antes de seguir adelante.

**Lead 2: Ana Gomez**

* BANT:
	+ Budget: Posible (empresa de 200 empleados y ha levantado Serie B, asumiendo que tienen presupuesto para inversiones)
	+ Authority: Probable (VP de Operaciones, lo que sugiere que tiene influencia en la toma de decisiones)
	+ Need: Alto (dice que "necesitamos resolver esto antes de Q3", lo que sugiere una necesidad urgente)
	+ Timeline: Alto (antes de Q3)
* Score: 8
* Acción: "Programar una llamada de ventas para discutir cómo podemos ayudar a resolver su problema"
* Razón: Ana Gomez tiene un claro problema que necesita resolver y parece tener la autoridad para tomar decisiones, por lo que es un lead caliente.

**Lead 3: Carlos Ruiz**

* BANT:
	+ Budget: Desconocido (no mencionado)
	+ Authority: Duda (es un intern de marketing, no está claro si tiene autoridad para tomar decisiones)
	+ Need: Bajo (su jefe le pidió "investigar herramientas de IA", no que tengan un problema urgente)
	+ Timeline: Desconocido (no mencionado)
* Score: 2
* Acción: "Contactar para preguntarle a su jefe si están interesados en una demo o una llamada de ventas"
* Razón: Carlos Ruiz no tiene autoridad para tomar decisiones y no hay una necesidad clara, por lo que es un lead frío.