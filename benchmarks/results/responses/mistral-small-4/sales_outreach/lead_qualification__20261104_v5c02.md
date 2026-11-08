# Mistral Small 4 — sales_outreach/lead_qualification

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 4.85 | quality: 3.33
- latency_total: 2.295s | tokens_per_second: 154.3
- input_tokens: 265 | output_tokens: 354

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
    "score": 4,
    "bant": {
      "budget": "No mencionado",
      "authority": "No es claro (posiblemente no decisor)",
      "need": "Sí (automatizar soporte)",
      "timeline": "No claro (vaga)"
    },
    "action": "Contactar para profundizar",
    "reason": "Lead con necesidad pero falta claridad en autoridad y presupuesto. Llegó por blog (bajo interés inicial). Necesita más cualificación."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Sí (empresa con Serie B)",
      "authority": "Sí (VP of Operations)",
      "need": "Sí (resolver antes de Q3)",
      "timeline": "Sí (urgencia Q3)"
    },
    "action": "Priorizar demo y seguimiento rápido",
    "reason": "Lead altamente calificado: decisor, presupuesto, necesidad urgente y clara. Alta probabilidad de cierre."
  },
  {
    "score": 3,
    "bant": {
      "budget": "No (intern, depende de su jefe)",
      "authority": "No (intern, no decisor)",
      "need": "Sí (task asignada)",
      "timeline": "No claro (pide PDF genérico)"
    },
    "action": "Responder con PDF pero priorizar contacto con el jefe",
    "reason": "Lead no decisor y sin presupuesto propio. Útil solo como puerta de entrada a la empresa, pero requiere escalar."
  }
]
```