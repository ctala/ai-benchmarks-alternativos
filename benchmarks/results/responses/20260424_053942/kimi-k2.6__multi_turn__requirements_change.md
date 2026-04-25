# Kimi K2.6 — multi_turn/requirements_change

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 5.6 | quality: 4.56
- latency_total: 30.24s | tokens_per_second: 67.7
- input_tokens: 266 | output_tokens: 2048
- judge_score: 2.6 | justificación: 

## Respuesta completa

 Aquí tienes el workflow paso a paso. Es mucho más eficiente filtrar directamente en Gmail antes de que entre a N8N, así no gastas operaciones en emails irrelevantes.

### Flujo completo

```
[Gmail Trigger] → [Set: Parsear datos] → [Notion: Crear entrada] → [Slack: Notificar]
```

---

### 1. Gmail