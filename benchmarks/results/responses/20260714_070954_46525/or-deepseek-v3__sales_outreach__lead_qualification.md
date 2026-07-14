# DeepSeek V3 — sales_outreach/lead_qualification

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 4.21 | quality: 3.33
- latency_total: 15.948s | tokens_per_second: 26.5
- input_tokens: 261 | output_tokens: 422
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una evaluación detallada y acciones específicas para cada lead.

## Respuesta completa

```json
{
    "leads": [
        {
            "score": 7,
            "bant": {
                "budget": "No mencionado, pero como CEO de startup podría tener flexibilidad",
                "authority": "Alto - CEO es decisión final",
                "need": "Claro - busca automatizar soporte",
                "timeline": "Implícito por 'estamos viendo opciones', pero no específico"
            },
            "action": "Seguimiento inmediato con consultoría personalizada y caso de éxito de startups",
            "reason": "CEO con autoridad total y necesidad definida, pero falta claridad de presupuesto y timeline específico"
        },
        {
            "score": 9,
            "bant": {
                "budget": "Alto - empresa con Serie B reciente indica capacidad",
                "authority": "Alto - VP of Operations es decision-maker",
                "need": "Implícito - pidió demo después de webinar",
                "timeline": "Claro - 'antes de Q3' es timeline definido"
            },
            "action": "Prioritario - agendar demo y preparar propuesta comercial para Q3",
            "reason": "Decision-maker con timeline urgente, presupuesto asegurado y empresa en crecimiento"
        },
        {
            "score": 3,
            "bant": {
                "budget": "Desconocido - solo pide PDF de precios",
                "authority": "Bajo - intern sin poder de decisión",
                "need": "Vago - 'investigar herramientas' no indica necesidad concreta",
                "timeline": "No especificado"
            },
            "action": "Enviar materiales educativos y solicitar conversación con el jefe/decision-maker",
            "reason": "Sin autoridad, necesidad poco definida y enfoque en precios sin contexto de necesidad"
        }
    ]
}
```