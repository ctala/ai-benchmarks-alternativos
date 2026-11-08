# MiMo V2.6 Flash — sales_outreach/lead_qualification

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 13.14s | tokens_per_second: 40.4
- input_tokens: 266 | output_tokens: 531

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
      "lead": "Juan Perez",
      "score": 6,
      "bant": {
        "budget": "No mencionado, pero es CEO de startup con 5 personas - presupuesto probablemente limitado pero decisión rápida",
        "authority": "Alta - es CEO, decision maker directo",
        "need": "Claro - está viendo opciones para automatizar soporte",
        "timeline": "Indefinido - 'estamos viendo opciones' sugiere fase temprana de investigación"
      },
      "action": "Nurturing - agendar llamada de descubrimiento",
      "reason": "Alta authority y need claro, pero falta budget y timeline. Llegó vía blog (inbound frío). Convertir a llamada para calificar presupuesto y urgencia. Score 6."
    },
    {
      "lead": "Ana Gomez",
      "score": 9,
      "bant": {
        "budget": "Alta probabilidad - empresa acaba de levantar Serie B, tiene capital fresco",
        "authority": "Alta - VP of Operations, probablemente dueña del presupuesto operativo",
        "need": "Claro - pidió demo activamente tras webinar",
        "timeline": "Explícito - 'antes de Q3', fecha comprometida"
      },
      "action": "Inmediato - agendar demo y asignar AE hoy",
      "reason": "BANT completo: presupuesto (Serie B), authority (VP), need (demo solicitada), timeline (Q3). Lead caliente, prioridad máxima. Score 9."
    },
    {
      "lead": "Carlos Ruiz",
      "score": 2,
      "bant": {
        "budget": "Desconocido - no es su rol",
        "authority": "Baja - intern, no decide ni influye en compra",
        "need": "Indirecto - su jefe pidió investigar, pero Carlos no es el buyer",
        "timeline": "Vago - 'investigar herramientas' sin urgencia"
      },
      "action": "Enviar PDF pero intentar identificar al jefe/buyer real",
      "reason": "Gatekeeper/investigador, no comprador. Baja authority. Útil solo si logramos mapear al decisor real. Score 2."
    }
  ]
}
```