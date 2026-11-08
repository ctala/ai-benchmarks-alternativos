# Nemotron 3.5 Lightning — ocr_extraction/screenshot_table_extraction

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 6.9 | quality: 6.0
- latency_total: 1.977s | tokens_per_second: 388.9
- input_tokens: 435 | output_tokens: 769

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
  "dashboard_info": {
    "title": "Dashboard - KPIs Marzo 2026",
    "period": "Enero - Marzo 2026",
    "overall_trend": "Positiva en todas las metricas"
  },
  "metrics": [
    {
      "name": "MRR",
      "jan": 45200,
      "feb": 48700,
      "mar": 52100,
      "mom_change_percent": 7.0,
      "mom_change_abs": 3400
    },
    {
      "name": "Churn Rate",
      "jan": 4.2,
      "feb": 3.8,
      "mar": 3.1,
      "mom_change_percent": -0.7,
      "mom_change_abs": -0.7
    },
    {
      "name": "NPS",
      "jan": 42,
      "feb": 45,
      "mar": 51,
      "mom_change_percent": 6,
      "mom_change_abs": 6
    },
    {
      "name": "CAC",
      "jan": 234,
      "feb": 198,
      "mar": 187,
      "mom_change_percent": -11,
      "mom_change_abs": -11
    },
    {
      "name": "LTV",
      "jan": 1890,
      "feb": 2010,
      "mar": 2340,
      "mom_change_percent": 330,
      "mom_change_abs": 330
    },
    {
      "name": "Active Users",
      "jan": 1234,
      "feb": 1456,
      "mar": 1678,
      "mom_change_percent": 15.3,
      "mom_change_abs": 222
    },
    {
      "name": "Support Tickets",
      "jan": 89,
      "feb": 76,
      "mar": 63,
      "mom_change_percent": -17.1,
      "mom_change_abs": -17
    },
    {
      "name": "Avg Response Time",
      "jan": 4.2,
      "feb": 3.1,
      "mar": 2.4,
      "mom_change_percent": -0.7,
      "mom_change_abs": -0.7
    }
  ],
  "calculations": {
    "ltv_cac_ratio": {
      "jan": 8.09,
      "feb": 10.15,
      "mar": 12.51
    },
    "best_improvement_metric": "Active Users",
    "best_improvement_percent": 15.3,
    "projection_april": {
      "mrr": 55747,
      "churn_rate": 2.59,
      "nps": 57,
      "cac": 176,
      "ltv": 2670,
      "active_users": 1895,
      "support_tickets": 52,
      "avg_response": 1.8
    }
  }
}