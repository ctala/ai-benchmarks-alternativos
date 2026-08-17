# GLM 5.2 — ocr_extraction/screenshot_table_extraction

- model_id: `z-ai/glm-5.2`
- success: True  | final: 5.73 | quality: 6.16
- latency_total: 62.17s | tokens_per_second: 53.0
- input_tokens: 395 | output_tokens: 3296
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard_info": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "general_trend": "Positiva en todas las metricas"
  },
  "metrics_data": [
    {
      "metrica": "MRR",
      "Enero": "$45.2K",
      "Feb": "$48.7K",
      "Marzo": "$52.1K",
      "var_m_m": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "Enero": "4.2%",
      "Feb": "3.8%",
      "Marzo": "3.1%",
      "var_m_m": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "Enero": 42,
      "Feb": 45,
      "Marzo": 51,
      "var_m_m": "+6"
    },
    {
      "metrica": "CAC",
      "Enero": "$234",
      "Feb": "$198",
      "Marzo": "$187",
      "var_m_m": "-$11"
    },
    {
      "metrica": "LTV",
      "Enero": "$1,890",
      "Feb": "$2,010",
      "Marzo": "$2,340",
      "var_m_m": "+$330"
    },
    {
      "metrica": "Active Users",
      "Enero": 1234,
      "Feb": 1456,
      "Marzo": 1678,
      "var_m_m": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "Enero": 89,
      "Feb": 76,
      "Marzo": 63,
      "var_m_m": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "Enero": 4.2,
      "Feb": 3.1,
      "Marzo": 2.4,
      "var_m_m": "-0.7"
    }
  ],
  "analisis_adicional": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Feb": 10.15,
      "Marzo": 12.51,
      "note": "Calculado dividiendo LTV entre CAC para cada mes."
    },
    "metrica_mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "mejora_calculada": "-22.58%",
      "detalle": "Redujo de 3.1 a 2.4 horas. Si se consideran solo metricas de crecimiento positivo, LTV lidera con un +16.42%."
    },
    "proyeccion_abril": {
      "supuesto": "Se aplico la variacion observada entre Febrero y Marzo (porcentual para tasas/usuarios, absoluta para puntos/dolares) a los valores de Marzo.",
      "valores_proyectados": {
        "MRR": "$55.7K",
        "Churn Rate": "2.4%",
        "NPS": 57,
        "CAC": "$176",
        "LTV": "$2,670",
        "Active Users": 1935,
        "Support Tickets": 52,
        "Avg Response (h)": 1.7
      }
    }
  }
}
```