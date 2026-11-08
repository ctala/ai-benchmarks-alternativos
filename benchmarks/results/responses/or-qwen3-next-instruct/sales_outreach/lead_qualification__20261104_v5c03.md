# Qwen 3-Next 80B Instruct — sales_outreach/lead_qualification

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 5.18 | quality: 3.33
- latency_total: 0.974s | tokens_per_second: 157.1
- input_tokens: 266 | output_tokens: 153

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

{
  "score": 8,
  "bant": {
    "budget": "Alta probabilidad (acaban de levantar Serie B)",
    "authority": "Sí, VP de Operations es decision maker",
    "need": "Sí, necesita resolver un problema específico de operaciones con plazo claro",
    "timeline": "Sí, necesita solución antes de Q3 (urgente)"
  },
  "action": "Agendar demo inmediata",
  "reason": "Ana Gomez cumple con todos los criterios BANT: tiene autoridad, presupuesto confirmado por la ronda de financiación, necesidad clara y plazo urgente. Es el lead más calificado."
}