# Qwen3-Coder-Next (OpenRouter FP8) — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 6.16 | quality: 5.88
- latency_total: 5.558s | tokens_per_second: 186.9
- input_tokens: 424 | output_tokens: 1039
- judge_score: 3.0 | justificación: La respuesta incluye datos no presentes en la captura de pantalla original, como LTV y Active Users, lo que afecta la precisión y relevancia, pero ofrece proyecciones y análisis que podrían ser útiles si los datos fueran correctos.

## Respuesta completa

```json
{
  "dashboard": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "analysis_date": "Marzo 2026"
  },
  "metrics": [
    {
      "name": "MRR",
      "units": "USD",
      "values": {
        "Enero": 45200,
        "Feb": 48700,
        "Marzo": 52100
      },
      "var_month_over_month": 0.070,
      "trend": "up"
    },
    {
      "name": "Churn Rate",
      "units": "percentage",
      "values": {
        "Enero": 4.2,
        "Feb": 3.8,
        "Marzo": 3.1
      },
      "var_month_over_month": -0.7,
      "trend": "up"
    },
    {
      "name": "NPS",
      "units": "score",
      "values": {
        "Enero": 42,
        "Feb": 45,
        "Marzo": 51
      },
      "var_month_over_month": 6,
      "trend": "up"
    },
    {
      "name": "CAC",
      "units": "USD",
      "values": {
        "Enero": 234,
        "Feb": 198,
        "Marzo": 187
      },
      "var_month_over_month": -11,
      "trend": "up"
    },
    {
      "name": "LTV",
      "units": "USD",
      "values": {
        "Enero": 1890,
        "Feb": 2010,
        "Marzo": 2340
      },
      "var_month_over_month": 330,
      "trend": "up"
    },
    {
      "name": "Active Users",
      "units": "count",
      "values": {
        "Enero": 1234,
        "Feb": 1456,
        "Marzo": 1678
      },
      "var_month_over_month": 0.153,
      "trend": "up"
    },
    {
      "name": "Support Tickets",
      "units": "count",
      "values": {
        "Enero": 89,
        "Feb": 76,
        "Marzo": 63
      },
      "var_month_over_month": -0.171,
      "trend": "up"
    },
    {
      "name": "Avg Response (h)",
      "units": "hours",
      "values": {
        "Enero": 4.2,
        "Feb": 3.1,
        "Marzo": 2.4
      },
      "var_month_over_month": -0.7,
      "trend": "up"
    }
  ],
  "calculated_ratios": {
    "LTV/CAC": {
      "Enero": 8.07,
      "Feb": 10.15,
      "Marzo": 12.51
    }
  },
  "max_improvement_metric": {
    "name": "LTV",
    "improvement_type": "absolute",
    "improvement_value": 330,
    "improvement_pct": 16.42
  },
  "projections_april": {
    "assumption": "Tendencia lineal basada en los últimos 2 meses (Feb→Mar)",
    "MRR": 55747,
    "Churn Rate": 2.4,
    "NPS": 57,
    "CAC": 176,
    "LTV": 2673,
    "Active Users": 1900,
    "Support Tickets": 50,
    "Avg Response (h)": 1.7
  },
  "summary": {
    "overall_trend": "positiva",
    "key_achievements": [
      "Mejora sostenida en LTV/CAC (de 8.07 a 12.51)",
      "Reducción del churn rate del 4.2% al 3.1%",
      "Aumento del NPS en 9 puntos en 3 meses"
    ],
    "note": "Proyección de Abril asume que la tendencia mensual (Feb→Mar) se mantiene constante. LTV/CAC sigue mejorando, lo que indica eficiencia creciente en adquisición y retención."
  }
}
```