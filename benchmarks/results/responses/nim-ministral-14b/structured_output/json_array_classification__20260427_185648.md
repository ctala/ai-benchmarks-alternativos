# Ministral 14B (NIM) — structured_output/json_array_classification

- model_id: `mistralai/ministral-14b-instruct-2512`
- success: True  | final: 7.3 | quality: 8.58
- latency_total: 14.642s | tokens_per_second: 9.8
- input_tokens: 180 | output_tokens: 143
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
[
    {
        "id": 1,
        "category": "shipping",
        "priority": "urgent",
        "sentiment": "negative"
    },
    {
        "id": 2,
        "category": "shipping",
        "priority": "low",
        "sentiment": "neutral"
    },
    {
        "id": 3,
        "category": "billing",
        "priority": "urgent",
        "sentiment": "negative"
    },
    {
        "id": 4,
        "category": "technical",
        "priority": "high",
        "sentiment": "negative"
    }
]
```