# GPT-5.4 — ocr_extraction/screenshot_table_extraction

- model_id: `gpt-5.4`
- success: True  | final: 6.46 | quality: 6.16
- latency_total: 12.77s | tokens_per_second: 94.4
- input_tokens: 379 | output_tokens: 1206
- judge_score: 3.2 | justificación: 

## Respuesta completa

{
  "dashboard": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "period": {
      "months": ["Enero", "Feb", "Marzo"],
      "projection_month": "Abril",
      "year": 2026
    },
    "general_trend": "Positiva en todas las metricas"
  },
  "data": {
    "MRR": {
      "unit": "USD",
      "Enero": 45200,
      "Feb": 48700,
      "Marzo": 52100,
      "Var_M_M": {
        "display": "+7.0%",
        "type": "percent"
      }
    },
    "Churn_Rate": {
      "unit": "percent",
      "Enero": 4.2,
      "Feb": 3.8,
      "Marzo": 3.1,
      "Var_M_M": {
        "display": "-0.7pp",
        "type": "percentage_points"
      }
    },
    "NPS": {
      "unit": "score",
      "Enero": 42,
      "Feb": 45,
      "Marzo": 51,
      "Var_M_M": {
        "display": "+6",
        "type": "absolute"
      }
    },
    "CAC": {
      "unit": "USD",
      "Enero": 234,
      "Feb": 198,
      "Marzo": 187,
      "Var_M_M": {
        "display": "-$11",
        "type": "absolute"
      }
    },
    "LTV": {
      "unit": "USD",
      "Enero": 1890,
      "Feb": 2010,
      "Marzo": 2340,
      "Var_M_M": {
        "display": "+$330",
        "type": "absolute"
      }
    },
    "Active_Users": {
      "unit": "count",
      "Enero": 1234,
      "Feb": 1456,
      "Marzo": 1678,
      "Var_M_M": {
        "display": "+15.3%",
        "type": "percent"
      }
    },
    "Support_Tickets": {
      "unit": "count",
      "Enero": 89,
      "Feb": 76,
      "Marzo": 63,
      "Var_M_M": {
        "display": "-17.1%",
        "type": "percent"
      }
    },
    "Avg_Response_h": {
      "unit": "hours",
      "Enero": 4.2,
      "Feb": 3.1,
      "Marzo": 2.4,
      "Var_M_M": {
        "display": "-0.7",
        "type": "absolute"
      }
    }
  },
  "calculations": {
    "LTV_CAC_ratio": {
      "Enero": 8.08,
      "Feb": 10.15,
      "Marzo": 12.51
    },
    "metric_with_greatest_percentage_improvement": {
      "metric": "Support_Tickets",
      "value": 17.1,
      "direction": "decrease_is_better",
      "basis": "La mayor mejora porcentual en valor absoluto es una reduccion de 17.1% de Febrero a Marzo"
    }
  },
  "projection_Abril": {
    "method": "Se proyecta Abril manteniendo la misma variacion mensual observada de Febrero a Marzo para cada metrica",
    "values": {
      "MRR": {
        "unit": "USD",
        "projected_value": 55747,
        "applied_change": "+7.0%"
      },
      "Churn_Rate": {
        "unit": "percent",
        "projected_value": 2.4,
        "applied_change": "-0.7pp"
      },
      "NPS": {
        "unit": "score",
        "projected_value": 57,
        "applied_change": "+6"
      },
      "CAC": {
        "unit": "USD",
        "projected_value": 176,
        "applied_change": "-11"
      },
      "LTV": {
        "unit": "USD",
        "projected_value": 2670,
        "applied_change": "+330"
      },
      "Active_Users": {
        "unit": "count",
        "projected_value": 1935,
        "applied_change": "+15.3%"
      },
      "Support_Tickets": {
        "unit": "count",
        "projected_value": 52,
        "applied_change": "-17.1%"
      },
      "Avg_Response_h": {
        "unit": "hours",
        "projected_value": 1.7,
        "applied_change": "-0.7"
      }
    }
  },
  "notes": {
    "assumptions": [
      "Para metricas con Var M/M expresada en porcentaje, se aplica ese mismo porcentaje a Marzo para proyectar Abril",
      "Para metricas con Var M/M expresada en puntos porcentuales o cambio absoluto, se aplica el mismo delta absoluto a Marzo para proyectar Abril",
      "La mejora porcentual se evalua por magnitud relativa favorable: aumentos para metricas positivas y reducciones para metricas donde menor es mejor"
    ],
    "rounding": "Ratios redondeados a 2 decimales; proyecciones de conteos y USD sin decimales cuando corresponde"
  }
}