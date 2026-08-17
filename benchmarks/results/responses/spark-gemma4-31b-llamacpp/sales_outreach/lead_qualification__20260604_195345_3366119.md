# Gemma 4 31B (Spark llama-server Q4_K_M) — sales_outreach/lead_qualification

- model_id: `gemma-4-31B-it-Q4_K_M.gguf`
- success: True  | final: 6.91 | quality: 7.68
- latency_total: 33.742s | tokens_per_second: 9.8
- input_tokens: 261 | output_tokens: 329
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
[
  {
    "score": 6,
    "bant": {
      "budget": "Desconocido",
      "authority": "Alta (CEO)",
      "need": "Confirmada (Automatizar soporte)",
      "timeline": "Desconocido"
    },
    "action": "Nutrir / Calificar",
    "reason": "Es el decisor y tiene la necesidad, pero falta validar presupuesto y urgencia."
  },
  {
    "score": 10,
    "bant": {
      "budget": "Alta (Serie B recién levantada)",
      "authority": "Alta (VP of Operations)",
      "need": "Confirmada (Solicitó demo)",
      "timeline": "Definido (Antes de Q3)"
    },
    "action": "Enviar a Ventas (Hot Lead)",
    "reason": "Cumple con todos los criterios de BANT. Tiene autoridad, presupuesto probable y una fecha límite clara."
  },
  {
    "score": 3,
    "bant": {
      "budget": "Desconocido",
      "authority": "Nula (Intern)",
      "need": "Exploratoria",
      "timeline": "Desconocido"
    },
    "action": "Automatizar / Low Priority",
    "reason": "No es el decisor. Solo está realizando una investigación preliminar para su superior."
  }
]
```