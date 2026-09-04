# GPT-5.6 Luna — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 9.15 | quality: 10.0
- latency_total: 9.853s | tokens_per_second: 125.6
- input_tokens: 379 | output_tokens: 1238

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
        "variacion_mensual": "+7.0%"
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
        "variacion_mensual": "+15.3%"
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
      "Avg Response (h)": {
        "unidad": "horas",
        "valores": {
          "Enero": 4.2,
          "Febrero": 3.1,
          "Marzo": 2.4
        },
        "variacion_mensual": "-0.7"
      }
    },
    "tendencia_general": "Positiva en todas las metricas"
  },
  "calculos": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Febrero": 10.15,
      "Marzo": 12.51
    },
    "mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "periodo": "Enero a Marzo",
      "mejora_porcentual": 42.86,
      "interpretacion": "Reduccion del tiempo promedio de respuesta de 4.2 a 2.4 horas"
    }
  },
  "proyeccion_abril": {
    "metodo": "Se mantiene la variacion absoluta o porcentual observada entre Febrero y Marzo",
    "valores": {
      "MRR": {
        "valor_proyectado": 55747,
        "unidad": "USD"
      },
      "Churn Rate": {
        "valor_proyectado": 2.4,
        "unidad": "%"
      },
      "NPS": {
        "valor_proyectado": 57,
        "unidad": "puntos"
      },
      "CAC": {
        "valor_proyectado": 176,
        "unidad": "USD"
      },
      "LTV": {
        "valor_proyectado": 2670,
        "unidad": "USD"
      },
      "Active Users": {
        "valor_proyectado": 1935,
        "unidad": "usuarios"
      },
      "Support Tickets": {
        "valor_proyectado": 52,
        "unidad": "tickets"
      },
      "Avg Response (h)": {
        "valor_proyectado": 1.7,
        "unidad": "horas"
      }
    }
  }
}