# Qwen 3.8 Flash — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.5 | quality: 10.0
- latency_total: 231.051s | tokens_per_second: 63.2
- input_tokens: 478 | output_tokens: 14602

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
  "datos_extraidos": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "tendencia_general": "↑ Positiva en todas las métricas",
    "periodos": [
      "Enero",
      "Febrero",
      "Marzo"
    ],
    "tabla": [
      {
        "metrica": "MRR",
        "unidad": "K USD",
        "valores": {
          "Enero": 45.2,
          "Febrero": 48.7,
          "Marzo": 52.1
        },
        "var_m_m_original": "+7.0%",
        "mejora_si": "aumenta"
      },
      {
        "metrica": "Churn Rate",
        "unidad": "%",
        "valores": {
          "Enero": 4.2,
          "Febrero": 3.8,
          "Marzo": 3.1
        },
        "var_m_m_original": "-0.7pp",
        "mejora_si": "disminuye"
      },
      {
        "metrica": "NPS",
        "unidad": "puntos",
        "valores": {
          "Enero": 42,
          "Febrero": 45,
          "Marzo": 51
        },
        "var_m_m_original": "+6",
        "mejora_si": "aumenta"
      },
      {
        "metrica": "CAC",
        "unidad": "USD",
        "valores": {
          "Enero": 234,
          "Febrero": 198,
          "Marzo": 187
        },
        "var_m_m_original": "-$11",
        "mejora_si": "disminuye"
      },
      {
        "metrica": "LTV",
        "unidad": "USD",
        "valores": {
          "Enero": 1890,
          "Febrero": 2010,
          "Marzo": 2340
        },
        "var_m_m_original": "+$330",
        "mejora_si": "aumenta"
      },
      {
        "metrica": "Active Users",
        "unidad": "usuarios",
        "valores": {
          "Enero": 1234,
          "Febrero": 1456,
          "Marzo": 1678
        },
        "var_m_m_original": "+15.3%",
        "mejora_si": "aumenta"
      },
      {
        "metrica": "Support Tickets",
        "unidad": "tickets",
        "valores": {
          "Enero": 89,
          "Febrero": 76,
          "Marzo": 63
        },
        "var_m_m_original": "-17.1%",
        "mejora_si": "disminuye"
      },
      {
        "metrica": "Avg Response (h)",
        "unidad": "horas",
        "valores": {
          "Enero": 4.2,
          "Febrero": 3.1,
          "Marzo": 2.4
        },
        "var_m_m_original": "-0.7",
        "mejora_si": "disminuye"
      }
    ]
  },
  "calculados": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Febrero": 10.15,
      "Marzo": 12.51,
      "detalle": [
        {
          "periodo": "Enero",
          "LTV": 1890,
          "CAC": 234,
          "ratio": 8.0769
        },
        {
          "periodo": "Febrero",
          "LTV": 2010,
          "CAC": 198,
          "ratio": 10.1515
        },
        {
          "periodo": "Marzo",
          "LTV": 2340,
          "CAC": 187,
          "ratio": 12.5134
        }
      ]
    }
  },
  "analisis": {
    "mejora_porcentual_mayor": {
      "metrica": "Avg Response (h)",
      "mejora_porcentual": 22.58,
      "cambio_relativo": -22.58,
      "criterio": "Se calculó el cambio relativo entre Febrero y Marzo. Para métricas donde menor es mejor, una reducción se considera mejora y se toma su valor absoluto.",
      "ranking": [
        {
          "posicion": 1,
          "metrica": "Avg Response (h)",
          "cambio_relativo": -22.58,
          "mejora_porcentual": 22.58,
          "direccion": "menor_es_mejor"
        },
        {
          "posicion": 2,
          "metrica": "Churn Rate",
          "cambio_relativo": -18.42,
          "mejora_porcentual": 18.42,
          "direccion": "menor_es_mejor"
        },
        {
          "posicion": 3,
          "metrica": "Support Tickets",
          "cambio_relativo": -17.11,
          "mejora_porcentual": 17.11,
          "direccion": "menor_es_mejor"
        },
        {
          "posicion": 4,
          "metrica": "LTV",
          "cambio_relativo": 16.42,
          "mejora_porcentual": 16.42,
          "direccion": "mayor_es_mejor"
        },
        {
          "posicion": 5,
          "metrica": "Active Users",
          "cambio_relativo": 15.25,
          "mejora_porcentual": 15.25,
          "direccion": "mayor_es_mejor"
        },
        {
          "posicion": 6,
          "metrica": "NPS",
          "cambio_relativo": 13.33,
          "mejora_porcentual": 13.33,
          "direccion": "mayor_es_mejor"
        },
        {
          "posicion": 7,
          "metrica": "MRR",
          "cambio_relativo": 6.98,
          "mejora_porcentual": 6.98,
          "direccion": "mayor_es_mejor"
        },
        {
          "posicion": 8,
          "metrica": "CAC",
          "cambio_relativo": -5.56,
          "mejora_porcentual": 5.56,
          "direccion": "menor_es_mejor"
        }
      ],
      "alternativa_por_var_visible": {
        "metrica": "Support Tickets",
        "mejora_porcentual": 17.1,
        "criterio": "Si solo se comparan las variaciones M/M originales que ya están expresadas en porcentaje, Support Tickets es la mayor mejora visible."
      }
    }
  },
  "proyeccion_abril": {
    "metodo_principal": "Extrapolación lineal: se mantiene el mismo cambio absoluto observado entre Febrero y Marzo.",
    "valores": {
      "MRR": {
        "unidad": "K USD",
        "abril": 55.5,
        "var_absoluta": 3.4,
        "var_porcentual": 6.53
      },
      "Churn Rate": {
        "unidad": "%",
        "abril": 2.4,
        "var_absoluta": -0.7,
        "var_absoluta_unidad": "pp",
        "var_porcentual": -22.58
      },
      "NPS": {
        "unidad": "puntos",
        "abril": 57,
        "var_absoluta": 6,
        "var_porcentual": 11.76
      },
      "CAC": {
        "unidad": "USD",
        "abril": 176,
        "var_absoluta": -11,
        "var_porcentual": -5.88
      },
      "LTV": {
        "unidad": "USD",
        "abril": 2670,
        "var_absoluta": 330,
        "var_porcentual": 14.1
      },
      "Active Users": {
        "unidad": "usuarios",
        "abril": 1900,
        "var_absoluta": 222,
        "var_porcentual": 13.23
      },
      "Support Tickets": {
        "unidad": "tickets",
        "abril": 50,
        "var_absoluta": -13,
        "var_porcentual": -20.63
      },
      "Avg Response (h)": {
        "unidad": "horas",
        "abril": 1.7,
        "var_absoluta": -0.7,
        "var_porcentual": -29.17
      }
    },
    "ltv_cac_ratio_proyectado": 15.17,
    "metodo_alternativo": "Extrapolación relativa: se mantiene el mismo cambio porcentual observado entre Febrero y Marzo.",
    "valores_alternativos": {
      "MRR": {
        "unidad": "K USD",
        "abril": 55.74,
        "var_porcentual": 6.98
      },
      "Churn Rate": {
        "unidad": "%",
        "abril": 2.53,
        "var_porcentual": -18.42
      },
      "NPS": {
        "unidad": "puntos",
        "abril": 57.8,
        "var_porcentual": 13.33
      },
      "CAC": {
        "unidad": "USD",
        "abril": 176.61,
        "var_porcentual": -5.56
      },
      "LTV": {
        "unidad": "USD",
        "abril": 2724.18,
        "var_porcentual": 16.42
      },
      "Active Users": {
        "unidad": "usuarios",
        "abril": 1933.85,
        "var_porcentual": 15.25
      },
      "Support Tickets": {
        "unidad": "tickets",
        "abril": 52.22,
        "var_porcentual": -17.11
      },
      "Avg Response (h)": {
        "unidad": "horas",
        "abril": 1.86,
        "var_porcentual": -22.58
      }
    },
    "ltv_cac_ratio_proyectado_alternativo": 15.42,
    "notas": [
      "Las proyecciones son hipotéticas y asumen que la tendencia de Febrero a Marzo continúa en Abril.",
      "El método lineal mantiene el mismo cambio absoluto; el método relativo mantiene el mismo cambio porcentual.",
      "Para Churn Rate, la proyección lineal puede ser más optimista en términos absolutos que la proyección relativa."
    ]
  }
}