# Ministral 14B — ocr_extraction/screenshot_table_extraction

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 7.69 | quality: 8.0
- latency_total: 13.935s | tokens_per_second: 92.1
- input_tokens: 422 | output_tokens: 1283
- judge_score: 4.0 | justificación: La respuesta es generalmente precisa y relevante, pero incluye datos no presentes en la captura de pantalla original, afectando la precisión; sin embargo, ofrece una buena profundidad y utilidad práctica con proyecciones y cálculos útiles.

## Respuesta completa

```json
{
  "dashboard_metadata": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "period": "Marzo 2026",
    "trend": "↑ Positiva en todas las métricas"
  },
  "metrics": [
    {
      "name": "MRR",
      "values": {
        "Enero": 45200,
        "Febrero": 48700,
        "Marzo": 52100
      },
      "variation": {
        "Feb_Mar": "+7.0%"
      }
    },
    {
      "name": "Churn Rate",
      "values": {
        "Enero": 4.2,
        "Febrero": 3.8,
        "Marzo": 3.1
      },
      "variation": {
        "Feb_Mar": "-0.7pp"
      }
    },
    {
      "name": "NPS",
      "values": {
        "Enero": 42,
        "Febrero": 45,
        "Marzo": 51
      },
      "variation": {
        "Feb_Mar": "+6"
      }
    },
    {
      "name": "CAC",
      "values": {
        "Enero": 234,
        "Febrero": 198,
        "Marzo": 187
      },
      "variation": {
        "Feb_Mar": "-11"
      }
    },
    {
      "name": "LTV",
      "values": {
        "Enero": 1890,
        "Febrero": 2010,
        "Marzo": 2340
      },
      "variation": {
        "Feb_Mar": "+330"
      }
    },
    {
      "name": "Active Users",
      "values": {
        "Enero": 1234,
        "Febrero": 1456,
        "Marzo": 1678
      },
      "variation": {
        "Feb_Mar": "+15.3%"
      }
    },
    {
      "name": "Support Tickets",
      "values": {
        "Enero": 89,
        "Febrero": 76,
        "Marzo": 63
      },
      "variation": {
        "Feb_Mar": "-17.1%"
      }
    },
    {
      "name": "Avg Response (h)",
      "values": {
        "Enero": 4.2,
        "Febrero": 3.1,
        "Marzo": 2.4
      },
      "variation": {
        "Feb_Mar": "-0.7"
      }
    }
  ],
  "calculations": {
    "LTV_CAC_ratio": {
      "Enero": 1890 / 234,
      "Febrero": 2010 / 198,
      "Marzo": 2340 / 187,
      "values": {
        "Enero": 8.077,
        "Febrero": 10.152,
        "Marzo": 12.513
      }
    },
    "metric_with_highest_improvement": {
      "name": "Active Users",
      "improvement": "+15.3%",
      "reason": "Mayor variación porcentual positiva en el período Febrero-Marzo"
    }
  },
  "projections": {
    "method": "Manteniendo la tendencia de mejora porcentual observada en Febrero-Marzo",
    "Abril": {
      "MRR": {
        "value": 52100 * 1.07,
        "projected": 55747
      },
      "Churn Rate": {
        "value": 3.1 - 0.7,
        "projected": 2.4
      },
      "NPS": {
        "value": 51 + 6,
        "projected": 57
      },
      "CAC": {
        "value": 187 - 11,
        "projected": 176
      },
      "LTV": {
        "value": 2340 + 330,
        "projected": 2670
      },
      "Active Users": {
        "value": 1678 * 1.153,
        "projected": 1933
      },
      "Support Tickets": {
        "value": 63 * (1 - 0.171),
        "projected": 52
      },
      "Avg Response (h)": {
        "value": 2.4 - 0.7,
        "projected": 1.7
      },
      "LTV_CAC_ratio": {
        "value": 2670 / 176,
        "projected": 15.17
      }
    }
  },
  "notes": [
    "1. El LTV/CAC ratio se calcula como LTV dividido por CAC (ejemplo: Marzo = 2340 / 187 = 12.513).",
    "2. La mejora porcentual más alta fue en 'Active Users' (+15.3%).",
    "3. Las proyecciones para Abril asumen que las tendencias de mejora se mantienen linealmente.",
    "4. Para métricas con variaciones absolutas (ej: CAC, Support Tickets), se aplicó la misma diferencia observada en Febrero-Marzo."
  ]
}
```