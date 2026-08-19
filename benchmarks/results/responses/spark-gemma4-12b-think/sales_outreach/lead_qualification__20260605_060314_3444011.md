# Gemma 4 12B (Spark llama-server, reasoning) — sales_outreach/lead_qualification

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 7.43 | quality: 8.28
- latency_total: 45.795s | tokens_per_second: 25.8
- input_tokens: 259 | output_tokens: 1181
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
[
  {
    "score": 6,
    "bant": {
      "budget": "No mencionado",
      "authority": "Alto (CEO)",
      "need": "Sí (Automatización de soporte)",
      "timeline": "No mencionado"
    },
    "action": "Discovery Call",
    "reason": "Tiene autoridad y una necesidad clara, pero falta calificar el presupuesto y la urgencia. Al ser una startup pequeña, el ciclo de venta podría ser rápido."
  },
  {
    "score": 10,
    "bant": {
      "budget": "Alto (Financiación Serie B)",
      "authority": "Alto (VP of Operations)",
      "need": "Sí (Solicitó demo)",
      "timeline": "Definido (Antes de Q3)"
    },
    "action": "Agendar Demo Inmediata",
    "reason": "Lead de alta calidad. Cumple con todos los criterios BANT: es decisora, tiene presupuesto confirmado por la ronda de inversión, tiene una necesidad activa y un plazo temporal claro."
  },
  {
    "score": 3,
    "bant": {
      "budget": "No mencionado",
      "authority": "Bajo (Interno)",
      "need": "Bajo (Investigación inicial)",
      "timeline": "No mencionado"
    },
    "action": "Marketing Automation / Enviar PDF",
    "reason": "No es el decisor (es un interno). Su objetivo es informativo. No es prioridad para ventas directas, pero es útil para nutrir la base de datos."
  }
]
```