# Qwen3-Coder-Next (OpenRouter FP8) — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 7.54 | quality: 8.0
- latency_total: 14.936s | tokens_per_second: 57.0
- input_tokens: 424 | output_tokens: 852

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
    "tendencia_general": "Positiva en todas las metricas"
  },
  "metrics": [
    {
      "name": "MRR",
      "units": "USD",
      "values": {
        "Enero": 45200,
        "Feb": 48700,
        "Marzo": 52100
      },
      "var_mm_percent": 7.0
    },
    {
      "name": "Churn Rate",
      "units": "percent",
      "values": {
        "Enero": 4.2,
        "Feb": 3.8,
        "Marzo": 3.1
      },
      "var_mm_percent": -18.42,
      "var_mm_pp": -0.7
    },
    {
      "name": "NPS",
      "units": "score",
      "values": {
        "Enero": 42,
        "Feb": 45,
        "Marzo": 51
      },
      "var_mm_percent": 13.33
    },
    {
      "name": "CAC",
      "units": "USD",
      "values": {
        "Enero": 234,
        "Feb": 198,
        "Marzo": 187
      },
      "var_mm_percent": -5.56
    },
    {
      "name": "LTV",
      "units": "USD",
      "values": {
        "Enero": 1890,
        "Feb": 2010,
        "Marzo": 2340
      },
      "var_mm_percent": 16.42
    },
    {
      "name": "Active Users",
      "units": "count",
      "values": {
        "Enero": 1234,
        "Feb": 1456,
        "Marzo": 1678
      },
      "var_mm_percent": 15.25
    },
    {
      "name": "Support Tickets",
      "units": "count",
      "values": {
        "Enero": 89,
        "Feb": 76,
        "Marzo": 63
      },
      "var_mm_percent": -17.11
    },
    {
      "name": "Avg Response (h)",
      "units": "hours",
      "values": {
        "Enero": 4.2,
        "Feb": 3.1,
        "Marzo": 2.4
      },
      "var_mm_percent": -22.58
    }
  ],
  "calculated_ratios": {
    "LTV_CAC_ratio": {
      "Enero": 8.08,
      "Feb": 10.15,
      "Marzo": 12.51
    }
  },
  "analysis": {
    "metrica_mayor_mejora_percentual": {
      "name": "LTV",
      "improvement_percent": 16.42,
      "reason": "Incremento del 16.42% mes a mes, el más alto entre las métricas con crecimiento positivo"
    },
    "proyeccion_abril_tendencia_lineal": {
      "MRR": 54700,
      "Churn_Rate": 2.4,
      "NPS": 55,
      "CAC": 176,
      "LTV": 2620,
      "Active_Users": 1892,
      "Support_Tickets": 51,
      "Avg_Response_h": 1.7
    }
  }
}
```