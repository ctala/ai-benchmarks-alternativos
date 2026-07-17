# Nemotron 3 Super — ocr_extraction/screenshot_table_extraction

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 7.68 | quality: 8.0
- latency_total: 10.811s | tokens_per_second: 58.9
- input_tokens: 389 | output_tokens: 637
- judge_score: 2.0 | justificación: La respuesta incluye datos no presentes en la tabla original y proyecciones sin base, afectando la precisión y relevancia, pero está claramente organizada.

## Respuesta completa



{
  "dashboard": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "metrics": [
      {
        "name": "MRR",
        "enero": 45.2,
        "feb": 48.7,
        "marzo": 52.1,
        "var_mm": "+7.0%",
        "unit": "K"
      },
      {
        "name": "Churn Rate",
        "enero": 4.2,
        "feb": 3.8,
        "marzo": 3.1,
        "var_mm": "-0.7pp",
        "unit": "%"
      },
      {
        "name": "NPS",
        "enero": 42,
        "feb": 45,
        "marzo": 51,
        "var_mm": "+6",
        "unit": "points"
      },
      {
        "name": "CAC",
        "enero": 234,
        "feb": 198,
        "marzo": 187,
        "var_mm": "-$11",
        "unit": "$"
      },
      {
        "name": "LTV",
        "enero": 1890,
        "feb": 2010,
        "marzo": 2340,
        "var_mm": "+$330",
        "unit": "$"
      },
      {
        "name": "Active Users",
        "enero": 1234,
        "feb": 1456,
        "marzo": 1678,
        "var_mm": "+15.3%",
        "unit": ""
      },
      {
        "name": "Support Tickets",
        "enero": 89,
        "feb": 76,
        "marzo": 63,
        "var_mm": "-17.1%",
        "unit": ""
      },
      {
        "name": "Avg Response (h)",
        "enero": 4.2,
        "feb": 3.1,
        "marzo": 2.4,
        "var_mm": "-0.7",
        "unit": "h"
      }
    ]
  },
  "ltv_cac_ratio": {
    "enero": 8.08,
    "feb": 10.15,
    "marzo": 12.51,
    "abril_proyectado": 15.17
  },
  "metric_with_greatest_improvement": {
    "metric": "Avg Response (h)",
    "improvement_percent": 22.58
  },
  "projection_april": {
    "MRR": 55.7,
    "Churn Rate": 2.4,
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "Active Users": 1935,
    "Support Tickets": 52,
    "Avg Response (h)": 1.7
  }
}