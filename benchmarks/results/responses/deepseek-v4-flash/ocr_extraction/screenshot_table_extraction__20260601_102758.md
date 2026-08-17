# DeepSeek V4 Flash (OpenRouter) — ocr_extraction/screenshot_table_extraction

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 6.11 | quality: 5.16
- latency_total: 37.772s | tokens_per_second: 102.5
- input_tokens: 386 | output_tokens: 3871
- judge_score: 3.0 | justificación: La respuesta incluye datos no presentes en la tabla original, afectando la precisión y exactitud de los datos, pero ofrece cálculos y proyecciones útiles y está bien organizada.

## Respuesta completa

{
  "dashboard": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "metrics": [
      {
        "name": "MRR",
        "values": {
          "Enero": "$45.2K",
          "Febrero": "$48.7K",
          "Marzo": "$52.1K"
        },
        "var_mm": "+7.0%"
      },
      {
        "name": "Churn Rate",
        "values": {
          "Enero": "4.2%",
          "Febrero": "3.8%",
          "Marzo": "3.1%"
        },
        "var_mm": "-0.7pp"
      },
      {
        "name": "NPS",
        "values": {
          "Enero": 42,
          "Febrero": 45,
          "Marzo": 51
        },
        "var_mm": "+6"
      },
      {
        "name": "CAC",
        "values": {
          "Enero": "$234",
          "Febrero": "$198",
          "Marzo": "$187"
        },
        "var_mm": "-$11"
      },
      {
        "name": "LTV",
        "values": {
          "Enero": "$1,890",
          "Febrero": "$2,010",
          "Marzo": "$2,340"
        },
        "var_mm": "+$330"
      },
      {
        "name": "Active Users",
        "values": {
          "Enero": 1234,
          "Febrero": 1456,
          "Marzo": 1678
        },
        "var_mm": "+15.3%"
      },
      {
        "name": "Support Tickets",
        "values": {
          "Enero": 89,
          "Febrero": 76,
          "Marzo": 63
        },
        "var_mm": "-17.1%"
      },
      {
        "name": "Avg Response (h)",
        "values": {
          "Enero": 4.2,
          "Febrero": 3.1,
          "Marzo": 2.4
        },
        "var_mm": "-0.7"
      }
    ]
  },
  "calculations": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Febrero": 10.15,
      "Marzo": 12.51
    },
    "highest_improvement": {
      "metric": "Avg Response (h)",
      "type": "reduction",
      "absolute_relative_change_enero_marzo": -42.86,
      "absolute_relative_change_febrero_marzo": -22.58,
      "description": "Largest percentage improvement from January to March (42.86% reduction) and also largest month-over-month (22.58% reduction)."
    },
    "projections_abril": {
      "assumption": "Last month-over-month change (Mar vs Feb) applied to March values.",
      "values": {
        "MRR": "$55.7K",
        "Churn Rate": "2.4%",
        "NPS": 57,
        "CAC": "$176",
        "LTV": "$2,670",
        "Active Users": 1935,
        "Support Tickets": 52,
        "Avg Response (h)": 1.7
      }
    }
  }
}