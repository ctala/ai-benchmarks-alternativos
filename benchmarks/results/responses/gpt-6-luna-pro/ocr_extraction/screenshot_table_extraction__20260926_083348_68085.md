# GPT-6 Luna Pro — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 7.47 | quality: 8.0
- latency_total: 15.78s | tokens_per_second: 210.8
- input_tokens: 5522 | output_tokens: 3327

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
  "datos": {
    "MRR": {
      "unidad": "USD",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "variacion_mensual": {
        "valor": 7.0,
        "unidad": "%"
      }
    },
    "Churn Rate": {
      "unidad": "%",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "variacion_mensual": {
        "valor": -0.7,
        "unidad": "puntos porcentuales"
      }
    },
    "NPS": {
      "unidad": "puntos",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "variacion_mensual": {
        "valor": 6,
        "unidad": "puntos"
      }
    },
    "CAC": {
      "unidad": "USD",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "variacion_mensual": {
        "valor": -11,
        "unidad": "USD"
      }
    },
    "LTV": {
      "unidad": "USD",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "variacion_mensual": {
        "valor": 330,
        "unidad": "USD"
      }
    },
    "Active Users": {
      "unidad": "usuarios",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "variacion_mensual": {
        "valor": 15.3,
        "unidad": "%"
      }
    },
    "Support Tickets": {
      "unidad": "tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "variacion_mensual": {
        "valor": -17.1,
        "unidad": "%"
      }
    },
    "Avg Response (h)": {
      "unidad": "horas",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "variacion_mensual": {
        "valor": -0.7,
        "unidad": "horas"
      }
    }
  },
  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51
  },
  "mayor_mejora_porcentual": {
    "metrica": "Avg Response (h)",
    "mejora": 42.86,
    "unidad": "%",
    "calculo": "Reducción de 4.2 a 2.4 horas entre enero y marzo"
  },
  "proyeccion_abril": {
    "metodo": "Se aplica a marzo el último cambio absoluto observado, de febrero a marzo.",
    "valores": {
      "MRR": {
        "valor": 55500,
        "unidad": "USD"
      },
      "Churn Rate": {
        "valor": 2.4,
        "unidad": "%"
      },
      "NPS": {
        "valor": 57,
        "unidad": "puntos"
      },
      "CAC": {
        "valor": 176,
        "unidad": "USD"
      },
      "LTV": {
        "valor": 2670,
        "unidad": "USD"
      },
      "Active Users": {
        "valor": 1900,
        "unidad": "usuarios"
      },
      "Support Tickets": {
        "valor": 50,
        "unidad": "tickets"
      },
      "Avg Response (h)": {
        "valor": 1.7,
        "unidad": "horas"
      }
    }
  }
}