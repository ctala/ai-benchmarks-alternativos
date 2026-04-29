# Gemma 4 31B (DGX Spark Q4_K_M) — sales_outreach/lead_qualification

- model_id: `gemma4:31b`
- success: True  | final: 6.69 | quality: 7.68
- latency_total: 106.036s | tokens_per_second: 9.4
- input_tokens: 259 | output_tokens: 992
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
[
  {
    "score": 6,
    "bant": {
      "budget": "Unknown",
      "authority": "Yes (CEO)",
      "need": "Yes (Automate support)",
      "timeline": "Unknown"
    },
    "action": "Discovery Call",
    "reason": "Es el decisor final y tiene una necesidad clara, pero falta validar presupuesto y urgencia debido al tamaño pequeño de la startup."
  },
  {
    "score": 10,
    "bant": {
      "budget": "High (Series B funding)",
      "authority": "Yes (VP of Operations)",
      "need": "Yes (Requested demo)",
      "timeline": "Urgent (Before Q3)"
    },
    "action": "Immediate Sales Handover",
    "reason": "Lead ideal: tiene autoridad, presupuesto respaldado por inversión reciente, necesidad validada y una fecha límite clara."
  },
  {
    "score": 3,
    "bant": {
      "budget": "Unknown",
      "authority": "No (Intern)",
      "need": "Exploratory (Researching)",
      "timeline": "Unknown"
    },
    "action": "Nurturing / Send Info",
    "reason": "No es el decisor y se encuentra en una etapa muy temprana de investigación. Se le envía la información solicitada pero no se prioriza para ventas."
  }
]
```