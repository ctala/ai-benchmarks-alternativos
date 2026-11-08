# Gemini 3.5 Flash Lite — ocr_extraction/screenshot_table_extraction

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 9.1 | quality: 10.0
- latency_total: 2.429s | tokens_per_second: 328.5
- input_tokens: 418 | output_tokens: 798

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
  "datos_originales": {
    "MRR": {
      "Enero": "$45.2K",
      "Febrero": "$48.7K",
      "Marzo": "$52.1K",
      "Var_MM": "+7.0%"
    },
    "Churn_Rate": {
      "Enero": "4.2%",
      "Febrero": "3.8%",
      "Marzo": "3.1%",
      "Var_MM": "-0.7pp"
    },
    "NPS": {
      "Enero": 42,
      "Febrero": 45,
      "Marzo": 51,
      "Var_MM": "+6"
    },
    "CAC": {
      "Enero": "$234",
      "Febrero": "$198",
      "Marzo": "$187",
      "Var_MM": "-$11"
    },
    "LTV": {
      "Enero": "$1,890",
      "Febrero": "$2,010",
      "Marzo": "$2,340",
      "Var_MM": "+$330"
    },
    "Active_Users": {
      "Enero": "1,234",
      "Febrero": "1,456",
      "Marzo": "1,678",
      "Var_MM": "+15.3%"
    },
    "Support_Tickets": {
      "Enero": 89,
      "Febrero": 76,
      "Marzo": 63,
      "Var_MM": "-17.1%"
    },
    "Avg_Response_h": {
      "Enero": 4.2,
      "Febrero": 3.1,
      "Marzo": 2.4,
      "Var_MM": "-0.7"
    }
  },
  "analisis_adicional": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Febrero": 10.15,
      "Marzo": 12.51
    },
    "metrica_mayor_mejora_porcentual": {
      "metrica": "Support Tickets",
      "descripcion": "Reducción del 17.1% en Marzo (y -15.8% de Ene a Feb, consolidando una mejora operativa destacada). En términos de crecimiento positivo, Active Users lidera con un +15.3% en Marzo."
    },
    "proyeccion_abril": {
      "metrica_metodologia": "Proyección basada en la variación porcentual o absoluta del mes de Marzo respecto a Febrero.",
      "valores": {
        "MRR": "$55.7K",
        "Churn_Rate": "2.4%",
        "NPS": 57,
        "CAC": "$176",
        "LTV": "$2,725",
        "Active_Users": "1,935",
        "Support_Tickets": 52,
        "Avg_Response_h": 1.7
      }
    }
  }
}
```