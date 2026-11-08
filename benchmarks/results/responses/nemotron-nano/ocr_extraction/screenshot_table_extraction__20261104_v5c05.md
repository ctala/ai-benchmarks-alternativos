# Nemotron 3 Nano 30B — ocr_extraction/screenshot_table_extraction

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 5.2 | quality: 4.0
- latency_total: 4.799s | tokens_per_second: 63.8
- input_tokens: 435 | output_tokens: 306

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
  "period": "Marzo 2026",
  "metrics": {
    "MRR": 52100,
    "Churn Rate": 0.031,
    "NPS": 51,
    "CAC": 187,
    "LTV": 2340,
    "Active Users": 1678,
    "Support Tickets": 63,
    "Avg Response (h)": 2.4
  },
  "LTV_CAC_ratios": {
    "Enero": 8.12,
    "Febrero": 10.16,
    "Marzo": 12.51
  },
  "metric_with_greatest_improvement_percent": {
    "metric": "Churn Rate",
    "percentage_improvement": 25.81
  },
  "projected_april_values": {
    "MRR": 55512,
    "Churn Rate": 0.024,
    "NPS": 57,
    "CAC": 176.25,
    "LTV": 2808,
    "Active Users": 1929.7,
    "Support Tickets": 52.11,
    "Avg Response (h)": 1.7
  }
}