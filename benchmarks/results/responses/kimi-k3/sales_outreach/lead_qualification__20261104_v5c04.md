# Kimi K3 — sales_outreach/lead_qualification

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 8.15 | quality: 10.0
- latency_total: 21.535s | tokens_per_second: 27.7
- input_tokens: 296 | output_tokens: 596

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

Aquí está la evaluación BANT de los 3 leads:

```json
[
  {
    "lead": "Juan Perez",
    "score": 5,
    "bant": {
      "budget": "desconocido - startup early-stage, no mencionó presupuesto",
      "authority": "alto - es CEO, decision maker directo",
      "need": "medio - está explorando, no hay urgencia expresada",
      "timeline": "indefinido - 'viendo opciones' sugiere etapa temprana de research"
    },
    "action": "nurturing",
    "reason": "Tiene autoridad pero está en fase exploratoria. Startup pequeña puede tener budget limitado. Enviar contenido educativo y hacer seguimiento en 2-3 semanas."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "alto - Serie B reciente indica capital disponible",
      "authority": "alto - VP of Operations, decisor o influencer fuerte",
      "need": "alto - pidió demo activamente, problema identificado",
      "timeline": "urgente - deadline explícito antes de Q3"
    },
    "action": "asignar a sales inmediatamente",
    "reason": "Lead caliente con todos los criterios BANT positivos. Empresa con funding, timeline claro, y engagement alto (webinar + demo request). Prioridad máxima."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 3,
    "bant": {
      "budget": "desconocido - no tiene visibilidad ni control del presupuesto",
      "authority": "nulo - es intern, solo hace research delegado",
      "need": "indirecto - la necesidad existe pero él no la articula",
      "timeline": "desconocido - sin indicadores de urgencia"
    },
    "action": "enviar PDF + intentar llegar al jefe",
    "reason": "No es decision maker ni tiene influencia real. Enviar el PDF solicitado pero incluir CTA para que su jefe agende una llamada. No invertir tiempo de sales directo."
  }
]
```

**Resumen de prioridades:**
1. 🔥 **Ana (9/10)** → Contactar hoy mismo
2. 📧 **Juan (5/10)** → Secuencia de nurturing
3. 📄 **Carlos (3/10)** → Material self-service + intento de reach al decision maker