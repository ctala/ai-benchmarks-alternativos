# KAT Coder Pro v2.5 — ocr_extraction/screenshot_table_extraction

- model_id: `kwaipilot/kat-coder-pro-v2.5`
- success: True  | final: 7.37 | quality: 8.0
- latency_total: 10.464s | tokens_per_second: 107.6
- input_tokens: 427 | output_tokens: 1126

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
  "dashboard": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "period": "Marzo 2026",
    "trend": "Positiva en todas las metricas"
  },
  "metrics": [
    {
      "name": "MRR",
      "unit": "currency",
      "values": {
        "Enero": 45200,
        "Feb": 48700,
        "Marzo": 52100
      },
      "var_m_m": "+7.0%"
    },
    {
      "name": "Churn Rate",
      "unit": "percentage",
      "values": {
        "Enero": 4.2,
        "Feb": 3.8,
        "Marzo": 3.1
      },
      "var_m_m": "-0.7pp"
    },
    {
      "name": "NPS",
      "unit": "score",
      "values": {
        "Enero": 42,
        "Feb": 45,
        "Marzo": 51
      },
      "var_m_m": "+6"
    },
    {
      "name": "CAC",
      "unit": "currency",
      "values": {
        "Enero": 234,
        "Feb": 198,
        "Marzo": 187
      },
      "var_m_m": "-$11"
    },
    {
      "name": "LTV",
      "unit": "currency",
      "values": {
        "Enero": 1890,
        "Feb": 2010,
        "Marzo": 2340
      },
      "var_m_m": "+$330"
    },
    {
      "name": "Active Users",
      "unit": "count",
      "values": {
        "Enero": 1234,
        "Feb": 1456,
        "Marzo": 1678
      },
      "var_m_m": "+15.3%"
    },
    {
      "name": "Support Tickets",
      "unit": "count",
      "values": {
        "Enero": 89,
        "Feb": 76,
        "Marzo": 63
      },
      "var_m_m": "-17.1%"
    },
    {
      "name": "Avg Response (h)",
      "unit": "hours",
      "values": {
        "Enero": 4.2,
        "Feb": 3.1,
        "Marzo": 2.4
      },
      "var_m_m": "-0.7"
    }
  ],
  "analysis": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Feb": 10.15,
      "Marzo": 12.51
    },
    "best_improvement_metric": {
      "name": "Active Users",
      "var_m_m": "+15.3%",
      "reason": "Mayor crecimiento porcentual mes a mes entre todas las metricas"
    },
    "april_projection": {
      "methodology": "Proyeccion lineal basada en la tendencia de crecimiento M/M de Marzo",
      "values": {
        "MRR": 55747,
        "Churn_Rate": 2.4,
        "NPS": 57,
        "CAC": 176,
        "LTV": 2670,
        "Active_Users": 1935,
        "Support_Tickets": 52,
        "Avg_Response_h": 1.7
      }
    }
  }
}