# Tencent Hy4 preview — sales_outreach/lead_qualification

- model_id: `tencent/hy4-preview`
- success: True  | final: 4.21 | quality: 3.33
- latency_total: 9.273s | tokens_per_second: 52.6
- input_tokens: 286 | output_tokens: 488

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
    "lead": "Lead 1",
    "score": 6,
    "bant": {
      "budget": "Desconocido - no mencionó presupuesto",
      "authority": "Alta - es CEO (decision maker en startup de 5 personas)",
      "need": "Media/Alta - quiere automatizar soporte, alineado con posible solución",
      "timeline": "Desconocido - no urgencia declarada"
    },
    "action": "Nurturing por email / secuencia educativa",
    "reason": "Es decision maker con necesidad latente pero sin presupuesto ni timeline claro. Vale nutrir hasta que madure el interés."
  },
  {
    "lead": "Lead 2",
    "score": 9,
    "bant": {
      "budget": "Alto - acaban de levantar Serie B, tienen capital",
      "authority": "Alta - VP of Operations en empresa de 200 empleados",
      "need": "Alta - pidio demo post-webinar, problema claro",
      "timeline": "Alta - necesita resolver antes de Q3"
    },
    "action": "Agendar demo lo antes posible / pasar a ventas",
    "reason": "Cumple BANT casi completo: presupuesto, autoridad, necesidad y urgencia temporal. Lead caliente."
  },
  {
    "lead": "Lead 3",
    "score": 3,
    "bant": {
      "budget": "Desconocido / Bajo - es intern, no controla presupuesto",
      "authority": "Nula - intern, no es decision maker",
      "need": "Investigativa - jefe pidió investigar, no necesariamente comprar",
      "timeline": "Desconocido / Largo - fase de research"
    },
    "action": "Enviar PDF con precios y descalificar temporalmente",
    "reason": "Sin autoridad ni presupuesto propio; solo investiga. Se le atiende con material pero no se invierte tiempo de ventas."
  }
]
```