# Qwen 3.5 (Ollama Cloud default) — ocr_extraction/screenshot_table_extraction

- model_id: `qwen3.5:cloud`
- success: True  | final: 7.3 | quality: 7.0
- latency_total: 18.766s | tokens_per_second: 106.5
- input_tokens: 427 | output_tokens: 1999
- judge_score: 3.8 | justificación: 

## Respuesta completa

```json
{
  "dashboard_info": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "period": "Enero - Marzo 2026",
    "trend": "Positiva en todas las metricas"
  },
  "metrics_data": [
    {
      "metric": "MRR",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_m_m": "+7.0%",
      "unit": "USD"
    },
    {
      "metric": "Churn Rate",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "var_m_m": "-0.7pp",
      "unit": "%"
    },
    {
      "metric": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_m_m": "+6",
      "unit": "points"
    },
    {
      "metric": "CAC",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_m_m": "-$11",
      "unit": "USD"
    },
    {
      "metric": "LTV",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_m_m": "+$330",
      "unit": "USD"
    },
    {
      "metric": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_m_m": "+15.3%",
      "unit": "users"
    },
    {
      "metric": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_m_m": "-17.1%",
      "unit": "tickets"
    },
    {
      "metric": "Avg Response Time",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_m_m": "-0.7",
      "unit": "hours"
    }
  ],
  "analysis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "trend": "Creciente - Excelente salud del negocio",
      "calculation_note": "LTV / CAC para cada mes"
    },
    "best_improvement_metric": {
      "metric": "Avg Response Time",
      "improvement_percentage": -42.86,
      "from_enero_to_marzo": {
        "start": 4.2,
        "end": 2.4,
        "change": -1.8
      },
      "note": "Mayor mejora porcentual (reducción es positiva para esta métrica)"
    },
    "april_projection": {
      "method": "Proyección basada en tendencia M/M de Marzo",
      "metrics": {
        "MRR": {
          "projected_value": 55747,
          "unit": "USD",
          "growth_rate": "7.0%"
        },
        "Churn Rate": {
          "projected_value": 2.4,
          "unit": "%",
          "change": "-0.7pp"
        },
        "NPS": {
          "projected_value": 57,
          "unit": "points",
          "change": "+6"
        },
        "CAC": {
          "projected_value": 176,
          "unit": "USD",
          "change": "-$11"
        },
        "LTV": {
          "projected_value": 2670,
          "unit": "USD",
          "change": "+$330"
        },
        "Active Users": {
          "projected_value": 1935,
          "unit": "users",
          "growth_rate": "15.3%"
        },
        "Support Tickets": {
          "projected_value": 52,
          "unit": "tickets",
          "change": "-17.1%"
        },
        "Avg Response Time": {
          "projected_value": 1.7,
          "unit": "hours",
          "change": "-0.7"
        }
      },
      "projected_ltv_cac_ratio": 15.17,
      "confidence_note": "Proyección asume continuidad de tendencias actuales"
    }
  },
  "summary": {
    "key_insights": [
      "LTV/CAC ratio mejoró 54.8% de Enero a Marzo (8.08 → 12.51)",
      "Avg Response Time es la métrica con mayor mejora (-42.86%)",
      "Todas las métricas muestran tendencia positiva",
      "Proyección Abril mantiene momentum de crecimiento"
    ],
    "health_score": "Excelente",
    "recommendation": "Continuar estrategias actuales de retención y eficiencia operativa"
  }
}
```