# GPT-OSS 120B (Ollama Cloud) — sales_outreach/lead_qualification

- model_id: `gpt-oss:120b-cloud`
- success: True  | final: 7.91 | quality: 8.88
- latency_total: 7.51s | tokens_per_second: 89.6
- input_tokens: 307 | output_tokens: 673
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
[
  {
    "lead": "Juan Perez",
    "score": 6,
    "bant": {
      "budget": "No mencionado; incertidumbre",
      "authority": "Sí (CEO)",
      "need": "Sí (automatizar soporte)",
      "timeline": "No especificado; está explorando opciones"
    },
    "action": "Follow‑up",
    "reason": "Tiene autoridad y una necesidad clara, pero no ha indicado presupuesto ni urgencia. Se recomienda enviar material de caso de éxito y preguntar sobre capacidad de inversión y plazos para calificar mejor."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Probable (empresa con Serie B reciente)",
      "authority": "Sí (VP of Operations)",
      "need": "Sí (resolver problema antes de Q3)",
      "timeline": "Urgente (antes de Q3)"
    },
    "action": "Schedule demo",
    "reason": "Cumple con todos los criterios BANT: autoridad, presupuesto probable, necesidad clara y un plazo definido. Es un lead caliente y debe avanzar rápidamente a una demostración."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "No mencionado; probablemente sin decisión de gasto",
      "authority": "No (intern)",
      "need": "Indeterminado (solo investigación)",
      "timeline": "No especificado"
    },
    "action": "Nurture / Disqualify",
    "reason": "Carece de autoridad y de señal de presupuesto, y la necesidad es solo exploratoria. Se puede mantener en un flujo de nutrición de contenidos, pero no se prioriza para ventas inmediatas."
  }
]
```