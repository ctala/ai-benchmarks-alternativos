# Gemma 4 31B — ocr_extraction/screenshot_table_extraction

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 7.54 | quality: 8.0
- latency_total: 29.261s | tokens_per_second: 68.7
- input_tokens: 433 | output_tokens: 2010

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
  "dashboard_info": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "general_trend": "Positiva en todas las métricas"
  },
  "extracted_metrics": [
    {
      "metric": "MRR",
      "january": 45200,
      "february": 48700,
      "march": 52100,
      "variance_mm": "+7.0%"
    },
    {
      "metric": "Churn Rate",
      "january": 0.042,
      "february": 0.038,
      "march": 0.031,
      "variance_mm": "-0.7pp"
    },
    {
      "metric": "NPS",
      "january": 42,
      "february": 45,
      "march": 51,
      "variance_mm": "+6"
    },
    {
      "metric": "CAC",
      "january": 234,
      "february": 198,
      "march": 187,
      "variance_mm": "-$11"
    },
    {
      "metric": "LTV",
      "january": 1890,
      "february": 2010,
      "march": 2340,
      "variance_mm": "+$330"
    },
    {
      "metric": "Active Users",
      "january": 1234,
      "february": 1456,
      "march": 1678,
      "variance_mm": "+15.3%"
    },
    {
      "metric": "Support Tickets",
      "january": 89,
      "february": 76,
      "march": 63,
      "variance_mm": "-17.1%"
    },
    {
      "metric": "Avg Response (h)",
      "january": 4.2,
      "february": 3.1,
      "march": 2.4,
      "variance_mm": "-0.7"
    }
  ],
  "ltv_cac_ratio": {
    "january": 8.08,
    "february": 10.15,
    "march": 12.51
  },
  "analysis": {
    "highest_percentage_improvement": {
      "metric": "Avg Response (h)",
      "improvement_relative": "-22.58%",
      "note": "Calculado sobre la reducción del tiempo de respuesta de Feb a Mar (2.4 vs 3.1)"
    }
  },
  "april_projections": {
    "methodology": "Linear projection based on March M/M variance",
    "projections": {
      "MRR": "$55.7K",
      "Churn Rate": "2.4%",
      "NPS": 57,
      "CAC": "$176",
      "LTV": "$2,670",
      "Active Users": 1934,
      "Support Tickets": 52,
      "Avg Response (h)": 1.7
    }
  }
}
```