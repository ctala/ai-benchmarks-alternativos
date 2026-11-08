# Mercury 2.5 — ocr_extraction/screenshot_table_extraction

- model_id: `inception/mercury-2.5`
- success: True  | final: 8.3 | quality: 8.0
- latency_total: 1.902s | tokens_per_second: 399.0
- input_tokens: 408 | output_tokens: 759

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

{
  "dashboard_title": "KPIs Marzo 2026",
  "data": {
    "MRR": {
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100
    },
    "churn_rate": {
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1
    },
    "nps": {
      "enero": 42,
      "febrero": 45,
      "marzo": 51
    },
    "cac": {
      "enero": 234,
      "febrero": 198,
      "marzo": 187
    },
    "ltv": {
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340
    },
    "active_users": {
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678
    },
    "support_tickets": {
      "enero": 89,
      "febrero": 76,
      "marzo": 63
    },
    "avg_response_hours": {
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4
    }
  },
  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51
  },
  "best_improvement": {
    "metric": "Avg Response (h)",
    "percent_change": -42.86,
    "note": "Menor tiempo de respuesta es mejora positiva. Cambio relativo más grande (42.86% de reducción)."
  },
  "proyccion_abril": {
    "method": "Tendencia M/M media observada",
    "metrics": {
      "MRR": {
        "value": 55800,
        "delta_mom": 7.1
      },
      "churn_rate": {
        "value": 2.45,
        "delta_mom": -0.65
      },
      "nps": {
        "value": 55,
        "delta_mom": 4
      },
      "cac": {
        "value": 179,
        "delta_mom": -8
      },
      "ltv": {
        "value": 2580,
        "delta_mom": 240
      },
      "active_users": {
        "value": 1910,
        "delta_mom": 13.8
      },
      "support_tickets": {
        "value": 52,
        "delta_mom": -17.5
      },
      "avg_response_hours": {
        "value": 1.9,
        "delta_mom": -0.5
      }
    }
  }
}