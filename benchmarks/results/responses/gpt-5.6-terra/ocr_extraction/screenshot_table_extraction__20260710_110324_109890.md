# GPT-5.6 Terra — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 5.19 | quality: 5.52
- latency_total: 19.249s | tokens_per_second: 122.9
- input_tokens: 379 | output_tokens: 2365
- judge_score: 3.0 | justificación: La respuesta incluye datos no presentes en la tabla original, como 'LTV', 'Active Users', 'Support Tickets', y 'Avg Response', lo que afecta la precisión y exactitud de los datos, pero ofrece proyecciones y análisis útiles.

## Respuesta completa

{
  "dashboard": "KPIs Marzo 2026",
  "tendencia_general": "Positiva en todas las métricas",
  "datos": [
    {
      "metrica": "MRR",
      "unidad": "USD",
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
      "unidad": "%",
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
        "unidad": "%"
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
        "unidad": "%"
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
    "formula": "LTV / CAC"
  },
  "mayor_mejora_porcentual": {
    "metrica": "Avg Response",
    "febrero": 3.1,
    "marzo": 2.4,
    "mejora_porcentual": 22.58,
    "direccion": "reducción",
    "calculo": "(3.1 - 2.4) / 3.1 * 100"
  },
  "proyeccion_abril_2026": {
    "metodologia": "Se repite la variación observada entre febrero y marzo: porcentual para métricas con variación porcentual y absoluta para métricas expresadas en USD, puntos, puntos porcentuales u horas.",
    "MRR": {
      "valor": 55737.37,
      "unidad": "USD",
      "valor_formateado": "$55.74K"
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
      "valor": 1934,
      "unidad": "usuarios",
      "valor_calculado_sin_redondear": 1933.85
    },
    "Support Tickets": {
      "valor": 52,
      "unidad": "tickets",
      "valor_calculado_sin_redondear": 52.22
    },
    "Avg Response": {
      "valor": 1.7,
      "unidad": "horas"
    },
    "ltv_cac_ratio_proyectado": 15.17
  }
}