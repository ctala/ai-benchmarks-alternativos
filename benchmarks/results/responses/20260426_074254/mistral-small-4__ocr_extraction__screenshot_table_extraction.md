# Mistral Small 4 — ocr_extraction/screenshot_table_extraction

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 6.46 | quality: 4.6
- latency_total: 4.848s | tokens_per_second: 152.9
- input_tokens: 434 | output_tokens: 741
- judge_score: 2.6 | justificación: 

## Respuesta completa

```json
{
  "dashboard_data": {
    "title": "Dashboard - KPIs Marzo 2026",
    "metrics": [
      {
        "name": "MRR",
        "values": {
          "Enero": "$45.2K",
          "Febrero": "$48.7K",
          "Marzo": "$52.1K",
          "Variación_M_M": "+7.0%"
        }
      },
      {
        "name": "Churn Rate",
        "values": {
          "Enero": "4.2%",
          "Febrero": "3.8%",
          "Marzo": "3.1%",
          "Variación_M_M": "-0.7pp"
        }
      },
      {
        "name": "NPS",
        "values": {
          "Enero": "42",
          "Febrero": "45",
          "Marzo": "51",
          "Variación_M_M": "+6"
        }
      },
      {
        "name": "CAC",
        "values": {
          "Enero": "$234",
          "Febrero": "$198",
          "Marzo": "$187",
          "Variación_M_M": "-$11"
        }
      },
      {
        "name": "LTV",
        "values": {
          "Enero": "$1,890",
          "Febrero": "$2,010",
          "Marzo": "$2,340",
          "Variación_M_M": "+$330"
        }
      },
      {
        "name": "Active Users",
        "values": {
          "Enero": "1,234",
          "Febrero": "1,456",
          "Marzo": "1,678",
          "Variación_M_M": "+15.3%"
        }
      },
      {
        "name": "Support Tickets",
        "values": {
          "Enero": "89",
          "Febrero": "76",
          "Marzo": "63",
          "Variación_M_M": "-17.1%"
        }
      },
      {
        "name": "Avg Response (h)",
        "values": {
          "Enero": "4.2",
          "Febrero": "3.1",
          "Marzo": "2.4",
          "Variación_M_M": "-0.7"
        }
      }
    ],
    "calculations": {
      "LTV_CAC_ratio": {
        "Enero": 8.08,
        "Febrero": 10.15,
        "Marzo": 12.51
      },
      "metric_with_greatest_improvement": {
        "name": "LTV",
        "improvement": "+$330 (+16.42%)"
      }
    },
    "projection_april": {
      "MRR": "$55.7K",
      "Churn Rate": "2.5%",
      "NPS": "57",
      "CAC": "$175",
      "LTV": "$2,680",
      "Active Users": "1,936",
      "Support Tickets": "52",
      "Avg Response (h)": "1.9"
    }
  }
}
```