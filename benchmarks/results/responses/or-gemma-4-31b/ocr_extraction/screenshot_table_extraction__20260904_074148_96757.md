# Gemma 4 31B — ocr_extraction/screenshot_table_extraction

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 8.4 | quality: 10.0
- latency_total: 585.269s | tokens_per_second: 3.7
- input_tokens: 433 | output_tokens: 2146

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
  "dashboard_data": {
    "period": "Marzo 2026",
    "metrics": [
      {
        "metrica": "MRR",
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100,
        "var_mm": "7.0%"
      },
      {
        "metrica": "Churn Rate",
        "enero": 0.042,
        "febrero": 0.038,
        "marzo": 0.031,
        "var_mm": "-0.7pp"
      },
      {
        "metrica": "NPS",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "var_mm": "+6"
      },
      {
        "metrica": "CAC",
        "enero": 234,
        "febrero": 198,
        "marzo": 187,
        "var_mm": "-$11"
      },
      {
        "metrica": "LTV",
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340,
        "var_mm": "+$330"
      },
      {
        "metrica": "Active Users",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "var_mm": "15.3%"
      },
      {
        "metrica": "Support Tickets",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "var_mm": "-17.1%"
      },
      {
        "metrica": "Avg Response (h)",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "var_mm": "-0.7"
      }
    ],
    "general_trend": "Positiva en todas las metricas"
  },
  "analysis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "best_improvement_metric": {
      "metrica": "Support Tickets",
      "improvement_percentage": "-17.1%",
      "note": "Mayor variación porcentual positiva (reducción de tickets)"
    }
  },
  "projections_april_2026": {
    "MRR": "$55.7K",
    "Churn Rate": "2.4%",
    "NPS": 57,
    "CAC": "$176",
    "LTV": "$2,670",
    "Active Users": 1935,
    "Support Tickets": 52,
    "Avg Response (h)": 1.7
  }
}
```