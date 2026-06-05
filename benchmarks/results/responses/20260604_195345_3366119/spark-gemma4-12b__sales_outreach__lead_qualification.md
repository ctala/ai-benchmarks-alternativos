# Gemma 4 12B (Spark llama-server Q4_K_M) — sales_outreach/lead_qualification

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 7.47 | quality: 8.28
- latency_total: 13.944s | tokens_per_second: 25.6
- input_tokens: 261 | output_tokens: 357
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
[
  {
    "score": 6,
    "bant": {
      "budget": "No mencionado",
      "authority": "Sí (CEO)",
      "need": "Sí (Automatizar soporte)",
      "timeline": "No mencionado"
    },
    "action": "Nurturing / Discovery Call",
    "reason": "Es un decisor clave (CEO) con una necesidad clara, pero falta información sobre presupuesto y urgencia. Requiere una llamada de descubrimiento para calificar el presupuesto."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto (Serie B)",
      "authority": "Sí (VP of Operations)",
      "need": "Sí (Eficiencia operativa)",
      "timeline": "Sí (Antes de Q3)"
    },
    "action": "Demo / Sales Presentation",
    "reason": "Lead de alta calidad. Tiene autoridad, presupuesto confirmado por la ronda de inversión, una necesidad clara y un deadline definido. Prioridad alta."
  },
  {
    "score": 3,
    "bant": {
      "budget": "Desconocido",
      "authority": "No (Intern)",
      "need": "Sí (Investigación)",
      "timeline": "No mencionado"
    },
    "action": "Marketing Automation",
    "reason": "No es el decisor. Está en etapa de investigación temprana. Se le debe enviar el material solicitado y dejarlo en flujo de nutrición hasta que el decisor entre en contacto."
  }
]
```