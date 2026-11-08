# Mistral Small 4 — ocr_extraction/screenshot_table_extraction

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 7.99 | quality: 8.0
- latency_total: 4.289s | tokens_per_second: 162.8
- input_tokens: 434 | output_tokens: 698

## Entrada exacta (lo que recibió el modelo)

**user:**

Tengo una captura de pantalla de un dashboard de metricas. El contenido visible es:

DASHBOARD - KPIs Marzo 2026

+------------------+--------+--------+--------+---------+
| Metrica          | Enero  | Feb    | Marzo  | Var M/M |
+------------------+--------+--------+--------+---------+
| MRR              | $45.2K | $48.7K | $52.1K | +7.0%   |
| Churn Rate       | 4.2%   | 3.8%   | 3.1%   | -0.7pp  |
| NPS              | 42     | 45     | 51     | +6      |
| CAC              | $234   | $198   | $187   | -$11    |
| LTV              | $1,890 | $2,010 | $2,340 | +$330   |
| Active Users     | 1,234  | 1,456  | 1,678  | +15.3%  |
| Support Tickets  | 89     | 76     | 63     | -17.1%  |
| Avg Response (h) | 4.2    | 3.1    | 2.4    | -0.7    |
+------------------+--------+--------+--------+---------+

Tendencia general: ↑ Positiva en todas las metricas

Extrae los datos en formato JSON y ademas:
1. Calcula el LTV/CAC ratio para cada mes
2. Identifica la metrica con mayor mejora porcentual
3. Proyecta los valores de Abril si la tendencia se mantiene

Responde en JSON estructurado.


## Respuesta completa

```json
{
  "dashboard": {
    "title": "KPIs Marzo 2026",
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
          "Enero": 42,
          "Feb": 45,
          "Marzo": 51,
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
          "Enero": 1234,
          "Feb": 1456,
          "Marzo": 1678,
          "Var M/M": "+15.3%"
        }
      },
      {
        "name": "Support Tickets",
        "values": {
          "Enero": 89,
          "Feb": 76,
          "Marzo": 63,
          "Var M/M": "-17.1%"
        }
      },
      {
        "name": "Avg Response (h)",
        "values": {
          "Enero": 4.2,
          "Feb": 3.1,
          "Marzo": 2.4,
          "Var M/M": "-0.7"
        }
      }
    ],
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Feb": 10.15,
      "Marzo": 12.51
    },
    "best_improvement": {
      "metric": "Active Users",
      "percentage_improvement": "+15.3%"
    },
    "april_projection": {
      "MRR": "$55.7K",
      "Churn Rate": "2.5%",
      "NPS": 58,
      "CAC": "$175",
      "LTV": "$2,730",
      "Active Users": 1936,
      "Support Tickets": 52,
      "Avg Response (h)": 1.8
    }
  }
}
```