# Nemotron Nano 9B v2 (NIM) — ocr_extraction/screenshot_table_extraction

- model_id: `nvidia/nvidia-nemotron-nano-9b-v2`
- success: True  | final: 5.71 | quality: 4.88
- latency_total: 51.367s | tokens_per_second: 60.0
- input_tokens: 431 | output_tokens: 3084
- judge_score: 2.8 | justificación: 

## Respuesta completa



```json
{
  "data": [
    {
      "metric": "MRR",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100
    },
    {
      "metric": "Churn Rate",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1
    },
    {
      "metric": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51
    },
    {
      "metric": "CAC",
      "enero": 234,
      "febrero": 198,
      "marzo": 187
    },
    {
      "metric": "LTV",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340
    },
    {
      "metric": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678
    },
    {
      "metric": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63
    },
    {
      "metric": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4
    }
  ],
  "ltv_cac_ratios": {
    "enero": 8.0769,
    "febrero": 10.1515,
    "marzo": 12.5134
  },
  "highest_improvement_metric": "Active Users",
  "april_projections": {
    "MRR": 55747,
    "Churn Rate": 2.4,
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "Active Users": 1934,
    "Support Tickets": 52,
    "Avg Response (h)": 1.7
  }
}
```
