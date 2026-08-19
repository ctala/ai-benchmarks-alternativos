# GPT-5.6 Luna Pro — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 8.74 | quality: 10.0
- latency_total: 25.265s | tokens_per_second: 232.6
- input_tokens: 8318 | output_tokens: 5876

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
  "dashboard": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "periodos": ["Enero", "Febrero", "Marzo"],
    "metricas": {
      "MRR": {
        "unidad": "USD",
        "valores": {
          "Enero": 45200,
          "Febrero": 48700,
          "Marzo": 52100
        },
        "variacion_mensual": "7.0%"
      },
      "Churn Rate": {
        "unidad": "%",
        "valores": {
          "Enero": 4.2,
          "Febrero": 3.8,
          "Marzo": 3.1
        },
        "variacion_mensual": "-0.7pp"
      },
      "NPS": {
        "unidad": "puntos",
        "valores": {
          "Enero": 42,
          "Febrero": 45,
          "Marzo": 51
        },
        "variacion_mensual": "+6"
      },
      "CAC": {
        "unidad": "USD",
        "valores": {
          "Enero": 234,
          "Febrero": 198,
          "Marzo": 187
        },
        "variacion_mensual": "-$11"
      },
      "LTV": {
        "unidad": "USD",
        "valores": {
          "Enero": 1890,
          "Febrero": 2010,
          "Marzo": 2340
        },
        "variacion_mensual": "+$330"
      },
      "Active Users": {
        "unidad": "usuarios",
        "valores": {
          "Enero": 1234,
          "Febrero": 1456,
          "Marzo": 1678
        },
        "variacion_mensual": "15.3%"
      },
      "Support Tickets": {
        "unidad": "tickets",
        "valores": {
          "Enero": 89,
          "Febrero": 76,
          "Marzo": 63
        },
        "variacion_mensual": "-17.1%"
      },
      "Avg Response": {
        "unidad": "horas",
        "valores": {
          "Enero": 4.2,
          "Febrero": 3.1,
          "Marzo": 2.4
        },
        "variacion_mensual": "-0.7"
      }
    }
  },
  "ltv_cac_ratio": {
    "Enero": {
      "ltv": 1890,
      "cac": 234,
      "ratio": 8.08
    },
    "Febrero": {
      "ltv": 2010,
      "cac": 198,
      "ratio": 10.15
    },
    "Marzo": {
      "ltv": 2340,
      "cac": 187,
      "ratio": 12.51
    }
  },
  "mayor_mejora_porcentual": {
    "metrica": "Avg Response",
    "periodo_comparado": "Febrero a Marzo",
    "cambio_absoluto": -0.7,
    "cambio_porcentual": -22.6,
    "interpretacion": "Es la mayor mejora relativa, al reducirse el tiempo promedio de respuesta de 3.1 a 2.4 horas."
  },
  "proyeccion_abril_2026": {
    "metodo": "Se mantiene la variacion observada de Febrero a Marzo; los cambios porcentuales se aplican sobre Marzo y los cambios absolutos se proyectan de forma lineal.",
    "valores": {
      "MRR": {
        "valor_proyectado": 55747,
        "unidad": "USD",
        "formula": "52100 * 1.07"
      },
      "Churn Rate": {
        "valor_proyectado": 2.4,
        "unidad": "%",
        "formula": "3.1 - 0.7pp"
      },
      "NPS": {
        "valor_proyectado": 57,
        "unidad": "puntos",
        "formula": "51 + 6"
      },
      "CAC": {
        "valor_proyectado": 176,
        "unidad": "USD",
        "formula": "187 - 11"
      },
      "LTV": {
        "valor_proyectado": 2670,
        "unidad": "USD",
        "formula": "2340 + 330"
      },
      "Active Users": {
        "valor_proyectado": 1935,
        "unidad": "usuarios",
        "formula": "1678 * 1.153"
      },
      "Support Tickets": {
        "valor_proyectado": 52,
        "unidad": "tickets",
        "formula": "63 * 0.829"
      },
      "Avg Response": {
        "valor_proyectado": 1.7,
        "unidad": "horas",
        "formula": "2.4 - 0.7"
      }
    },
    "ltv_cac_ratio_proyectado": 15.17
  },
  "tendencia_general": "Positiva en todas las métricas"
}