# Qwen 3.5 397B — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 8.62 | quality: 10.0
- latency_total: 17.492s | tokens_per_second: 57.7
- input_tokens: 429 | output_tokens: 1010

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
    "trend_summary": "Positiva en todas las metricas"
  },
  "extracted_data": [
    {
      "metric": "MRR",
      "unit": "currency",
      "values": {
        "Enero": 45200,
        "Feb": 48700,
        "Marzo": 52100
      },
      "var_m_m": "+7.0%"
    },
    {
      "metric": "Churn Rate",
      "unit": "percentage_points",
      "values": {
        "Enero": 4.2,
        "Feb": 3.8,
        "Marzo": 3.1
      },
      "var_m_m": "-0.7pp"
    },
    {
      "metric": "NPS",
      "unit": "score",
      "values": {
        "Enero": 42,
        "Feb": 45,
        "Marzo": 51
      },
      "var_m_m": "+6"
    },
    {
      "metric": "CAC",
      "unit": "currency",
      "values": {
        "Enero": 234,
        "Feb": 198,
        "Marzo": 187
      },
      "var_m_m": "-$11"
    },
    {
      "metric": "LTV",
      "unit": "currency",
      "values": {
        "Enero": 1890,
        "Feb": 2010,
        "Marzo": 2340
      },
      "var_m_m": "+$330"
    },
    {
      "metric": "Active Users",
      "unit": "count",
      "values": {
        "Enero": 1234,
        "Feb": 1456,
        "Marzo": 1678
      },
      "var_m_m": "+15.3%"
    },
    {
      "metric": "Support Tickets",
      "unit": "count",
      "values": {
        "Enero": 89,
        "Feb": 76,
        "Marzo": 63
      },
      "var_m_m": "-17.1%"
    },
    {
      "metric": "Avg Response (h)",
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
      "Marzo": 12.51,
      "calculation_note": "Ratio calculado como LTV / CAC para cada mes."
    },
    "highest_percentage_improvement": {
      "metric": "Support Tickets",
      "improvement_value": -17.1,
      "direction": "decrease",
      "reasoning": "Aunque 'Active Users' tuvo un crecimiento del 15.3%, la reducción de 'Support Tickets' en un 17.1% representa el mayor cambio porcentual absoluto en dirección positiva (menos tickets es mejor). Si se considera solo crecimiento positivo, sería 'Active Users' (+15.3%)."
    },
    "april_projection": {
      "methodology": "Proyección lineal basada en la diferencia absoluta entre Febrero y Marzo aplicada a Marzo.",
      "projected_values": {
        "MRR": 55500,
        "Churn Rate": 2.4,
        "NPS": 57,
        "CAC": 176,
        "LTV": 2670,
        "Active Users": 1900,
        "Support Tickets": 50,
        "Avg Response (h)": 1.7
      }
    }
  }
}
```