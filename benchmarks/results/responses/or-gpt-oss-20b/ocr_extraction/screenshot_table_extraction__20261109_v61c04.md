# GPT-OSS 20B — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.88 | quality: 8.0
- latency_total: 15.409s | tokens_per_second: 119.2
- input_tokens: 440 | output_tokens: 1837

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
  "metrics": [
    {
      "name": "MRR",
      "values": { "Enero": 45200, "Feb": 48700, "Mar": 52100 },
      "var_m_m": 7.0,
      "ltv_cac_ratio": null
    },
    {
      "name": "Churn Rate",
      "values": { "Enero": 4.2, "Feb": 3.8, "Mar": 3.1 },
      "var_m_m": -0.7,
      "ltv_cac_ratio": null
    },
    {
      "name": "NPS",
      "values": { "Enero": 42, "Feb": 45, "Mar": 51 },
      "var_m_m": 6,
      "ltv_cac_ratio": null
    },
    {
      "name": "CAC",
      "values": { "Enero": 234, "Feb": 198, "Mar": 187 },
      "var_m_m": -11,
      "ltv_cac_ratio": null
    },
    {
      "name": "LTV",
      "values": { "Enero": 1890, "Feb": 2010, "Mar": 2340 },
      "var_m_m": 330,
      "ltv_cac_ratio": null
    },
    {
      "name": "Active Users",
      "values": { "Enero": 1234, "Feb": 1456, "Mar": 1678 },
      "var_m_m": 15.3,
      "ltv_cac_ratio": null
    },
    {
      "name": "Support Tickets",
      "values": { "Enero": 89, "Feb": 76, "Mar": 63 },
      "var_m_m": -17.1,
      "ltv_cac_ratio": null
    },
    {
      "name": "Avg Response (h)",
      "values": { "Enero": 4.2, "Feb": 3.1, "Mar": 2.4 },
      "var_m_m": -0.7,
      "ltv_cac_ratio": null
    }
  ],
  "ltv_cac_ratios": {
    "Enero": 8.08,
    "Feb": 10.15,
    "Mar": 12.52
  },
  "greatest_improvement_metric": "Active Users",
  "April_projection": {
    "MRR": 55787,
    "Churn Rate": 2.4,
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "Active Users": 1937,
    "Support Tickets": 52,
    "Avg Response (h)": 1.7
  }
}
```