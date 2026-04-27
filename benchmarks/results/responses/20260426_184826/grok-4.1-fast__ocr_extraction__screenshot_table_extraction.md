# Grok 4.1 Fast — ocr_extraction/screenshot_table_extraction

- model_id: `x-ai/grok-4.1-fast`
- success: True  | final: 6.43 | quality: 5.8
- latency_total: 21.735s | tokens_per_second: 132.4
- input_tokens: 510 | output_tokens: 2877
- judge_score: 3.2 | justificación: 

## Respuesta completa

{
  "extracted_data": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "tendencia_general": "↑ Positiva en todas las metricas",
    "metrics": {
      "MRR": {
        "Enero": "$45.2K",
        "Feb": "$48.7K",
        "Marzo": "$52.1K",
        "Var_M_M": "+7.0%"
      },
      "Churn Rate": {
        "Enero": "4.2%",
        "Feb": "3.8%",
        "Marzo": "3.1%",
        "Var_M_M": "-0.7pp"
      },
      "NPS": {
        "Enero": "42",
        "Feb": "45",
        "Marzo": "51",
        "Var_M_M": "+6"
      },
      "CAC": {
        "Enero": "$234",
        "Feb": "$198",
        "Marzo": "$187",
        "Var_M_M": "-$11"
      },
      "LTV": {
        "Enero": "$1,890",
        "Feb": "$2,010",
        "Marzo": "$2,340",
        "Var_M_M": "+$330"
      },
      "Active Users": {
        "Enero": "1,234",
        "Feb": "1,456",
        "Marzo": "1,678",
        "Var_M_M": "+15.3%"
      },
      "Support Tickets": {
        "Enero": "89",
        "Feb": "76",
        "Marzo": "63",
        "Var_M_M": "-17.1%"
      },
      "Avg Response (h)": {
        "Enero": "4.2",
        "Feb": "3.1",
        "Marzo": "2.4",
        "Var_M_M": "-0.7"
      }
    }
  },
  "ltv_cac_ratios": {
    "Enero": 8.08,
    "Feb": 10.15,
    "Marzo": 12.51
  },
  "metrica_mayor_mejora_porcentual": {
    "nombre": "Active Users",
    "var": "+15.3%"
  },
  "proyeccion_abril": {
    "MRR": "$55.7K",
    "Churn Rate": "2.4%",
    "NPS": "57",
    "CAC": "$176",
    "LTV": "$2,670",
    "Active Users": "1,935",
    "Support Tickets": "52",
    "Avg Response (h)": "1.7"
  }
}