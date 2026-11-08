# MiniMax M2.5 — sales_outreach/lead_qualification

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 6.8 | quality: 6.67
- latency_total: 6.612s | tokens_per_second: 107.5
- input_tokens: 249 | output_tokens: 711

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
    "lead": "Juan Perez - CEO startup 5 personas",
    "score": 5,
    "bant": {
      "budget": "No mencionado. Startup pequeña = presupuesto limitado probable",
      "authority": "Alto - CEO tiene poder de decisión total",
      "need": "Medio - Está evaluando opciones de automatización de soporte",
      "timeline": "Bajo - No mencionó urgencia"
    },
    "action": "Nurture",
    "reason": "Buena autoridad y necesidad, pero falta desarrollo en presupuesto y timeline. Necesita más cualificación antes de pasar a ventas."
  },
  {
    "lead": "Ana Gomez - VP Operations empresa 200 empleados",
    "score": 9,
    "bant": {
      "budget": "Alto - Serie B reciente = capital disponible",
      "authority": "Alto - VP Operations puede aprobar decisiones operativas",
      "need": "Alto - Problema claro que necesita resolverse",
      "timeline": "Alto - Deadline Q3 = urgencia concreta"
    },
    "action": "Prioridad alta - Contactar inmediatamente",
    "reason": "Perfil BANT perfecto. Tiene presupuesto, autoridad, necesidad y timeline definido. Listo para demo y propuesta comercial."
  },
  {
    "lead": "Carlos Ruiz - Intern de marketing",
    "score": 2,
    "bant": {
      "budget": "No mencionado",
      "authority": "Muy bajo - Intern no tiene poder de decisión",
      "need": "Bajo - Investigación por cuenta de otro, no necesidad propia",
      "timeline": "No mencionado"
    },
    "action": "Descartar o derivar",
    "reason": "No es decision maker. Necesita encontrar al jefe que pidió la información para cualificar properly. Enviar PDF pero no invertir tiempo en follow-up activo."
  }
]
```