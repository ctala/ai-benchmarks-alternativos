# Muse Glimmer 30B — sales_outreach/lead_qualification

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 6.53 | quality: 6.67
- latency_total: 10.141s | tokens_per_second: 143.9
- input_tokens: 259 | output_tokens: 1459

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

**Lead 1 - Juan Perez**

```json
{
  "score": 5,
  "bant": {
    "budget": "No declarado. Startup de 5 personas, presupuesto probable limitado y no confirmado.",
    "authority": "Sí. CEO, es decision maker.",
    "need": "Sí. Interés explícito en automatizar soporte.",
    "timeline": "No definido. 'Viendo opciones' indica exploración sin urgencia."
  },
  "action": "Calificar / Nurture",
  "reason": "Alta autoridad y need claro, pero falta presupuesto y timeline. Requiere discovery para validar capacidad de pago y urgencia antes de pasar a Sales."
}
```

**Lead 2 - Ana Gomez**

```json
{
  "score": 9,
  "bant": {
    "budget": "Probable sí. Empresa de 200 empleados con Serie B reciente, capacidad de inversión.",
    "authority": "Sí. VP of Operations, rol de decisión/influencia clave.",
    "need": "Sí. Necesidad explícita de resolver el problema.",
    "timeline": "Sí, urgente. Necesita resolver antes de Q3."
  },
  "action": "SQL - Agendar demo inmediata",
  "reason": "BANT completo y fuerte. Alta autoridad, need validado, timeline definido y señales de presupuesto por funding. Prioridad alta para Sales."
}
```

**Lead 3 - Carlos Ruiz**

```json
{
  "score": 2,
  "bant": {
    "budget": "Desconocido.",
    "authority": "No. Intern de marketing sin poder de decisión.",
    "need": "Indirecto. Investiga por pedido del jefe, no necesidad propia confirmada.",
    "timeline": "No definido."
  },
  "action": "Nurture / Disqualify temporal",
  "reason": "Baja autoridad y sin señales de BANT. Útil como puerta de entrada. Enviar PDF de precios y pedir contacto con el decisor real."
}
```