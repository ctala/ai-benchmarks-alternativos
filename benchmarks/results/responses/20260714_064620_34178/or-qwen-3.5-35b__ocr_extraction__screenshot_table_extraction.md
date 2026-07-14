# Qwen 3.5 35B — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.5-35b-a3b`
- success: True  | final: 7.32 | quality: 8.0
- latency_total: 37.349s | tokens_per_second: 126.1
- input_tokens: 427 | output_tokens: 4711
- judge_score: 4.0 | justificación: La respuesta es relevante y proporciona un análisis y proyecciones útiles, aunque incluye datos no presentes en la captura de pantalla original, afectando la precisión.

## Respuesta completa

{
  "metadata": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "periodo": "Enero 2026 - Marzo 2026",
    "tendencia_general": "Positiva (Mejora en todas las métricas clave)",
    "fuente": "Extracto de Dashboard (Captura de Pantalla)"
  },
  "datos_raw": [
    {
      "metrica": "MRR",
      "enero": "$45.2K",
      "febrero": "$48.7K",
      "marzo": "$52.1K",
      "var_m_m": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "enero": "4.2%",
      "febrero": "3.8%",
      "marzo": "3.1%",
      "var_m_m": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_m_m": "+6"
    },
    {
      "metrica": "CAC",
      "enero": "$234",
      "febrero": "$198",
      "marzo": "$187",
      "var_m_m": "-$11"
    },
    {
      "metrica": "LTV",
      "enero": "$1,890",
      "febrero": "$2,010",
      "marzo": "$2,340",
      "var_m_m": "+$330"
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_m_m": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_m_m": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_m_m": "-0.7"
    }
  ],
  "analisis": {
    "ltv_cac_ratio": {
      "enero": {
        "ltv": 1890,
        "cac": 234,
        "ratio": 8.08
      },
      "febrero": {
        "ltv": 2010,
        "cac": 198,
        "ratio": 10.15
      },
      "marzo": {
        "ltv": 2340,
        "cac": 187,
        "ratio": 12.51
      }
    },
    "mejora_porcentual_maxima": {
      "metrica": "Avg Response (h)",
      "descripcion": "Reducción del tiempo de respuesta",
      "porcentaje_calculado": "22.58%",
      "cambio_absoluto": "De 3.1h a 2.4h",
      "nota": "Aunque Support Tickets muestra -17.1% en la tabla, el cálculo preciso de Avg Response (0.7/3.1) supera este porcentaje en términos de mejora operativa."
    }
  },
  "proyeccion_abril": {
    "metodo": "Tendencia lineal basada en Variación Mes a Mes (M/M) de Marzo",
    "metricas": [
      {
        "metrica": "MRR",
        "valor_proyectado": "$55.7K",
        "calculadora": "52.1K * 1.07"
      },
      {
        "metrica": "Churn Rate",
        "valor_proyectado": "2.4%",
        "calculadora": "3.1% - 0.7pp"
      },
      {
        "metrica": "NPS",
        "valor_proyectado": 57,
        "calculadora": "51 + 6"
      },
      {
        "metrica": "CAC",
        "valor_proyectado": "$176",
        "calculadora": "187 - 11"
      },
      {
        "metrica": "LTV",
        "valor_proyectado": "$2,670",
        "calculadora": "2340 + 330"
      },
      {
        "metrica": "Active Users",
        "valor_proyectado": 1935,
        "calculadora": "1678 * 1.153"
      },
      {
        "metrica": "Support Tickets",
        "valor_proyectado": 52,
        "calculadora": "63 * (1 - 0.171)"
      },
      {
        "metrica": "Avg Response (h)",
        "valor_proyectado": 1.9,
        "calculadora": "2.4 * (1 - 0.2258)"
      }
    ],
    "advertencia": "Las proyecciones asumen una continuidad lineal de la tendencia actual. Factores estacionales o saturación de mercado podrían alterar estos valores."
  }
}