# GLM 5 — ocr_extraction/screenshot_table_extraction

- model_id: `z-ai/glm-5`
- success: True  | final: 6.93 | quality: 8.0
- latency_total: 86.386s | tokens_per_second: 45.3
- input_tokens: 388 | output_tokens: 3911
- judge_score: 3.0 | justificación: La respuesta incluye datos correctos de la tabla, pero introduce métricas no presentes en la captura de pantalla original, afectando la precisión y exactitud de los datos; sin embargo, ofrece análisis y proyecciones útiles.

## Respuesta completa

```json
{
  "dashboard_info": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "periodo": "Enero - Marzo 2026",
    "tendencia_general": "Positiva en todas las métricas"
  },
  "datos_historicos": [
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
      "descripcion": "Relación LTV/CAC (Valor de Vida del Cliente / Costo de Adquisición)",
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "tendencia": "Mejora significativa en la eficiencia de adquisición"
    },
    "mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "mejora_calculada": "-22.58%",
      "razon": "Aunque el dashboard muestra variaciones mixtas (pp, absolutos, %), al normalizar los datos, la reducción del tiempo de respuesta de 3.1h a 2.4h representa una caída del 22.6% (mejora positiva). Otras métricas con gran mejora son Churn Rate (-18.4%) y Active Users (+15.3%)."
    },
    "proyeccion_abril": {
      "metodologia": "Extrapolación lineal basada en la variación de Marzo (M/M) o porcentaje de crecimiento reciente",
      "valores_estimados": {
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