# Qwen3 Coder — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3-coder`
- success: True  | final: 9.38 | quality: 10.0
- latency_total: 4.491s | tokens_per_second: 164.1
- input_tokens: 424 | output_tokens: 737
- judge_score: 3.0 | justificación: La respuesta incluye datos no presentes en la tabla original, como 'LTV', 'Active Users', 'Support Tickets', y 'Avg Response (h)', lo que afecta la precisión y relevancia, pero ofrece un análisis y proyecciones útiles.

## Respuesta completa

```json
{
  "dashboard_kpis": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "metricas": [
        {
          "nombre": "MRR",
          "valores": {
            "enero": "$45.2K",
            "febrero": "$48.7K",
            "marzo": "$52.1K",
            "variacion_mensual": "+7.0%"
          }
        },
        {
          "nombre": "Churn Rate",
          "valores": {
            "enero": "4.2%",
            "febrero": "3.8%",
            "marzo": "3.1%",
            "variacion_mensual": "-0.7pp"
          }
        },
        {
          "nombre": "NPS",
          "valores": {
            "enero": 42,
            "febrero": 45,
            "marzo": 51,
            "variacion_mensual": "+6"
          }
        },
        {
          "nombre": "CAC",
          "valores": {
            "enero": "$234",
            "febrero": "$198",
            "marzo": "$187",
            "variacion_mensual": "-$11"
          }
        },
        {
          "nombre": "LTV",
          "valores": {
            "enero": "$1,890",
            "febrero": "$2,010",
            "marzo": "$2,340",
            "variacion_mensual": "+$330"
          }
        },
        {
          "nombre": "Active Users",
          "valores": {
            "enero": 1234,
            "febrero": 1456,
            "marzo": 1678,
            "variacion_mensual": "+15.3%"
          }
        },
        {
          "nombre": "Support Tickets",
          "valores": {
            "enero": 89,
            "febrero": 76,
            "marzo": 63,
            "variacion_mensual": "-17.1%"
          }
        },
        {
          "nombre": "Avg Response (h)",
          "valores": {
            "enero": 4.2,
            "febrero": 3.1,
            "marzo": 2.4,
            "variacion_mensual": "-0.7"
          }
        }
      ]
  },
  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "mejora_porcentual_mayor": {
      "metrica": "Support Tickets",
      "porcentaje": "-17.1%"
    }
  },
  "proyeccion_abril": {
    "MRR": "$55,747",
    "Churn Rate": "2.9%",
    "NPS": 54,
    "CAC": "$179",
    "LTV": "$2,504",
    "Active Users": 1935,
    "Support Tickets": 52,
    "Avg Response (h)": 1.9
  }
}
```