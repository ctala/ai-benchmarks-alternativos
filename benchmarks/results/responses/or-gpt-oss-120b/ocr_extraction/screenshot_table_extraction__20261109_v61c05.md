# GPT-OSS 120B — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 7.81 | quality: 8.0
- latency_total: 14.472s | tokens_per_second: 145.3
- input_tokens: 440 | output_tokens: 2103

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
      "Jan": 45200,
      "Feb": 48700,
      "Mar": 52100,
      "unit": "USD"
    },
    "ChurnRate": {
      "Jan": 4.2,
      "Feb": 3.8,
      "Mar": 3.1,
      "unit": "percent"
    },
    "NPS": {
      "Jan": 42,
      "Feb": 45,
      "Mar": 51,
      "unit": "points"
    },
    "CAC": {
      "Jan": 234,
      "Feb": 198,
      "Mar": 187,
      "unit": "USD"
    },
    "LTV": {
      "Jan": 1890,
      "Feb": 2010,
      "Mar": 2340,
      "unit": "USD"
    },
    "ActiveUsers": {
      "Jan": 1234,
      "Feb": 1456,
      "Mar": 1678,
      "unit": "count"
    },
    "SupportTickets": {
      "Jan": 89,
      "Feb": 76,
      "Mar": 63,
      "unit": "count"
    },
    "AvgResponseHours": {
      "Jan": 4.2,
      "Feb": 3.1,
      "Mar": 2.4,
      "unit": "hours"
    }
  },
  "ltv_cac_ratio": {
    "Jan": 8.08,
    "Feb": 10.15,
    "Mar": 12.52,
    "AprProjected": 15.17,
    "note": "Rounded to two decimal places"
  },
  "highest_improvement_metric": {
    "metric": "Active Users",
    "improvement": "15.3%",
    "type": "percentage",
    "period": "Feb→Mar"
  },
  "projection_april": {
    "MRR": 55747,
    "ChurnRate": 2.4,
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "ActiveUsers": 1935,
    "SupportTickets": 52,
    "AvgResponseHours": 1.7,
    "LTV_CAC_Ratio": 15.17,
    "assumptions": "April values are obtained by applying the most recent month‑over‑month change (Feb→Mar) to the March figures."
  }
}
```