# Gemini 2.5 Flash Lite — sales_outreach/lead_qualification

- model_id: `google/gemini-2.5-flash-lite`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 2.046s | tokens_per_second: 214.1
- input_tokens: 243 | output_tokens: 438
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para un emprendedor, proporcionando una evaluación detallada de cada lead basada en criterios BANT.

## Respuesta completa

```json
[
  {
    "score": 7,
    "bant": {
      "budget": "Desconocido",
      "authority": "Alto (CEO)",
      "need": "Alto (buscando activamente automatización)",
      "timeline": "Desconocido"
    },
    "action": "Contactar para calificar presupuesto y timeline",
    "reason": "Juan es CEO, lo que le da autoridad. La mención de 'ver opciones para automatizar' indica una necesidad clara. Sin embargo, el presupuesto y el timeline son desconocidos y deben ser calificados."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto (Serie B)",
      "authority": "Alto (VP of Operations)",
      "need": "Alto (necesidad de resolver antes de Q3)",
      "timeline": "Medio-Alto (antes de Q3)"
    },
    "action": "Agendar reunión de calificacion y presentar propuesta",
    "reason": "Ana tiene autoridad como VP of Operations, una necesidad clara con un timeline definido (antes de Q3) y el hecho de que su empresa levantó Serie B sugiere un presupuesto disponible. Es un lead muy calificado."
  },
  {
    "score": 2,
    "bant": {
      "budget": "Desconocido (probablemente bajo o nulo)",
      "authority": "Bajo (intern)",
      "need": "Bajo (investigación inicial, no necesidad directa)",
      "timeline": "Desconocido (probablemente bajo)"
    },
    "action": "Enviar material informativo general y monitorear",
    "reason": "Carlos es un intern con poca autoridad y su necesidad parece ser de investigación inicial, no una necesidad inmediata. No hay indicación de presupuesto. Es mejor enviarle información general y ver si el lead evoluciona a través de otros canales."
  }
]
```