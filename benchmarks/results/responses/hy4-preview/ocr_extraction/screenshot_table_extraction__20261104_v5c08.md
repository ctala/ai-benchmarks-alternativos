# Tencent Hy4 preview — ocr_extraction/screenshot_table_extraction

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.8 | quality: 10.0
- latency_total: 9.255s | tokens_per_second: 76.9
- input_tokens: 402 | output_tokens: 712

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
  "dashboard_data": {
    "periodo": "Enero - Marzo 2026",
    "metricas": {
      "MRR": {
        "Enero": 45200,
        "Febrero": 48700,
        "Marzo": 52100,
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
        "Enero": 234,
        "Febrero": 198,
        "Marzo": 187,
        "Var_MM": "-$11"
      },
      "LTV": {
        "Enero": 1890,
        "Febrero": 2010,
        "Marzo": 2340,
        "Var_MM": "+$330"
      },
      "Active_Users": {
        "Enero": 1234,
        "Febrero": 1456,
        "Marzo": 1678,
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
    }
  },
  "analisis": {
    "LTV_CAC_Ratio": {
      "Enero": 8.08,
      "Febrero": 10.15,
      "Marzo": 12.51,
      "calculo": "LTV / CAC (redondeado a 2 decimales)"
    },
    "metrica_mayor_mejora_porcentual": {
      "metrica": "Support Tickets",
      "valor": "-17.1%",
      "razon": "Mayor reducción porcentual en métricas negativas, indicando una fuerte disminución de tickets de soporte."
    },
    "proyeccion_abril": {
      "MRR": 55700,
      "Churn_Rate": "2.4%",
      "NPS": 57,
      "CAC": 176,
      "LTV": 2670,
      "Active_Users": 1900,
      "Support_Tickets": 50,
      "Avg_Response_h": 1.7,
      "nota": "Proyección basada en tendencia lineal del cambio mes a mes (Marzo vs Febrero)."
    }
  }
}
```