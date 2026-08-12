# Poolside Laguna XS 2.1 — ocr_extraction/screenshot_table_extraction

- model_id: `poolside/laguna-xs-2.1`
- success: True  | final: 7.81 | quality: 8.0
- latency_total: 16.097s | tokens_per_second: 191.8
- input_tokens: 443 | output_tokens: 3088

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
  "dashboard": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "metrics": [
      {
        "name": "MRR",
        "enero": "$45.2K",
        "febrero": "$48.7K",
        "marzo": "$52.1K",
        "var_m_m": "+7.0%",
        "ltv_cac_ratio": 22.31
      },
      {
        "name": "Churn Rate",
        "enero": "4.2%",
        "febrero": "3.8%",
        "marzo": "3.1%",
        "var_m_m": "-0.7pp",
        "ltv_cac_ratio": null
      },
      {
        "name": "NPS",
        "enero": "42",
        "febrero": "45",
        "marzo": "51",
        "var_m_m": "+6",
        "ltv_cac_ratio": null
      },
      {
        "name": "CAC",
        "enero": "$234",
        "febrero": "$198",
        "marzo": "$187",
        "var_m_m": "-$11",
        "ltv_cac_ratio": 12.51
      },
      {
        "name": "LTV",
        "enero": "$1,890",
        "febrero": "$2,010",
        "marzo": "$2,340",
        "var_m_m": "+$330",
        "ltv_cac_ratio": 12.51
      },
      {
        "name": "Active Users",
        "enero": "1,234",
        "febrero": "1,456",
        "marzo": "1,678",
        "var_m_m": "+15.3%",
        "ltv_cac_ratio": null
      },
      {
        "name": "Support Tickets",
        "enero": "89",
        "febrero": "76",
        "marzo": "63",
        "var_m_m": "-17.1%",
        "ltv_cac_ratio": null
      },
      {
        "name": "Avg Response (h)",
        "enero": "4.2",
        "febrero": "3.1",
        "marzo": "2.4",
        "var_m_m": "-0.7",
        "ltv_cac_ratio": null
      }
    ],
    "ltv_cac_ratios": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "highest_improvement": {
      "metric": "Churn Rate",
      "percentage_improvement": "26.19%"
    },
    "projection_abril": [
      {
        "name": "MRR",
        "abril": "$55.75K",
        "calculation": "52.1K * 1.07"
      },
      {
        "name": "Churn Rate",
        "abril": "2.4%",
        "calculation": "3.1% - 0.7pp"
      },
      {
        "name": "NPS",
        "abril": "57",
        "calculation": "51 + 6"
      },
      {
        "name": "CAC",
        "abril": "$176",
        "calculation": "187 - $11"
      },
      {
        "name": "LTV",
        "abril": "$2,670",
        "calculation": "2340 + $330"
      },
      {
        "name": "Active Users",
        "abril": "1,935.5",
        "calculation": "1678 * 1.153"
      },
      {
        "name": "Support Tickets",
        "abril": "52.2",
        "calculation": "63 * 0.829"
      },
      {
        "name": "Avg Response (h)",
        "abril": "1.7h",
        "calculation": "2.4 - 0.7h"
      }
    ]
  }
}
```