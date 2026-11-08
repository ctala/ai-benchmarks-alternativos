# Gemma 4 26B MoE (3.8B activos) — ocr_extraction/screenshot_table_extraction

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 8.98 | quality: 10.0
- latency_total: 21.951s | tokens_per_second: 36.3
- input_tokens: 431 | output_tokens: 796

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
    "trend_general": "Positiva"
  },
  "raw_data": {
    "metrics": [
      {
        "metric": "MRR",
        "january": 45200,
        "february": 48700,
        "march": 52100,
        "var_mom": "+7.0%"
      },
      {
        "metric": "Churn Rate",
        "january": 4.2,
        "february": 3.8,
        "march": 3.1,
        "var_mom": "-0.7pp"
      },
      {
        "metric": "NPS",
        "january": 42,
        "february": 45,
        "march": 51,
        "var_mom": "+6"
      },
      {
        "metric": "CAC",
        "january": 234,
        "february": 198,
        "march": 187,
        "var_mom": "-$11"
      },
      {
        "metric": "LTV",
        "january": 1890,
        "february": 2010,
        "march": 2340,
        "var_mom": "+$330"
      },
      {
        "metric": "Active Users",
        "january": 1234,
        "february": 1456,
        "march": 1678,
        "var_mom": "+15.3%"
      },
      {
        "metric": "Support Tickets",
        "january": 89,
        "february": 76,
        "march": 63,
        "var_mom": "-17.1%"
      },
      {
        "metric": "Avg Response (h)",
        "january": 4.2,
        "february": 3.1,
        "march": 2.4,
        "var_mom": "-0.7"
      }
    ]
  },
  "analysis": {
    "ltv_cac_ratio": {
      "january": 8.08,
      "february": 10.15,
      "march": 12.51
    },
    "highest_improvement_metric": {
      "metric": "Support Tickets",
      "improvement_percentage": "-17.1%",
      "note": "Basado en la reducción de volumen de tickets (mejora operativa)"
    },
    "projections_april": {
      "methodology": "Lineal/Tendencia M/M",
      "projected_values": {
        "MRR": 55747,
        "Churn Rate": 2.4,
        "NPS": 57,
        "CAC": 176,
        "LTV": 2670,
        "Active Users": 1936,
        "Support Tickets": 52,
        "Avg Response (h)": 1.7
      }
    }
  }
}
```