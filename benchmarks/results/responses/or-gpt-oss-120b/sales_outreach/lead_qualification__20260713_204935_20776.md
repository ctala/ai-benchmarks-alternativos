# GPT-OSS 120B — sales_outreach/lead_qualification

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 22.404s | tokens_per_second: 22.2
- input_tokens: 303 | output_tokens: 498
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para un emprendedor, proporcionando una evaluación detallada y acciones específicas para cada lead.

## Respuesta completa

```json
[
  {
    "lead": "Juan Perez",
    "score": 6,
    "bant": {
      "budget": "No mencionado; necesita ser descubierto",
      "authority": "CEO – alto nivel de decisión",
      "need": "Busca automatizar soporte – coincide con nuestra solución",
      "timeline": "No especificado"
    },
    "action": "Contactar para calificar presupuesto y timeline",
    "reason": "Tiene autoridad y necesidad clara, pero falta información crítica de presupuesto y urgencia."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Empresa con Serie B, probable disponibilidad de fondos",
      "authority": "VP of Operations – decisora o influenciadora clave",
      "need": "Necesita resolver el problema antes de Q3 – alineado con nuestra oferta",
      "timeline": "Urgente (antes de Q3)"
    },
    "action": "Programar demo lo antes posible",
    "reason": "Cumple con todos los criterios BANT; alta probabilidad de cierre rápido."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "No mencionado y poco probable que tenga autoridad para decidir",
      "authority": "Intern – no es decision maker",
      "need": "Investigación preliminar de herramientas de IA",
      "timeline": "No especificado"
    },
    "action": "Descalificar / nutrir con contenido genérico",
    "reason": "Falta de autoridad y presupuesto, interés muy preliminar; no es un lead cualificado para ventas directas."
  }
]
```