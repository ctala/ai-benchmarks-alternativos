# Mistral Large 3 675B — sales_outreach/lead_qualification

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 4.37 | quality: 3.33
- latency_total: 6.088s | tokens_per_second: 58.0
- input_tokens: 253 | output_tokens: 353
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una evaluación detallada y acciones específicas para cada lead.

## Respuesta completa

```json
[
    {
        "score": 5,
        "bant": {
            "budget": "No mencionado (neutral)",
            "authority": "Alto (CEO)",
            "need": "Claro (automatizar soporte)",
            "timeline": "No claro (solo 'viendo opciones')"
        },
        "action": "Nurture con contenido educativo (casos de éxito, ROI)",
        "reason": "Decision maker con necesidad clara, pero falta confirmar presupuesto y urgencia. Lead frío (vía blog)."
    },
    {
        "score": 9,
        "bant": {
            "budget": "Alto (empresa en Serie B)",
            "authority": "Alto (VP of Operations)",
            "need": "Claro (resolver problema específico)",
            "timeline": "Urgente (antes de Q3)"
        },
        "action": "Contacto inmediato (demo + propuesta personalizada)",
        "reason": "Cumple todos los criterios BANT con alta prioridad. Lead caliente (pidió demo)."
    },
    {
        "score": 2,
        "bant": {
            "budget": "No mencionado",
            "authority": "Bajo (intern)",
            "need": "Indirecto (investigación para jefe)",
            "timeline": "No claro"
        },
        "action": "Enviar PDF genérico + preguntar por contacto del decision maker",
        "reason": "Baja autoridad y necesidad no confirmada. Riesgo de ser un 'tire-kicker'."
    }
]
```