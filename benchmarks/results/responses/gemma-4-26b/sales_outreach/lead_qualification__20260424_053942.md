# Gemma 4 26B MoE (3.8B activos) — sales_outreach/lead_qualification

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 7.52 | quality: 9.48
- latency_total: 10.202s | tokens_per_second: 43.9
- input_tokens: 277 | output_tokens: 448
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
[
  {
    "lead": "Juan Perez",
    "score": 4,
    "bant": {
      "budget": "Desconocido. No lo mencionó.",
      "authority": "Alto. Es el CEO de la startup.",
      "need": "Medio. Tiene el interés de automatizar soporte.",
      "timeline": "Bajo. Está en fase de exploración ('viendo opciones')."
    },
    "action": "Nurturing / Lead Magnet",
    "reason": "Es un decision maker, pero no hay urgencia ni presupuesto claro. Se debe mantener en flujo de contenido para educarlo."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Alto. Empresa en fase Serie B (capital disponible).",
      "authority": "Alto. VP of Operations es decision maker o influenciador clave.",
      "need": "Alto. Problema identificado y validado tras webinar.",
      "timeline": "Alto. Fecha límite clara (antes de Q3)."
    },
    "action": "Sales Qualified Lead (SQL) - Agendar Demo Inmediata",
    "reason": "Cumple con casi todos los criterios BANT. Tiene capacidad financiera, autoridad, necesidad clara y un plazo definido."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido. Solo pide precios.",
      "authority": "Bajo. Es un intern (investigador, no decisor).",
      "need": "Medio. Tiene una tarea asignada de investigación.",
      "timeline": "Desconocido."
    },
    "action": "Low Touch / Automated Response",
    "reason": "Es un perfil de investigación sin poder de decisión. Se le debe enviar el PDF solicitado automáticamente para no perder tiempo de ventas, pero no requiere atención humana inmediata."
  }
]
```