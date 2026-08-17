# MiniMax M2.5 — sales_outreach/lead_qualification

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 8.95 | quality: 10.0
- latency_total: 11.567s | tokens_per_second: 61.0
- input_tokens: 247 | output_tokens: 706
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y ofrece insights útiles, siendo altamente práctica para un emprendedor.

## Respuesta completa

```json
[
  {
    "lead": "Juan Perez, CEO startup 5 personas",
    "score": 5,
    "bant": {
      "budget": "No mentioned - startup pequeña probablemente budget limitado",
      "authority": "SI - CEO, decision maker",
      "need": "SI - buscando automatizar soporte",
      "timeline": "No mentioned"
    },
    "action": "Nurture - enviar contenido educativo",
    "reason": "Tiene autoridad y necesidad clara, pero falta info de budget y timeline. Startup pequeña = budget reducido. Necesita más qualification."
  },
  {
    "lead": "Ana Gomez, VP Operations, empresa 200 empleados Serie B",
    "score": 9,
    "bant": {
      "budget": "SI - Serie B = capital disponible",
      "authority": "SI - VP Operations con poder de decisión",
      "need": "SI - necesita resolver problema de operaciones",
      "timeline": "SI - antes de Q3 (urgente)"
    },
    "action": "Prioritize - demo inmediata",
    "reason": "Cumple BANT completo. Empresa establecida, funding reciente, timeline claro. Lead caliente listo para venta."
  },
  {
    "lead": "Carlos Ruiz, intern de marketing",
    "score": 2,
    "bant": {
      "budget": "Unknown - no tiene poder de decisión",
      "authority": "NO - intern no tiene autoridad para comprar",
      "need": "Débil - solo 'investigando' por pedido de jefe",
      "timeline": "No mentioned"
    },
    "action": "Descartar - pasar a contenido genérico",
    "reason": "No es decision maker. Solo quiere PDF de precios por curiosidad. No tiene necesidad real ni urgencia. Lead no cualificado."
  }
]
```