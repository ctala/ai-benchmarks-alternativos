# Nemotron Nano 9B v2 — ocr_extraction/screenshot_table_extraction

- model_id: `nvidia/nemotron-nano-9b-v2:free`
- success: True  | final: 7.62 | quality: 8.0
- latency_total: 96.807s | tokens_per_second: 38.6
- input_tokens: 431 | output_tokens: 3734
- judge_score: 2.0 | justificación: La respuesta contiene datos no presentes en la tabla original, como 'LTV', 'Active Users', 'Support Tickets', y 'Avg Response (h)', lo que afecta la precisión y relevancia; sin embargo, está bien organizada y clara.

## Respuesta completa

```json
{
  "metrics": [
    {
      "name": "MRR",
      "enero": 45200,
      "feb": 48700,
      "marzo": 52100,
      "var_m_m": 7.0
    },
    {
      "name": "Churn Rate",
      "enero": 4.2,
      "feb": 3.8,
      "marzo": 3.1,
      "var_m_m": -0.7
    },
    {
      "name": "NPS",
      "enero": 42,
      "feb": 45,
      "marzo": 51,
      "var_m_m": 6
    },
    {
      "name": "CAC",
      "enero": 234,
      "feb": 198,
      "marzo": 187,
      "var_m_m": -11
    },
    {
      "name": "LTV",
      "enero": 1890,
      "feb": 2010,
      "marzo": 2340,
      "var_m_m": 330
    },
    {
      "name": "Active Users",
      "enero": 1234,
      "feb": 1456,
      "marzo": 1678,
      "var_m_m": 15.3
    },
    {
      "name": "Support Tickets",
      "enero": 89,
      "feb": 76,
      "marzo": 63,
      "var_m_m": -17.1
    },
    {
      "name": "Avg Response (h)",
      "enero": 4.2,
      "feb": 3.1,
      "marzo": 2.4,
      "var_m_m": -0.7
    }
  ],
  "ltv_cac_ratio": {
    "enero": 8.08,
    "feb": 10.15,
    "marzo": 12.51
  },
  "top_improvement_metric": "Active Users",
  "april_projections": {
    "MRR": 55500,
    "Churn Rate": 2.4,
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "Active Users": 1900,
    "Support Tickets": 50,
    "Avg Response (h)": 1.7
  }
}
```
