# DeepSeek V3 — sales_outreach/lead_qualification

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 4.32 | quality: 3.33
- latency_total: 13.566s | tokens_per_second: 34.3
- input_tokens: 261 | output_tokens: 466

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
[
  {
    "score": 7,
    "bant": {
      "budget": "No mencionado, pero como CEO de startup probablemente tiene control presupuestario",
      "authority": "Alto - CEO es decision maker definitivo",
      "need": "Claro - busca automatizar soporte",
      "timeline": "Implícito pero no urgente ('estamos viendo opciones')"
    },
    "action": "Calificado para seguimiento inmediato por ventas",
    "reason": "CEO con necesidad clara y autoridad total. Aunque timeline no es urgente y budget no mencionado, el rol y necesidad justifican seguimiento proactivo."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto - empresa con Serie B reciente tiene capacidad financiera",
      "authority": "Alto - VP of Operations tiene influencia significativa",
      "need": "Claro - 'necesitamos resolver esto' indica problema identificado",
      "timeline": "Muy claro - 'antes de Q3' establece deadline específico"
    },
    "action": "Calificado como lead caliente - programar demo cuanto antes",
    "reason": "Todas las dimensiones BANT están presentes: necesidad clara, autoridad, timeline específico y capacidad presupuestaria demostrada por el funding reciente."
  },
  {
    "score": 2,
    "bant": {
      "budget": "No evaluado - intern sin información presupuestaria",
      "authority": "Bajo - intern sin poder de decisión",
      "need": "Vago - 'investigar herramientas' no indica problema concreto",
      "timeline": "No especificado"
    },
    "action": "Descalificar para ventas - enviar materiales educativos y PDF genérico",
    "reason": "Intern sin autoridad ni necesidad clara. Solicitud de precios sin contexto sugiere investigación temprana, no compra inminente. Mejor nutrir con contenido educativo."
  }
]
```