# GLM 5.3 Flash — sales_outreach/lead_qualification

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 24.35s | tokens_per_second: 76.1
- input_tokens: 255 | output_tokens: 1854

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

```json
{
  "leads": [
    {
      "lead": "Juan Perez (CEO, startup 5 personas)",
      "score": 5,
      "bant": {
        "budget": "Desconocido — no lo mencionó; empresa de 5 personas sugiere presupuesto probablemente limitado",
        "authority": "Alto — es CEO, decision maker directo",
        "need": "Medio — problema identificado (automatizar soporte), pero lenguaje exploratorio ('viendo opciones')",
        "timeline": "Desconocido — sin señales de urgencia"
      },
      "action": "Agendar llamada de descubrimiento de 15-20 min para cualificar presupuesto y timeline. No invertir tiempo de un AE senior todavía.",
      "reason": "Tiene autoridad y una necesidad plausible, pero llegó vía blog (intent bajo-medio) y no dio señales de presupuesto ni urgencia. Lead a cualificar, no a cerrar."
    },
    {
      "lead": "Ana Gomez (VP Operations, empresa 200 empleados)",
      "score": 9,
      "bant": {
        "budget": "Alto — acaban de levantar Serie B, funding reciente disponible",
        "authority": "Alto — VP of Operations en empresa de 200 personas, probablemente decision maker o influyente clave",
        "need": "Explícito — 'necesitamos resolver esto', problema confirmado",
        "timeline": "Explícito y cercano — 'antes de Q3'"
      },
      "action": "Prioridad máxima: agendar la demo esta semana o la próxima, asignar AE senior, y preparar material para posible buying committee (CFO/CEO aprobarán gasto post-Serie B).",
      "reason": "Cumple los 4 criterios BANT con señales fuertes: presupuesto reciente, autoridad, necesidad explícita, timeline definido y alta intención (pidió demo tras webinar). Hot lead."
    },
    {
      "lead": "Carlos Ruiz (intern de marketing)",
      "score": 2,
      "bant": {
        "budget": "Nulo — un intern no maneja presupuesto",
        "authority": "Nulo — él mismo dice que su jefe decidió delegar la investigación",
        "need": "Vago — 'investigar herramientas de IA' no revela un problema concreto ni fit con nuestra solución",
        "timeline": "Desconocido — sin señales"
      },
      "action": "Enviar el PDF de precios sin fricción, sumarlo a secuencia de nurturing automatizada, y en el follow-up pedir que conecte al decisor si hay interés real de su jefe.",
      "reason": "Sin autoridad ni presupuesto, necesidad indefinida y comportamiento de investigación pasiva (solo quiere un PDF). Bajo esfuerzo de sales, pero puede ser puerta de entrada al decisor si se cultiva bien."
    }
  ]
}
```