# Qwen 3.8 27B — sales_outreach/lead_qualification

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 3.55 | quality: 3.33
- latency_total: 79.557s | tokens_per_second: 23.7
- input_tokens: 298 | output_tokens: 1885

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



[
  {
    "score": 4,
    "bant": {
      "budget": "No mencionado; startup pequeña, presupuesto probablemente limitado o por definir.",
      "authority": "Alta: es CEO y puede decidir.",
      "need": "Clara: quiere automatizar el soporte.",
      "timeline": "Baja/incierta: solo está viendo opciones."
    },
    "action": "Nurturing: enviar casos de éxito para startups y agendar llamada para definir presupuesto, caso de uso y timeline.",
    "reason": "Tiene autoridad y necesidad, pero falta presupuesto y urgencia; es lead temprano con potencial si se valida el caso."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto/verificable: empresa de 200 empleados con Serie B recién levantada.",
      "authority": "Alta: VP of Operations, probablemente decision maker o influyente clave.",
      "need": "Alta: pidió demo y expresa necesidad de resolver un problema.",
      "timeline": "Alta: necesita resolver antes de Q3."
    },
    "action": "Priorizar: agendar demo inmediata con sales senior y preparar propuesta para antes de Q3.",
    "reason": "Cumple BANT con fuerte urgencia, presupuesto probable y autoridad; es lead calificado de alta prioridad."
  },
  {
    "score": 2,
    "bant": {
      "budget": "No mencionado; intern sin control de presupuesto.",
      "authority": "Baja: intern de marketing; el decision maker es su jefe.",
      "need": "Baja/vaga: investigar herramientas de IA, sin problema específico claro.",
      "timeline": "No mencionado."
    },
    "action": "Enviar PDF de precios y pedir introducción al decision maker; mantener en nurturing con contenido educativo.",
    "reason": "Es lead de bajo valor operativo: poca autoridad, necesidad genérica y sin timeline; solo se puede avanzar si se conecta con el jefe."
  }
]