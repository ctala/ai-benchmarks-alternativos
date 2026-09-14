# Granite 4.2 8B — ocr_extraction/screenshot_table_extraction

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 5.96 | quality: 6.0
- latency_total: 139.642s | tokens_per_second: 109.7
- input_tokens: 417 | output_tokens: 15323

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
  "extracted_data": {
    "metricas": {
      "MRR": [45200, 48700, 52100],
      "Churn Rate": [4.2, 3.8, 3.1],
      "NPS": [42, 45, 51],
      "CAC": [234, 198, 187],
      "LTV": [1900, 2010, 2340],
      "Active Users": [1234, 1456, 1678],
      "Support Tickets": [89, 76, 63],
      "Avg Response (h)": [4.2, 3.1, 2.4]
    },
    "var_mm": ["+7.0%", "-0.7pp", "+6", "-$11", "+$330", "+15.3%", "-17.1%", "-0.7"]
  },
  "ltv_cac_ratios": [8.10, 10.15, 12.51],
  "metrica_max_mejora": "Support Tickets",
  "proyeccion_abril": {
    "MRR": "$55.5K",
    "Churn Rate": "2.4%",
    "NPS": 57,
    "CAC": "$176",
    "LTV": "$2,670",
    "Active Users": "1,900",
    "Support Tickets": 50,
    "Avg Response (h)": 1.7
  }
}