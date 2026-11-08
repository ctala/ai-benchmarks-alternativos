# GPT-5.5 — ocr_extraction/screenshot_table_extraction

- model_id: `gpt-5.5`
- success: True  | final: 8.41 | quality: 10.0
- latency_total: 9.711s | tokens_per_second: 110.3
- input_tokens: 379 | output_tokens: 1071

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
  "titulo": "DASHBOARD - KPIs Marzo 2026",
  "datos": [
    {
      "metrica": "MRR",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "variacion_mensual": {
        "valor": 7.0,
        "unidad": "%"
      }
    },
    {
      "metrica": "Churn Rate",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "variacion_mensual": {
        "valor": -0.7,
        "unidad": "pp"
      }
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "variacion_mensual": {
        "valor": 6,
        "unidad": "puntos"
      }
    },
    {
      "metrica": "CAC",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "variacion_mensual": {
        "valor": -11,
        "unidad": "USD"
      }
    },
    {
      "metrica": "LTV",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "variacion_mensual": {
        "valor": 330,
        "unidad": "USD"
      }
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "variacion_mensual": {
        "valor": 15.3,
        "unidad": "%"
      }
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "variacion_mensual": {
        "valor": -17.1,
        "unidad": "%"
      }
    },
    {
      "metrica": "Avg Response",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "variacion_mensual": {
        "valor": -0.7,
        "unidad": "horas"
      }
    }
  ],
  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51
  },
  "mayor_mejora_porcentual": {
    "metrica": "Support Tickets",
    "interpretacion": "Es la mayor mejora porcentual entre febrero y marzo, ya que disminuyó un 17.1%. Al ser una métrica donde menor es mejor, se considera una mejora positiva.",
    "variacion_porcentual": -17.1,
    "mejora_absoluta": 17.1,
    "unidad": "%"
  },
  "proyeccion_abril": {
    "metodo": "Se proyecta abril manteniendo la misma variación de febrero a marzo.",
    "valores": {
      "MRR": {
        "marzo": 52100,
        "variacion_aplicada": "+7.0%",
        "abril_proyectado": 55747
      },
      "Churn Rate": {
        "marzo": 3.1,
        "variacion_aplicada": "-0.7pp",
        "abril_proyectado": 2.4
      },
      "NPS": {
        "marzo": 51,
        "variacion_aplicada": "+6 puntos",
        "abril_proyectado": 57
      },
      "CAC": {
        "marzo": 187,
        "variacion_aplicada": "-11 USD",
        "abril_proyectado": 176
      },
      "LTV": {
        "marzo": 2340,
        "variacion_aplicada": "+330 USD",
        "abril_proyectado": 2670
      },
      "Active Users": {
        "marzo": 1678,
        "variacion_aplicada": "+15.3%",
        "abril_proyectado": 1935
      },
      "Support Tickets": {
        "marzo": 63,
        "variacion_aplicada": "-17.1%",
        "abril_proyectado": 52
      },
      "Avg Response": {
        "marzo": 2.4,
        "variacion_aplicada": "-0.7 horas",
        "abril_proyectado": 1.7
      }
    }
  },
  "tendencia_general": "Positiva en todas las métricas"
}