# Gemini 2.5 Flash Lite — ocr_extraction/screenshot_table_extraction

- model_id: `google/gemini-2.5-flash-lite`
- success: True  | final: 7.8 | quality: 8.0
- latency_total: 6.155s | tokens_per_second: 223.1
- input_tokens: 418 | output_tokens: 1373
- judge_score: 3.0 | justificación: La respuesta incluye datos no presentes en la tabla original, como 'LTV', 'Active Users', 'Support Tickets', y 'Avg Response (h)', lo que afecta la precisión y relevancia; sin embargo, ofrece proyecciones y análisis adicionales que añaden profundidad, y está bien organizada y clara.

## Respuesta completa

```json
{
  "dashboard_title": "KPIs Marzo 2026",
  "data": [
    {
      "metrica": "MRR",
      "enero": "$45.2K",
      "febrero": "$48.7K",
      "marzo": "$52.1K",
      "var_m_m": "+7.0%",
      "ltv_cac_ratio": null,
      "mejora_porcentual": 7.0,
      "abril_proyectado": "$55.7K"
    },
    {
      "metrica": "Churn Rate",
      "enero": "4.2%",
      "febrero": "3.8%",
      "marzo": "3.1%",
      "var_m_m": "-0.7pp",
      "ltv_cac_ratio": null,
      "mejora_porcentual": -0.7,
      "abril_proyectado": "2.4%"
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_m_m": "+6",
      "ltv_cac_ratio": null,
      "mejora_porcentual": 14.28,
      "abril_proyectado": 57
    },
    {
      "metrica": "CAC",
      "enero": "$234",
      "febrero": "$198",
      "marzo": "$187",
      "var_m_m": "-$11",
      "ltv_cac_ratio": null,
      "mejora_porcentual": -5.55,
      "abril_proyectado": "$176"
    },
    {
      "metrica": "LTV",
      "enero": "$1,890",
      "febrero": "$2,010",
      "marzo": "$2,340",
      "var_m_m": "+$330",
      "ltv_cac_ratio": null,
      "mejora_porcentual": 16.41,
      "abril_proyectado": "$2,710"
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_m_m": "+15.3%",
      "ltv_cac_ratio": null,
      "mejora_porcentual": 15.3,
      "abril_proyectado": 1935
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_m_m": "-17.1%",
      "ltv_cac_ratio": null,
      "mejora_porcentual": -17.1,
      "abril_proyectado": 52
    },
    {
      "metrica": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_m_m": "-0.7",
      "ltv_cac_ratio": null,
      "mejora_porcentual": -22.58,
      "abril_proyectado": 1.7
    }
  ],
  "analisis_adicional": {
    "ltv_cac_ratios": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "metrica_mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "valor_porcentual": -22.58,
      "nota": "Se considera mejora la disminución en 'Avg Response (h)'"
    },
    "tendencia_general": "↑ Positiva en todas las métricas",
    "proyecciones_abril": {
      "nota": "Proyectado asumiendo que la tasa de cambio mes a mes se mantiene constante.",
      "ejemplo_mrr_calculo": "52.1K * (1 + 7.0%) = 55.7K",
      "ejemplo_churn_calculo": "3.1% * (1 - 0.7pp) = 2.4%",
      "ejemplo_nps_calculo": "51 + 6 = 57",
      "ejemplo_cac_calculo": "187 * (1 - (11/198)) = 176 (aproximado)",
      "ejemplo_ltv_calculo": "2340 * (1 + (330/2340)) = 2710 (aproximado)",
      "ejemplo_active_users_calculo": "1678 * (1 + 15.3%) = 1935 (aproximado)",
      "ejemplo_support_tickets_calculo": "63 * (1 - 17.1%) = 52 (aproximado)",
      "ejemplo_avg_response_calculo": "2.4 * (1 - 0.7/3.1) = 1.7 (aproximado)"
    }
  }
}
```