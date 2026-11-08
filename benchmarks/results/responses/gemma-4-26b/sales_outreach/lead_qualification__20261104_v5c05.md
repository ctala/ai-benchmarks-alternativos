# Gemma 4 26B MoE (3.8B activos) — sales_outreach/lead_qualification

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 4.36 | quality: 3.33
- latency_total: 11.088s | tokens_per_second: 34.6
- input_tokens: 262 | output_tokens: 384

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
    "score": 5,
    "bant": {
      "budget": "Desconocido",
      "authority": "Alto (CEO)",
      "need": "Alto (Automatización de soporte)",
      "timeline": "Desconocido (Fase de exploración)"
    },
    "action": "Nurturing / Calificación secundaria",
    "reason": "Es un decision maker con una necesidad clara, pero el tamaño de la empresa es pequeño y no hay urgencia ni presupuesto definido. Se debe mantener en flujo de contenido para cuando esté listo."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto (Serie B recién levantada)",
      "authority": "Alto (VP of Operations)",
      "need": "Alto (Solicitó demo)",
      "timeline": "Definido (Antes de Q3)"
    },
    "action": "Sales Priority / Demo inmediata",
    "reason": "Lead ideal. Tiene autoridad, una necesidad validada, un plazo temporal claro y capacidad financiera demostrada por la reciente ronda de inversión."
  },
  {
    "score": 2,
    "bant": {
      "budget": "Desconocido (Solo pide precios)",
      "authority": "Bajo (Intern)",
      "need": "Medio (Investigación)",
      "timeline": "Desconocido"
    },
    "action": "Automated Response / Low Touch",
    "reason": "No tiene poder de decisión. Es un perfil de investigación que busca información de bajo costo (PDF). Se le debe enviar material automático para no perder tiempo de ventas humanas."
  }
]
```