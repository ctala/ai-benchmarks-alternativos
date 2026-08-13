# Poolside Laguna S 2.1 — ocr_extraction/screenshot_table_extraction

- model_id: `poolside/laguna-s-2.1`
- success: True  | final: 7.85 | quality: 8.0
- latency_total: 9.239s | tokens_per_second: 96.0
- input_tokens: 471 | output_tokens: 887
- judge_score: 3.8 | justificación: 

## Respuesta completa

{
  "dashboard": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "datos": [
      {
        "metrica": "MRR",
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100,
        "var_m_m": "+7.0%"
      },
      {
        "metrica": "Churn Rate",
        "enero": 4.2,
        "febrero": 3.8,
        "marzo": 3.1,
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
        "enero": 234,
        "febrero": 198,
        "marzo": 187,
        "var_m_m": "-$11"
      },
      {
        "metrica": "LTV",
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340,
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
    "tendencia_general": "↑ Positiva en todas las metricas"
  },
  "analisis": {
    "lTV_CAC_ratio": [
      {
        "mes": "Enero",
        "lTV": 1890,
        "cAC": 234,
        "ratio": 8.08
      },
      {
        "mes": "Febrero",
        "lTV": 2010,
        "cAC": 198,
        "ratio": 10.15
      },
      {
        "mes": "Marzo",
        "lTV": 2340,
        "cAC": 187,
        "ratio": 12.51
      }
    ],
    "mayor_mejora_porcentual": {
      "metrica": "LTV",
      "mejora_porcentual": 23.78
    },
    "proyeccion_abril": {
      "MRR": 55847,
      "Churn Rate": 2.4,
      "NPS": 57,
      "CAC": 176,
      "LTV": 2634,
      "Active Users": 1937,
      "Support Tickets": 52,
      "Avg Response (h)": 1.7
    }
  }
}