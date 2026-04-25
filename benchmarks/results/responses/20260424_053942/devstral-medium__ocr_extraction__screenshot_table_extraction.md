# Devstral Medium — ocr_extraction/screenshot_table_extraction

- model_id: `mistralai/devstral-medium`
- success: True  | final: 6.94 | quality: 7.12
- latency_total: 7.188s | tokens_per_second: 147.3
- input_tokens: 422 | output_tokens: 1059
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard": {
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
    "LTV_CAC_ratio": {
      "Enero": 8.08,
      "Feb": 10.15,
      "Marzo": 12.51
    },
    "metric_with_highest_improvement": {
      "name": "LTV",
      "improvement": "+$330"
    },
    "projected_values_April": {
      "MRR": "$55.7K",
      "Churn Rate": "2.4%",
      "NPS": "57",
      "CAC": "$176",
      "LTV": "$2,670",
      "Active Users": "1,933",
      "Support Tickets": "52",
      "Avg Response (h)": "1.7"
    }
  }
}
```

### Explicaciones:
1. **LTV/CAC Ratio**:
   - Enero: \( \frac{1890}{234} \approx 8.08 \)
   - Feb: \( \frac{2010}{198} \approx 10.15 \)
   - Marzo: \( \frac{2340}{187} \approx 12.51 \)

2. **Metrica con mayor mejora porcentual**:
   - La metrica con mayor mejora porcentual es "LTV" con un aumento de $330.

3. **Proyección de valores para Abril**:
   - MRR: \( 52.1K + (52.1K - 48.7K) = 55.7K \)
   - Churn Rate: \( 3.1\% - 0.7pp = 2.4\% \)
   - NPS: \( 51 + 6 = 57 \)
   - CAC: \( 187 - 11 = 176 \)
   - LTV: \( 2340 + 330 = 2670 \)
   - Active Users: \( 1678 + (1678 - 1456) = 1933 \)
   - Support Tickets: \( 63 - 17.1\% \approx 52 \)
   - Avg Response (h): \( 2.4 - 0.7 = 1.7 \)