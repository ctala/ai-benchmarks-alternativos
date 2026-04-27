# MiMo-V2-Omni (multimodal) — ocr_extraction/screenshot_table_extraction

- model_id: `xiaomi/mimo-v2-omni`
- success: True  | final: 6.72 | quality: 6.64
- latency_total: 13.576s | tokens_per_second: 102.7
- input_tokens: 666 | output_tokens: 1394
- judge_score: 3.8 | justificación: 

## Respuesta completa

```json
{
  "dashboard_data": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "metrics": [
      {
        "name": "MRR",
        "values": {
          "Enero": 45200,
          "Febrero": 48700,
          "Marzo": 52100
        },
        "var_m_m": "+7.0%"
      },
      {
        "name": "Churn Rate",
        "values": {
          "Enero": 4.2,
          "Febrero": 3.8,
          "Marzo": 3.1
        },
        "var_m_m": "-0.7pp"
      },
      {
        "name": "NPS",
        "values": {
          "Enero": 42,
          "Febrero": 45,
          "Marzo": 51
        },
        "var_m_m": "+6"
      },
      {
        "name": "CAC",
        "values": {
          "Enero": 234,
          "Febrero": 198,
          "Marzo": 187
        },
        "var_m_m": "-$11"
      },
      {
        "name": "LTV",
        "values": {
          "Enero": 1890,
          "Febrero": 2010,
          "Marzo": 2340
        },
        "var_m_m": "+$330"
      },
      {
        "name": "Active Users",
        "values": {
          "Enero": 1234,
          "Febrero": 1456,
          "Marzo": 1678
        },
        "var_m_m": "+15.3%"
      },
      {
        "name": "Support Tickets",
        "values": {
          "Enero": 89,
          "Febrero": 76,
          "Marzo": 63
        },
        "var_m_m": "-17.1%"
      },
      {
        "name": "Avg Response (h)",
        "values": {
          "Enero": 4.2,
          "Febrero": 3.1,
          "Marzo": 2.4
        },
        "var_m_m": "-0.7"
      }
    ],
    "general_trend": "↑ Positiva en todas las métricas"
  },
  "analysis": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Febrero": 10.15,
      "Marzo": 12.51,
      "note": "Ratio = LTV / CAC. Crecimiento consistente indica mayor eficiencia en adquisición."
    },
    "metric_with_highest_percentage_improvement": {
      "metric": "Support Tickets",
      "improvement_percentage": -17.1,
      "explanation": "Reducción del 17.1% en tickets de soporte (de 76 a 63), la mayor mejora porcentual absoluta entre todas las métricas."
    },
    "april_projections": {
      "assumption": "Proyección basada en la tendencia promedio de los últimos 2 meses (Feb-Mar), aplicando el mismo patrón de crecimiento/decrecimiento.",
      "projections": {
        "MRR": {
          "value": 55700,
          "trend": "+$3,600 (≈7.0% crecimiento similar a Mar)"
        },
        "Churn Rate": {
          "value": 2.4,
          "trend": "-0.7pp (misma reducción que Feb-Mar)"
        },
        "NPS": {
          "value": 57,
          "trend": "+6 puntos (mismo incremento que Feb-Mar)"
        },
        "CAC": {
          "value": 176,
          "trend": "-$11 (misma reducción que Feb-Mar)"
        },
        "LTV": {
          "value": 2670,
          "trend": "+$330 (mismo incremento que Feb-Mar)"
        },
        "Active Users": {
          "value": 1900,
          "trend": "+222 usuarios (≈15.3% crecimiento similar a Mar)"
        },
        "Support Tickets": {
          "value": 50,
          "trend": "-13 tickets (≈17.1% reducción similar a Mar)"
        },
        "Avg Response (h)": {
          "value": 1.7,
          "trend": "-0.7h (misma reducción que Feb-Mar)"
        }
      },
      "note": "Proyecciones optimistas basadas en tendencia actual. Factores externos podrían alterar estos valores."
    }
  }
}
```