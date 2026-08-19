# Qwen 3.8 2.4T (A95B) — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.8-2.4t-a95b`
- success: True  | final: 6.8 | quality: 8.0
- latency_total: 76.425s | tokens_per_second: 146.0
- input_tokens: 469 | output_tokens: 11155

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
  "extraccion": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "tendencia_general": "↑ Positiva en todas las metricas",
    "metricas": {
      "MRR": {
        "Enero": "$45.2K",
        "Feb": "$48.7K",
        "Marzo": "$52.1K",
        "Var_M_M": "+7.0%",
        "numeric": {
          "Enero": 45200,
          "Feb": 48700,
          "Marzo": 52100
        },
        "unidad": "USD"
      },
      "Churn_Rate": {
        "Enero": "4.2%",
        "Feb": "3.8%",
        "Marzo": "3.1%",
        "Var_M_M": "-0.7pp",
        "numeric": {
          "Enero": 4.2,
          "Feb": 3.8,
          "Marzo": 3.1
        },
        "unidad": "%"
      },
      "NPS": {
        "Enero": "42",
        "Feb": "45",
        "Marzo": "51",
        "Var_M_M": "+6",
        "numeric": {
          "Enero": 42,
          "Feb": 45,
          "Marzo": 51
        },
        "unidad": "puntos"
      },
      "CAC": {
        "Enero": "$234",
        "Feb": "$198",
        "Marzo": "$187",
        "Var_M_M": "-$11",
        "numeric": {
          "Enero": 234,
          "Feb": 198,
          "Marzo": 187
        },
        "unidad": "USD"
      },
      "LTV": {
        "Enero": "$1,890",
        "Feb": "$2,010",
        "Marzo": "$2,340",
        "Var_M_M": "+$330",
        "numeric": {
          "Enero": 1890,
          "Feb": 2010,
          "Marzo": 2340
        },
        "unidad": "USD"
      },
      "Active_Users": {
        "Enero": "1,234",
        "Feb": "1,456",
        "Marzo": "1,678",
        "Var_M_M": "+15.3%",
        "numeric": {
          "Enero": 1234,
          "Feb": 1456,
          "Marzo": 1678
        },
        "unidad": "usuarios"
      },
      "Support_Tickets": {
        "Enero": "89",
        "Feb": "76",
        "Marzo": "63",
        "Var_M_M": "-17.1%",
        "numeric": {
          "Enero": 89,
          "Feb": 76,
          "Marzo": 63
        },
        "unidad": "tickets"
      },
      "Avg_Response_h": {
        "Enero": "4.2",
        "Feb": "3.1",
        "Marzo": "2.4",
        "Var_M_M": "-0.7",
        "numeric": {
          "Enero": 4.2,
          "Feb": 3.1,
          "Marzo": 2.4
        },
        "unidad": "horas"
      }
    }
  },
  "calculos": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Feb": 10.15,
      "Marzo": 12.51,
      "formula": "LTV / CAC",
      "redondeo": "2 decimales"
    },
    "variacion_porcentual_feb_mar": {
      "MRR": 6.98,
      "Churn_Rate": -18.42,
      "NPS": 13.33,
      "CAC": -5.56,
      "LTV": 16.42,
      "Active_Users": 15.25,
      "Support_Tickets": -17.11,
      "Avg_Response_h": -22.58,
      "nota": "En Churn Rate, CAC, Support Tickets y Avg Response, una variación negativa indica mejora porque son métricas donde menor es mejor."
    },
    "metrica_con_mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "variacion_porcentual": -22.58,
      "mejora_porcentual": 22.58,
      "detalle": "El tiempo medio de respuesta bajó de 3.1 h en Feb a 2.4 h en Mar, la mayor mejora relativa calculada.",
      "alternativa_si_solo_var_visible": "Si solo se consideran las variaciones ya mostradas como porcentaje en la captura, Support Tickets (-17.1%) sería la mayor mejora visible."
    }
  },
  "proyeccion_abril": {
    "metodo": "Se aplica la variación mensual Feb->Mar sobre el valor de Marzo: porcentual para MRR, Active Users y Support Tickets; absoluta para NPS, CAC, LTV y Avg Response; puntos porcentuales para Churn Rate.",
    "valores": {
      "MRR": {
        "proyectado": 55747,
        "formato": "$55.7K",
        "unidad": "USD",
        "variacion_aplicada": "+7.0%"
      },
      "Churn_Rate": {
        "proyectado": 2.4,
        "formato": "2.4%",
        "unidad": "%",
        "variacion_aplicada": "-0.7pp"
      },
      "NPS": {
        "proyectado": 57,
        "formato": "57",
        "unidad": "puntos",
        "variacion_aplicada": "+6"
      },
      "CAC": {
        "proyectado": 176,
        "formato": "$176",
        "unidad": "USD",
        "variacion_aplicada": "-$11"
      },
      "LTV": {
        "proyectado": 2670,
        "formato": "$2,670",
        "unidad": "USD",
        "variacion_aplicada": "+$330"
      },
      "Active_Users": {
        "proyectado": 1935,
        "formato": "1,935",
        "unidad": "usuarios",
        "variacion_aplicada": "+15.3%"
      },
      "Support_Tickets": {
        "proyectado": 52,
        "formato": "52",
        "unidad": "tickets",
        "variacion_aplicada": "-17.1%"
      },
      "Avg_Response_h": {
        "proyectado": 1.7,
        "formato": "1.7",
        "unidad": "horas",
        "variacion_aplicada": "-0.7 h"
      }
    },
    "ltv_cac_ratio_abril": 15.17
  }
}