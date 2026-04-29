# Ministral 14B (NIM) — ocr_extraction/screenshot_table_extraction

- model_id: `mistralai/ministral-14b-instruct-2512`
- success: True  | final: 6.68 | quality: 7.36
- latency_total: 48.682s | tokens_per_second: 21.5
- input_tokens: 422 | output_tokens: 1048
- judge_score: 3.8 | justificación: 

## Respuesta completa

```json
{
  "dashboard_data": {
    "month": "Marzo 2026",
    "metrics": [
      {
        "name": "MRR",
        "values": {
          "Enero": 45200,
          "Febrero": 48700,
          "Marzo": 52100,
          "variation_MM": "+7.0%"
        }
      },
      {
        "name": "Churn Rate",
        "values": {
          "Enero": 4.2,
          "Febrero": 3.8,
          "Marzo": 3.1,
          "variation_MM": "-0.7pp"
        }
      },
      {
        "name": "NPS",
        "values": {
          "Enero": 42,
          "Febrero": 45,
          "Marzo": 51,
          "variation_MM": "+6"
        }
      },
      {
        "name": "CAC",
        "values": {
          "Enero": 234,
          "Febrero": 198,
          "Marzo": 187,
          "variation_MM": "-11"
        }
      },
      {
        "name": "LTV",
        "values": {
          "Enero": 1890,
          "Febrero": 2010,
          "Marzo": 2340,
          "variation_MM": "+330"
        }
      },
      {
        "name": "Active Users",
        "values": {
          "Enero": 1234,
          "Febrero": 1456,
          "Marzo": 1678,
          "variation_MM": "+15.3%"
        }
      },
      {
        "name": "Support Tickets",
        "values": {
          "Enero": 89,
          "Febrero": 76,
          "Marzo": 63,
          "variation_MM": "-17.1%"
        }
      },
      {
        "name": "Avg Response (hours)",
        "values": {
          "Enero": 4.2,
          "Febrero": 3.1,
          "Marzo": 2.4,
          "variation_MM": "-0.7"
        }
      }
    ],
    "trend": "↑ Positiva en todas las metricas"
  },
  "calculations": {
    "LTV_CAC_ratio": {
      "Enero": 8.077,
      "Febrero": 10.152,
      "Marzo": 12.513
    },
    "metric_with_greatest_improvement": {
      "name": "Support Tickets",
      "improvement": "-17.1%"
    },
    "projected_April": {
      "MRR": {
        "value": 56043,
        "growth_rate": "+7.6%"
      },
      "Churn_Rate": {
        "value": 2.41,
        "growth_rate": "-0.69pp"
      },
      "NPS": {
        "value": 57,
        "growth_rate": "+6%"
      },
      "CAC": {
        "value": 174.79,
        "growth_rate": "-6.5%"
      },
      "LTV": {
        "value": 2547.3,
        "growth_rate": "+8.9%"
      },
      "Active_Users": {
        "value": 1929,
        "growth_rate": "+15.0%"
      },
      "Support_Tickets": {
        "value": 52.99,
        "growth_rate": "-15.9%"
      },
      "Avg_Response_Hours": {
        "value": 1.86,
        "growth_rate": "-0.54"
      }
    },
    "notes": [
      {
        "calculation_details": {
          "LTV_CAC_ratio": "LTV/CAC por mes (ej: Marzo = 2340/187 = 12.513). Porcentajes anualizados si son necesarios.",
          "greatest_improvement": "Se calculó la mayor mejora en términos de variación M/M (Support Tickets con -17.1%).",
          "projection_method": "Para Abril, se aplicó la variación M/M de Marzo a los valores de Marzo (ej: MRR: 52100 * 1.07 = 56043)."
        }
      }
    ]
  }
}
```