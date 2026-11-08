# Qwen3-Coder-Next (OpenRouter FP8) — sales_outreach/lead_qualification

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 4.45 | quality: 3.33
- latency_total: 5.341s | tokens_per_second: 93.6
- input_tokens: 266 | output_tokens: 500

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
  "leads": [
    {
      "score": 6,
      "bant": {
        "budget": "No especificado, pero startup pequeña puede tener limitado; posible acceso a fondos tempranos.",
        "authority": "CEO = decision maker, tiene autoridad para comprar.",
        "need": "Tiene el problema (automatizar soporte) y está en fase exploratoria.",
        "timeline": "Sin plazo claro; 'viendo opciones' sugiere etapa inicial de investigación."
      },
      "action": "Nurture (follow-up con caso de uso y pricing)",
      "reason": "Buena autoridad y necesidad identificadas, pero falta presupuesto y timeline definidos. Vale la pena educar y avanzar su pipeline."
    },
    {
      "score": 9,
      "bant": {
        "budget": "Empresa acaba de levantar Serie B → presupuesto disponible y prioridad en crecimiento.",
        "authority": "VP of Operations = decision maker clave en operaciones y adopción de herramientas.",
        "need": "Problema claro y urgente: necesitan resolverlo antes de Q3.",
        "timeline": "Muy claro: 'antes de Q3' → plazo concreto y cercano."
      },
      "action": "Demo inmediata + follow-up dentro de 48h",
      "reason": "Lead altamente calificado: BANT completo, urgencia y capacidad de compra. Alta probabilidad de cierre rápido."
    },
    {
      "score": 3,
      "bant": {
        "budget": "Solicita PDF con precios → interés en costo, pero no indica presupuesto autorizado.",
        "authority": "Intern no es decision maker; solo investiga bajo supervisión.",
        "need": "Solo tiene una tarea delegada ('investigar herramientas'), no un problema propio.",
        "timeline": "Sin plazo definido; parece tarea de investigación genérica."
      },
      "action": "De-qualify o reasignar a dueño del lead (su jefe)",
      "reason": "Falta autoridad y necesidad real. El lead no está en estado para avanzar. Mejor enviarle contenido y pedir que lo revise su jefe si tiene interés."
    }
  ]
}