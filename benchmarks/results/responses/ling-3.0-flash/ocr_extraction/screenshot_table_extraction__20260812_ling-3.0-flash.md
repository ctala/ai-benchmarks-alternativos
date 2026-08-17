# Ling 3.0 Flash — ocr_extraction/screenshot_table_extraction

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 7.97 | quality: 8.0
- latency_total: 9.284s | tokens_per_second: 424.1
- input_tokens: 456 | output_tokens: 3937
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard": "KPIs Marzo 2026",
  "datos_extraidos": [
    {
      "metrica": "MRR",
      "enero": "$45.2K",
      "febrero": "$48.7K",
      "marzo": "$52.1K",
      "var_mm": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "enero": "4.2%",
      "febrero": "3.8%",
      "marzo": "3.1%",
      "var_mm": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_mm": "+6"
    },
    {
      "metrica": "CAC",
      "enero": "$234",
      "febrero": "$198",
      "marzo": "$187",
      "var_mm": "-$11"
    },
    {
      "metrica": "LTV",
      "enero": "$1,890",
      "febrero": "$2,010",
      "marzo": "$2,340",
      "var_mm": "+$330"
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_mm": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_mm": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_mm": "-0.7"
    }
  ],
  "ltv_cac_ratio": {
    "descripcion": "Ratio LTV / CAC por mes",
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
    },
    "tendencia": "El ratio LTV/CAC crece de 8.08 a 12.51, indicando mayor eficiencia en la generación de valor por cada dólar de adquisición."
  },
  "mayor_mejora_porcentual": {
    "metrica": "Avg Response (h)",
    "mejora": "-42.86%",
    "detalle": "Reducción del tiempo promedio de respuesta de 4.2h (Enero) a 2.4h (Marzo), una mejora porcentual del 42.86% respecto al valor inicial.",
    "ranking_mejoras": [
      { "metrica": "Avg Response (h)", "mejora_pct": "-42.86%", "desde": 4.2, "hasta": 2.4 },
      { "metrica": "Support Tickets", "mejora_pct": "-29.21%", "desde": 89, "hasta": 63 },
      { "metrica": "Active Users", "mejora_pct": "+35.98%", "desde": 1234, "hasta": 1678 },
      { "metrica": "LTV", "mejora_pct": "+23.81%", "desde": 1890, "hasta": 2340 },
      { "metrica": "NPS", "mejora_pct": "+21.43%", "desde": 42, "hasta": 51 },
      { "metrica": "CAC", "mejora_pct": "-20.09%", "desde": 234, "hasta": 187 },
      { "metrica": "Churn Rate", "mejora_pct": "-26.19%", "desde": "4.2%", "hasta": "3.1%" },
      { "metrica": "MRR", "mejora_pct": "+15.27%", "desde": "$45.2K", "hasta": "$52.1K" }
    ]
  },
  "proyeccion_abril": {
    "metodo": "Se aplica la variación más reciente (Febrero → Marzo) sobre el valor de Marzo para proyectar Abril.",
    "proyecciones": [
      {
        "metrica": "MRR",
        "marzo": "$52.1K",
        "variacion_aplicada": "+7.0%",
        "proyectado_abril": "$55.7K"
      },
      {
        "metrica": "Churn Rate",
        "marzo": "3.1%",
        "variacion_aplicada": "-0.7pp",
        "proyectado_abril": "2.4%"
      },
      {
        "metrica": "NPS",
        "marzo": 51,
        "variacion_aplicada": "+6",
        "proyectado_abril": 57
      },
      {
        "metrica": "CAC",
        "marzo": "$187",
        "variacion_aplicada": "-$11",
        "proyectado_abril": "$176"
      },
      {
        "metrica": "LTV",
        "marzo": "$2,340",
        "variacion_aplicada": "+$330",
        "proyectado_abril": "$2,670"
      },
      {
        "metrica": "Active Users",
        "marzo": 1678,
        "variacion_aplicada": "+15.3%",
        "proyectado_abril": 1935
      },
      {
        "metrica": "Support Tickets",
        "marzo": 63,
        "variacion_aplicada": "-17.1%",
        "proyectado_abril": 52
      },
      {
        "metrica": "Avg Response (h)",
        "marzo": 2.4,
        "variacion_aplicada": "-0.7h",
        "proyectado_abril": 1.7
      }
    ],
    "ltv_cac_ratio_proyectado_abril": {
      "ltv": 2670,
      "cac": 176,
      "ratio": 15.17
    },
    "nota": "Las proyecciones asumen que la tendencia más reciente (variación Febrero → Marzo) se mantiene linealmente. No consideran estacionalidad ni factores externos."
  }
}
```