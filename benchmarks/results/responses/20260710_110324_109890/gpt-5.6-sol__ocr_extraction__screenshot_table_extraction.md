# GPT-5.6 Sol — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 5.18 | quality: 5.88
- latency_total: 24.052s | tokens_per_second: 87.2
- input_tokens: 379 | output_tokens: 2097
- judge_score: 3.0 | justificación: La respuesta incluye datos no presentes en la captura de pantalla original, como LTV y Active Users, lo que afecta la precisión y exactitud de los datos, pero ofrece una estructura clara y algunos insights útiles.

## Respuesta completa

{
  "dashboard": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "periodo": "Marzo 2026",
    "tendencia_general": "Positiva en todas las métricas"
  },
  "metricas": [
    {
      "metrica": "MRR",
      "unidad": "USD",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "variacion_mensual": {
        "valor": 7.0,
        "unidad": "porcentaje"
      }
    },
    {
      "metrica": "Churn Rate",
      "unidad": "porcentaje",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "variacion_mensual": {
        "valor": -0.7,
        "unidad": "puntos_porcentuales"
      }
    },
    {
      "metrica": "NPS",
      "unidad": "puntos",
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
      "unidad": "USD",
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
      "unidad": "USD",
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
      "unidad": "usuarios",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "variacion_mensual": {
        "valor": 15.3,
        "unidad": "porcentaje"
      }
    },
    {
      "metrica": "Support Tickets",
      "unidad": "tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "variacion_mensual": {
        "valor": -17.1,
        "unidad": "porcentaje"
      }
    },
    {
      "metrica": "Avg Response",
      "unidad": "horas",
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
    "marzo": 12.51,
    "interpretacion_marzo": "Por cada USD 1 de CAC se generan aproximadamente USD 12.51 de LTV"
  },
  "mayor_mejora_porcentual": {
    "metrica": "Avg Response",
    "periodo_comparado": "Febrero a marzo",
    "mejora_porcentual": 22.58,
    "calculo": "(3.1 - 2.4) / 3.1 * 100",
    "criterio": "Las reducciones en Churn Rate, CAC, Support Tickets y Avg Response se consideran mejoras"
  },
  "proyeccion_abril": {
    "metodologia": "Se repite la variación mensual indicada entre febrero y marzo. Las cantidades discretas se redondean al entero más cercano.",
    "valores": {
      "MRR": {
        "valor": 55747,
        "unidad": "USD",
        "formato": "$55.7K"
      },
      "Churn Rate": {
        "valor": 2.4,
        "unidad": "porcentaje"
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
        "valor": 1935,
        "unidad": "usuarios"
      },
      "Support Tickets": {
        "valor": 52,
        "unidad": "tickets"
      },
      "Avg Response": {
        "valor": 1.7,
        "unidad": "horas"
      },
      "LTV_CAC_ratio": {
        "valor": 15.17,
        "calculo": "2670 / 176"
      }
    }
  }
}