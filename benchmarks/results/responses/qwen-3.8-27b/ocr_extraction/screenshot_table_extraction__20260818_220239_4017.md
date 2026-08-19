# Qwen 3.8 27B — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 6.86 | quality: 8.0
- latency_total: 92.779s | tokens_per_second: 166.2
- input_tokens: 469 | output_tokens: 15423

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
  "dashboard": "KPIs Marzo 2026",
  "datos_extraidos": {
    "metricas": [
      {
        "metrica": "MRR",
        "unidades": "USD_K",
        "valores": {
          "enero": 45.2,
          "febrero": 48.7,
          "marzo": 52.1
        },
        "valores_visuales": {
          "enero": "$45.2K",
          "febrero": "$48.7K",
          "marzo": "$52.1K"
        },
        "var_m_m": "+7.0%"
      },
      {
        "metrica": "Churn Rate",
        "unidades": "%",
        "valores": {
          "enero": 4.2,
          "febrero": 3.8,
          "marzo": 3.1
        },
        "valores_visuales": {
          "enero": "4.2%",
          "febrero": "3.8%",
          "marzo": "3.1%"
        },
        "var_m_m": "-0.7pp"
      },
      {
        "metrica": "NPS",
        "unidades": "puntos",
        "valores": {
          "enero": 42,
          "febrero": 45,
          "marzo": 51
        },
        "valores_visuales": {
          "enero": "42",
          "febrero": "45",
          "marzo": "51"
        },
        "var_m_m": "+6"
      },
      {
        "metrica": "CAC",
        "unidades": "USD",
        "valores": {
          "enero": 234,
          "febrero": 198,
          "marzo": 187
        },
        "valores_visuales": {
          "enero": "$234",
          "febrero": "$198",
          "marzo": "$187"
        },
        "var_m_m": "-$11"
      },
      {
        "metrica": "LTV",
        "unidades": "USD",
        "valores": {
          "enero": 1890,
          "febrero": 2010,
          "marzo": 2340
        },
        "valores_visuales": {
          "enero": "$1,890",
          "febrero": "$2,010",
          "marzo": "$2,340"
        },
        "var_m_m": "+$330"
      },
      {
        "metrica": "Active Users",
        "unidades": "usuarios",
        "valores": {
          "enero": 1234,
          "febrero": 1456,
          "marzo": 1678
        },
        "valores_visuales": {
          "enero": "1,234",
          "febrero": "1,456",
          "marzo": "1,678"
        },
        "var_m_m": "+15.3%"
      },
      {
        "metrica": "Support Tickets",
        "unidades": "tickets",
        "valores": {
          "enero": 89,
          "febrero": 76,
          "marzo": 63
        },
        "valores_visuales": {
          "enero": "89",
          "febrero": "76",
          "marzo": "63"
        },
        "var_m_m": "-17.1%"
      },
      {
        "metrica": "Avg Response (h)",
        "unidades": "horas",
        "valores": {
          "enero": 4.2,
          "febrero": 3.1,
          "marzo": 2.4
        },
        "valores_visuales": {
          "enero": "4.2",
          "febrero": "3.1",
          "marzo": "2.4"
        },
        "var_m_m": "-0.7"
      }
    ],
    "tendencia_general": "↑ Positiva en todas las metricas"
  },
  "ltv_cac_ratio": {
    "metodo": "LTV / CAC",
    "valores": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    }
  },
  "mayor_mejora_porcentual": {
    "criterio": "Cambio favorable de Febrero a Marzo expresado en porcentaje. Para métricas donde menor es mejor, se mide la reducción.",
    "metrica": "Avg Response (h)",
    "mejora_porcentual": 22.58,
    "detalle": "El tiempo promedio de respuesta bajó de 3.1 h a 2.4 h, una reducción del 22.58%.",
    "mejoras_porcentuales_feb_mar": {
      "MRR": 6.98,
      "Churn Rate": 18.42,
      "NPS": 13.33,
      "CAC": 5.56,
      "LTV": 16.42,
      "Active Users": 15.25,
      "Support Tickets": 17.11,
      "Avg Response (h)": 22.58
    }
  },
  "proyeccion_abril": {
    "metodo": "Se aplica la variación M/M observada de Febrero a Marzo al valor de Marzo: variación porcentual para métricas con M/M porcentual y variación absoluta para métricas con M/M absoluto.",
    "valores": [
      {
        "metrica": "MRR",
        "valor": 55.74,
        "unidades": "USD_K",
        "redondeo": "$55.7K",
        "cambio_aplicado": "+6.98%"
      },
      {
        "metrica": "Churn Rate",
        "valor": 2.4,
        "unidades": "%",
        "redondeo": "2.4%",
        "cambio_aplicado": "-0.7 pp"
      },
      {
        "metrica": "NPS",
        "valor": 57,
        "unidades": "puntos",
        "redondeo": "57",
        "cambio_aplicado": "+6 puntos"
      },
      {
        "metrica": "CAC",
        "valor": 176,
        "unidades": "USD",
        "redondeo": "$176",
        "cambio_aplicado": "-$11"
      },
      {
        "metrica": "LTV",
        "valor": 2670,
        "unidades": "USD",
        "redondeo": "$2,670",
        "cambio_aplicado": "+$330"
      },
      {
        "metrica": "Active Users",
        "valor": 1933.85,
        "unidades": "usuarios",
        "redondeo": "1,934",
        "cambio_aplicado": "+15.25%"
      },
      {
        "metrica": "Support Tickets",
        "valor": 52.22,
        "unidades": "tickets",
        "redondeo": "52",
        "cambio_aplicado": "-17.11%"
      },
      {
        "metrica": "Avg Response (h)",
        "valor": 1.7,
        "unidades": "horas",
        "redondeo": "1.7 h",
        "cambio_aplicado": "-0.7 h"
      }
    ]
  }
}