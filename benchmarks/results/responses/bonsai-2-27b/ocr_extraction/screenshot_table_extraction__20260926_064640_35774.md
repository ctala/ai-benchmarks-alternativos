# Bonsai 2 27B — ocr_extraction/screenshot_table_extraction

- model_id: `prism-ml/ternary-bonsai-2-27b`
- success: True  | final: 8.32 | quality: 10.0
- latency_total: 412.067s | tokens_per_second: 38.4
- input_tokens: 469 | output_tokens: 15834

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
  "tendencia_general": "↑ Positiva en todas las metricas",
  "notas": [
    "MRR se expresa en miles de USD (KUSD).",
    "Para métricas inversas, la mejora se interpreta como reducción.",
    "La proyección de abril aplica la variación M/M de febrero-marzo a los valores de marzo."
  ],
  "extraccion": {
    "meses": [
      "Enero",
      "Febrero",
      "Marzo"
    ],
    "metricas": [
      {
        "nombre": "MRR",
        "unidad": "KUSD",
        "direccion": "mayor_es_buena",
        "valores": {
          "enero": 45.2,
          "febrero": 48.7,
          "marzo": 52.1
        },
        "valores_display": {
          "enero": "$45.2K",
          "febrero": "$48.7K",
          "marzo": "$52.1K"
        },
        "var_m_m": {
          "valor": 7.0,
          "unidad": "%",
          "display": "+7.0%"
        }
      },
      {
        "nombre": "Churn Rate",
        "unidad": "%",
        "direccion": "menor_es_buena",
        "valores": {
          "enero": 4.2,
          "febrero": 3.8,
          "marzo": 3.1
        },
        "valores_display": {
          "enero": "4.2%",
          "febrero": "3.8%",
          "marzo": "3.1%"
        },
        "var_m_m": {
          "valor": -0.7,
          "unidad": "pp",
          "display": "-0.7pp"
        }
      },
      {
        "nombre": "NPS",
        "unidad": "puntos",
        "direccion": "mayor_es_buena",
        "valores": {
          "enero": 42,
          "febrero": 45,
          "marzo": 51
        },
        "valores_display": {
          "enero": "42",
          "febrero": "45",
          "marzo": "51"
        },
        "var_m_m": {
          "valor": 6,
          "unidad": "puntos",
          "display": "+6"
        }
      },
      {
        "nombre": "CAC",
        "unidad": "USD",
        "direccion": "menor_es_buena",
        "valores": {
          "enero": 234,
          "febrero": 198,
          "marzo": 187
        },
        "valores_display": {
          "enero": "$234",
          "febrero": "$198",
          "marzo": "$187"
        },
        "var_m_m": {
          "valor": -11,
          "unidad": "USD",
          "display": "-$11"
        }
      },
      {
        "nombre": "LTV",
        "unidad": "USD",
        "direccion": "mayor_es_buena",
        "valores": {
          "enero": 1890,
          "febrero": 2010,
          "marzo": 2340
        },
        "valores_display": {
          "enero": "$1,890",
          "febrero": "$2,010",
          "marzo": "$2,340"
        },
        "var_m_m": {
          "valor": 330,
          "unidad": "USD",
          "display": "+$330"
        }
      },
      {
        "nombre": "Active Users",
        "unidad": "usuarios",
        "direccion": "mayor_es_buena",
        "valores": {
          "enero": 1234,
          "febrero": 1456,
          "marzo": 1678
        },
        "valores_display": {
          "enero": "1,234",
          "febrero": "1,456",
          "marzo": "1,678"
        },
        "var_m_m": {
          "valor": 15.3,
          "unidad": "%",
          "display": "+15.3%"
        }
      },
      {
        "nombre": "Support Tickets",
        "unidad": "tickets",
        "direccion": "menor_es_buena",
        "valores": {
          "enero": 89,
          "febrero": 76,
          "marzo": 63
        },
        "valores_display": {
          "enero": "89",
          "febrero": "76",
          "marzo": "63"
        },
        "var_m_m": {
          "valor": -17.1,
          "unidad": "%",
          "display": "-17.1%"
        }
      },
      {
        "nombre": "Avg Response (h)",
        "unidad": "horas",
        "direccion": "menor_es_buena",
        "valores": {
          "enero": 4.2,
          "febrero": 3.1,
          "marzo": 2.4
        },
        "valores_display": {
          "enero": "4.2",
          "febrero": "3.1",
          "marzo": "2.4"
        },
        "var_m_m": {
          "valor": -0.7,
          "unidad": "horas",
          "display": "-0.7"
        }
      }
    ]
  },
  "calculos": {
    "ltv_cac_ratio": {
      "formula": "LTV / CAC",
      "valores": {
        "enero": 8.08,
        "febrero": 10.15,
        "marzo": 12.51
      },
      "tendencia": "Mejora sostenida del ratio LTV/CAC"
    },
    "analisis_mayor_mejora": {
      "criterio": "Se considera mejora el aumento en métricas mayores es buena y la reducción en métricas menores es buenas.",
      "mejoras_pct_m_m": {
        "MRR": 6.98,
        "Churn Rate": 18.42,
        "NPS": 13.33,
        "CAC": 5.56,
        "LTV": 16.42,
        "Active Users": 15.25,
        "Support Tickets": 17.11,
        "Avg Response (h)": 22.58
      },
      "mejoras_pct_jan_mar": {
        "MRR": 15.27,
        "Churn Rate": 26.19,
        "NPS": 21.43,
        "CAC": 20.09,
        "LTV": 23.81,
        "Active Users": 36.39,
        "Support Tickets": 29.21,
        "Avg Response (h)": 42.86
      },
      "metrica_con_mayor_mejora": {
        "nombre": "Avg Response (h)",
        "base": "feb-mar",
        "mejora_pct_m_m": 22.58,
        "mejora_pct_jan_mar": 42.86,
        "detalle": "Reducción del tiempo promedio de respuesta de 3.1 h a 2.4 h."
      }
    },
    "proyeccion_abril": {
      "metodo": "Se aplica la variación M/M indicada en la captura, correspondiente a febrero-marzo, a los valores de marzo.",
      "supuestos": [
        "Para métricas con variación en puntos porcentuales (pp), se aplica la variación absoluta.",
        "Para métricas con variación absoluta en USD o horas, se aplica la variación absoluta.",
        "Para métricas con variación porcentual, se aplica la variación porcentual.",
        "Los valores de usuarios y tickets se redondean a entero; los demás a 2 decimales cuando aplica."
      ],
      "valores": {
        "MRR": {
          "valor": 55.75,
          "unidad": "KUSD",
          "display": "$55.75K"
        },
        "Churn Rate": {
          "valor": 2.4,
          "unidad": "%",
          "display": "2.4%"
        },
        "NPS": {
          "valor": 57,
          "unidad": "puntos",
          "display": "57"
        },
        "CAC": {
          "valor": 176,
          "unidad": "USD",
          "display": "$176"
        },
        "LTV": {
          "valor": 2670,
          "unidad": "USD",
          "display": "$2,670"
        },
        "Active Users": {
          "valor": 1935,
          "unidad": "usuarios",
          "display": "1,935"
        },
        "Support Tickets": {
          "valor": 52,
          "unidad": "tickets",
          "display": "52"
        },
        "Avg Response (h)": {
          "valor": 1.7,
          "unidad": "horas",
          "display": "1.7 h"
        }
      },
      "ratio_ltv_cac_proyectado": {
        "formula": "LTV proyectado / CAC proyectado",
        "valor": 15.17
      }
    }
  }
}