# MiMo V2-Omni (Xiaomi direct) — ocr_extraction/screenshot_table_extraction

- model_id: `mimo-v2-omni`
- success: True  | final: 6.78 | quality: 5.8
- latency_total: 7.423s | tokens_per_second: 124.6
- input_tokens: 666 | output_tokens: 925
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard_data": {
    "period": "KPIs Marzo 2026",
    "metrics": {
      "MRR": {
        "Enero": 45200,
        "Feb": 48700,
        "Marzo": 52100,
        "Var_M_M": "+7.0%"
      },
      "Churn_Rate": {
        "Enero": 4.2,
        "Feb": 3.8,
        "Marzo": 3.1,
        "Var_M_M": "-0.7pp"
      },
      "NPS": {
        "Enero": 42,
        "Feb": 45,
        "Marzo": 51,
        "Var_M_M": "+6"
      },
      "CAC": {
        "Enero": 234,
        "Feb": 198,
        "Marzo": 187,
        "Var_M_M": "-$11"
      },
      "LTV": {
        "Enero": 1890,
        "Feb": 2010,
        "Marzo": 2340,
        "Var_M_M": "+$330"
      },
      "Active_Users": {
        "Enero": 1234,
        "Feb": 1456,
        "Marzo": 1678,
        "Var_M_M": "+15.3%"
      },
      "Support_Tickets": {
        "Enero": 89,
        "Feb": 76,
        "Marzo": 63,
        "Var_M_M": "-17.1%"
      },
      "Avg_Response_Hours": {
        "Enero": 4.2,
        "Feb": 3.1,
        "Marzo": 2.4,
        "Var_M_M": "-0.7"
      }
    },
    "general_trend": "↑ Positiva en todas las métricas"
  },
  "analysis": {
    "LTV_CAC_ratio": {
      "Enero": 8.08,
      "Feb": 10.15,
      "Marzo": 12.51
    },
    "highest_percentage_improvement": {
      "metric": "Support_Tickets",
      "change": "-17.1%",
      "description": "Mayor mejora porcentual absoluta (disminución de tickets)"
    },
    "april_projections": {
      "assumption": "Tendencia de marzo se mantiene (variación porcentual similar)",
      "MRR": 55747,
      "Churn_Rate": 2.4,
      "NPS": 57,
      "CAC": 176,
      "LTV": 2670,
      "Active_Users": 1935,
      "Support_Tickets": 52,
      "Avg_Response_Hours": 1.7
    }
  }
}
```