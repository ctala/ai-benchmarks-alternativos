# Gemini 3.1 Flash Lite — sales_outreach/lead_qualification

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 8.06 | quality: 8.88
- latency_total: 1.845s | tokens_per_second: 193.5
- input_tokens: 245 | output_tokens: 357
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
{
  "lead_1": {
    "score": 6,
    "bant": {
      "budget": "No mencionado",
      "authority": "Alto (CEO)",
      "need": "Clara (automatización de soporte)",
      "timeline": "Indefinido"
    },
    "action": "Agendar llamada de descubrimiento",
    "reason": "Es un tomador de decisiones con una necesidad clara, pero falta calificar su capacidad financiera y urgencia."
  },
  "lead_2": {
    "score": 10,
    "bant": {
      "budget": "Alto (Serie B confirmada)",
      "authority": "Alto (VP of Operations)",
      "need": "Alta (solicitó demo tras webinar)",
      "timeline": "Definido (antes de Q3)"
    },
    "action": "Priorizar demo inmediata con Account Executive",
    "reason": "Cumple con todos los criterios BANT. Es un lead de alta intención y capacidad de compra."
  },
  "lead_3": {
    "score": 2,
    "bant": {
      "budget": "Desconocido",
      "authority": "Nulo (Intern)",
      "need": "Exploratoria",
      "timeline": "No urgente"
    },
    "action": "Enviar material informativo por email (nurturing)",
    "reason": "No es un decision maker y su intención es puramente informativa/investigativa. No requiere atención comercial directa."
  }
}
```