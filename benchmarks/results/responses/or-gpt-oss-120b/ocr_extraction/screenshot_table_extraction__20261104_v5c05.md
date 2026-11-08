# GPT-OSS 120B — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 7.54 | quality: 8.0
- latency_total: 50.583s | tokens_per_second: 35.3
- input_tokens: 427 | output_tokens: 1785

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
  "title": "DASHBOARD - KPIs Marzo 2026",
  "monthly_data": {
    "Enero": {
      "MRR_K": 45.2,
      "Churn_Rate_pct": 4.2,
      "NPS": 42,
      "CAC_$": 234,
      "LTV_$": 1890,
      "Active_Users": 1234,
      "Support_Tickets": 89,
      "Avg_Response_h": 4.2
    },
    "Febrero": {
      "MRR_K": 48.7,
      "Churn_Rate_pct": 3.8,
      "NPS": 45,
      "CAC_$": 198,
      "LTV_$": 2010,
      "Active_Users": 1456,
      "Support_Tickets": 76,
      "Avg_Response_h": 3.1
    },
    "Marzo": {
      "MRR_K": 52.1,
      "Churn_Rate_pct": 3.1,
      "NPS": 51,
      "CAC_$": 187,
      "LTV_$": 2340,
      "Active_Users": 1678,
      "Support_Tickets": 63,
      "Avg_Response_h": 2.4
    }
  },
  "ltv_cac_ratio": {
    "Enero": 8.08,
    "Febrero": 10.15,
    "Marzo": 12.52
  },
  "highest_improvement_metric": {
    "metric": "Active Users",
    "improvement_percent": 15.3
  },
  "projection_Abril": {
    "MRR_K": 55.7,
    "Churn_Rate_pct": 2.4,
    "NPS": 57,
    "CAC_$": 176,
    "LTV_$": 2670,
    "Active_Users": 1934,
    "Support_Tickets": 52,
    "Avg_Response_h": 1.7
  },
  "notes": "Proyecciones de abril se calcularon aplicando la variación mes‑a‑mes observada en marzo (porcentaje para métricas porcentuales, incremento absoluto para CAC y LTV, y porcentaje para Active Users y Support Tickets)."
}
```