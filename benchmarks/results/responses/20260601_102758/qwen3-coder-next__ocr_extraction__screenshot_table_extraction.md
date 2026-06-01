# Qwen3-Coder-Next (OpenRouter FP8) — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 5.56 | quality: 4.6
- latency_total: 7.148s | tokens_per_second: 122.6
- input_tokens: 424 | output_tokens: 876
- judge_score: 2.6 | justificación: 

## Respuesta completa

```json
{
  "dashboard": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "reporting_period": "Marzo 2026"
  },
  "metrics": [
    {
      "name": "MRR",
      "unit": "USD",
      "values": {
        "Enero": 45200,
        "Feb": 48700,
        "Marzo": 52100
      },
      "var_month_over_month": 0.070,
      "trend": "up"
    },
    {
      "name": "Churn Rate",
      "unit": "%",
      "values": {
        "Enero": 4.2,
        "Feb": 3.8,
        "Marzo": 3.1
      },
      "var_month_over_month": -0.7,
      "trend": "up"
    },
    {
      "name": "NPS",
      "unit": "points",
      "values": {
        "Enero": 42,
        "Feb": 45,
        "Marzo": 51
      },
      "var_month_over_month": 6,
      "trend": "up"
    },
    {
      "name": "CAC",
      "unit": "USD",
      "values": {
        "Enero": 234,
        "Feb": 198,
        "Marzo": 187
      },
      "var_month_over_month": -11,
      "trend": "up"
    },
    {
      "name": "LTV",
      "unit": "USD",
      "values": {
        "Enero": 1890,
        "Feb": 2010,
        "Marzo": 2340
      },
      "var_month_over_month": 330,
      "trend": "up"
    },
    {
      "name": "Active Users",
      "unit": "users",
      "values": {
        "Enero": 1234,
        "Feb": 1456,
        "Marzo": 1678
      },
      "var_month_over_month": 0.153,
      "trend": "up"
    },
    {
      "name": "Support Tickets",
      "unit": "tickets",
      "values": {
        "Enero": 89,
        "Feb": 76,
        "Marzo": 63
      },
      "var_month_over_month": -0.171,
      "trend": "up"
    },
    {
      "name": "Avg Response (h)",
      "unit": "hours",
      "values": {
        "Enero": 4.2,
        "Feb": 3.1,
        "Marzo": 2.4
      },
      "var_month_over_month": -0.7,
      "trend": "up"
    }
  ],
  "computed_ratios": {
    "LTV/CAC": {
      "Enero": 8.079,
      "Feb": 10.152,
      "Marzo": 12.513
    }
  },
  "analysis": {
    "overall_trend": "positive",
    "best_improvement_percentual": {
      "metric": "Active Users",
      "improvement_percent": 15.3,
      "reason": "Highest month-over-month growth rate"
    },
    "projections_april": {
      "MRR": 55867,
      "Churn Rate": 2.5,
      "NPS": 56,
      "CAC": 176,
      "LTV": 2670,
      "Active Users": 1934,
      "Support Tickets": 52,
      "Avg Response (h)": 1.8
    }
  }
}
```