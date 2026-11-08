# Qwen 3.8 27B — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 35.849s | tokens_per_second: 42.2
- input_tokens: 429 | output_tokens: 1513

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
  "dashboard_metadata": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "period": "Enero - Marzo 2026",
    "general_trend": "↑ Positiva en todas las metricas"
  },
  "extracted_data": {
    "metrics": [
      {
        "name": "MRR",
        "values": {
          "Enero": 45200,
          "Feb": 48700,
          "Marzo": 52100
        },
        "unit": "USD",
        "var_mom_marzo": "+7.0%"
      },
      {
        "name": "Churn Rate",
        "values": {
          "Enero": 4.2,
          "Feb": 3.8,
          "Marzo": 3.1
        },
        "unit": "percent",
        "var_mom_marzo": "-0.7pp"
      },
      {
        "name": "NPS",
        "values": {
          "Enero": 42,
          "Feb": 45,
          "Marzo": 51
        },
        "unit": "score",
        "var_mom_marzo": "+6"
      },
      {
        "name": "CAC",
        "values": {
          "Enero": 234,
          "Feb": 198,
          "Marzo": 187
        },
        "unit": "USD",
        "var_mom_marzo": "-$11"
      },
      {
        "name": "LTV",
        "values": {
          "Enero": 1890,
          "Feb": 2010,
          "Marzo": 2340
        },
        "unit": "USD",
        "var_mom_marzo": "+$330"
      },
      {
        "name": "Active Users",
        "values": {
          "Enero": 1234,
          "Feb": 1456,
          "Marzo": 1678
        },
        "unit": "users",
        "var_mom_marzo": "+15.3%"
      },
      {
        "name": "Support Tickets",
        "values": {
          "Enero": 89,
          "Feb": 76,
          "Marzo": 63
        },
        "unit": "tickets",
        "var_mom_marzo": "-17.1%"
      },
      {
        "name": "Avg Response (h)",
        "values": {
          "Enero": 4.2,
          "Feb": 3.1,
          "Marzo": 2.4
        },
        "unit": "hours",
        "var_mom_marzo": "-0.7"
      }
    ]
  },
  "ltv_cac_ratio": {
    "Enero": 8.08,
    "Feb": 10.15,
    "Marzo": 12.51,
    "note": "Ratio = LTV / CAC. Mejora significativa de 8.08x a 12.51x en 3 meses."
  },
  "best_improving_metric": {
    "name": "Support Tickets",
    "improvement_percentage": 29.21,
    "details": "Disminución del 29.21% desde Enero (89) a Marzo (63), indicando mejora en eficiencia operativa y reducción de carga de soporte.",
    "calculation": "((89 - 63) / 89) * 100 = 29.21%"
  },
  "april_projection": {
    "methodology": "Extrapolación lineal basada en el promedio de variaciones mensuales (Enero→Feb, Feb→Marzo).",
    "projections": {
      "MRR": {
        "value": 55470,
        "unit": "USD",
        "avg_monthly_change": 3450,
        "note": "Promedio de +$3.5K (Ene-Feb) y +$3.4K (Feb-Mar)"
      },
      "Churn Rate": {
        "value": 2.75,
        "unit": "percent",
        "avg_monthly_change": -0.55,
        "note": "Promedio de -0.4pp y -0.7pp"
      },
      "NPS": {
        "value": 56,
        "unit": "score",
        "avg_monthly_change": 4.5,
        "note": "Promedio de +3 y +6"
      },
      "CAC": {
        "value": 174,
        "unit": "USD",
        "avg_monthly_change": -17.5,
        "note": "Promedio de -$36 y -$11"
      },
      "LTV": {
        "value": 2610,
        "unit": "USD",
        "avg_monthly_change": 270,
        "note": "Promedio de +$120 y +$330"
      },
      "Active Users": {
        "value": 1896,
        "unit": "users",
        "avg_monthly_change": 222,
        "note": "Promedio de +222 (Ene-Feb) y +222 (Feb-Mar)"
      },
      "Support Tickets": {
        "value": 52.5,
        "unit": "tickets",
        "avg_monthly_change": -13.5,
        "note": "Promedio de -13 y -13.5"
      },
      "Avg Response (h)": {
        "value": 1.95,
        "unit": "hours",
        "avg_monthly_change": -0.85,
        "note": "Promedio de -1.1h y -0.7h"
      }
    },
    "disclaimer": "Proyecciones basadas en tendencia lineal. No consideran estacionalidad, eventos externos o cambios estratégicos."
  }
}
```