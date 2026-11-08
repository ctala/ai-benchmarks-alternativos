# Qwen 3-Next 80B Instruct — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 7.85 | quality: 8.0
- latency_total: 3.904s | tokens_per_second: 221.9
- input_tokens: 424 | output_tokens: 866

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
  "dashboard": "KPIs Marzo 2026",
  "data": [
    {
      "metric": "MRR",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_mm": 0.07,
      "ltv_cac_ratio": 8.08
    },
    {
      "metric": "Churn Rate",
      "enero": 0.042,
      "febrero": 0.038,
      "marzo": 0.031,
      "var_mm": -0.007,
      "ltv_cac_ratio": 50.79
    },
    {
      "metric": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_mm": 6,
      "ltv_cac_ratio": 10.09
    },
    {
      "metric": "CAC",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_mm": -11,
      "ltv_cac_ratio": 8.02
    },
    {
      "metric": "LTV",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_mm": 330,
      "ltv_cac_ratio": 12.51
    },
    {
      "metric": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_mm": 0.153,
      "ltv_cac_ratio": 10.08
    },
    {
      "metric": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_mm": -0.171,
      "ltv_cac_ratio": 11.78
    },
    {
      "metric": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_mm": -0.7,
      "ltv_cac_ratio": 12.51
    }
  ],
  "ltv_cac_ratios": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51
  },
  "metric_with_greatest_percentage_improvement": "Churn Rate",
  "april_projection": {
    "MRR": 55947,
    "Churn Rate": 0.0248,
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "Active Users": 1900,
    "Support Tickets": 50,
    "Avg Response (h)": 1.7
  },
  "notes": {
    "ltv_cac_calculation": "LTV/CAC = LTV / CAC (redondeado a 2 decimales)",
    "april_projection_method": "Tendencia lineal basada en los cambios mensuales promedio de enero a marzo",
    "greatest_improvement": "Churn Rate tuvo la mayor mejora porcentual (-18.1% desde enero a marzo), superando a otras métricas como Active Users (+35.9%) pero siendo una métrica inversa (menor es mejor)"
  }
}