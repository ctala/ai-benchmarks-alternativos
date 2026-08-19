# Sakana Namazu — sales_outreach/lead_qualification

- model_id: `sakana/sakana-namazu`
- success: True  | final: 4.02 | quality: 3.33
- latency_total: 8.384s | tokens_per_second: 244.3
- input_tokens: 279 | output_tokens: 2048

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
  "lead_1_juan_perez": {
    "score": 6,
    "bant": {
      "budget": "Desconocido. Startup de 5 personas con presupuesto probablemente limitado.",
      "authority": "Alto. Es el CEO (main decision maker).",
      "need": "Moderado. Reconoce el problema (automatizar soporte) pero está en fase exploratoria ('viendo opciones').",
      "timeline": "No definido. No menciona urgencia ni fecha de decisión."
    },
    "action": "Nurture / MQL. Enviar contenido de valor (case studies de startups similares) y retargeting. No asignar SDR aún.",
    "reason": "Tiene autoridad máxima, pero la necesidad es temprana y no hay indicios claros de budget ni timeline. Requiere educación antes de una conversación de ventas."
  },
 