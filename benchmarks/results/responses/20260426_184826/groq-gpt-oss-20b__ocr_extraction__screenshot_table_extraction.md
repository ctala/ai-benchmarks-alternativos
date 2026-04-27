# GPT-OSS 20B (Groq) — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 6.75 | quality: 5.44
- latency_total: 2.52s | tokens_per_second: 812.7
- input_tokens: 444 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard": {
    "title": "KPIs Marzo 2026",
    "trend": "Positiva en todas las métricas"
  },

  "metrics": [
    {
      "name": "MRR",
      "units": "USD",
      "values": {
        "Jan": 45200,
        "Feb": 48700,
        "Mar": 52100,
        "Apr": 55787
      },
      "var_MoM": "+7.0%"
    },
    {
      "name": "Churn Rate",
      "units": "%",
      "values": {
        "Jan": 4.2,
        "Feb": 3.8,
        "Mar": 3.1,
        "Apr": 2.4
      },
      "var_MoM": "-0.7pp"
    },
    {
      "name": "NPS",
      "units": "points",
      "values": {
        "Jan": 42,
        "Feb": 45,
        "Mar": 51,
        "Apr": 57
      },
      "var_MoM": "+6"
    },
    {
      "name": "CAC",
      "units": "USD",
      "values": {
        "Jan": 234,
        "Feb": 198,
        "Mar": 187,
        "Apr": 176
      },
      "var_MoM": "-$11"
    },
    {
      "name": "LTV",
      "units": "USD",
      "values": {
        "Jan": 1890,
        "Feb": 2010,
        "Mar": 2340,
        "Apr": 2670
      },
      "var_MoM": "+$330"
    },
    {
      "name": "Active Users",
      "units": "users",
      "values": {
        "Jan": 1234,
        "Feb": 1456,
        "Mar": 1678,
        "Apr": 1936
      },
      "var_MoM": "+15.3%"
    },
    {
      "name": "Support Tickets",
      "units": "tickets",
      "values": {
        "Jan": 89,
        "Feb": 76,
        "Mar": 63,
        "Apr": 52
      },
      "var_MoM": "-17.1%"
    },
    {
      "name": "Avg Response Time",
      "units": "hours",
      "values": {
        "Jan": 4.2,
        "Feb": 3.1,
        "Mar": 2.4,
        "Apr": 1.7
      },
      "var_MoM": "-0.7"
    }
  ],

  "ltv_cac_ratios": {
    "Jan": 8.08,
    "Feb": 10.15,
    "Mar": 12.52,
    "Apr": 15.17
  },

  "analysis": {
    "metric_with_greatest_improvement_percent": "Support Tickets",
    "reasoning": "Support Tickets decreased by 17.1% MoM, the largest percentage improvement among all metrics."
  },

  "projections": {
    "Apr": {
      "MRR": 55787,
      "Churn Rate": 2.4,
      "