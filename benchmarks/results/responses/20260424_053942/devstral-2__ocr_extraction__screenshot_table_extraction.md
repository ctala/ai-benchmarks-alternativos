# Devstral 2 (Dic 2025) — ocr_extraction/screenshot_table_extraction

- model_id: `mistralai/devstral-2512`
- success: True  | final: 6.25 | quality: 5.44
- latency_total: 9.052s | tokens_per_second: 81.8
- input_tokens: 422 | output_tokens: 740
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard_data": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "metrics": [
      {
        "name": "MRR",
        "values": {
          "Enero": "$45.2K",
          "Feb": "$48.7K",
          "Marzo": "$52.1K",
          "Var M/M": "+7.0%"
        }
      },
      {
        "name": "Churn Rate",
        "values": {
          "Enero": "4.2%",
          "Feb": "3.8%",
          "Marzo": "3.1%",
          "Var M/M": "-0.7pp"
        }
      },
      {
        "name": "NPS",
        "values": {
          "Enero": "42",
          "Feb": "45",
          "Marzo": "51",
          "Var M/M": "+6"
        }
      },
      {
        "name": "CAC",
        "values": {
          "Enero": "$234",
          "Feb": "$198",
          "Marzo": "$187",
          "Var M/M": "-$11"
        }
      },
      {
        "name": "LTV",
        "values": {
          "Enero": "$1,890",
          "Feb": "$2,010",
          "Marzo": "$2,340",
          "Var M/M": "+$330"
        }
      },
      {
        "name": "Active Users",
        "values": {
          "Enero": "1,234",
          "Feb": "1,456",
          "Marzo": "1,678",
          "Var M/M": "+15.3%"
        }
      },
      {
        "name": "Support Tickets",
        "values": {
          "Enero": "89",
          "Feb": "76",
          "Marzo": "63",
          "Var M/M": "-17.1%"
        }
      },
      {
        "name": "Avg Response (h)",
        "values": {
          "Enero": "4.2",
          "Feb": "3.1",
          "Marzo": "2.4",
          "Var M/M": "-0.7"
        }
      }
    ],
    "trend": "↑ Positiva en todas las métricas"
  },
  "calculations": {
    "LTV_CAC_ratio": {
      "Enero": 8.08,
      "Feb": 10.15,
      "Marzo": 12.51
    },
    "metric_with_highest_improvement": {
      "name": "Support Tickets",
      "improvement": "-17.1%"
    },
    "projected_April_values": {
      "MRR": "$55.7K",
      "Churn Rate": "2.4%",
      "NPS": "57",
      "CAC": "$176",
      "LTV": "$2,670",
      "Active Users": "1,934",
      "Support Tickets": "52",
      "Avg Response (h)": "1.7"
    }
  }
}
```