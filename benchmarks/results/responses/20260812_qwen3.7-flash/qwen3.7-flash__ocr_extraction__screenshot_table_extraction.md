# Qwen 3.7 Flash — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 7.64 | quality: 8.0
- latency_total: 47.014s | tokens_per_second: 146.9
- input_tokens: 427 | output_tokens: 6908

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
    "general_trend": "↑ Positiva en todas las métricas"
  },
  "raw_data": [
    {"metric": "MRR", "unit": "USD", "values": {"enero": 45200, "feb": 48700, "marzo": 52100}},
    {"metric": "Churn Rate", "unit": "%", "values": {"enero": 4.2, "feb": 3.8, "marzo": 3.1}},
    {"metric": "NPS", "unit": "puntos", "values": {"enero": 42, "feb": 45, "marzo": 51}},
    {"metric": "CAC", "unit": "USD", "values": {"enero": 234, "feb": 198, "marzo": 187}},
    {"metric": "LTV", "unit": "USD", "values": {"enero": 1890, "feb": 2010, "marzo": 2340}},
    {"metric": "Active Users", "unit": "usuarios", "values": {"enero": 1234, "feb": 1456, "marzo": 1678}},
    {"metric": "Support Tickets", "unit": "tickets", "values": {"enero": 89, "feb": 76, "marzo": 63}},
    {"metric": "Avg Response (h)", "unit": "horas", "values": {"enero": 4.2, "feb": 3.1, "marzo": 2.4}}
  ],
  "analysis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "feb": 10.15,
      "marzo": 12.51
    },
    "best_improving_metric": {
      "name": "Avg Response (h)",
      "improvement_mom_pct": -22.58,
      "context": "Aunque otras métricas muestran mejoras absolutas o relativas, al aplicar la convención estándar ('menos es mejor' para tiempos/costos), el tiempo promedio de respuesta reduce un 22.58% respecto a Febrero, siendo la mayor mejora porcentual del período."
    },
    "april_projection": {
      "assumption": "Se mantiene la tasa de variación M/M calculada (Feb→Mar) con crecimiento compuesto mensual",
      "values": {
        "MRR": 55747,
        "Churn Rate": 2.53,
        "NPS": 57.8,
        "CAC": 176.6,
        "LTV": 2724.2,
        "Active Users": 1935,
        "Support Tickets": 52,
        "Avg Response (h)": 1.86
      }
    }
  }
}
```