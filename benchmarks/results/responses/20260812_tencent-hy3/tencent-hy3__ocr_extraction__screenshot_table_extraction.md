# Tencent Hy3 — ocr_extraction/screenshot_table_extraction

- model_id: `tencent/hy3`
- success: True  | final: 7.19 | quality: 8.0
- latency_total: 88.22s | tokens_per_second: 92.9
- input_tokens: 401 | output_tokens: 8192

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
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "tendencia_general": "Positiva en todas las metricas"
  },
  "datos_extraidos": {
    "enero": {
      "MRR": "$45.2K",
      "Churn_Rate": "4.2%",
      "NPS": 42,
      "CAC": "$234",
      "LTV": "$1,890",
      "Active_Users": 1234,
      "Support_Tickets": 89,
      "Avg_Response_h": 4.2
    },
    "febrero": {
      "MRR": "$48.7K",
      "Churn_Rate": "3.8%",
      "NPS": 45,
      "CAC": "$198",
      "LTV": "$2,010",
      "Active_Users": 1456,
      "Support_Tickets": 76,
      "Avg_Response_h": 3.1
    },
    "marzo": {
      "MRR": "$52.1K",
      "Churn_Rate": "3.1%",
      "NPS": 51,
      "CAC": "$187",
      "LTV": "$2,340",
      "Active_Users": 1678,
      "Support_Tickets": 63,
      "Avg_Response_h": 2.4
    }
  },
  "calculos": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "descripcion": "Calculado como LTV / CAC usando valores numéricos sin formato de moneda (redondeado a 2 decimales)"
    }
  },
  "analisis_mejoras": {
    "metrica_mayor_mejora_porcentual": "Avg Response (h)",
    "mejora_porcentual_relativa": -22.58,
    "nota": "Se calculó la variación porcentual relativa de Febrero a Marzo para todas las métricas. Aunque 'Support Tickets' tiene la mayor caída porcentual explícita en la tabla (-17.1%), 'Avg Response (h)' bajó de 3.1 a 2.4h, lo que representa una mejora relativa del 22.58% (la mayor en valor absoluto