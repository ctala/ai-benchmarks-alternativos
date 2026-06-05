# Gemma 4 31B (Spark llama-server Q4_K_M) — ocr_extraction/screenshot_table_extraction

- model_id: `gemma-4-31B-it-Q4_K_M.gguf`
- success: True  | final: 5.67 | quality: 5.8
- latency_total: 78.78s | tokens_per_second: 9.7
- input_tokens: 431 | output_tokens: 763
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard_data": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "metrics": [
      {
        "metrica": "MRR",
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100,
        "var_mm": 0.07
      },
      {
        "metrica": "Churn Rate",
        "enero": 0.042,
        "febrero": 0.038,
        "marzo": 0.031,
        "var_mm": -0.007
      },
      {
        "metrica": "NPS",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "var_mm": 6
      },
      {
        "metrica": "CAC",
        "enero": 234,
        "febrero": 198,
        "marzo": 187,
        "var_mm": -11
      },
      {
        "metrica": "LTV",
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340,
        "var_mm": 330
      },
      {
        "metrica": "Active Users",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "var_mm": 0.153
      },
      {
        "metrica": "Support Tickets",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "var_mm": -0.171
      },
      {
        "metrica": "Avg Response (h)",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "var_mm": -0.7
      }
    ]
  },
  "analysis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "highest_improvement_metric": {
      "metrica": "Support Tickets",
      "percentage_change": -17.1,
      "note": "Mayor variación porcentual absoluta en el periodo M/M"
    },
    "projections_april": {
      "MRR": 55747,
      "Churn Rate": 0.024,
      "NPS": 57,
      "CAC": 176,
      "LTV": 2670,
      "Active Users": 1935,
      "Support Tickets": 52,
      "Avg Response (h)": 1.7
    }
  }
}
```