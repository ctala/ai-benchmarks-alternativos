# Gemini 3.5 Flash Lite — ocr_extraction/screenshot_table_extraction

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 7.74 | quality: 8.0
- latency_total: 2.698s | tokens_per_second: 237.6
- input_tokens: 418 | output_tokens: 641

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
  "dashboard": "KPIs Marzo 2026",
  "datos_mensuales": {
    "Enero": {
      "MRR": 45200.0,
      "Churn_Rate": 0.042,
      "NPS": 42.0,
      "CAC": 234.0,
      "LTV": 1890.0,
      "Active_Users": 1234.0,
      "Support_Tickets": 89.0,
      "Avg_Response_h": 4.2
    },
    "Febrero": {
      "MRR": 48700.0,
      "Churn_Rate": 0.038,
      "NPS": 45.0,
      "CAC": 198.0,
      "LTV": 2010.0,
      "Active_Users": 1456.0,
      "Support_Tickets": 76.0,
      "Avg_Response_h": 3.1
    },
    "Marzo": {
      "MRR": 52100.0,
      "Churn_Rate": 0.031,
      "NPS": 51.0,
      "CAC": 187.0,
      "LTV": 2340.0,
      "Active_Users": 1678.0,
      "Support_Tickets": 63.0,
      "Avg_Response_h": 2.4
    }
  },
  "analisis": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Febrero": 10.15,
      "Marzo": 12.51
    },
    "metrica_mayor_mejora_porcentual": {
      "metrica": "Active Users",
      "variacion_marzo": "+15.3%"
    },
    "proyeccion_abril": {
      "metodo": "Aplicando la variación porcentual (o absoluta lineal para tickets y tiempos) del mes de Marzo",
      "valores": {
        "MRR": "$55.7K",
        "Churn_Rate": "2.4%",
        "NPS": 57,
        "CAC": "$176",
        "LTV": "$2,670",
        "Active_Users": "1,935",
        "Support_Tickets": 52,
        "Avg_Response_h": 1.7
      }
    }
  }
}
```