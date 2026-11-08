# GPT-OSS 20B — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.73 | quality: 8.0
- latency_total: 20.09s | tokens_per_second: 90.3
- input_tokens: 427 | output_tokens: 1815

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
  "metrics": {
    "MRR": {
      "January": 45200,
      "February": 48700,
      "March": 52100,
      "April_projection": 55770
    },
    "Churn Rate": {
      "January": 4.2,
      "February": 3.8,
      "March": 3.1,
      "April_projection": 2.4
    },
    "NPS": {
      "January": 42,
      "February": 45,
      "March": 51,
      "April_projection": 57
    },
    "CAC": {
      "January": 234,
      "February": 198,
      "March": 187,
      "April_projection": 176
    },
    "LTV": {
      "January": 1890,
      "February": 2010,
      "March": 2340,
      "April_projection": 2670
    },
    "Active Users": {
      "January": 1234,
      "February": 1456,
      "March": 1678,
      "April_projection": 1934
    },
    "Support Tickets": {
      "January": 89,
      "February": 76,
      "March": 63,
      "April_projection": 52
    },
    "Avg Response (h)": {
      "January": 4.2,
      "February": 3.1,
      "March": 2.4,
      "April_projection": 1.7
    }
  },
  "ltv_cac_ratio": {
    "January": 8.08,
    "February": 10.15,
    "March": 12.52
  },
  "best_improvement_metric": {
    "name": "Active Users",
    "percentage_change": 15.3
  },
  "projections_for_April": {
    "MRR": 55770,
    "Churn Rate": 2.4,
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "Active Users": 1934,
    "Support Tickets": 52,
    "Avg Response (h)": 1.7
  }
}
```
