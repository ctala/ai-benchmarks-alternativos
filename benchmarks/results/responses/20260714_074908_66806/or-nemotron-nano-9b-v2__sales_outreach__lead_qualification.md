# Nemotron Nano 9B v2 — sales_outreach/lead_qualification

- model_id: `nvidia/nemotron-nano-9b-v2:free`
- success: True  | final: 4.36 | quality: 3.33
- latency_total: 29.367s | tokens_per_second: 43.5
- input_tokens: 260 | output_tokens: 1277
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando una evaluación detallada y acciones específicas para cada lead.

## Respuesta completa

```json
[
  {
    "score": 6,
    "bant": {
      "budget": "No",
      "authority": "Sí",
      "need": "Sí",
      "timeline": "No"
    },
    "action": "Seguimiento para dialogar sobre presupuesto y plazo",
    "reason": "Es CEO (autoridad) y menciona necesidad de automatización, pero no hay información sobre presupuesto ni urgencia."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Sí",
      "authority": "Sí",
      "need": "Sí",
      "timeline": "Sí"
    },
    "action": "Programar demo y seguimiento urgente",
    "reason": "VP de una empresa con reciente financiación (presupuesto), necesidad clara y plazo definido (antes de Q3)."
  },
  {
    "score": 3,
    "bant": {
      "budget": "No",
      "authority": "No",
      "need": "Parcial",
      "timeline": "No"
    },
    "action": "Proporcionar PDF de precios",
    "reason": "Es un intern sin autoridad ni presupuesto, pero hay interés en investigar herramientas (necesidad parcial)."
  }
]
```
