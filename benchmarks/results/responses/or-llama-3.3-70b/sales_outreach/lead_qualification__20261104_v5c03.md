# Llama 3.3 70B — sales_outreach/lead_qualification

- model_id: `meta-llama/llama-3.3-70b-instruct`
- success: True  | final: 9.25 | quality: 10.0
- latency_total: 5.265s | tokens_per_second: 89.1
- input_tokens: 265 | output_tokens: 469

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

Aquí te dejo la evaluación de los 3 leads:

**Lead 1: Juan Perez**
```json
{
  "score": 6,
  "bant": {
    "budget": "Desconocido",
    "authority": "Alto (CEO)",
    "need": "Interés en automatizar soporte",
    "timeline": "No especificado"
  },
  "action": "Enviar correo electrónico de follow-up para obtener más información",
  "reason": "Aunque Juan es el CEO y muestra interés en automatizar el soporte, no hay información sobre presupuesto y no hay una fecha límite clara para la implementación."
}
```

**Lead 2: Ana Gomez**
```json
{
  "score": 9,
  "bant": {
    "budget": "Probablemente alto (Serie B)",
    "authority": "Alto (VP of Operations)",
    "need": "Necesidad urgente de resolver un problema",
    "timeline": "Antes de Q3 (fecha límite clara)"
  },
  "action": "Agendar demo y seguimiento personalizado",
  "reason": "Ana es una persona con autoridad en la empresa, muestra una necesidad urgente de resolver un problema y hay una fecha límite clara para la implementación. La empresa acaba de levantar Serie B, lo que sugiere que tienen presupuesto para invertir en soluciones."
}
```

**Lead 3: Carlos Ruiz**
```json
{
  "score": 2,
  "bant": {
    "budget": "Desconocido",
    "authority": "Bajo (intern de marketing)",
    "need": "Investigación general",
    "timeline": "No especificado"
  },
  "action": "Enviar respuesta automática con información general",
  "reason": "Carlos no tiene autoridad para tomar decisiones y solo está investigando herramientas de IA por solicitud de su jefe. No hay una necesidad urgente o una fecha límite clara para la implementación."
}
```
Espero que esto te sea útil. ¡Si necesitas algo más, no dudes en preguntar!