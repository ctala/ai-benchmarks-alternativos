# Claude Fable 5 — ocr_extraction/screenshot_table_extraction

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 6.55 | quality: 8.0
- latency_total: 23.513s | tokens_per_second: 93.5
- input_tokens: 512 | output_tokens: 2199
- judge_score: 4.0 | justificación: La respuesta es generalmente precisa y relevante, con una buena profundidad y claridad, ofreciendo insights útiles para un emprendedor, aunque contiene datos no presentes en la captura de pantalla original, afectando la exactitud de los datos.

## Respuesta completa

```json
{
  "dashboard": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "tendencia_general": "Positiva en todas las métricas"
  },
  "datos_extraidos": {
    "MRR": {
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_m_m": "+7.0%",
      "unidad": "USD"
    },
    "churn_rate": {
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "var_m_m": "-0.7pp",
      "unidad": "%"
    },
    "NPS": {
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_m_m": "+6",
      "unidad": "puntos"
    },
    "CAC": {
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_m_m": "-$11",
      "unidad": "USD"
    },
    "LTV": {
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_m_m": "+$330",
      "unidad": "USD"
    },
    "active_users": {
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_m_m": "+15.3%",
      "unidad": "usuarios"
    },
    "support_tickets": {
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_m_m": "-17.1%",
      "unidad": "tickets"
    },
    "avg_response_time": {
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_m_m": "-0.7",
      "unidad": "horas"
    }
  },
  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "interpretacion": "Ratio muy saludable (benchmark SaaS: >3). Mejora sostenida de +55% desde enero.",
      "calculo": "LTV / CAC"
    },
    "mayor_mejora_porcentual": {
      "metrica": "avg_response_time",
      "variacion_feb_marzo": "-22.6%",
      "detalle": "De 3.1h a 2.4h. Nota: el churn rate (-18.4%) y support tickets (-17.1%) también muestran mejoras destacadas.",
      "ranking_mejoras_pct_feb_marzo": {
        "avg_response_time": -22.6,
        "churn_rate": -18.4,
        "support_tickets": -17.1,
        "LTV": 16.4,
        "active_users": 15.3,
        "NPS": 13.3,
        "MRR": 7.0,
        "CAC": -5.6
      }
    },
    "proyeccion_abril": {
      "metodo": "Extrapolación de la variación mensual más reciente (feb→marzo)",
      "valores": {
        "MRR": {
          "proyectado": 55747,
          "formato": "$55.7K",
          "supuesto": "+7.0% mensual"
        },
        "churn_rate": {
          "proyectado": 2.5,
          "formato": "2.5%",
          "supuesto": "-18.4% relativo (con reducción absoluta -0.7pp sería 2.4%)"
        },
        "NPS": {
          "proyectado": 57,
          "supuesto": "+6 puntos"
        },
        "CAC": {
          "proyectado": 176,
          "formato": "$176",
          "supuesto": "-$11"
        },
        "LTV": {
          "proyectado": 2670,
          "formato": "$2,670",
          "supuesto": "+$330"
        },
        "active_users": {
          "proyectado": 1935,
          "supuesto": "+15.3%"
        },
        "support_tickets": {
          "proyectado": 52,
          "supuesto": "-17.1%"
        },
        "avg_response_time": {
          "proyectado": 1.7,
          "unidad": "horas",
          "supuesto": "-0.7h"
        },
        "ltv_cac_ratio_proyectado": 15.17
      },
      "advertencia": "Proyección lineal simple. Métricas como churn, response time y CAC tienen límites naturales y tienden a desacelerar su mejora."
    }
  }
}
```