# GPT-5.4 Mini — ocr_extraction/screenshot_table_extraction

- model_id: `gpt-5.4-mini`
- success: True  | final: 7.63 | quality: 8.0
- latency_total: 5.006s | tokens_per_second: 170.2
- input_tokens: 379 | output_tokens: 852
- judge_score: 3.0 | justificación: La respuesta incluye datos correctos para las métricas visibles, pero introduce métricas no presentes en la captura de pantalla original, afectando la precisión y exactitud de los datos.

## Respuesta completa

{
  "dashboard_title": "DASHBOARD - KPIs Marzo 2026",
  "data": [
    {
      "metric": "MRR",
      "unit": "currency",
      "values": {
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100
      },
      "var_m_m": {
        "value": 7.0,
        "unit": "percent"
      }
    },
    {
      "metric": "Churn Rate",
      "unit": "percent",
      "values": {
        "enero": 4.2,
        "febrero": 3.8,
        "marzo": 3.1
      },
      "var_m_m": {
        "value": -0.7,
        "unit": "pp"
      }
    },
    {
      "metric": "NPS",
      "unit": "score",
      "values": {
        "enero": 42,
        "febrero": 45,
        "marzo": 51
      },
      "var_m_m": {
        "value": 6,
        "unit": "points"
      }
    },
    {
      "metric": "CAC",
      "unit": "currency",
      "values": {
        "enero": 234,
        "febrero": 198,
        "marzo": 187
      },
      "var_m_m": {
        "value": -11,
        "unit": "currency"
      }
    },
    {
      "metric": "LTV",
      "unit": "currency",
      "values": {
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340
      },
      "var_m_m": {
        "value": 330,
        "unit": "currency"
      }
    },
    {
      "metric": "Active Users",
      "unit": "count",
      "values": {
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678
      },
      "var_m_m": {
        "value": 15.3,
        "unit": "percent"
      }
    },
    {
      "metric": "Support Tickets",
      "unit": "count",
      "values": {
        "enero": 89,
        "febrero": 76,
        "marzo": 63
      },
      "var_m_m": {
        "value": -17.1,
        "unit": "percent"
      }
    },
    {
      "metric": "Avg Response (h)",
      "unit": "hours",
      "values": {
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4
      },
      "var_m_m": {
        "value": -0.7,
        "unit": "hours"
      }
    }
  ],
  "analysis": {
    "general_trend": "positive",
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "highest_percentage_improvement": {
      "metric": "Active Users",
      "value": 15.3,
      "direction": "increase"
    },
    "april_projection": {
      "method": "linear_month_over_month_extrapolation",
      "values": {
        "MRR": 55500,
        "Churn Rate": 2.4,
        "NPS": 57,
        "CAC": 176,
        "LTV": 2670,
        "Active Users": 1900,
        "Support Tickets": 50,
        "Avg Response (h)": 1.7
      },
      "ltv_cac_ratio": 15.17
    }
  }
}