# Gemma 4 31B (NIM) — ocr_extraction/screenshot_table_extraction

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 6.33 | quality: 5.8
- latency_total: 61.415s | tokens_per_second: 13.8
- input_tokens: 377 | output_tokens: 850
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "data_extraction": {
    "dashboard_name": "DASHBOARD - KPIs Marzo 2026",
    "metrics": [
      {
        "metric": "MRR",
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100,
        "var_m_m": 0.07,
        "unit": "USD"
      },
      {
        "metric": "Churn Rate",
        "enero": 0.042,
        "febrero": 0.038,
        "marzo": 0.031,
        "var_m_m": -0.007,
        "unit": "percentage"
      },
      {
        "metric": "NPS",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "var_m_m": 6,
        "unit": "score"
      },
      {
        "metric": "CAC",
        "enero": 234,
        "febrero": 198,
        "marzo": 187,
        "var_m_m": -11,
        "unit": "USD"
      },
      {
        "metric": "LTV",
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340,
        "var_m_m": 330,
        "unit": "USD"
      },
      {
        "metric": "Active Users",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "var_m_m": 0.153,
        "unit": "count"
      },
      {
        "metric": "Support Tickets",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "var_m_m": -0.171,
        "unit": "count"
      },
      {
        "metric": "Avg Response (h)",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "var_m_m": -0.7,
        "unit": "hours"
      }
    ],
    "general_trend": "Positiva"
  },
  "analysis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "highest_percentage_improvement": {
      "metric": "Support Tickets",
      "value": "-17.1%",
      "note": "Mayor reducción porcentual (mejora en eficiencia)"
    }
  },
  "projections_april": {
    "MRR": 55747,
    "Churn Rate": "2.4%",
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "Active Users": 1935,
    "Support Tickets": 52,
    "Avg Response (h)": 1.7
  }
}
```