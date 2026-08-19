# Kimi K2.5 — ocr_extraction/screenshot_table_extraction

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 2.47 | quality: 2.0
- latency_total: 175.466s | tokens_per_second: 11.7
- input_tokens: 386 | output_tokens: 2048

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
  "datos_extraidos": {
    "periodos": ["Enero", "Febrero", "Marzo"],
    "metricas": {
      "MRR": {"valores": [45200, 48700, 52100], "unidad": "USD", "formato": "moneda"},
      "Churn_Rate": {"valores": [4.2, 3.8, 3.1], "unidad": "%", "formato": "porcentaje"},
      "NPS": {"valores": [42, 45, 51], "unidad": "puntos", "formato": "entero"},
      "CAC": {"valores": [234, 198, 187], "unidad": "USD", "formato": "moneda"},
      "LTV": {"valores": [1890, 2010, 2340], "unidad": "USD", "formato": "moneda"},
      "Active_Users": {"valores": [1234, 1456, 1678], "unidad": "usuarios", "formato": "entero"},
      "Support_Tickets": {"valores": [89, 76, 63], "unidad": "tickets", "formato": "entero"},
      "Avg_Response_Time": {"valores": [4.2, 3.1, 2.4], "unidad": "horas", "formato": "decimal"}
    }
  },
  "analisis_ltv_cac":