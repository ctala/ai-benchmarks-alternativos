# Gemma 4 31B (NIM) — sales_outreach/lead_qualification

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 7.24 | quality: 7.68
- latency_total: 8.31s | tokens_per_second: 46.9
- input_tokens: 264 | output_tokens: 390
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
[
  {
    "lead": "Juan Perez",
    "score": 5,
    "bant": {
      "budget": "Desconocido",
      "authority": "Sí (CEO)",
      "need": "Sí (Automatizar soporte)",
      "timeline": "Desconocido"
    },
    "action": "Nutrir / Calificar",
    "reason": "Es el decisor y tiene la necesidad, pero falta información crítica sobre presupuesto y urgencia. El origen (blog) indica un interés temprano."
  },
  {
    "lead": "Ana Gomez",
    "score": 10,
    "bant": {
      "budget": "Probable (Serie B levantada)",
      "authority": "Sí (VP of Operations)",
      "need": "Sí (Interés post-webinar)",
      "timeline": "Sí (Antes de Q3)"
    },
    "action": "Prioridad Alta / Demo inmediata",
    "reason": "Cumple con todos los criterios de BANT. Tiene autoridad, urgencia clara y solvencia económica probable por la ronda de inversión."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido",
      "authority": "No (Intern)",
      "need": "Indefinido (Investigación)",
      "timeline": "Desconocido"
    },
    "action": "Automatización / Low touch",
    "reason": "No es el decisor y se encuentra en una fase de investigación muy temprana. Se le debe enviar la información solicitada pero sin asignar tiempo de ventas humano."
  }
]
```