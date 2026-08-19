# MiniMax M3 (directo / sub) — multi_turn/requirements_change

- model_id: `MiniMax-M3`
- success: True  | final: 7.14 | quality: 7.36
- latency_total: 6.606s | tokens_per_second: 17.3
- input_tokens: 385 | output_tokens: 114
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, ajustándose bien a los requisitos actualizados, con una estructura clara y utilidad práctica, aunque la profundidad podría mejorarse con más detalles sobre la implementación.

## Respuesta completa

Buen cambio. Entonces el flujo queda asi:

1. **Gmail Trigger**: Detecta emails nuevos
2. **IF Node**: Filtra por asunto (palabra clave: "propuesta" o "cotizacion")
3. **Function Node**: Extrae y limpia los datos del remitente
4. **Notion**: Crea una pagina en tu database
5. **Slack**: Envia notificacion

Quieres que te pase el JSON del workflow listo para importar, o prefieres la guia paso a paso para armarlo tu?