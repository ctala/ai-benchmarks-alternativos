# GPT-OSS 20B (Groq) — sales_outreach/lead_qualification

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.81 | quality: 8.16
- latency_total: 1.327s | tokens_per_second: 628.3
- input_tokens: 306 | output_tokens: 834
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
{
  "leads": [
    {
      "name": "Juan Perez",
      "score": 6,
      "bant": {
        "budget": "no mencionado",
        "authority": "sí",
        "need": "sí",
        "timeline": "no mencionado"
      },
      "action": "Follow up to confirm budget and timeline",
      "reason": "El CEO muestra interés y necesidad, pero no se ha mencionado presupuesto ni plazo."
    },
    {
      "name": "Ana Gomez",
      "score": 9,
      "bant": {
        "budget": "probable (Serie B reciente)",
        "authority": "sí",
        "need": "sí",
        "timeline": "sí (antes del Q3)"
      },
      "action": "Schedule a demo",
      "reason": "Decision maker con necesidad clara, presupuesto probable y plazo urgente."
    },
    {
      "name": "Carlos Ruiz",
      "score": 2,
      "bant": {
        "budget": "no mencionado",
        "authority": "no",
        "need": "sí",
        "timeline": "no mencionado"
      },
      "action": "Send PDF and ask to connect with the decision maker",
      "reason": "Intern no tiene autoridad ni presupuesto; necesita ser escalado a quien tome la decisión."
    }
  ]
}
```