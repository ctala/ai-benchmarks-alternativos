# GLM 5 — ocr_extraction/screenshot_table_extraction

- model_id: `z-ai/glm-5`
- success: True  | final: 7.36 | quality: 8.0
- latency_total: 10.796s | tokens_per_second: 75.7
- input_tokens: 389 | output_tokens: 817

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
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "tendencia_general": "Positiva en todas las metricas",
    "metricas": [
      {
        "nombre": "MRR",
        "valores": {
          "Enero": 45200,
          "Febrero": 48700,
          "Marzo": 52100
        },
        "var_m_m": "+7.0%"
      },
      {
        "nombre": "Churn Rate",
        "valores": {
          "Enero": 4.2,
          "Febrero": 3.8,
          "Marzo": 3.1
        },
        "var_m_m": "-0.7pp"
      },
      {
        "nombre": "NPS",
        "valores": {
          "Enero": 42,
          "Febrero": 45,
          "Marzo": 51
        },
        "var_m_m": "+6"
      },
      {
        "nombre": "CAC",
        "valores": {
          "Enero": 234,
          "Febrero": 198,
          "Marzo": 187
        },
        "var_m_m": "-$11"
      },
      {
        "nombre": "LTV",
        "valores": {
          "Enero": 1890,
          "Febrero": 2010,
          "Marzo": 2340
        },
        "var_m_m": "+$330"
      },
      {
        "nombre": "Active Users",
        "valores": {
          "Enero": 1234,
          "Febrero": 1456,
          "Marzo": 1678
        },
        "var_m_m": "+15.3%"
      },
      {
        "nombre": "Support Tickets",
        "valores": {
          "Enero": 89,
          "Febrero": 76,
          "Marzo": 63
        },
        "var_m_m": "-17.1%"
      },
      {
        "nombre": "Avg Response (h)",
        "valores": {
          "Enero": 4.2,
          "Febrero": 3.1,
          "Marzo": 2.4
        },
        "var_m_m": "-0.7"
      }
    ]
  },
  "analisis": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Febrero": 10.15,
      "Marzo": 12.52,
      "observacion": "El ratio LTV/CAC muestra una mejora constante y sólida, triplicando el valor mínimo recomendado de 3:1 en marzo."
    },
    "metrica_mayor_mejora": {
      "metrica": "LTV",
      "mejora_porcentual": "+23.81%",
      "detalle": "Calculado sobre el valor de Enero ($1,890) hacia Marzo ($2,340). Representa el mayor crecimiento porcentual absoluto en el trimestre."
    },
    "proyeccion_abril": {
      "metodologia": "Proyección basada en la continuación de la tasa de crecimiento o variación absoluta del último mes (Febrero a Marzo)",
      "valores_estimados": {
        "MRR": 55500,
        "Churn_Rate": 2.4,
        "NPS": 57,
        "CAC": 176,
        "LTV": 2670,
        "Active_Users": 1900,
        "Support_Tickets": 50,
        "Avg_Response_h": 1.7
      }
    }
  }
}
```