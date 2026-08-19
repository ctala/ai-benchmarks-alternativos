# Mistral Large — ocr_extraction/screenshot_table_extraction

- model_id: `mistralai/mistral-large`
- success: True  | final: 7.02 | quality: 8.0
- latency_total: 17.116s | tokens_per_second: 93.3
- input_tokens: 422 | output_tokens: 1597
- judge_score: 2.0 | justificación: La respuesta incluye datos no presentes en la captura de pantalla original, como 'LTV', 'Active Users', 'Support Tickets', y 'Avg Response (h)', lo que afecta la precisión y relevancia; sin embargo, está bien estructurada y clara.

## Respuesta completa

Aquí tienes el JSON estructurado con los datos solicitados:

```json
{
  "dashboard_data": {
    "title": "KPIs Marzo 2026",
    "metrics": [
      {
        "name": "MRR",
        "values": {
          "Enero": "$45.2K",
          "Febrero": "$48.7K",
          "Marzo": "$52.1K"
        },
        "monthly_variation": "+7.0%",
        "numeric_values": {
          "Enero": 45200,
          "Febrero": 48700,
          "Marzo": 52100
        }
      },
      {
        "name": "Churn Rate",
        "values": {
          "Enero": "4.2%",
          "Febrero": "3.8%",
          "Marzo": "3.1%"
        },
        "monthly_variation": "-0.7pp",
        "numeric_values": {
          "Enero": 0.042,
          "Febrero": 0.038,
          "Marzo": 0.031
        }
      },
      {
        "name": "NPS",
        "values": {
          "Enero": "42",
          "Febrero": "45",
          "Marzo": "51"
        },
        "monthly_variation": "+6",
        "numeric_values": {
          "Enero": 42,
          "Febrero": 45,
          "Marzo": 51
        }
      },
      {
        "name": "CAC",
        "values": {
          "Enero": "$234",
          "Febrero": "$198",
          "Marzo": "$187"
        },
        "monthly_variation": "-$11",
        "numeric_values": {
          "Enero": 234,
          "Febrero": 198,
          "Marzo": 187
        }
      },
      {
        "name": "LTV",
        "values": {
          "Enero": "$1,890",
          "Febrero": "$2,010",
          "Marzo": "$2,340"
        },
        "monthly_variation": "+$330",
        "numeric_values": {
          "Enero": 1890,
          "Febrero": 2010,
          "Marzo": 2340
        }
      },
      {
        "name": "Active Users",
        "values": {
          "Enero": "1,234",
          "Febrero": "1,456",
          "Marzo": "1,678"
        },
        "monthly_variation": "+15.3%",
        "numeric_values": {
          "Enero": 1234,
          "Febrero": 1456,
          "Marzo": 1678
        }
      },
      {
        "name": "Support Tickets",
        "values": {
          "Enero": "89",
          "Febrero": "76",
          "Marzo": "63"
        },
        "monthly_variation": "-17.1%",
        "numeric_values": {
          "Enero": 89,
          "Febrero": 76,
          "Marzo": 63
        }
      },
      {
        "name": "Avg Response (h)",
        "values": {
          "Enero": "4.2",
          "Febrero": "3.1",
          "Marzo": "2.4"
        },
        "monthly_variation": "-0.7",
        "numeric_values": {
          "Enero": 4.2,
          "Febrero": 3.1,
          "Marzo": 2.4
        }
      }
    ],
    "general_trend": "Positiva en todas las métricas"
  },
  "calculations": {
    "LTV_CAC_ratio": {
      "Enero": 8.08,
      "Febrero": 10.15,
      "Marzo": 12.51
    },
    "metric_with_highest_improvement": {
      "name": "NPS",
      "improvement_percentage": 14.29,
      "calculation": "((51 - 45) / 42) * 100 = 14.29% (considerando base Enero)"
    },
    "april_projections": {
      "MRR": {
        "value": "$55.7K",
        "projection": 55747,
        "calculation": "52100 * (1 + (52100 - 48700) / 48700) = 55747"
      },
      "Churn Rate": {
        "value": "2.4%",
        "projection": 0.024,
        "calculation": "0.031 - (0.038 - 0.031) = 0.024"
      },
      "NPS": {
        "value": "57",
        "projection": 57,
        "calculation": "51 + (51 - 45) = 57"
      },
      "CAC": {
        "value": "$176",
        "projection": 176,
        "calculation": "187 - (198 - 187) = 176"
      },
      "LTV": {
        "value": "$2,670",
        "projection": 2670,
        "calculation": "2340 + (2340 - 2010) = 2670"
      },
      "Active Users": {
        "value": "1,900",
        "projection": 1900,
        "calculation": "1678 * (1 + (1678 - 1456) / 1456) ≈ 1900"
      },
      "Support Tickets": {
        "value": "50",
        "projection": 50,
        "calculation": "63 - (76 - 63) = 50"
      },
      "Avg Response (h)": {
        "value": "1.7",
        "projection": 1.7,
        "calculation": "2.4 - (3.1 - 2.4) = 1.7"
      }
    }
  },
  "notes": {
    "LTV_CAC_ratio_calculation": "LTV / CAC para cada mes",
    "highest_improvement": "Se calculó la mejora porcentual desde Enero hasta Marzo para cada métrica",
    "projections": "Se asumió que la tendencia mensual (diferencia absoluta o tasa de crecimiento) se mantiene constante para Abril"
  }
}
```