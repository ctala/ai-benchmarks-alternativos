# DeepSeek V4 Pro — ocr_extraction/screenshot_table_extraction

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 7.22 | quality: 8.0
- latency_total: 63.949s | tokens_per_second: 64.5
- input_tokens: 386 | output_tokens: 4124
- judge_score: 3.0 | justificación: La respuesta incluye datos no presentes en la captura de pantalla original, afectando la precisión y relevancia, pero ofrece algunos insights útiles y está bien organizada.

## Respuesta completa

```json
{
  "data": [
    {
      "metrica": "MRR",
      "enero": "$45.2K",
      "feb": "$48.7K",
      "marzo": "$52.1K",
      "var_mm": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "enero": "4.2%",
      "feb": "3.8%",
      "marzo": "3.1%",
      "var_mm": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "enero": "42",
      "feb": "45",
      "marzo": "51",
      "var_mm": "+6"
    },
    {
      "metrica": "CAC",
      "enero": "$234",
      "feb": "$198",
      "marzo": "$187",
      "var_mm": "-$11"
    },
    {
      "metrica": "LTV",
      "enero": "$1,890",
      "feb": "$2,010",
      "marzo": "$2,340",
      "var_mm": "+$330"
    },
    {
      "metrica": "Active Users",
      "enero": "1,234",
      "feb": "1,456",
      "marzo": "1,678",
      "var_mm": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "enero": "89",
      "feb": "76",
      "marzo": "63",
      "var_mm": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "enero": "4.2",
      "feb": "3.1",
      "marzo": "2.4",
      "var_mm": "-0.7"
    }
  ],
  "ltv_cac_ratio": {
    "enero": 8.08,
    "feb": 10.15,
    "marzo": 12.51
  },
  "metric_with_highest_improvement_percentage": {
    "metrica": "Avg Response (h)",
    "improvement_percentage": "42.9%"
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
```