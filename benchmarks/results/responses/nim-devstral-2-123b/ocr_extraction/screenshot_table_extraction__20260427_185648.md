# Devstral 2 123B (NIM) — ocr_extraction/screenshot_table_extraction

- model_id: `mistralai/devstral-2-123b-instruct-2512`
- success: True  | final: 5.9 | quality: 5.44
- latency_total: 64.829s | tokens_per_second: 12.2
- input_tokens: 422 | output_tokens: 790
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard_data": {
    "period": "KPIs Marzo 2026",
    "metrics": [
      {
        "name": "MRR",
        "units": "$",
        "values": {
          "Enero": 45200,
          "Feb": 48700,
          "Marzo": 52100
        },
        "var_m_m": "+7.0%"
      },
      {
        "name": "Churn Rate",
        "units": "%",
        "values": {
          "Enero": 4.2,
          "Feb": 3.8,
          "Marzo": 3.1
        },
        "var_m_m": "-0.7pp"
      },
      {
        "name": "NPS",
        "units": "points",
        "values": {
          "Enero": 42,
          "Feb": 45,
          "Marzo": 51
        },
        "var_m_m": "+6"
      },
      {
        "name": "CAC",
        "units": "$",
        "values": {
          "Enero": 234,
          "Feb": 198,
          "Marzo": 187
        },
        "var_m_m": "-$11"
      },
      {
        "name": "LTV",
        "units": "$",
        "values": {
          "Enero": 1890,
          "Feb": 2010,
          "Marzo": 2340
        },
        "var_m_m": "+$330"
      },
      {
        "name": "Active Users",
        "units": "count",
        "values": {
          "Enero": 1234,
          "Feb": 1456,
          "Marzo": 1678
        },
        "var_m_m": "+15.3%"
      },
      {
        "name": "Support Tickets",
        "units": "count",
        "values": {
          "Enero": 89,
          "Feb": 76,
          "Marzo": 63
        },
        "var_m_m": "-17.1%"
      },
      {
        "name": "Avg Response (h)",
        "units": "hours",
        "values": {
          "Enero": 4.2,
          "Feb": 3.1,
          "Marzo": 2.4
        },
        "var_m_m": "-0.7"
      }
    ],
    "general_trend": "Positiva en todas las métricas"
  },
  "calculated_metrics": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Feb": 10.15,
      "Marzo": 12.51
    },
    "metric_with_highest_improvement": {
      "name": "LTV",
      "improvement": 330,
      "percentage_improvement": 16.42
    }
  },
  "projections_for_april": {
    "MRR": 55747,
    "Churn Rate": 2.8,
    "NPS": 54,
    "CAC": 178,
    "LTV": 2577,
    "Active Users": 1935,
    "Support Tickets": 52,
    "Avg Response (h)": 1.9
  }
}
```