# Gemini 2.5 Flash — ocr_extraction/screenshot_table_extraction

- model_id: `google/gemini-2.5-flash`
- success: True  | final: 6.58 | quality: 5.8
- latency_total: 4.664s | tokens_per_second: 188.5
- input_tokens: 419 | output_tokens: 879
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard_title": "DASHBOARD - KPIs Marzo 2026",
  "data": [
    {
      "Metrica": "MRR",
      "Enero": "$45.2K",
      "Febrero": "$48.7K",
      "Marzo": "$52.1K",
      "Var M/M": "+7.0%"
    },
    {
      "Metrica": "Churn Rate",
      "Enero": "4.2%",
      "Febrero": "3.8%",
      "Marzo": "3.1%",
      "Var M/M": "-0.7pp"
    },
    {
      "Metrica": "NPS",
      "Enero": 42,
      "Febrero": 45,
      "Marzo": 51,
      "Var M/M": "+6"
    },
    {
      "Metrica": "CAC",
      "Enero": "$234",
      "Febrero": "$198",
      "Marzo": "$187",
      "Var M/M": "-$11"
    },
    {
      "Metrica": "LTV",
      "Enero": "$1,890",
      "Febrero": "$2,010",
      "Marzo": "$2,340",
      "Var M/M": "+$330"
    },
    {
      "Metrica": "Active Users",
      "Enero": 1234,
      "Febrero": 1456,
      "Marzo": 1678,
      "Var M/M": "+15.3%"
    },
    {
      "Metrica": "Support Tickets",
      "Enero": 89,
      "Febrero": 76,
      "Marzo": 63,
      "Var M/M": "-17.1%"
    },
    {
      "Metrica": "Avg Response (h)",
      "Enero": 4.2,
      "Febrero": 3.1,
      "Marzo": 2.4,
      "Var M/M": "-0.7"
    }
  ],
  "LTV_CAC_ratio": {
    "Enero": 8.085,
    "Febrero": 10.152,
    "Marzo": 12.513
  },
  "metrica_mayor_mejora_porcentual": {
    "metrica": "LTV",
    "mejora_porcentual": "+16.48%"
  },
  "proyeccion_abril": [
    {
      "Metrica": "MRR",
      "Abril": "$55.7K"
    },
    {
      "Metrica": "Churn Rate",
      "Abril": "2.4%"
    },
    {
      "Metrica": "NPS",
      "Abril": 57
    },
    {
      "Metrica": "CAC",
      "Abril": "$176"
    },
    {
      "Metrica": "LTV",
      "Abril": "$2,670"
    },
    {
      "Metrica": "Active Users",
      "Abril": 1900
    },
    {
      "Metrica": "Support Tickets",
      "Abril": 50
    },
    {
      "Metrica": "Avg Response (h)",
      "Abril": 1.7
    }
  ],
  "tendencia_general": "Positiva en todas las metricas"
}
```