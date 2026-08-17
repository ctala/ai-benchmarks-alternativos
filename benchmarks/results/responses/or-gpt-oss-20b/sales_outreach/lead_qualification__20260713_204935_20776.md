# GPT-OSS 20B — sales_outreach/lead_qualification

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 2.18 | quality: 0.0
- latency_total: 14.205s | tokens_per_second: 75.5
- input_tokens: 293 | output_tokens: 1073
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza adecuadamente en cada lead, proporcionando acciones prácticas que un emprendedor podría implementar directamente.

## Respuesta completa

```json
[
  {
    "score": 6,
    "bant": {
      "budget": "unknown",
      "authority": "yes",
      "need": "yes",
      "timeline": "unknown"
    },
    "action": "Nurture: enviar contenido educativo sobre automatización de soporte y dar seguimiento para aclarar presupuesto y plazos.",
    "reason": "El CEO es decisor y muestra necesidad, pero no se menciona presupuesto ni plazo."
  },
  {
    "score": 9,
    "bant": {
      "budget": "yes",
      "authority": "yes",
      "need": "yes",
      "timeline": "yes"
    },
    "action": "Programar demo lo antes posible y preparar materiales urgentes.",
    "reason": "VP de Operaciones, empresa con reciente financiación, expresa urgencia y necesita solución antes de Q3."
  },
  {
    "score": 2,
    "bant": {
      "budget": "no",
      "authority": "no",
      "need": "yes",
      "timeline": "unknown"
    },
    "action": "Solicitar contacto del responsable de decisiones o reenviar a la persona adecuada.",
    "reason": "El interno no tiene autoridad ni presupuesto; se necesita identificar al tomador de decisiones y confirmar plazos."
  }
]
```