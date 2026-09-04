# GPT-5.6 Luna — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 7.65 | quality: 8.0
- latency_total: 14.088s | tokens_per_second: 102.2
- input_tokens: 379 | output_tokens: 1440

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
    "periodo": "Marzo 2026",
    "tendencia_general": "Positiva en todas las métricas",
    "datos": {
      "MRR": {
        "unidad": "USD",
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100,
        "variacion_m_m": {
          "valor": 3400,
          "porcentaje": 7.0
        }
      },
      "Churn Rate": {
        "unidad": "porcentaje",
        "enero": 4.2,
        "febrero": 3.8,
        "marzo": 3.1,
        "variacion_m_m": {
          "valor_pp": -0.7
        }
      },
      "NPS": {
        "unidad": "puntos",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "variacion_m_m": {
          "valor": 6
        }
      },
      "CAC": {
        "unidad": "USD",
        "enero": 234,
        "febrero": 198,
        "marzo": 187,
        "variacion_m_m": {
          "valor": -11
        }
      },
      "LTV": {
        "unidad": "USD",
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340,
        "variacion_m_m": {
          "valor": 330
        }
      },
      "Active Users": {
        "unidad": "usuarios",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "variacion_m_m": {
          "valor": 222,
          "porcentaje": 15.3
        }
      },
      "Support Tickets": {
        "unidad": "tickets",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "variacion_m_m": {
          "valor": -13,
          "porcentaje": -17.1
        }
      },
      "Avg Response (h)": {
        "unidad": "horas",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "variacion_m_m": {
          "valor": -0.7
        }
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
    "periodo_comparado": "Enero a Marzo 2026",
    "valor_inicial": 4.2,
    "valor_final": 2.4,
    "mejora_porcentual": 42.86,
    "interpretacion": "El tiempo promedio de respuesta disminuyó un 42.86%, lo que representa la mayor mejora relativa entre las métricas."
  },
  "proyeccion_abril_2026": {
    "metodologia": "Se aplica a marzo el mismo cambio absoluto observado entre febrero y marzo.",
    "valores": {
      "MRR": {
        "valor_proyectado": 55500,
        "unidad": "USD"
      },
      "Churn Rate": {
        "valor_proyectado": 2.4,
        "unidad": "porcentaje"
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
        "valor_proyectado": 1900,
        "unidad": "usuarios"
      },
      "Support Tickets": {
        "valor_proyectado": 50,
        "unidad": "tickets"
      },
      "Avg Response (h)": {
        "valor_proyectado": 1.7,
        "unidad": "horas"
      }
    },
    "ltv_cac_ratio_proyectado": 15.17
  }
}