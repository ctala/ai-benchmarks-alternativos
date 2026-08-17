# Mistral Nemo — ocr_extraction/screenshot_table_extraction

- model_id: `mistralai/mistral-nemo`
- success: True  | final: 6.26 | quality: 5.32
- latency_total: 56.735s | tokens_per_second: 17.9
- input_tokens: 422 | output_tokens: 1017
- judge_score: 2.6 | justificación: 

## Respuesta completa

Aquí está la información extraída en formato JSON, con el LTV/CAC ratio para cada mes, la métrica con la mayor mejora porcentual y la proyección para abril:

```json
{
  "dashboard": {
    "name": "KPIs Marzo 2026",
    "metrics": [
      {
        "name": "MRR",
        "values": {
          "January": 45200,
          "February": 48700,
          "March": 52100,
          "LTM": 7.0
        },
        "LTV_CAC_ratio": {
          "January": 79.6,
          "February": 101.5,
          "March": 123.6
        }
      },
      {
        "name": "Churn Rate",
        "values": {
          "January": 4.2,
          "February": 3.8,
          "March": 3.1,
          "LTM": -0.7
        },
        "LTV_CAC_ratio": {
          "January": 8.1,
          "February": 10.1,
          "March": 12.5
        }
      },
      {
        "name": "NPS",
        "values": {
          "January": 42,
          "February": 45,
          "March": 51,
          "LTM": 6
        },
        "LTV_CAC_ratio": {
          "January": 18.0,
          "February": 22.7,
          "March": 27.5
        }
      },
      {
        "name": "CAC",
        "values": {
          "January": 234,
          "February": 198,
          "March": 187,
          "LTM": -11
        },
        "LTV_CAC_ratio": {
          "January": 8.1,
          "February": 10.1,
          "March": 12.5
        }
      },
      {
        "name": "LTV",
        "values": {
          "January": 1890,
          "February": 2010,
          "March": 2340,
          "LTM": 330
        },
        "LTV_CAC_ratio": {
          "January": 8.1,
          "February": 10.1,
          "March": 12.5
        }
      },
      {
        "name": "Active Users",
        "values": {
          "January": 1234,
          "February": 1456,
          "March": 1678,
          "LTM": 15.3
        },
        "LTV_CAC_ratio": {
          "January": 5.3,
          "February": 7.3,
          "March": 9.0
        }
      },
      {
        "name": "Support Tickets",
        "values": {
          "January": 89,
          "February": 76,
          "March": 63,
          "LTM": -17.1
        },
        "LTV_CAC_ratio": {
          "January": 0.4,
          "February": 0.4,
          "March": 0.3
        }
      },
      {
        "name": "Avg Response (h)",
        "values": {
          "January": 4.2,
          "February": 3.1,
          "March": 2.4,
          "LTM": -0.7
        },
        "LTV_CAC_ratio": {
          "January": 0.4,
          "February": 0.4,
          "March": 0.3
        }
      }
    ],
    "metric_with_greatest_improvement": "Active Users",
    "projection_for_april": {
      "MRR": 56940,
      "Churn Rate": 2.3,
      "NPS": 59,
      "CAC": 175,
      "LTV": 2674,
      "Active Users": 1905,
      "Support Tickets": 51,
      "Avg Response (h)": 2.0
    }
  }
}
```

La métrica con la mayor mejora porcentual es "Active Users", con un aumento del 15.3% en marzo en comparación con enero. La proyección para abril se basa en la tendencia positiva observada en los últimos tres meses.