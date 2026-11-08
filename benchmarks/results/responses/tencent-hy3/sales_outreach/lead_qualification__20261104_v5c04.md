# Tencent Hy3 — sales_outreach/lead_qualification

- model_id: `tencent/hy3`
- success: True  | final: 4.28 | quality: 3.33
- latency_total: 11.637s | tokens_per_second: 45.7
- input_tokens: 291 | output_tokens: 532

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
      "budget": "No mencionado. Startup pequeña de 5 personas, presupuesto probablemente limitado o indefinido.",
      "authority": "Alto. Es CEO, decisor final o fuertemente influyente.",
      "need": "Medio. Menciona interés en automatizar soporte, problema alineado pero en fase exploratoria.",
      "timeline": "No especificado. Sin urgencia clara."
    },
    "action": "Nutrir con contenido educativo y agendar llamada de descubrimiento",
    "reason": "CEO con autoridad y necesidad incipiente, pero sin presupuesto ni timeline definidos. Llegó por blog, es lead temprano."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto. Empresa con Serie B reciente, capital disponible.",
      "authority": "Alto. VP of Operations, dueño del proceso operativo y decisor/influyente clave.",
      "need": "Alto. Busca solución activa post-webinar y pide demo.",
      "timeline": "Alto. Necesita resolver antes de Q3 (urgencia clara)."
    },
    "action": "Agendar demo inmediata y preparar propuesta comercial",
    "reason": "Lead calificado en los 4 ejes BANT: presupuesto por Serie B, autoridad real, necesidad confirmada y urgencia antes de Q3."
  },
  {
    "score": 2,
    "bant": {
      "budget": "Desconocido. Solo pide PDF de precios.",
      "authority": "Bajo. Intern, no decisor.",
      "need": "Bajo/Medio. Investigación mandada por jefe, no dolor propio.",
      "timeline": "No mencionado."
    },
    "action": "Enviar material y solicitar contacto con el decisor (su jefe)",
    "reason": "Intern en modo investigación, sin autoridad ni presupuesto. Útil como puerta de entrada pero poco calificado."
  }
]
```